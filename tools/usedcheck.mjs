import { chromium } from 'playwright';
import { readdirSync, statSync, writeFileSync } from 'fs';
function walk(d, base=''){ return readdirSync(d).flatMap(f=>{ const p=d+'/'+f;
  return statSync(p).isDirectory()?walk(p,base+f+'/'):(f.endsWith('.html')?[base+f]:[]); }); }
const pages = walk('src/public/_final');
const VIEWS = [[390,844,2],[1024,900,1],[1920,1080,2]];
const requested = new Set(); const broken = [];
const b = await chromium.launch();
for (const page of pages) {
  for (const [w,h,dpr] of VIEWS) {
    const p = await (await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:dpr})).newPage();
    p.on('request', r => { const u=r.url();
      if (u.startsWith('http://localhost:8801')) requested.add(u.replace('http://localhost:8801','')); });
    p.on('response', r => { if (r.status()>=400) broken.push(r.status()+' '+r.url().replace('http://localhost:8801','')); });
    await p.goto('http://localhost:8787/_final/'+page, {waitUntil:'domcontentloaded'});
    await p.evaluate(async () => {
      const tr=[...document.querySelectorAll('*')].filter(e=>{const o=getComputedStyle(e).overflowX;
        return (o==='auto'||o==='scroll')&&e.scrollWidth>e.clientWidth+40;});
      for(const t of tr){ for(let x=0;x<=t.scrollWidth;x+=Math.max(300,t.clientWidth-60)){t.scrollLeft=x;await new Promise(r=>setTimeout(r,40));} }
    });
    const H = await p.evaluate(()=>document.body.scrollHeight);
    for (let y=0;y<H;y+=800){ await p.evaluate(v=>scrollTo(0,v),y); await p.waitForTimeout(45); }
    await p.waitForTimeout(500);
    await p.close();
  }
}
await b.close();
writeFileSync('/tmp/requested.txt', [...requested].sort().join('\n'));
console.log('distinct assets a browser actually fetched:', requested.size);
console.log('4xx/5xx during the sweep:', broken.length ? broken.slice(0,5) : 'none');
