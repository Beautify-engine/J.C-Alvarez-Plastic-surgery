/* Is the step's primary button reachable without hunting for it? Scrolls to a few
   depths on the tallest step and checks the button is still on screen. */
import { chromium } from 'playwright';
const b = await chromium.launch();
for (const [w,h,name] of [[1440,900,'desktop'],[1280,720,'laptop'],[390,844,'iPhone']]) {
  const ctx = await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:2});
  const p = await ctx.newPage();
  await p.goto('http://localhost:8787/book/',{waitUntil:'networkidle'});
  await p.waitForTimeout(500);
  const rows = [];
  for (const frac of [0, .25, .5, .75, 1]) {
    await p.evaluate(f=>window.scrollTo(0, (document.body.scrollHeight-innerHeight)*f), frac);
    await p.waitForTimeout(250);
    const r = await p.evaluate(()=>{ const e=document.getElementById('bNext');
      const b=e.getBoundingClientRect();
      return {top:Math.round(b.top), bot:Math.round(b.bottom),
              onScreen: b.top>=0 && b.bottom<=innerHeight}; });
    rows.push(`${String(frac*100).padStart(3)}%  top ${String(r.top).padStart(4)}  ${r.onScreen?'on screen':'OFF SCREEN'}`);
  }
  console.log(`\n${name} ${w}x${h}`); rows.forEach(r=>console.log('  '+r));
  await p.evaluate(()=>window.scrollTo(0,600)); await p.waitForTimeout(300);
  await p.screenshot({path:`design/shots/STICKY-${name}.png`});
  await ctx.close();
}
await b.close();
