const fs = require('fs');
const path = require('path');

const digestFile = process.argv[2];
const dataFile = path.join(__dirname, 'data.js');

if (!digestFile) {
    console.error('Usage: node update.js <path-to-digest.md>');
    process.exit(1);
}

try {
    const rawMarkdown = fs.readFileSync(digestFile, 'utf8');
    
    // Extract today's date
    const now = new Date();
    const dateStr = now.toISOString().split('T')[0];
    
    // Read current data.js
    const currentDataFile = fs.readFileSync(dataFile, 'utf8');
    
    // Extract the JSON part using a regex
    let currentArray = [];
    const jsonMatch = currentDataFile.match(/const\s+aiPulseData\s*=\s*(\[[\s\S]*\])\s*;/);
    if (jsonMatch && jsonMatch[1]) {
        currentArray = JSON.parse(jsonMatch[1]);
    } else {
        console.error('Could not parse data.js, starting with empty array');
    }

    // Unshift new item
    currentArray.unshift({
        date: dateStr,
        content: rawMarkdown
    });

    // Limit to 30 items
    if (currentArray.length > 30) {
        currentArray.pop();
    }

    // Write back
    const newFileContent = `const aiPulseData = ${JSON.stringify(currentArray, null, 4)};\n`;
    fs.writeFileSync(dataFile, newFileContent, 'utf8');

    console.log(`Successfully updated data.js with ${dateStr} digest. Total items: ${currentArray.length}`);
} catch (e) {
    console.error('Failed to update data.js:', e);
    process.exit(1);
}
