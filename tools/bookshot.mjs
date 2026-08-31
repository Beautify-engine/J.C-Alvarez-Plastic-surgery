import { chromium } from 'playwright';
const b = await chromium.launch();
for (const [w,h,name] of [[1440,900,'desktop'],[390,844,'mobile']]) {
  const ctx = await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:2});
  const p = await ctx.newPage();
  const errs=[]; p.on('pageerror',e=>errs.push(String(e)));
  await p.goto('http://localhost:8787/book/',{waitUntil:'networkidle',timeout:30000});
  await p.waitForTimeout(900);
  await p.screenshot({path:`design/shots/BK-1-${name}.png`, fullPage:true});
  // pick a few procedures
  await p.click('input[value="tummy-tuck"] + .bopt__box').catch(()=>{});
  await p.click('input[value="hd-liposuction"] + .bopt__box').catch(()=>{});
  await p.waitForTimeout(400);
  await p.screenshot({path:`design/shots/BK-1b-${name}.png`, fullPage:true});
  await p.click('#bNext'); await p.waitForTimeout(400);
  await p.click('input[value="3m"] + .bopt__box'); await p.waitForTimeout(300);
  await p.screenshot({path:`design/shots/BK-2-${name}.png`, fullPage:true});
  await p.click('#bNext'); await p.waitForTimeout(400);
  await p.fill('#f-name','Marisol Reyes'); await p.fill('#f-email','m.reyes@example.com');
  await p.fill('#f-phone','305 555 0142');
  await p.fill('#f-note','I had two children and the skin below my navel never went back.');
  await p.waitForTimeout(300);
  await p.screenshot({path:`design/shots/BK-3-${name}.png`, fullPage:true});
  await p.click('#bNext'); await p.waitForTimeout(500);
  await p.screenshot({path:`design/shots/BK-4-${name}.png`, fullPage:true});
  console.log(name, 'errors:', errs.length?errs:'none');
  await ctx.close();
}
await b.close();
