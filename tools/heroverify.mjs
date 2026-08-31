import { chromium } from 'playwright';
const b = await chromium.launch();
for (const [w,h,tag] of [[1440,900,'d'],[390,844,'m']]) {
  const p = await (await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:2})).newPage();
  p.on('console', m => { if (m.type()==='error') console.log(tag,'CONSOLE',m.text()); });
  await p.goto('http://localhost:8787/hero-headlines.html',{waitUntil:'networkidle'});
  await p.waitForTimeout(2500);
  const info = await p.evaluate(() => {
    const v = document.querySelector('video.hero-v');
    return { src: v && v.currentSrc, rs: v && v.readyState, t: v && v.currentTime,
             vw: v && v.videoWidth, vh: v && v.videoHeight, paused: v && v.paused };
  });
  console.log(tag, JSON.stringify(info));
  await p.addStyleTag({content:'.ho-label{display:none !important}'});
  const sec = p.locator('section.hA').first();
  await sec.scrollIntoViewIfNeeded(); await p.waitForTimeout(600);
  await sec.screenshot({path:`design/shots/hv-hero-${tag}.png`});
  const cr = p.locator('section.creds');
  await cr.scrollIntoViewIfNeeded(); await p.waitForTimeout(400);
  await cr.screenshot({path:`design/shots/hv-creds-${tag}.png`});
}
await b.close();
