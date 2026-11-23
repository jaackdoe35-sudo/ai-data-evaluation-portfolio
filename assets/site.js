(()=>{'use strict';
const one=(s,r=document)=>r.querySelector(s),all=(s,r=document)=>[...r.querySelectorAll(s)];
const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
const fine=matchMedia('(pointer:fine)').matches;
const menu=one('.menu'),links=one('.links');
if(menu&&links)menu.addEventListener('click',()=>{links.classList.toggle('open');menu.setAttribute('aria-expanded',links.classList.contains('open')?'true':'false')});
const observer=('IntersectionObserver'in window)?new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');observer.unobserve(e.target)}}),{threshold:.08,rootMargin:'0px 0px -35px 0px'}):null;
all('.reveal').forEach((el,i)=>{el.dataset.delay=String(i%4);observer?observer.observe(el):el.classList.add('in')});
const glow=one('.cursor-glow');
if(glow&&fine&&!reduced){let gx=innerWidth/2,gy=innerHeight/2,px=gx,py=gy;window.addEventListener('pointermove',e=>{gx=e.clientX;gy=e.clientY},{passive:true});const move=()=>{px+=(gx-px)*.12;py+=(gy-py)*.12;glow.style.left=px+'px';glow.style.top=py+'px';requestAnimationFrame(move)};move()}
const progress=document.createElement('div');progress.className='scroll-progress';document.body.append(progress);
const nav=one('.nav');let scrollTick=false;
const updateScroll=()=>{const max=document.documentElement.scrollHeight-innerHeight;progress.style.scale=(max>0?scrollY/max:0)+' 1';if(nav)nav.classList.toggle('scrolled',scrollY>12);const back=one('.backtop');if(back)back.classList.toggle('show',scrollY>500);scrollTick=false};
window.addEventListener('scroll',()=>{if(!scrollTick){requestAnimationFrame(updateScroll);scrollTick=true}},{passive:true});updateScroll();
const back=one('.backtop');if(back)back.addEventListener('click',()=>window.scrollTo({top:0,behavior:reduced?'auto':'smooth'}));
all('[data-tilt],.card,.feature,.timeline-item').forEach(el=>{
 if(!fine||reduced)return;
 el.addEventListener('pointermove',e=>{const r=el.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;const max=el.matches('[data-tilt]')?8:3;el.style.transform='perspective(1100px) rotateX('+(-y*max)+'deg) rotateY('+(x*max)+'deg) translateY(-4px)'},{passive:true});
 el.addEventListener('pointerleave',()=>el.style.transform='');
});
if(fine&&!reduced)all('.btn,.navcta').forEach(el=>{el.classList.add('magnetic');el.addEventListener('pointermove',e=>{const r=el.getBoundingClientRect(),x=(e.clientX-r.left-r.width/2)/r.width,y=(e.clientY-r.top-r.height/2)/r.height;el.style.transform='translate('+x*7+'px,'+y*6+'px)'},{passive:true});el.addEventListener('pointerleave',()=>el.style.transform='')});
// Animate verified numeric figures only when they enter the viewport.
const counters=all('[data-count]');
if(counters.length&&!reduced){const countObserver=new IntersectionObserver(entries=>entries.forEach(entry=>{if(!entry.isIntersecting)return;const node=entry.target,target=Number(node.dataset.count);if(!Number.isFinite(target)){countObserver.unobserve(node);return}const start=performance.now(),duration=1250;node.classList.add('counting');const tick=now=>{const t=Math.min(1,(now-start)/duration),ease=1-Math.pow(1-t,4);node.textContent=Math.round(target*ease).toLocaleString();if(t<1)requestAnimationFrame(tick);else node.textContent=target.toLocaleString()};requestAnimationFrame(tick);countObserver.unobserve(node)}),{threshold:.6});counters.forEach(n=>countObserver.observe(n))}
// Canvas particle field: restrained, lightweight, and disabled for reduced-motion users.
if(!reduced){const canvas=document.createElement('canvas');canvas.id='fx-canvas';canvas.setAttribute('aria-hidden','true');document.body.prepend(canvas);const ctx=canvas.getContext('2d');if(ctx){let w=0,h=0,dpr=1,pts=[],raf=0,visible=true;const mobile=matchMedia('(max-width:650px)').matches;const resize=()=>{w=innerWidth;h=innerHeight;dpr=Math.min(devicePixelRatio||1,mobile?1:1.5);canvas.width=w*dpr;canvas.height=h*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);const n=Math.min(mobile?24:48,Math.round(w*h/(mobile?24000:22000)));pts=Array.from({length:n},()=>({x:Math.random()*w,y:Math.random()*h,vx:(Math.random()-.5)*.24,vy:(Math.random()-.5)*.24,r:Math.random()*1.5+.5}))};const draw=()=>{if(!visible)return;ctx.clearRect(0,0,w,h);for(let i=0;i<pts.length;i++){const p=pts[i];p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>w)p.vx*=-1;if(p.y<0||p.y>h)p.vy*=-1;ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fillStyle='rgba(83,91,230,.55)';ctx.fill();for(let j=i+1;j<pts.length;j++){const q=pts[j],d=Math.hypot(p.x-q.x,p.y-q.y);if(d<115){ctx.beginPath();ctx.moveTo(p.x,p.y);ctx.lineTo(q.x,q.y);ctx.strokeStyle='rgba(112,81,230,'+(1-d/115)*.11+')';ctx.lineWidth=.7;ctx.stroke()}}}raf=requestAnimationFrame(draw)};resize();draw();addEventListener('resize',resize,{passive:true});document.addEventListener('visibilitychange',()=>{visible=!document.hidden;if(visible&&!raf)draw();else{cancelAnimationFrame(raf);raf=0}})}}
// Smooth cross-page transition where supported; normal navigation remains the fallback.
document.addEventListener('click',e=>{const a=e.target.closest('a');if(!a||a.target==='_blank'||a.origin!==location.origin||a.pathname===location.pathname||a.hash||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;if(document.startViewTransition){e.preventDefault();document.startViewTransition(()=>location.href=a.href)}});
})();