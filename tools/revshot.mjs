import { chromium } from 'playwright';
const b = await chromium.launch();
for (const [url,sel,name] of [['http://localhost:8787/','section.rev','rev-home'],
                              ['http://localhost:8787/results.html','section.rev','rev-results'],
                              ['http://localhost:8787/preparation.html','.pr-voices','rev-prep']]) {
  const p = await (await b.newContext({viewport:{width:1440,height:900},deviceScaleFactor:1})).newPage();
  await p.goto(url,{waitUntil:'networkidle'});
  await p.evaluate(()=>document.querySelectorAll('[data-rise],[data-rise-group],[data-reveal]').forEach(e=>e.classList.add('is-in')));
  const s = p.locator(sel); await s.scrollIntoViewIfNeeded(); await p.waitForTimeout(900);
  await s.screenshot({path:`design/shots/${name}.png`});
  await p.close();
}
await b.close();
