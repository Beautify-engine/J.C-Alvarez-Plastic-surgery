import { chromium } from 'playwright';
/* Hide the headline, screenshot the exact band it occupies at several points in
   the loop, and dump the background pixels. axe cannot evaluate text over video,
   so the worst frame has to be measured, not assumed. */
const b = await chromium.launch();
for (const [w,h,tag] of [[1440,900,'d'],[390,844,'m']]) {
  const p = await (await b.newContext({viewport:{width:w,height:h}})).newPage();
  await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
  await p.waitForTimeout(2600);
  const box = await p.evaluate(()=>{
    const h1=document.querySelector('.hA h1'); const r=h1.getBoundingClientRect();
    return {x:Math.round(r.x), y:Math.round(r.y), width:Math.round(r.width), height:Math.round(r.height)};
  });
  await p.addStyleTag({content:'.hA h1,.hA__more,.hA__row,.hA__proof{visibility:hidden!important}'});
  for (const t of [0,2,4,6,8,10,11.5]) {
    await p.evaluate(v=>{const el=document.getElementById('heroVid'); el.pause(); el.currentTime=v;}, t);
    await p.waitForTimeout(420);
    await p.screenshot({path:`/private/tmp/claude-501/-Users-tatiana-Desktop-PLASTIC-SURGERY-FUNNEL---/88913f83-cd0b-4fca-b1df-ad16d840092f/scratchpad/bg-${tag}-${t}.png`, clip:box});
  }
  await p.close();
}
await b.close();
console.log('sampled');
