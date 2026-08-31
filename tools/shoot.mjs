import { chromium } from 'playwright';
const url = process.argv[2] || 'http://localhost:8787/';
const tag = process.argv[3] || 'hero';
const b = await chromium.launch();
for (const [w,h,name] of [[1440,900,'desktop'],[390,844,'mobile']]) {
  const ctx = await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:2});
  const p = await ctx.newPage();
  await p.goto(url,{waitUntil:'networkidle',timeout:30000});
  await p.waitForTimeout(2500);
  await p.screenshot({path:`design/shots/${tag}-${name}.png`});
  console.log(`shot ${tag}-${name}`);
  await ctx.close();
}
await b.close();
