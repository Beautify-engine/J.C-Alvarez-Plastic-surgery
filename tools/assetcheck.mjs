import { chromium } from 'playwright';
const b = await chromium.launch();
let bad = 0;
for (const page of ['home','results','preparation']) {
  const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
  const miss = [];
  p.on('response', r => { if (r.status() >= 400) miss.push(r.status()+' '+r.url().split('/').pop()); });
  await p.goto(`http://localhost:8787/_final/${page}.html`, {waitUntil:'networkidle'});
  await p.evaluate(async () => {
    const tr=[...document.querySelectorAll('*')].filter(e=>{const o=getComputedStyle(e).overflowX;
      return (o==='auto'||o==='scroll')&&e.scrollWidth>e.clientWidth+40;});
    for(const t of tr){ for(let x=0;x<=t.scrollWidth;x+=Math.max(300,t.clientWidth-60)){t.scrollLeft=x;await new Promise(r=>setTimeout(r,50));} t.scrollLeft=0; }
  });
  const H = await p.evaluate(()=>document.body.scrollHeight);
  for (let y=0;y<H;y+=700){ await p.evaluate(v=>scrollTo(0,v),y); await p.waitForTimeout(60); }
  await p.waitForTimeout(1500);
  const r = await p.evaluate(()=>{
    const v=document.getElementById('heroVid');
    return { hero: v?{w:v.videoWidth,playing:!v.paused}:null,
             brokenImgs: [...document.querySelectorAll('img')].filter(i=>{
               if(i.naturalWidth!==0||!i.getAttribute('src')) return false;
               if(i.loading!=='lazy') return true;
               const b=i.getBoundingClientRect();
               return b.width>0&&b.bottom>0&&b.top<innerHeight&&b.right>0&&b.left<innerWidth;}).length };
  });
  const ok = !miss.length && !r.brokenImgs;
  if(!ok) bad++;
  console.log(`  ${ok?'✓':'✗'} ${page.padEnd(13)} ${r.hero?`hero ${r.hero.w}px playing:${r.hero.playing}`:'—'.padEnd(22)}  broken:${r.brokenImgs}  ${miss.slice(0,3).join(' ')}`);
  await p.close();
}
await b.close(); process.exit(bad?1:0);
