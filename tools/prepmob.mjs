import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();
await p.goto('http://localhost:8787/preparation.html',{waitUntil:'networkidle'});
const H=await p.evaluate(()=>document.body.scrollHeight);
for(let y=0;y<H;y+=500){ await p.evaluate(v=>scrollTo(0,v),y); await p.waitForTimeout(110); }
await p.evaluate(()=>scrollTo(0,0)); await p.waitForTimeout(800);
console.log(JSON.stringify(await p.evaluate(()=>({
  overflow: document.documentElement.scrollWidth>document.documentElement.clientWidth,
  scrollW: document.documentElement.scrollWidth,
  marks: document.querySelectorAll('.pr-mk').length,
  imgsOk: [...document.querySelectorAll('img')].every(i=>i.naturalWidth>0)
}))));
await p.screenshot({path:'design/shots/prep-m.png', fullPage:true});
await b.close();
