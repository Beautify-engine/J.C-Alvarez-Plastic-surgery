import { chromium } from 'playwright';
const b = await chromium.launch();
for (const [w,h,tag] of [[1440,900,'d'],[390,844,'m']]) {
  const p = await (await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:2})).newPage();
  const errs=[]; p.on('requestfailed', r=>errs.push('REQFAIL '+r.url().slice(-50)));
  await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
  await p.evaluate(()=>document.querySelectorAll('[data-rise],[data-reveal]').forEach(e=>e.classList.add('is-in')));
  await p.waitForTimeout(700);
  const sec = p.locator('section.about');
  await sec.scrollIntoViewIfNeeded(); await p.waitForTimeout(600);
  await sec.screenshot({path:`design/shots/about-${tag}.png`});
  console.log(tag, errs.length?errs.slice(0,3):'no failed requests');
  await p.close();
}
await b.close();
