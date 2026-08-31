import { chromium } from 'playwright';
const b = await chromium.launch();
for (const page of ['home','preparation','results']) {
  for (const [w,h,tag] of [[1440,900,'d'],[390,844,'m']]) {
    const p = await (await b.newContext({viewport:{width:w,height:h}})).newPage();
    const errs=[]; p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
    p.on('response',r=>{ if(r.status()>=400) errs.push(r.status()+' '+r.url().split('/').pop()); });
    await p.goto(`http://localhost:8787/_ghltest/${page}.html`,{waitUntil:'networkidle'});
    await p.evaluate(async () => {
      const tracks=[...document.querySelectorAll('*')].filter(e=>{
        const o=getComputedStyle(e).overflowX;
        return (o==='auto'||o==='scroll') && e.scrollWidth>e.clientWidth+40;});
      for (const t of tracks){ for(let x=0;x<=t.scrollWidth;x+=Math.max(200,t.clientWidth-60)){
        t.scrollLeft=x; await new Promise(r=>setTimeout(r,80));} t.scrollLeft=0; }
    });
    const H=await p.evaluate(()=>document.body.scrollHeight);
    for(let y=0;y<Math.min(H,9000);y+=500){ await p.evaluate(v=>scrollTo(0,v),y); await p.waitForTimeout(90); }
    await p.evaluate(()=>scrollTo(0,0)); await p.waitForTimeout(1800);
    const r = await p.evaluate(()=>{
      const cs=e=>e?getComputedStyle(e):null;
      const chrome=document.querySelector('.ghl-chrome');
      const hostP=document.querySelector('body > p');
      const sec=document.querySelector('.jca > main > section') || document.querySelector('.jca section');
      const v=document.getElementById('heroVid');
      return {
        hostChromeBg: cs(chrome).backgroundColor,
        hostFont: cs(hostP).fontFamily.split(',')[0],
        ourFont: cs(document.querySelector('.jca h1, .jca h2')).fontFamily.split(',')[0],
        sectionW: Math.round(sec.getBoundingClientRect().width),
        viewportW: window.innerWidth,
        docOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
        video: v ? {w:v.videoWidth, playing:!v.paused} : null,
        // lazy images parked off-screen have legitimately not loaded; only count
        // ones that are actually in view (same rule as tools/artverify.mjs)
        brokenImgs: [...document.querySelectorAll('.jca img')].filter(i=>{
          if (i.naturalWidth !== 0 || !i.getAttribute('src')) return false;
          if (i.loading !== 'lazy') return true;
          const r = i.getBoundingClientRect();
          return r.width > 0 && r.bottom > 0 && r.top < innerHeight && r.right > 0 && r.left < innerWidth;
        }).length,
      };
    });
    const bleedOK = r.sectionW >= r.viewportW - 2;
    console.log(`${page}/${tag}`, JSON.stringify(r), bleedOK && !r.docOverflow && !r.brokenImgs && !errs.length ? '✓' : '✗', errs.slice(0,2));
    await p.close();
  }
}
await b.close();
