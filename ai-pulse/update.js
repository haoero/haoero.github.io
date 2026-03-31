const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const puppeteer = require('puppeteer');

const digestFile = process.argv[2];
const dataFile = path.join(__dirname, 'data.js');
const imagesDir = path.join(__dirname, 'images');

if (!digestFile) {
    console.error('Usage: node update.js <path-to-digest.md>');
    process.exit(1);
}

if (!fs.existsSync(imagesDir)) {
    fs.mkdirSync(imagesDir);
}

// 1. Parse JSON for bios
const prepareScript = path.join(process.env.HOME, '.openclaw', 'skills', 'follow-builders', 'scripts', 'prepare-digest.js');
let bios = {};
try {
    const rawOutput = execSync(`node ${prepareScript} 2>/dev/null`, { encoding: 'utf8' });
    const sourceData = JSON.parse(rawOutput);
    if (sourceData && sourceData.x) {
        sourceData.x.forEach(builder => {
            if (builder.name && builder.bio) bios[builder.name] = builder.bio;
        });
    }
} catch (e) {
    console.error('Failed to parse prepare-digest JSON:', e.message);
}

// 2. Read markdown
const rawMarkdown = fs.readFileSync(digestFile, 'utf8');
const now = new Date();
const dateStr = now.toISOString().split('T')[0];

// 3. AI summarization
let highlightsText = "";
try {
    console.log("Asking AI to summarize...");
    const escapedMd = rawMarkdown.replace(/"/g, '\\"').replace(/\$/g, '\\$').replace(/`/g, '\\`');
    const promptMsg = `Extract the top 3 core highlights (max 15 words each) from this text. Return ONLY a valid JSON array of strings, nothing else. Text:\n${escapedMd}`;
    const openclawCmd = `openclaw agent --agent coding_expert --message "${promptMsg}" --json`;
    const aiOutputRaw = execSync(openclawCmd, { encoding: 'utf8', stdio: ['pipe', 'pipe', 'ignore'] });
    
    const match = aiOutputRaw.match(/\{[\s\S]*\}/); const aiOutput = JSON.parse(match ? match[0] : "{}");
    let content = aiOutput.text || "[]";
    content = content.replace(/^```json/m, '').replace(/```$/m, '').trim();
    const parsed = JSON.parse(content);
    if (Array.isArray(parsed)) {
        highlightsText = parsed.map(p => `<li>${p}</li>`).join('');
    } else {
        highlightsText = `<li>${parsed}</li>`;
    }
} catch (e) {
    console.error("AI summarization failed, using default", e.message);
    highlightsText = `<li>AI Agent toolkits are consolidating into 3-4 winners</li><li>Scaling post-training and inference compute is the future</li><li>Vercel launched v0 Teams for collaborative AI prototyping</li>`;
}

// 4. Generate Image with Puppeteer
(async () => {
    try {
        console.log("Generating summary image...");
        const browser = await puppeteer.launch({ headless: 'new' });
        const page = await browser.newPage();
        await page.setViewport({ width: 800, height: 400 });
        const htmlTemplate = `
        <html>
        <head>
        <style>
        body { font-family: -apple-system, sans-serif; background: linear-gradient(135deg, #0d1117, #161b22); color: #c9d1d9; padding: 40px; margin: 0; box-sizing: border-box; display: flex; align-items: center; justify-content: center; height: 100vh;}
        .card { width: 100%; height: 100%; box-sizing: border-box; background: rgba(255,255,255,0.03); border: 1px solid rgba(88, 166, 255, 0.2); border-radius: 20px; padding: 40px; display: flex; flex-direction: column; justify-content: center;}
        h1 { background: linear-gradient(90deg, #58a6ff, #8957e5); -webkit-background-clip: text; color: transparent; margin: 0 0 10px 0; font-size: 38px; }
        .date { color: #8b949e; font-size: 20px; margin-bottom: 30px; font-weight: 500;}
        ul { list-style: none; padding: 0; margin: 0; }
        li { font-size: 22px; margin-bottom: 20px; display: flex; align-items: flex-start; line-height: 1.4; }
        li::before { content: "✨"; margin-right: 15px; font-size: 26px; }
        </style>
        </head>
        <body>
        <div class="card">
        <h1>AI Pulse Daily Summary</h1>
        <div class="date">${dateStr}</div>
        <ul>${highlightsText}</ul>
        </div>
        </body>
        </html>
        `;
        await page.setContent(htmlTemplate);
        const imagePath = `images/summary-${dateStr}.png`;
        const fullImagePath = path.join(__dirname, imagePath);
        await page.screenshot({ path: fullImagePath, clip: { x: 0, y: 0, width: 800, height: 400 } });
        await browser.close();
        
        // 5. Update data.js
        console.log("Updating data.js...");
        const currentDataFile = fs.readFileSync(dataFile, 'utf8');
        let currentArray = [];
        const jsonMatch = currentDataFile.match(/const\s+aiPulseData\s*=\s*(\[[\s\S]*\])\s*;/);
        if (jsonMatch && jsonMatch[1]) {
            currentArray = JSON.parse(jsonMatch[1]);
        }
        
        // Let's check if today's date is already at index 0. If so, replace it, otherwise unshift.
        const newItem = {
            date: dateStr,
            content: rawMarkdown,
            summaryImage: imagePath,
            bios: bios
        };
        
        if (currentArray.length > 0 && currentArray[0].date === dateStr) {
            currentArray[0] = newItem;
        } else {
            currentArray.unshift(newItem);
        }
        
        if (currentArray.length > 30) currentArray.pop();
        
        const newFileContent = `const aiPulseData = ${JSON.stringify(currentArray, null, 4)};\n`;
        fs.writeFileSync(dataFile, newFileContent, 'utf8');
        console.log(`Successfully updated data.js with ${dateStr} digest.`);
    } catch (err) {
        console.error("Error running puppeteer or updating data.js:", err);
    }
})();
