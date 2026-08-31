import { chromium } from 'playwright';
import { readdirSync, statSync } from 'fs';
function walk(d,b=''){ return readdirSync(d).flatMap(f=>{const p=d+'/'+f;
  return statSync(p).isDirectory()?walk(p,b+f+'/'):(f.endsWith('.html')?[b+f]:[]);}); }
const pages = walk('src/public/_dep').sort();
const br = await chromium.launch();
const rows = [];
for (const page of pages) {
  const p = await (await br.newContext({viewport:{width:1440,height:900}})).newPage();
  const errs=[], miss=[];
  p.on('console',m=>{if(m.type()==='error')errs.push(m.text().slice(0,50))});
  p.on('response',r=>{if(r.status()>=400)miss.push(r.status()+' '+r.url().split('/').pop())});
  await p.goto('http://localhost:8787/_dep/'+page,{waitUntil:'networkidle'});
  await p.evaluate(async()=>{const tr=[...document.querySelectorAll('*')].filter(e=>{const o=getComputedStyle(e).overflowX;
    return (o==='auto'||o==='scroll')&&e.scrollWidth>e.clientWidth+40;});
    for(const t of tr){for(let x=0;x<=t.scrollWidth;x+=Math.max(300,t.clientWidth-60)){t.scrollLeft=x;await new Promise(r=>setTimeout(r,40));}}});
  const H=await p.evaluate(()=>document.body.scrollHeight);
  for(let y=0;y<H;y+=800){await p.evaluate(v=>scrollTo(0,v),y);await p.waitForTimeout(45);}
  await p.waitForTimeout(900);
  const r = await p.evaluate(()=>{
    const sec=document.querySelector('.jca>main>section')||document.querySelector('.jca section');
    return { bleed: sec?Math.round(sec.getBoundingClientRect().width):0, vw: innerWidth,
      overflow: document.documentElement.scrollWidth>document.documentElement.clientWidth,
      font: getComputedStyle(document.querySelector('.jca h1,.jca h2')).fontFamily.split(',')[0].replace(/"/g,''),
      hostFont: getComputedStyle(document.body).fontFamily.split(',')[0],
      broken: [...document.querySelectorAll('.jca img')].filter(i=>{
        if(i.naturalWidth!==0||!i.getAttribute('src'))return false;
        if(i.loading!=='lazy')return true;
        const b=i.getBoundingClientRect();
        return b.width>0&&b.bottom>0&&b.top<innerHeight&&b.right>0&&b.left<innerWidth;}).length };
  });
  const ok = r.bleed>=r.vw-2 && !r.overflow && !r.broken && !miss.length && !errs.length
             && r.font==='Instrument Serif' && r.hostFont==='Roboto';
  rows.push([page.replace('.html',''), ok, r, miss, errs]);
  await p.close();
}
await br.close();
for (const [n,ok,r,miss,errs] of rows)
  console.log(`  ${ok?'✓':'✗'} ${n.padEnd(30)} bleed ${r.bleed}/${r.vw}  broken ${r.broken}  ${miss.slice(0,2).join(' ')}${errs.slice(0,1).join(' ')}`);
console.log(`\n${rows.filter(r=>r[1]).length}/${rows.length} pages deployment-clean`);
