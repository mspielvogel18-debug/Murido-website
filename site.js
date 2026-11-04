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
    if(!reduce){var k=0;timer=setInterval(function(){k=(k+1)%tabs.length;sel(tabs[k]);},11000);tl.addEventListener('mouseenter',function(){clearInterval(timer);});}
  });
})();
(function(){var b=document.querySelectorAll('.theme-toggle');b.forEach(function(x){x.addEventListener('click',function(){var r=document.documentElement,t=r.getAttribute('data-theme')==='dark'?'light':'dark';r.setAttribute('data-theme',t);try{localStorage.setItem('theme',t);}catch(e){}});});})();
// theme-color sync for iOS Safari top bar
(function(){function sync(){var d=document.documentElement.getAttribute('data-theme')==='dark';document.querySelectorAll('meta[name=theme-color]').forEach(function(m){m.setAttribute('content',d?'#121A2B':'#F2EAE0');});}sync();new MutationObserver(sync).observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});})();
// phone chat mockups
(function(){var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
function run(ph){if(ph._t)ph._t.forEach(clearTimeout);ph._t=[];var steps=[].slice.call(ph.querySelectorAll('.step'));
 steps.forEach(function(s){s.classList.remove('show','gone');if(s.dataset.type!==undefined){s.textContent=reduce?s.dataset.type:'';}});
 if(reduce){steps.forEach(function(s){s.classList.add('show');});return;}
 var t=500;function at(ms,f){ph._t.push(setTimeout(f,ms));}
 steps.forEach(function(s){if(s.dataset.type!==undefined){var txt=s.dataset.type;at(t,function(){s.classList.add('show');});for(var i=1;i<=txt.length;i++){(function(i){at(t+i*38,function(){s.textContent=txt.slice(0,i);});})(i);}t+=txt.length*38+500;}
 else if(s.classList.contains('dots')){at(t,function(){s.classList.add('show');});t+=1400;at(t,function(){s.classList.add('gone');});}
 else{at(t,function(){s.classList.add('show');});t+=600;}});}
document.querySelectorAll('.panel').forEach(function(p){var ph=p.querySelector('.phone');if(!ph)return;if(p.classList.contains('active'))run(ph);new MutationObserver(function(){if(p.classList.contains('active'))run(ph);}).observe(p,{attributes:true,attributeFilter:['class']});});})();
