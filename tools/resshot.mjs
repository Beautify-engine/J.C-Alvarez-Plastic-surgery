import { chromium } from 'playwright';
const b = await chromium.launch();
for (const [w,h,tag] of [[1440,1000,'d'],[390,844,'m']]) {
  const p = await (await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:2})).newPage();
  await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
  await p.evaluate(()=>document.querySelectorAll('[data-rise],[data-reveal],[data-rise-group]').forEach(e=>e.classList.add('is-in')));
  const s = p.locator('section.res');
  await s.scrollIntoViewIfNeeded(); await p.waitForTimeout(1600);
  await s.screenshot({path:`design/shots/res-${tag}.png`});
  await p.close();
}
await b.close();
