/* Video library — topic filter + facade embeds (youtube-nocookie, click to load). */
(function(){
  var grid=document.getElementById('vidGrid'); if(!grid) return;
  var items=[].slice.call(grid.querySelectorAll('.vid__item'));
  var btns=[].slice.call(document.querySelectorAll('.vid__filters button'));

  btns.forEach(function(b){
    b.addEventListener('click',function(){
      btns.forEach(function(x){ x.setAttribute('aria-pressed', String(x===b)); });
      var f=b.dataset.f;
      items.forEach(function(li){
        li.classList.toggle('vid__hidden', !(f==='all'||li.dataset.topic===f));
      });
    });
  });

  grid.addEventListener('click',function(e){
    var btn=e.target.closest('.vid__play'); if(!btn) return;
    var frame=btn.closest('.vid__frame');
    var f=document.createElement('iframe');
    f.src='https://www.youtube-nocookie.com/embed/'+frame.dataset.id+'?autoplay=1&rel=0';
    f.title=btn.getAttribute('aria-label').replace(/^Play: /,'');
    f.allow='accelerometer; autoplay; encrypted-media; picture-in-picture';
    f.setAttribute('allowfullscreen','');
    frame.appendChild(f);
    btn.remove();
    var t=frame.querySelector('.vid__topic'); if(t) t.remove();
  });
})();
