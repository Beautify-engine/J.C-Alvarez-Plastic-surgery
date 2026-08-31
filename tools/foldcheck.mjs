/* Is the form actually in the first screen? Measures the top of each landmark against
   the fold, at the two review viewports plus a short laptop. */
import { chromium } from 'playwright';
const b = await chromium.launch();
for (const [w,h,name] of [[1440,900,'desktop 1440x900'],[1280,720,'laptop 1280x720'],[390,844,'iPhone 390x844']]) {
  const ctx = await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:2});
  const p = await ctx.newPage();
  await p.goto('http://localhost:8787/book/',{waitUntil:'networkidle'});
  await p.waitForTimeout(600);
  const m = await p.evaluate(()=>{
    const t = s => { const e=document.querySelector(s); if(!e) return null;
      const r=e.getBoundingClientRect(); return {top:Math.round(r.top), bot:Math.round(r.bottom)}; };
    return {h1:t('#b-h1'), rail:t('#bSteps'), q:t('#p1 legend'),
            card1:t('.pcard'), row1:t('.bgroup:first-child .pcards'), cta:t('#bNext')};
  });
  console.log(`\n${name}  (fold at ${h}px)`);
  for (const [k,v] of Object.entries(m)) {
    if(!v) continue;
    console.log(`  ${k.padEnd(6)} top ${String(v.top).padStart(4)}  bottom ${String(v.bot).padStart(4)}  ${v.bot<=h?'fully visible':(v.top<h?'partly visible':'BELOW FOLD')}`);
  }
  await p.screenshot({path:`design/shots/FOLD-${name.split(' ')[0]}.png`});
  await ctx.close();
}
await b.close();
