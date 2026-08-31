import { chromium } from 'playwright';
const b = await chromium.launch();
for (const [w,h,tag] of [[1440,900,'d'],[390,844,'m']]) {
  const p = await (await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:2})).newPage();
  await p.goto('http://localhost:8787/',{waitUntil:'domcontentloaded'});
  await p.waitForTimeout(900);
  const f = p.locator('footer.ft');
  await f.scrollIntoViewIfNeeded(); await p.waitForTimeout(400);
  await f.screenshot({path:`design/shots/foot-${tag}.png`});
  await p.close();
}
await b.close();
