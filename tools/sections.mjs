import { chromium } from 'playwright';
const url = process.argv[2], w = +process.argv[3], tag = process.argv[4];
const out = process.argv[5];
const b = await chromium.launch();
const ctx = await b.newContext({viewport:{width:w,height:900},deviceScaleFactor:1});
const p = await ctx.newPage();
await p.goto(url,{waitUntil:'networkidle'});
await p.evaluate(()=>window.scrollTo(0,document.body.scrollHeight));
await p.waitForTimeout(800);
await p.evaluate(async()=>{
  document.querySelectorAll('img[loading="lazy"]').forEach(i=>i.loading='eager');
  document.querySelectorAll('[data-reveal]').forEach(e=>e.classList.add('is-in'));
  await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})));
});
await p.addStyleTag({content:'.cta-bar{display:none!important}.pidx{position:static!important}'});
await p.evaluate(()=>window.scrollTo(0,0));
await p.waitForTimeout(500);
const sels = process.argv[6].split(',');
for (const s of sels) {
  const el = await p.$(s);
  if (!el) { console.log('miss '+s); continue; }
  await el.screenshot({path:`${out}/${tag}-${s.replace(/[^a-z0-9]/gi,'')}.png`});
  console.log(s);
}
await b.close();
