import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:390,height:844}})).newPage();
await p.goto('http://localhost:8787/hero-headlines.html',{waitUntil:'networkidle'});
await p.waitForTimeout(800);
console.log(JSON.stringify(await p.evaluate(() => {
  const q = s => document.querySelector(s);
  const r = e => { const b = e.getBoundingClientRect(); return {l:+b.left.toFixed(1), r:+b.right.toFixed(1), w:+b.width.toFixed(1)}; };
  const wrap = q('.creds__in'), marks = q('.creds__marks');
  const imgs = [...document.querySelectorAll('.creds__marks img')].map(i => ({a:i.alt.slice(0,18), ...r(i)}));
  const cs = getComputedStyle(wrap);
  return { docW: document.documentElement.clientWidth,
           wrap: r(wrap), padL: cs.paddingLeft, padR: cs.paddingRight,
           marks: r(marks), imgs,
           scrollW: document.documentElement.scrollWidth };
}), null, 1));
await b.close();
