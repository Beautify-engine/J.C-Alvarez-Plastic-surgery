import { chromium } from 'playwright';
const b=await chromium.launch();
const ctx=await b.newContext({viewport:{width:1440,height:1000},deviceScaleFactor:2});
const p=await ctx.newPage();
await p.goto('http://localhost:8787/gallery-options.html',{waitUntil:'networkidle'});
await p.waitForTimeout(1200);
await p.evaluate(async()=>{document.querySelectorAll('img[loading="lazy"]').forEach(i=>i.loading='eager');
  await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})));});
await p.addStyleTag({content:'.opt-label{position:static !important}'});
// advance coverflow + deck into the middle so the stacking reads
for(let i=0;i<3;i++){ await p.click('#cfNext'); await p.waitForTimeout(250); }
for(let i=0;i<2;i++){ await p.click('#dkNext'); await p.waitForTimeout(250); }
await p.waitForTimeout(900);
const secs=await p.locator('section.gb').all();
for(let i=0;i<secs.length;i++){
  await secs[i].scrollIntoViewIfNeeded(); await p.waitForTimeout(700);
  await secs[i].screenshot({path:`design/shots/gopt-${'abc'[i]}.png`});
  console.log('gopt-'+'abc'[i]);
}
await b.close();
