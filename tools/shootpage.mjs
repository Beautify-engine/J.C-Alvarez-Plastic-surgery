import { chromium } from 'playwright';
const url = process.argv[2] || 'http://localhost:8787/';
const tag = process.argv[3] || 'home';
const b = await chromium.launch();
for (const [w,h,name] of [[1440,900,'desktop'],[390,844,'mobile']]) {
  const ctx = await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:1});
  const p = await ctx.newPage();
  await p.goto(url,{waitUntil:'networkidle',timeout:40000});
  await p.evaluate(()=>window.scrollTo(0,document.body.scrollHeight));
  await p.waitForTimeout(1200);
  await p.evaluate(async()=>{
    document.querySelectorAll('img[loading="lazy"]').forEach(i=>i.loading='eager');
    // reveals are IntersectionObserver-driven; a fullPage capture never scrolls
    // through, so without this every [data-reveal] block shoots at opacity 0
    document.querySelectorAll('[data-reveal]').forEach(e=>e.classList.add('is-in'));
    await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})));
  });
  // fullPage composites position:fixed elements at their scroll offset, which reads as a
  // layout bug that isn't there. Hide them for the full-page pass; use tools/viewport.mjs
  // to check sticky behaviour for real.
  await p.addStyleTag({content:'.cta-bar{display:none!important}'});
  await p.evaluate(()=>window.scrollTo(0,0));
  await p.waitForTimeout(900);
  await p.screenshot({path:`design/shots/${tag}-${name}.png`, fullPage:true});
  console.log(`${tag}-${name}`);
  await ctx.close();
}
await b.close();
