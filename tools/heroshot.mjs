import { chromium } from 'playwright';
const b = await chromium.launch();
for (const [w,h,tag] of [[1440,900,'d'],[390,844,'m']]) {
  const p = await (await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:2})).newPage();
  const errs=[]; p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
  await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
  await p.waitForTimeout(2600);
  const info = await p.evaluate(()=>{
    const v=document.getElementById('heroVid');
    const cs=e=>getComputedStyle(e);
    return { vid:v&&v.currentSrc.split('/').pop(), vw:v&&v.videoWidth, vh:v&&v.videoHeight,
             playing:v&&!v.paused,
             h1:document.querySelector('.hA h1').textContent.trim().slice(0,42),
             h1px:Math.round(parseFloat(cs(document.querySelector('.hA h1')).fontSize)),
             faces:document.querySelectorAll('.faces img').length,
             radius:cs(document.querySelector('.faces img')).borderRadius,
             stat:document.querySelector('.hA__stat').textContent.trim() };
  });
  console.log(tag, JSON.stringify(info), errs.length?errs.slice(0,2):'');
  await p.locator('section.hA').screenshot({path:`design/shots/newhero-${tag}.png`});
  await p.close();
}
await b.close();
