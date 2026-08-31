import { chromium } from 'playwright';
const b=await chromium.launch();
const p=await (await b.newContext({viewport:{width:1440,height:1000},deviceScaleFactor:2})).newPage();
await p.goto('http://localhost:8787/_artifact-check.html',{waitUntil:'networkidle'});
await p.waitForTimeout(1800);
const el=p.locator('section.about');
await el.scrollIntoViewIfNeeded(); await p.waitForTimeout(700);
await el.screenshot({path:'design/shots/artifact-about.png'});
const r=await p.evaluate(()=>{
  const g=document.querySelector('.about__grid'), h=document.querySelector('.about h2');
  const t=document.querySelector('.trk');
  return {gridDisplay:getComputedStyle(g).display,
          cols:getComputedStyle(g).gridTemplateColumns.split(' ').length,
          h2Font:getComputedStyle(h).fontFamily.split(',')[0],
          trkDisplay:getComputedStyle(t).display,
          aboutH:Math.round(document.querySelector('section.about').getBoundingClientRect().height)};
});
console.log(JSON.stringify(r,null,1));
await b.close();
