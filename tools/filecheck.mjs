import { chromium } from 'playwright';
import { writeFileSync, readFileSync, mkdirSync } from 'fs';
/* The real test: open the exported HTML straight off disk with file://, no
   server, no asset host. This is what "just give me the html" actually means. */
mkdirSync('/tmp/jca-file', { recursive: true });
const blob = readFileSync('dist/ghl/home.html', 'utf8');
writeFileSync('/tmp/jca-file/home.html',
  '<!doctype html><html lang="en"><head><meta charset="utf-8">' +
  '<meta name="viewport" content="width=device-width,initial-scale=1"></head>' +
  '<body style="margin:0">\n' + blob + '\n</body></html>');

const probe = async p => p.evaluate(() => {
  const g = (s, prop) => { const e = document.querySelector(s); return e ? getComputedStyle(e)[prop] : null; };
  const h1 = document.querySelector('h1');
  return {
    h1font: g('h1','fontFamily').split(',')[0],
    h1size: g('h1','fontSize'),
    h1w:    Math.round(h1.getBoundingClientRect().width),
    h1h:    Math.round(h1.getBoundingClientRect().height),
    bodyfont: g('.res__lede','fontFamily').split(',')[0],
    ledeH:  Math.round(document.querySelector('.res__lede').getBoundingClientRect().height),
    faces:  document.fonts ? [...document.fonts].map(f=>f.family+':'+f.status).join(' ') : 'n/a',
  };
});
const b = await chromium.launch();
for (const [w,h,tag] of [[1440,900,'desktop'],[390,844,'mobile']]) {
  const out = {};
  for (const [n,url] of [['dev(server)','http://localhost:8787/'],
                         ['ghl(file://)','file:///tmp/jca-file/home.html']]) {
    const p = await (await b.newContext({viewport:{width:w,height:h}})).newPage();
    await p.goto(url,{waitUntil:'load'});
    await p.evaluate(()=>document.fonts && document.fonts.ready);
    await p.waitForTimeout(1500);
    out[n] = await probe(p); await p.close();
  }
  const keys = ['h1font','h1size','h1w','h1h','bodyfont','ledeH'];
  const diff = keys.filter(k=>JSON.stringify(out['dev(server)'][k])!==JSON.stringify(out['ghl(file://)'][k]));
  console.log(`\n${tag}`);
  for (const n of Object.keys(out)) console.log('  '+n.padEnd(13), JSON.stringify(out[n]));
  console.log(diff.length ? '  ✗ DIFFERS: '+diff.join(', ') : '  ✓ identical typography and metrics');
}
await b.close();
