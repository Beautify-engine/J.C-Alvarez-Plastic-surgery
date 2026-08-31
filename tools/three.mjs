import { chromium } from 'playwright';
const b = await chromium.launch();
for (const [w,h,tag] of [[1440,900,'d'],[820,1180,'t'],[390,844,'m']]) {
  const p = await (await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:2})).newPage();
  await p.goto('http://localhost:8787/hero-headlines.html',{waitUntil:'networkidle'});
  await p.waitForTimeout(2200);
  await p.addStyleTag({content:'.ho-label{display:none !important}'});
  const sec = p.locator('section.hA').first();
  await sec.scrollIntoViewIfNeeded(); await p.waitForTimeout(500);
  const m = await p.evaluate(() => {
    const h1 = document.querySelector('.hA h1');
    const cs = getComputedStyle(h1);
    const lines = Math.round(h1.getBoundingClientRect().height / parseFloat(cs.lineHeight));
    return { fs: cs.fontSize, lh: cs.lineHeight, lines,
             proof: !!document.querySelector('.hA__proof'),
             faces: document.querySelectorAll('.faces img').length };
  });
  console.log(tag, JSON.stringify(m));
  await sec.screenshot({path:`design/shots/t3-${tag}.png`});
}
await b.close();
