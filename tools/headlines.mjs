import { chromium } from 'playwright';
const b=await chromium.launch();
for (const [w,h,tag] of [[1440,900,'d'],[390,780,'m']]){
  const p=await (await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:2})).newPage();
  await p.goto('http://localhost:8787/hero-headlines.html',{waitUntil:'networkidle'});
  await p.waitForTimeout(2200);
  await p.addStyleTag({content:'.ho-label{position:static !important}'});
  const secs=await p.locator('section.hA').all();
  for(let i=0;i<secs.length;i++){
    await secs[i].scrollIntoViewIfNeeded(); await p.waitForTimeout(700);
    await secs[i].screenshot({path:`design/shots/hl${i+1}-${tag}.png`});
  }
  console.log('captured',tag);
}
await b.close();
