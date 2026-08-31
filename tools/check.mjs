import { chromium } from 'playwright';
const b = await chromium.launch();
const ctx = await b.newContext({viewport:{width:1440,height:900}});
const p = await ctx.newPage();
const bad=[], ok=[];
p.on('response', r => { (r.status()>=400?bad:ok).push(`${r.status()} ${r.url()}`); });
p.on('console', m => { if(m.type()==='error') console.log('CONSOLE ERROR:', m.text().slice(0,120)); });
await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
await p.waitForTimeout(3000);
console.log(`requests ok: ${ok.length}`);
console.log(bad.length? 'FAILED:\n  '+bad.join('\n  ') : 'no 4xx/5xx');
const m = await p.evaluate(()=>{
  const v=document.getElementById('heroVid');
  return {videoPlaying: v && !v.paused && v.currentTime>0, videoSrc: v&&v.currentSrc,
          h1: document.querySelectorAll('h1').length,
          title: document.title};
});
console.log(JSON.stringify(m,null,2));
await b.close();
