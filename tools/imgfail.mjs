import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
await p.goto('http://localhost:8787/about.html',{waitUntil:'networkidle'});
await p.waitForTimeout(1500);
await p.evaluate(()=>window.scrollTo(0,document.body.scrollHeight));
await p.waitForTimeout(1500);
console.log(await p.evaluate(()=>[...document.querySelectorAll('img')]
  .filter(i=>i.naturalWidth===0)
  .map(i=>({src:i.currentSrc||i.src, alt:i.alt.slice(0,30)}))));
await b.close();
