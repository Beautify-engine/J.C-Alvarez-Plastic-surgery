// reduced-motion + no-JS smoke test
import { chromium } from 'playwright';
const b = await chromium.launch();
const url = process.argv[2];
for (const [label, opts] of [['reduced-motion',{reducedMotion:'reduce'}],['no-js',{javaScriptEnabled:false}]]) {
  const ctx = await b.newContext({viewport:{width:1440,height:900},...opts});
  const p = await ctx.newPage();
  await p.goto(url,{waitUntil:'load'});
  const r = await p.evaluate(()=>({
    hiddenReveals: [...document.querySelectorAll('[data-reveal]')]
      .filter(e=>getComputedStyle(e).opacity==='0').length,
    visiblePanels: [...document.querySelectorAll('.ptime__panel')]
      .filter(e=>getComputedStyle(e).display!=='none').length,
    visibleChecks: [...document.querySelectorAll('.pchk__card')]
      .filter(e=>getComputedStyle(e).display!=='none').length,
    scrollW: document.documentElement.scrollWidth
  }));
  console.log(label, JSON.stringify(r));
  await ctx.close();
}
await b.close();
