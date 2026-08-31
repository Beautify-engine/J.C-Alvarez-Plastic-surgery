import { chromium } from 'playwright';
const b=await chromium.launch();
const ctx=await b.newContext({viewport:{width:1440,height:940},deviceScaleFactor:2});
const p=await ctx.newPage();
await p.goto('http://localhost:8787/hero-options.html',{waitUntil:'networkidle'});
await p.waitForTimeout(2200);
await p.addStyleTag({content:'.ho-label{position:static !important}'});
const secs=await p.locator('section').all();
for(let i=0;i<secs.length;i++){
  await secs[i].scrollIntoViewIfNeeded(); await p.waitForTimeout(900);
  await secs[i].screenshot({path:`design/shots/hero-${'ABC'[i]}.png`});
  console.log('hero-'+'ABC'[i]);
}
await b.close();
