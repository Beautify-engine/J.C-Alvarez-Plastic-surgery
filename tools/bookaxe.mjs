import { chromium } from 'playwright';
import { readFileSync } from 'fs';
const src = readFileSync('node_modules/axe-core/axe.min.js','utf8');
const b = await chromium.launch();
let total = 0;
for (const w of [1440, 390, 320]) {
  const p = await b.newPage({viewport:{width:w,height:900}});
  await p.goto('http://localhost:8787/book/',{waitUntil:'networkidle'});
  await p.addStyleTag({content:'*,*::before,*::after{transition:none!important;animation:none!important}'});
  await p.addScriptTag({content:src});
  for (let step=1; step<=3; step++){
    if (step===2){ await p.click('label:has(input[value=\"tummy-tuck\"])'); await p.click('#bNext'); }
    if (step===3){ await p.click('label:has(input[value=\"3m\"])'); await p.click('#bNext'); }
    await p.waitForTimeout(250);
    const r = await p.evaluate(()=>axe.run(document,{runOnly:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']}));
    total += r.violations.length;
    console.log(`${w}px step ${step}: ${r.violations.length} violations`);
    r.violations.forEach(v=>{ console.log(`  [${v.impact}] ${v.id}`);
      v.nodes.slice(0,3).forEach(n=>console.log('     '+n.target.join(' ')+' | '+(n.failureSummary||'').split('\n')[1])); });
  }
  await p.close();
}
console.log('\nTOTAL VIOLATIONS:', total);
await b.close();
