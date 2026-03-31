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
    fs.mkdirSync(imagesDir, { recursive: true });
}

// 1. Parse JSON for bios from the original feed if possible
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
    if (sourceData && sourceData.podcasts) {
        sourceData.podcasts.forEach(p => {
            if (p.name) bios[p.name] = "AI Builder / Podcast Guest";
        });
    }
} catch (e) {
    console.error('Failed to parse prepare-digest JSON for bios:', e.message);
}

// 2. Read markdown
const rawMarkdown = fs.readFileSync(digestFile, 'utf8');
const now = new Date();
const dateStr = now.toISOString().split('T')[0];

// 3. Extract Highlights for the Image (Simple heuristic)
const lines = rawMarkdown.split('\n').filter(l => l.trim().length > 10 && !l.startsWith('#') && !l.startsWith('http'));
const summaryLines = lines.slice(0, 3).map(l => l.replace(/\*\*/g, '').substring(0, 50) + '...');
let highlightsHtml = summaryLines.map(l => `<li>${l}</li>`).join('');

if (!highlightsHtml) {
    highlightsHtml = "<li>🚀 AI 行业今日前沿动态更新</li><li>💡 大佬最新观点提炼</li><li>🛠️ 产研工具链演进洞察</li>";
}

// 4. Generate Image with Puppeteer
(async () => {
    try {
        console.log("Generating summary poster...");
        const browser = await puppeteer.launch({ 
            headless: 'new',
            args: ['--no-sandbox', '--disable-setuid-sandbox'] 
        });
        const page = await browser.newPage();
        await page.setViewport({ width: 1200, height: 630 });
        
        const htmlTemplate = `
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Microsoft YaHei", sans-serif;
            margin: 0; padding: 0; width: 1200px; height: 630px;
            background: #0d1117; color: #ffffff;
            display: flex; align-items: center; justify-content: center;
            overflow: hidden; position: relative;
        }
        .bg {
            position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
            z-index: 1;
        }
        .glow {
            position: absolute; width: 600px; height: 600px;
            background: radial-gradient(circle, rgba(88, 166, 255, 0.15) 0%, transparent 70%);
            top: -100px; left: -100px; z-index: 2;
        }
        .container {
            position: relative; z-index: 10;
            width: 1060px; height: 500px;
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 32px; padding: 50px;
            display: flex; flex-direction: column;
            box-shadow: 0 25px 50px rgba(0,0,0,0.4);
        }
        .header {
            display: flex; justify-content: space-between; align-items: flex-end;
            margin-bottom: 40px; border-bottom: 1px solid rgba(255,255,255,0.1);
            padding-bottom: 25px;
        }
        h1 {
            margin: 0; font-size: 56px; font-weight: 800;
            background: linear-gradient(90deg, #58a6ff, #8957e5);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }
        .date-badge {
            font-size: 24px; color: #58a6ff; font-weight: 600;
            padding: 8px 20px; background: rgba(88, 166, 255, 0.1);
            border-radius: 12px; border: 1px solid rgba(88, 166, 255, 0.2);
        }
        .main-content { flex-grow: 1; display: flex; flex-direction: column; justify-content: center; }
        ul { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 25px; }
        li {
            font-size: 30px; line-height: 1.4; color: #e6edf3;
            display: flex; align-items: flex-start;
            padding: 20px 25px; background: rgba(0,0,0,0.2);
            border-radius: 16px; border-left: 5px solid #8957e5;
        }
        li::before { content: "⚡"; margin-right: 15px; filter: drop-shadow(0 0 5px #8957e5); }
        .footer { margin-top: 30px; text-align: right; color: #8b949e; font-size: 18px; font-weight: 300; }
        </style>
        </head>
        <body>
        <div class="bg"></div>
        <div class="glow"></div>
        <div class="container">
            <div class="header">
                <h1>AI 脉搏 | 今日概览</h1>
                <div class="date-badge">${dateStr}</div>
            </div>
            <div class="main-content">
                <ul>${highlightsHtml}</ul>
            </div>
            <div class="footer">由 龟丞相 · 龙宫情报局 自动生成</div>
        </div>
        </body>
        </html>
        `;
        
        await page.setContent(htmlTemplate);
        const imagePath = `images/summary-${dateStr}.png`;
        const fullImagePath = path.join(__dirname, imagePath);
        await page.screenshot({ path: fullImagePath });
        await browser.close();
        
        // 5. Update data.js
        console.log("Syncing to data.js...");
        const currentDataFile = fs.readFileSync(dataFile, 'utf8');
        let currentArray = [];
        const jsonMatch = currentDataFile.match(/const\s+aiPulseData\s*=\s*(\[[\s\S]*\])\s*;/);
        if (jsonMatch && jsonMatch[1]) {
            try {
                currentArray = JSON.parse(jsonMatch[1]);
            } catch(e) {
                console.error("Parse existing data.js failed, starting fresh.");
            }
        }
        
        const newItem = {
            date: dateStr,
            content: rawMarkdown,
            summaryImage: imagePath,
            bios: bios
        };
        
        // Dedup by date
        const index = currentArray.findIndex(i => i.date === dateStr);
        if (index !== -1) {
            currentArray[index] = newItem;
        } else {
            currentArray.unshift(newItem);
        }
        
        if (currentArray.length > 30) currentArray.pop();
        
        fs.writeFileSync(dataFile, `const aiPulseData = ${JSON.stringify(currentArray, null, 4)};\n`, 'utf8');
        console.log("Success!");
    } catch (err) {
        console.error("Critical failure:", err);
    }
})();