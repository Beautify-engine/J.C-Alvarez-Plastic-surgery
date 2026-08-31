import { chromium } from 'playwright';
import { readFileSync } from 'fs';
const url = process.argv[2];
const src = readFileSync('node_modules/axe-core/axe.min.js','utf8');
const b = await chromium.launch();
for (const w of [1440, 390]) {
  const p = await b.newPage({viewport:{width:w,height:900}});
  await p.goto(url,{waitUntil:'networkidle'});
  // [data-reveal] blocks sit at opacity 0 until IntersectionObserver fires, and axe
  // skips invisible nodes — so without this the audit silently ignores most of the page.
  // kill transitions first, or axe samples colours mid-fade and reports phantom failures
  await p.addStyleTag({content:'*,*::before,*::after{transition:none!important;animation:none!important}'});
  await p.evaluate(()=>document.querySelectorAll('[data-reveal]').forEach(e=>e.classList.add('is-in')));
  await p.waitForTimeout(300);
  await p.addScriptTag({content:src});
  const r = await p.evaluate(()=>axe.run(document,{runOnly:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']}));
  console.log(`\n=== ${w}px — ${r.violations.length} violations ===`);
  r.violations.forEach(v=>{
    console.log(`[${v.impact}] ${v.id}: ${v.help}`);
    v.nodes.slice(0,3).forEach(n=>console.log('   '+n.target.join(' ')+'  |  '+(n.failureSummary||'').split('\n').slice(1,3).join(' ').trim()));
  });
  await p.close();
}
await b.close();
