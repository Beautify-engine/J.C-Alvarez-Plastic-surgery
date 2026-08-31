import { chromium } from 'playwright';
const b = await chromium.launch();
const sections = [['a','Option A'],['b','Option B'],['c','Option C']];
for (const [w,h,tag] of [[1440,900,'desktop'],[390,844,'mobile']]) {
  const ctx = await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:2});
  const p = await ctx.newPage();
  await p.goto('http://localhost:8787/carousels.html',{waitUntil:'networkidle'});
  await p.waitForTimeout(1200);
  // force lazy images to load, then wait for decode
  await p.evaluate(async () => {
    document.querySelectorAll('img[loading="lazy"]').forEach(i => { i.loading = 'eager'; });
    // explicitly decode every image so Chromium has a rasterized bitmap at capture time
    await Promise.all([...document.images].map(i => i.decode().catch(() => {})));
  });
  await p.waitForTimeout(1200);
  const secs = await p.locator('section.band').all();
  for (let i=0;i<secs.length;i++){
    await secs[i].scrollIntoViewIfNeeded();
    await p.waitForTimeout(900);
    await secs[i].screenshot({path:`design/shots/opt${'abc'[i]}-${tag}.png`});
    console.log(`opt${'abc'[i]}-${tag}`);
  }
  await ctx.close();
}
await b.close();
