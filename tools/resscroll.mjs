import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
await p.waitForTimeout(1200);
// drive the coverflow to the end
for (let i=0;i<50;i++){ await p.click('.res .ctl button[data-trk="next"], .res button[aria-label*="More"], .res button[aria-label*="Next"]').catch(()=>{}); await p.waitForTimeout(60); }
await p.waitForTimeout(1500);
console.log(await p.evaluate(()=>{
  const imgs=[...document.querySelectorAll('.res img')];
  return {total:imgs.length, broken:imgs.filter(i=>i.naturalWidth===0).length};
}));
await b.close();
