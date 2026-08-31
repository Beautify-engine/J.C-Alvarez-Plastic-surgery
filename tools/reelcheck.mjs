import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
const errs=[], vids=[];
p.on('console',m=>{if(m.type()==='error')errs.push(m.text().slice(0,70))});
p.on('response',r=>{ if(r.url().includes('/video/reels/')) vids.push(r.status()+' '+r.url().split('/').pop()); });
await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
await p.evaluate(()=>document.querySelector('section.reel').scrollIntoView());
await p.waitForTimeout(2000);
for (let i=0;i<3;i++){ await p.click('#reelNext').catch(()=>{}); await p.waitForTimeout(700); }
console.log(JSON.stringify(await p.evaluate(()=>{
  const live = document.querySelector('.reel__item.is-live video');
  return { tiles: document.querySelectorAll('.reel__item').length,
           videos: document.querySelectorAll('.reel video').length,
           live: document.querySelectorAll('.reel__item.is-live').length,
           livePlaying: live ? !live.paused : null,
           liveSrc: live && live.currentSrc ? live.currentSrc.split('/').pop() : null,
           postersOk: [...document.querySelectorAll('.reel__frame img')].every(i=>i.naturalWidth>0) };
}),null,1));
console.log('reel video responses:', vids.length ? [...new Set(vids)] : 'none');
console.log('console errors:', errs.length ? errs : 'none');
await b.close();
