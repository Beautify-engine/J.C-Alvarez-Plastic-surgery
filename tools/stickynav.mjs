/* The sticky nav bar, both halves of it.
   1. Is the step's primary button reachable without hunting? Scroll to several depths
      on the tallest step and check it is still on screen.
   2. Does the bar hide anything you tab to? Walk the procedure cards by keyboard and
      check none ends up behind it. Neither scroll-margin nor scroll-padding fixes this
      case, so book.js corrects it by measuring — this is the regression test for that. */
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
console.log('\n--- keyboard: nothing should end up behind the bar ---');
for (const [w,h,name] of [[1440,900,'desktop'],[390,844,'iPhone']]) {
  const p = await (await b.newContext({viewport:{width:w,height:h}})).newPage();
  await p.goto('http://localhost:8787/book/',{waitUntil:'networkidle'});
  await p.waitForTimeout(400);
  await p.evaluate(()=>document.querySelector('input[name="procedure"]').focus());
  let hidden=0, checked=0;
  for (let i=0;i<11;i++){
    await p.keyboard.press('Tab'); await p.waitForTimeout(140);
    const r = await p.evaluate(()=>{
      const a=document.activeElement; if(!a||a.name!=='procedure') return null;
      const card=a.closest('.pcard'); if(!card) return null;
      const b=card.getBoundingClientRect(), bar=document.querySelector('.bnav').getBoundingClientRect();
      return {covered: b.bottom > bar.top && b.top < bar.bottom, label:a.value};
    });
    if(r){ checked++; if(r.covered){hidden++; console.log('   covered:', r.label);} }
  }
  console.log(`${name}: ${checked} cards tabbed, ${hidden} hidden behind the sticky bar`);
  await p.context().close();
}
await b.close();
