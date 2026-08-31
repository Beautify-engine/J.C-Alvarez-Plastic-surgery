import { chromium } from 'playwright';
const sites = [
  ['shafer','https://www.shaferplasticsurgery.com/'],
  ['5c','https://5c.co/'],
  ['md','https://mdplasticsurgery.com/'],
];
const b = await chromium.launch();
for (const [name,url] of sites) {
  for (const [w,h,tag] of [[1440,900,'desktop'],[390,844,'mobile']]) {
    const ctx = await b.newContext({ viewport:{width:w,height:h}, deviceScaleFactor:1,
      userAgent:'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36' });
    const p = await ctx.newPage();
    try {
      await p.goto(url,{waitUntil:'domcontentloaded',timeout:60000});
      await p.waitForTimeout(6000);
      await p.screenshot({ path:`design/reference-shots/${name}-${tag}-hero.png` });
      // full page, capped
      await p.evaluate(()=>window.scrollTo(0,0));
      await p.screenshot({ path:`design/reference-shots/${name}-${tag}-full.png`, fullPage:true });
      console.log(`ok ${name} ${tag}`);
    } catch(e){ console.log(`FAIL ${name} ${tag}: ${e.message.slice(0,80)}`); }
    await ctx.close();
  }
}
await b.close();
