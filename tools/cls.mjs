/* Measure CLS the way Lighthouse does: throttled network so the font swap actually
   happens after first paint, then sum layout-shift entries without recent input. */
import { chromium } from 'playwright';
const URLS = process.argv.slice(2);
const b = await chromium.launch();
for (const u of URLS) {
  const ctx = await b.newContext({viewport:{width:390,height:844}});
  const p = await ctx.newPage();
  const cdp = await ctx.newCDPSession(p);
  await cdp.send('Network.emulateNetworkConditions',
    {offline:false, downloadThroughput:1.6*1024*1024/8, uploadThroughput:750*1024/8, latency:150});
  await cdp.send('Emulation.setCPUThrottlingRate',{rate:4});
  await p.addInitScript(()=>{ window.__cls=0; window.__shifts=[];
    new PerformanceObserver(l=>{for(const e of l.getEntries()){
      if(!e.hadRecentInput){ window.__cls+=e.value;
        window.__shifts.push({v:+e.value.toFixed(4), t:Math.round(e.startTime)}); }}})
      .observe({type:'layout-shift', buffered:true}); });
  await p.goto(u,{waitUntil:'load',timeout:60000});
  await p.waitForTimeout(4000);
  await p.evaluate(()=>window.scrollTo(0,document.body.scrollHeight/3));
  await p.waitForTimeout(2000);
  const r = await p.evaluate(()=>({cls:window.__cls, shifts:window.__shifts.slice(0,4)}));
  const path = u.replace(/^https?:\/\/[^/]+/,'') || '/';
  console.log(`${path.padEnd(30)} CLS ${r.cls.toFixed(4)}  ${r.cls<0.05?'PASS':'FAIL (target <0.05)'}`);
  if (r.shifts.length) console.log('    largest shifts:', JSON.stringify(r.shifts));
  await ctx.close();
}
await b.close();
