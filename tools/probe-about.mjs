import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
await p.goto('http://localhost:8787/about.html',{waitUntil:'networkidle'});
await p.waitForTimeout(600);
console.log(JSON.stringify(await p.evaluate(() => {
  const rows = [];
  for (const sel of ['.ab-intro','.ab-arc','.ab-why','.ab-more','.ab-cta','footer.ft','.ft__legalnav','h2.vh']) {
    document.querySelectorAll(sel).forEach(e => {
      const r = e.getBoundingClientRect();
      rows.push({sel, top: Math.round(r.top + scrollY), h: Math.round(r.height),
                 vis: getComputedStyle(e).position});
    });
  }
  return rows.sort((a,b)=>a.top-b.top);
}), null, 1));
await b.close();
