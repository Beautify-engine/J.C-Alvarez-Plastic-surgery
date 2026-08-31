/* ---- motion: scroll reveals + magnetic CTA ----
   Gated on prefers-reduced-motion; elements are visible by default if JS never runs. */
(function(){
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var targets=[].slice.call(document.querySelectorAll('[data-rise],[data-rise-group]'));
  if(reduce || !('IntersectionObserver' in window)){
    targets.forEach(function(el){ el.classList.add('in'); });
  } else {
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); }
      });
    },{rootMargin:'0px 0px -12% 0px', threshold:0.12});
    targets.forEach(function(el){ io.observe(el); });
  }

  // magnetic primary CTA — pointer only, small displacement, snaps back
  if(!reduce && matchMedia('(hover:hover) and (pointer:fine)').matches){
    [].slice.call(document.querySelectorAll('.btn,.loc__cta')).forEach(function(b){
      b.addEventListener('pointermove',function(e){
        var r=b.getBoundingClientRect();
        var x=(e.clientX-(r.left+r.width/2))/r.width;
        var y=(e.clientY-(r.top+r.height/2))/r.height;
        b.style.transform='translate('+(x*6).toFixed(2)+'px,'+(y*4).toFixed(2)+'px)';
      });
      b.addEventListener('pointerleave',function(){ b.style.transform=''; });
    });
  }
})();

// LCP is the poster image. Video is fetched only after load, only if motion is welcome,
// and never on a metered/slow connection. (CLAUDE.md §6, DECISIONS D-005)
(function(){
  var v=document.getElementById('heroVid');
  if(!v) return;
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)');
  var c=navigator.connection||{};
  if(reduce.matches||c.saveData===true||/2g/.test(c.effectiveType||'')) return;
  function start(){
    // Two cuts exist: 16:9 for desktop, a purpose-built 9:16 for phones (D-039).
    // `media` on <source> is only honoured inside <picture>, never inside <video>,
    // so the choice is made here — which also means the unused cut is never fetched.
    if(!v.querySelector('source')){
      var mob=window.matchMedia('(max-width: 48rem)').matches;
      var srcs=mob?[['/video/hero-m-608.webm','video/webm'],['/video/hero-m-608.mp4','video/mp4']]
                  :[['/video/hero-1600.webm','video/webm'],['/video/hero-1920.mp4','video/mp4']];
      srcs.forEach(function(s){
        var el=document.createElement('source'); el.src=s[0]; el.type=s[1]; v.appendChild(el);
      });
    }
    v.preload='auto';
    v.addEventListener('canplay',function(){v.classList.add('is-ready');v.play().catch(function(){});},{once:true});
    v.load();
  }
  if(document.readyState==='complete') start();
  else window.addEventListener('load',start,{once:true});
})();

// Sticky mobile CTA reveals only once the hero CTA has scrolled away,
// so exactly one primary CTA is ever on screen (CLAUDE.md §5.5).
(function(){
  var bar=document.querySelector('.cta-bar'), anchor=document.querySelector('.hero__cta');
  if(!bar||!anchor||!('IntersectionObserver' in window)) return;
  new IntersectionObserver(function(e){
    bar.classList.toggle('is-shown',!e[0].isIntersecting);
  },{threshold:0}).observe(anchor);
})();

/* Option A — classic track. Arrows page by one viewport; state reflects scroll position. */
(function(){
  var trk=document.getElementById('trk'); if(!trk) return;
  var prev=document.querySelector('[data-trk="prev"]'), next=document.querySelector('[data-trk="next"]');
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  function page(dir){
    var item=trk.querySelector('.trk__item');
    var step=item? item.getBoundingClientRect().width + 16 : trk.clientWidth;
    var n=Math.max(1,Math.floor(trk.clientWidth/step));
    trk.scrollBy({left:dir*step*n, behavior: reduce?'auto':'smooth'});
  }
  function sync(){
    var max=trk.scrollWidth-trk.clientWidth-2;
    prev.disabled = trk.scrollLeft<=2;
    next.disabled = trk.scrollLeft>=max;
  }
  prev.addEventListener('click',function(){page(-1);});
  next.addEventListener('click',function(){page(1);});
  trk.addEventListener('scroll',sync,{passive:true});
  trk.addEventListener('keydown',function(e){
    if(e.key==='ArrowRight'){e.preventDefault();page(1);}
    if(e.key==='ArrowLeft'){e.preventDefault();page(-1);}
  });
  sync(); addEventListener('resize',sync);
})();


/* Results — infinite coverflow. Blur carries depth; nothing auto-advances. */
(function(){
  var flow=document.getElementById('resFlow'); if(!flow) return;
  var all=[].slice.call(flow.querySelectorAll('.res__case'));
  var btns=[].slice.call(document.querySelectorAll('.res__filters button'));
  var pos=document.getElementById('resPos');
  var list=all, at=0;
  function pad(n){ return String(n).padStart(2,'0'); }
  function layout(){
    var n=list.length;
    var span=Math.min(3, Math.floor((n-1)/2));   // never let one case appear twice in the ring
    all.forEach(function(el){ el.style.display='none'; el.removeAttribute('data-off'); el.tabIndex=-1; });
    list.forEach(function(el,i){
      var d=i-at;
      if(d> n/2) d-=n;
      if(d<-n/2) d+=n;
      var ad=Math.abs(d);
      if(ad>span){ el.style.display='none'; return; }
      el.style.display='block';
      el.setAttribute('data-off', String(Math.max(-2,Math.min(2,d))));
      el.style.zIndex=String(10-ad);
      el.style.transform='translateX('+(d*(ad>1?34:30)-50)+'%) translateZ('+(-ad*170)+'px) rotateY('+(d*-22)+'deg) scale('+(1-Math.min(ad*0.10,0.34))+')';
      el.style.filter = ad===0 ? 'none' : 'blur('+Math.min(ad*4,12)+'px)';
      el.style.opacity = (ad>=span && span>2) ? 0 : 1;
      el.tabIndex = ad===0 ? 0 : -1;
      el.setAttribute('aria-hidden', String(d!==0));
    });
    pos.textContent = pad(at+1)+' / '+pad(n);
  }
  function go(i){ at=(i+list.length)%list.length; layout(); }
  document.getElementById('resPrev').addEventListener('click',function(){ go(at-1); });
  document.getElementById('resNext').addEventListener('click',function(){ go(at+1); });
  flow.addEventListener('click',function(e){
    var c=e.target.closest('.res__case'); if(!c) return;
    var i=list.indexOf(c); if(i>-1&&i!==at) go(i);
  });
  flow.addEventListener('keydown',function(e){
    if(e.key==='ArrowRight'){e.preventDefault();go(at+1);}
    if(e.key==='ArrowLeft'){e.preventDefault();go(at-1);}
  });
  btns.forEach(function(b){
    b.addEventListener('click',function(){
      btns.forEach(function(x){ x.setAttribute('aria-pressed', String(x===b)); });
      var f=b.dataset.filter;
      list = f==='all' ? all : all.filter(function(el){ return el.dataset.procedure===f; });
      at=0; layout();
    });
  });
  layout();
})();


/* Reels — only the centred card ever holds a video source. Seven live <video>
   elements would wreck memory and LCP on a phone. */
(function(){
  var track=document.getElementById('reelTrack'); if(!track) return;
  var items=[].slice.call(track.querySelectorAll('.reel__item'));
  var prev=document.getElementById('reelPrev'), next=document.getElementById('reelNext');
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;

  function activate(li){
    items.forEach(function(o){
      var v=o.querySelector('video');
      if(o===li) return;
      if(o.classList.contains('is-live')){
        o.classList.remove('is-live');
        v.classList.remove('on');
        try{ v.pause(); v.removeAttribute('src'); v.load(); }catch(e){}
      }
    });
    if(!li || li.classList.contains('is-live')) return;
    li.classList.add('is-live');
    var v=li.querySelector('video');
    if(reduce) return;                       // poster only under reduced motion
    if(!v.getAttribute('src')) v.src=v.dataset.src;
    v.addEventListener('canplay',function(){ v.classList.add('on'); },{once:true});
    var p=v.play(); if(p&&p.catch) p.catch(function(){});
  }

  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.intersectionRatio>0.85) activate(e.target); });
    },{root:track, threshold:[0,0.85,1]});
    items.forEach(function(li){ io.observe(li); });
  } else { activate(items[0]); }

  function page(dir){
    var w=items[0].getBoundingClientRect().width+16;
    track.scrollBy({left:dir*w, behavior: reduce?'auto':'smooth'});
  }
  function sync(){
    var max=track.scrollWidth-track.clientWidth-2;
    prev.disabled=track.scrollLeft<=2; next.disabled=track.scrollLeft>=max;
  }
  prev.addEventListener('click',function(){ page(-1); });
  next.addEventListener('click',function(){ page(1); });
  track.addEventListener('scroll',sync,{passive:true});
  track.addEventListener('keydown',function(e){
    if(e.key==='ArrowRight'){e.preventDefault();page(1);}
    if(e.key==='ArrowLeft'){e.preventDefault();page(-1);}
  });
  // pause everything when the section leaves the viewport
  if('IntersectionObserver' in window){
    new IntersectionObserver(function(es){
      if(!es[0].isIntersecting) items.forEach(function(o){
        var v=o.querySelector('video'); try{ v.pause(); }catch(e){}
      });
    },{threshold:0}).observe(track.closest('.reel'));
  }
  sync(); addEventListener('resize',sync);
})();


/* Map facade — the Google embed is ~500KB of third-party script and cookies, so it
   only loads when someone actually asks for it. */
(function(){
  var box=document.getElementById('locMap'), btn=document.getElementById('locLoad');
  if(!box||!btn) return;
  btn.addEventListener('click',function(){
    var f=document.createElement('iframe');
    f.src=box.dataset.src;
    f.title='Map showing 8400 SW 8th St, 4th Floor, Miami, Florida';
    f.loading='lazy';
    f.referrerPolicy='strict-origin-when-cross-origin';
    f.setAttribute('allowfullscreen','');
    box.appendChild(f);
    btn.remove();
  });
})();
