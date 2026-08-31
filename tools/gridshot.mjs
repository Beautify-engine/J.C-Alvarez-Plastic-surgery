import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:1000},deviceScaleFactor:1})).newPage();
await p.goto('http://localhost:8787/results.html',{waitUntil:'networkidle'});
const H=await p.evaluate(()=>document.body.scrollHeight);
for(let y=0;y<H;y+=500){ await p.evaluate(v=>scrollTo(0,v),y); await p.waitForTimeout(120); }
await p.waitForTimeout(1200);
const items = await p.locator('.gal__i').all();
for (let i=0;i<9;i++){ await items[i].scrollIntoViewIfNeeded(); }
await p.waitForTimeout(600);
await p.locator('.gal__grid').screenshot({path:'design/shots/grid-check.png'});
console.log(await p.evaluate(()=>{
  const f=document.querySelector('.gal__frame'), i=f.querySelector('img');
  const cs=getComputedStyle(i);
  return {fit:cs.objectFit, frameBox:f.getBoundingClientRect().width+'x'+f.getBoundingClientRect().height,
          natural:i.naturalWidth+'x'+i.naturalHeight, rendered:i.getBoundingClientRect().width+'x'+i.getBoundingClientRect().height};
}));
await b.close();
