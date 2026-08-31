import { chromium } from 'playwright';
const b = await chromium.launch();
for (const [w,h,tag] of [[1440,1000,'d'],[390,844,'m']]) {
  const p = await (await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:2})).newPage();
  await p.goto('http://localhost:8787/results.html',{waitUntil:'networkidle'});
  await p.waitForTimeout(1400);
  await p.screenshot({path:`design/shots/gal-${tag}.png`});
  if (tag==='d'){
    await p.click('.gal__c'); await p.waitForTimeout(700);
    await p.screenshot({path:'design/shots/gal-lb.png'});
  }
  await p.close();
}
await b.close();
