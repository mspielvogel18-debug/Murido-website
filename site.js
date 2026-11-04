// Murido site interactions: reveal on scroll, sticky header, mobile menu, tabs.
(function(){
  var d=document.documentElement; d.classList.add('js');
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  // Stagger children of [data-stagger]
  document.querySelectorAll('[data-stagger]').forEach(function(g){
    Array.prototype.forEach.call(g.children,function(c,i){c.classList.add('reveal');c.style.setProperty('--d',(i*90)+'ms');});
  });
  var els=document.querySelectorAll('.reveal');
  if(reduce||!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('in');});}
  else{var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{rootMargin:'0px 0px -8% 0px',threshold:.08});els.forEach(function(e){io.observe(e);});}
  var h=document.querySelector('.site-header');
  function onS(){if(h)h.classList.toggle('scrolled',window.scrollY>8);} onS(); window.addEventListener('scroll',onS,{passive:true});
  var mb=document.querySelector('.menu-btn'),nav=document.getElementById('site-nav');
  if(mb&&nav){mb.addEventListener('click',function(){var o=nav.classList.toggle('open');mb.setAttribute('aria-expanded',o);});}
  document.querySelectorAll('[role=tablist]').forEach(function(tl){
    var tabs=tl.querySelectorAll('[role=tab]'),timer;
    function sel(t,focus){tabs.forEach(function(x){var on=x===t;x.setAttribute('aria-selected',on);x.tabIndex=on?0:-1;var p=document.getElementById(x.getAttribute('aria-controls'));p.classList.toggle('active',on);p.hidden=false;p.setAttribute('aria-hidden',!on);});if(focus)t.focus();}
    tabs.forEach(function(t,i){
      t.addEventListener('click',function(){clearInterval(timer);sel(t);});
      t.addEventListener('keydown',function(e){var n=null;if(e.key==='ArrowDown'||e.key==='ArrowRight')n=tabs[(i+1)%tabs.length];if(e.key==='ArrowUp'||e.key==='ArrowLeft')n=tabs[(i-1+tabs.length)%tabs.length];if(n){e.preventDefault();clearInterval(timer);sel(n,true);}});
    });
    if(!reduce){var k=0;timer=setInterval(function(){k=(k+1)%tabs.length;sel(tabs[k]);},6000);tl.addEventListener('mouseenter',function(){clearInterval(timer);});}
  });
})();
(function(){var b=document.querySelectorAll('.theme-toggle');b.forEach(function(x){x.addEventListener('click',function(){var r=document.documentElement,t=r.getAttribute('data-theme')==='dark'?'light':'dark';r.setAttribute('data-theme',t);try{localStorage.setItem('theme',t);}catch(e){}});});})();
