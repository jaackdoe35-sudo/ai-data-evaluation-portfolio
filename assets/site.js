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

// Portfolio motion layer: progressive enhancement, accessible by default.
// If JavaScript or IntersectionObserver is unavailable, content remains visible.
const motionTargets = document.querySelectorAll(
  '.hero-copy, .about-band, .section-heading, .service-card, .tools-panel, .project-card, .process-grid > div, .evidence-card, .contact-inner, .page-hero .wrap, .arena-research-group, .other-research, .research-project-card'
);
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window) {
  document.documentElement.classList.add('js-motion');
  motionTargets.forEach((node, index) => {
    node.classList.add('motion-reveal');
    if (node.matches('.service-card,.project-card,.process-grid > div,.evidence-card,.research-project-card')) {
      node.dataset.motionDelay = String((index % 4));
    }
  });
  const motionObserver = new IntersectionObserver(entries => entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-visible');
      motionObserver.unobserve(entry.target);
    }
  }), {threshold: 0.08, rootMargin: '0px 0px -28px 0px'});
  motionTargets.forEach(node => motionObserver.observe(node));
}

// Desktop-only pointer light, deliberately disabled for touch and coarse pointers.
if (window.matchMedia('(hover:hover) and (pointer:fine)').matches) {
  const heroCopy = document.querySelector('.hero-copy');
  if (heroCopy) heroCopy.addEventListener('pointermove', event => {
    const rect = heroCopy.getBoundingClientRect();
    heroCopy.style.setProperty('--pointer-x', (event.clientX - rect.left) + 'px');
    heroCopy.style.setProperty('--pointer-y', (event.clientY - rect.top) + 'px');
  }, {passive:true});
}


(function(){
'use strict';
const reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const all=selector=>Array.from(document.querySelectorAll(selector));
// Consistent site-wide motion: target the real components used by every page.
const pageMotionTargets=all([
  'main > .page-hero .wrap',
  'main > .section > .wrap',
  '.section-head', '.section-heading', '.feature-grid > *', '.feature',
  '.timeline-item', '.cards > .card', '.project-list > .card',
  '.arena-banner', '.arena-grid > .arena-number', '.contact-grid > .contact-panel',
  '.case-grid > .case-panel', '.case-kpis > .case-kpi', '.case-index',
  '.guide-steps > *', '.service-grid > .service-card', '.evidence-grid > .evidence-card',
  '.tools-panel', '.process-grid > *', '.project-grid > .project-card'
].join(','));
if('IntersectionObserver' in window&&!reduced){
  document.documentElement.classList.add('site-motion-ready');
  pageMotionTargets.forEach((node,index)=>{
    node.classList.add('site-reveal');
    node.style.setProperty('--site-motion-delay',Math.min(index%4,3)*70+'ms');
  });
  const pageObserver=new IntersectionObserver(entries=>entries.forEach(entry=>{
    if(entry.isIntersecting){entry.target.classList.add('site-revealed');pageObserver.unobserve(entry.target);}
  }),{threshold:.07,rootMargin:'0px 0px -24px 0px'});
  pageMotionTargets.forEach(node=>pageObserver.observe(node));
}else pageMotionTargets.forEach(node=>node.classList.add('site-revealed'));

// Cross-page transitions are enabled globally, not only on pages with research diagrams.
if(!reduced&&document.startViewTransition){
  document.addEventListener('click',event=>{
    const link=event.target.closest('a[href]');
    if(!link||event.defaultPrevented||event.button!==0||event.metaKey||event.ctrlKey||event.shiftKey||event.altKey||link.target||link.hasAttribute('download'))return;
    const destination=new URL(link.href,location.href);
    if(destination.origin!==location.origin||destination.pathname===location.pathname)return;
    event.preventDefault();
    document.startViewTransition(()=>{location.href=destination.href;});
  });
}

})();
