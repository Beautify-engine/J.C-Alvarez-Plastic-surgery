import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:390,height:844}})).newPage();
const fails=[]; p.on('requestfailed',r=>fails.push(r.url().slice(-40)+' :: '+r.failure()?.errorText));
p.on('response',r=>{ if(r.status()>=400) fails.push(r.status()+' '+r.url().slice(-40)); });
await p.goto('http://localhost:8787/about.html',{waitUntil:'networkidle'});
// step-scroll so lazy loading actually fires
for (let y=0; y<await p.evaluate(()=>document.body.scrollHeight); y+=600){
  await p.evaluate(v=>window.scrollTo(0,v), y); await p.waitForTimeout(180);
}
await p.waitForTimeout(1200);
console.log('bad responses:', fails.length?fails:'none');
console.log(await p.evaluate(()=>[...document.querySelectorAll('img')]
  .filter(i=>i.naturalWidth===0)
  .map(i=>({cur:i.currentSrc.slice(-46), loading:i.loading, alt:i.alt.slice(0,26)}))));
await b.close();
