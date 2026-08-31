import { chromium } from 'playwright';
import { readdirSync } from 'fs';
const pages = readdirSync('src/public/procedures').filter(f=>f.endsWith('.html'));
const b = await chromium.launch();
let bad = 0;
for (const f of pages) {
  const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
  const errs=[], miss=[];
  p.on('console',m=>{if(m.type()==='error')errs.push(m.text().slice(0,60))});
  p.on('response',r=>{ if(r.status()>=400) miss.push(r.status()+' '+r.url().split('/').pop()); });
  await p.goto(`http://localhost:8787/procedures/${f}`,{waitUntil:'networkidle'});
  const H=await p.evaluate(()=>document.body.scrollHeight);
  for(let y=0;y<H;y+=500){ await p.evaluate(v=>scrollTo(0,v),y); await p.waitForTimeout(80); }
  await p.waitForTimeout(700);
  const r = await p.evaluate(()=>({
    broken:[...document.querySelectorAll('img')].filter(i=>i.naturalWidth===0&&i.getAttribute('src')).length,
    overflow: document.documentElement.scrollWidth>document.documentElement.clientWidth,
    footer: !!document.querySelector('footer.ft'),
    h: Math.round(document.body.scrollHeight),
  }));
  const ok = !r.broken && !r.overflow && !miss.length && !errs.length;
  if(!ok) bad++;
  console.log(`  ${f.padEnd(24)} ${String(r.h).padStart(5)}px  broken:${r.broken}  overflow:${r.overflow}  foot:${r.footer?'y':'N'}  ${ok?'✓':'✗'}`,
              miss.slice(0,2).join(' ')||'', errs.slice(0,1).join('')||'');
  await p.close();
}
await b.close();
console.log(bad ? `\n${bad} page(s) with problems` : '\nall render clean');
