(()=>{'use strict';
const one=(selector,root=document)=>root.querySelector(selector);
const all=(selector,root=document)=>[...root.querySelectorAll(selector)];
const reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;

// Accessible mobile navigation: open, close on selection, and expose state to assistive tech.
const menu=one('.menu');
const navLinks=one('.nav .links');
if(menu&&navLinks){
  menu.addEventListener('click',()=>{
    const open=navLinks.classList.toggle('open');
    menu.setAttribute('aria-expanded',String(open));
    menu.setAttribute('aria-label',open?'Close navigation':'Open navigation');
  });
  all('a',navLinks).forEach(link=>link.addEventListener('click',()=>{
    navLinks.classList.remove('open');
    menu.setAttribute('aria-expanded','false');
    menu.setAttribute('aria-label','Open navigation');
  }));
  document.addEventListener('keydown',event=>{
    if(event.key==='Escape'&&navLinks.classList.contains('open')){
      navLinks.classList.remove('open');
      menu.setAttribute('aria-expanded','false');
      menu.focus();
    }
  });
}

// Reading progress and back-to-top affordance.
const progress=document.createElement('div');
progress.className='scroll-progress';
progress.setAttribute('aria-hidden','true');
document.body.append(progress);
const back=one('.backtop');
let ticking=false;
const update=()=>{
  const max=document.documentElement.scrollHeight-window.innerHeight;
  progress.style.transform='scaleX('+(max>0?window.scrollY/max:0)+')';
  if(back)back.classList.toggle('show',window.scrollY>500);
  ticking=false;
};
window.addEventListener('scroll',()=>{
  if(!ticking){window.requestAnimationFrame(update);ticking=true;}
},{passive:true});
update();
if(back)back.addEventListener('click',()=>window.scrollTo({top:0,behavior:reduced?'auto':'smooth'}));

// Subtle reveal only; no cursor-following glow, particles, tilt or magnetic motion.
const revealItems=all('.reveal');
if('IntersectionObserver'in window&&!reduced){
  const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{
    if(entry.isIntersecting){entry.target.classList.add('in');observer.unobserve(entry.target);}
  }),{threshold:.08,rootMargin:'0px 0px -24px 0px'});
  revealItems.forEach(item=>observer.observe(item));
}else revealItems.forEach(item=>item.classList.add('in'));

// Count up figures once when visible; static values remain available without JavaScript.
const counters=all('[data-count]');
if(counters.length&&!reduced&&'IntersectionObserver'in window){
  const countObserver=new IntersectionObserver(entries=>entries.forEach(entry=>{
    if(!entry.isIntersecting)return;
    const node=entry.target,target=Number(node.dataset.count);
    if(!Number.isFinite(target)){countObserver.unobserve(node);return;}
    const start=performance.now(),duration=850;
    const tick=now=>{
      const t=Math.min(1,(now-start)/duration);
      node.textContent=Math.round(target*(1-Math.pow(1-t,3))).toLocaleString();
      if(t<1)requestAnimationFrame(tick);else node.textContent=target.toLocaleString();
    };
    requestAnimationFrame(tick);countObserver.unobserve(node);
  }),{threshold:.6});
  counters.forEach(node=>countObserver.observe(node));
}
})();