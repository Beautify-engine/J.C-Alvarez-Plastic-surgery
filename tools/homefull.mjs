import { chromium } from 'playwright';
const probe = async p => p.evaluate(()=>{
  const secs=[...document.querySelectorAll('main section')].map(s=>({
    cls:s.className.split(' ')[0],
    h:(s.querySelector('h1,h2')||{textContent:'(none)'}).textContent.trim().slice(0,40),
    px:Math.round(s.getBoundingClientRect().height)
  }));
  return {
    order: secs.map(s=>s.cls).join('>'),
    heads: secs.map(s=>s.h),
    reviews: document.querySelectorAll('.rev__q').length,
    cases: document.querySelectorAll('.res__case').length,
    reels: document.querySelectorAll('.reel video, .reel img').length,
    procs: document.querySelectorAll('.trk__fig img').length,
    footer: !!document.querySelector('footer.ft'),
    hero: (document.querySelector('.hA h1, .hero h1')||{textContent:''}).textContent.trim().slice(0,44),
    heroVid: (document.getElementById('heroVid')||{currentSrc:''}).currentSrc.split('/').pop(),
    faces: document.querySelectorAll('.faces img').length,
    facesRound: document.querySelector('.faces img') ? getComputedStyle(document.querySelector('.faces img')).borderRadius : null,
    brokenNow: [...document.querySelectorAll('img')].filter(i=>i.naturalWidth===0 && i.loading!=='lazy').length,
  };
});
const b = await chromium.launch(); let bad=0;
for (const [w,h,tag] of [[1440,900,'desktop'],[390,844,'mobile']]) {
  const out={};
  for (const [n,url] of [['dev','http://localhost:8787/'],['art','http://localhost:8787/_homechk.html']]) {
    const p=await (await b.newContext({viewport:{width:w,height:h}})).newPage();
    const errs=[]; p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
    await p.goto(url,{waitUntil:'networkidle'});
    await p.evaluate(()=>document.querySelectorAll('[data-rise],[data-reveal],[data-rise-group]').forEach(e=>e.classList.add('is-in')));
    const H=await p.evaluate(()=>document.body.scrollHeight);
    for(let y=0;y<H;y+=600){ await p.evaluate(v=>window.scrollTo(0,v),y); await p.waitForTimeout(110); }
    await p.waitForTimeout(900);
    out[n]=await probe(p);
    if(errs.length){console.log(tag,n,'ERRORS',errs.slice(0,3));bad++;}
    await p.close();
  }
  const diff=Object.keys(out.dev).filter(k=>JSON.stringify(out.dev[k])!==JSON.stringify(out.art[k]));
  console.log(`\n${tag}`);
  console.log('  dev', JSON.stringify(out.dev));
  console.log('  art', JSON.stringify(out.art));
  if(diff.length){console.log('  ✗ MISMATCH:',diff.join(', '));bad++;} else console.log('  ✓ matches');
}
await b.close(); process.exit(bad?1:0);
