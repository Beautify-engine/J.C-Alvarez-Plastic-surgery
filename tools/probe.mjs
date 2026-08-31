import { chromium } from 'playwright';
import path from 'path';
const file = path.resolve(process.argv[2]);
const b = await chromium.launch();
const p = await b.newPage();
await p.setContent(`<video id="v" src="file://${file}" preload="metadata"></video>`);
const info = await p.evaluate(() => new Promise((res,rej)=>{
  const v=document.getElementById('v');
  v.onloadedmetadata=()=>res({duration:v.duration,w:v.videoWidth,h:v.videoHeight});
  v.onerror=()=>rej(new Error('decode failed'));
  setTimeout(()=>rej(new Error('timeout')),20000);
}));
console.log(JSON.stringify(info,null,2));
await b.close();
