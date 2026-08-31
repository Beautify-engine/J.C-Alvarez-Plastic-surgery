import { chromium } from 'playwright';
const b = await chromium.launch();
for (const [w,h,tag] of [[1440,900,'d'],[390,844,'m']]) {
  const p = await (await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:1})).newPage();
  await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
  await p.evaluate(()=>document.querySelectorAll('[data-rise],[data-reveal],[data-rise-group]').forEach(e=>e.classList.add('is-in')));
  const H=await p.evaluate(()=>document.body.scrollHeight);
  for(let y=0;y<Math.min(H,4000);y+=400){ await p.evaluate(v=>scrollTo(0,v),y); await p.waitForTimeout(120); }
  await p.evaluate(()=>scrollTo(0,0)); await p.waitForTimeout(2200);
  const box = await p.evaluate(()=>{
    const a=document.querySelector('.about').getBoundingClientRect();
    return Math.round(a.top + window.scrollY + a.height);
  });
  await p.screenshot({path:`design/shots/top-${tag}.png`, fullPage:true, clip:{x:0,y:0,width:w,height:box}});
  await p.close();
}
await b.close();
