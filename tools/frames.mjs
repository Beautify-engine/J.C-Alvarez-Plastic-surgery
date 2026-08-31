import { chromium } from 'playwright';
import path from 'path';
const file = path.resolve(process.argv[2]);
const b = await chromium.launch({args:['--autoplay-policy=no-user-gesture-required']});
const p = await b.newPage({viewport:{width:960,height:540}});
await p.setContent(`<body style="margin:0;background:#000">
<video id="v" width="960" height="540" src="file://${file}" muted preload="auto"></video></body>`);
await p.waitForFunction(()=>{const v=document.getElementById('v');return v.readyState>=2;},{timeout:120000});
const meta = await p.evaluate(()=>{const v=document.getElementById('v');return {d:v.duration,w:v.videoWidth,h:v.videoHeight};});
console.log('meta',JSON.stringify(meta));
for (const t of [0.5, 3, 6, 9, 12, 15, 18]) {
  await p.evaluate((tt)=>new Promise(r=>{const v=document.getElementById('v');v.onseeked=()=>r();v.currentTime=tt;}),t);
  await p.waitForTimeout(350);
  await p.locator('#v').screenshot({path:`/tmp/frames/f${String(t).padStart(4,'0')}.png`});
  console.log('frame',t);
}
await b.close();
