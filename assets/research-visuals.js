(()=>{'use strict';
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
const $=(s,r=document)=>r.querySelector(s);
const el=(tag,cls,txt)=>{const n=document.createElement(tag);if(cls)n.className=cls;if(txt!==undefined)n.textContent=txt;return n;};
const svg=(tag,attrs={})=>{const n=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attrs).forEach(([k,v])=>n.setAttribute(k,v));return n;};
const section=(eyebrow,title,copy)=>{const s=el('section','deep-visual wrap');s.append(el('div','eyebrow',eyebrow),el('h2','',title),el('p','deep-visual-intro',copy));return s;};
const stages=[
 ['Scope','Confirm authorization, target system, boundaries and success criteria.','Authorization record · target/version · scope exclusions · acceptance criteria'],
 ['Reconnaissance','Map exposed capabilities, trust boundaries and available tools.','Capability inventory · trust-boundary notes · observed interfaces'],
 ['Attack attempt','Exercise one controlled hypothesis using a bounded test case.','Exact test input · run identifier · model/configuration · timestamp'],
 ['Observed behavior','Capture the actual response and any tool action or state change.','Raw output · tool trace · state evidence · reproducibility notes'],
 ['Evaluation','Compare observed behavior with the predefined success criteria.','Evaluator decision · rubric mapping · reviewer rationale'],
 ['Finding','Document impact, confidence, limitations and safe remediation.','Evidence-linked finding · impact statement · retest procedure']
];
function attackPath(root){
 const s=section('ATTACK-PATH EXPLORER','Follow a test from entry point to verified finding','A selectable, animated sequence showing how an authorized AI security test moves through trust boundaries. The diagram describes a research method, not a claim that every stage succeeded.');
 const frame=el('div','attack-frame');const graphic=svg('svg',{viewBox:'0 0 900 190',role:'img','aria-label':'Six connected stages from scope to finding'});
 const path=svg('path',{d:'M85 90 H815',class:'attack-track'});graphic.append(path);
 const prog=svg('path',{d:'M85 90 H815',class:'attack-progress'});graphic.append(prog);
 const nodes=[];stages.forEach((st,i)=>{const x=85+i*146;const g=svg('g',{class:'attack-node','data-index':i,tabindex:'0',role:'button','aria-label':st[0]});g.append(svg('circle',{cx:x,cy:90,r:27}),svg('text',{x,y:96,'text-anchor':'middle'},));const t=svg('text',{x,y:96,'text-anchor':'middle',class:'attack-number'});t.textContent=String(i+1).padStart(2,'0');g.append(t);const label=svg('text',{x,y:139,'text-anchor':'middle',class:'attack-label'});label.textContent=st[0];g.append(label);graphic.append(g);nodes.push(g);});
 frame.append(graphic);
 const controls=el('div','attack-controls');const prev=el('button','visual-control','← Previous');const next=el('button','visual-control','Next stage →');const status=el('span','visual-status','Stage 1 of 6');controls.append(prev,next,status);
 const detail=el('article','visual-detail');const dtitle=el('h3');const dcopy=el('p');const devidence=el('div','visual-evidence');detail.append(el('div','eyebrow','STAGE DETAIL'),dtitle,dcopy,devidence);
 let active=0;function set(i){active=Math.max(0,Math.min(stages.length-1,i));nodes.forEach((n,j)=>{n.classList.toggle('active',j===active);n.classList.toggle('complete',j<active);n.setAttribute('aria-pressed',String(j===active));});prog.style.strokeDasharray='730';prog.style.strokeDashoffset=String(730*(1-active/(stages.length-1)));dtitle.textContent=stages[active][0];dcopy.textContent=stages[active][1];devidence.textContent=stages[active][2];status.textContent='Stage '+(active+1)+' of '+stages.length;prev.disabled=active===0;next.disabled=active===stages.length-1;}
 prev.addEventListener('click',()=>set(active-1));next.addEventListener('click',()=>set(active+1));nodes.forEach((n,i)=>{n.addEventListener('click',()=>set(i));n.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();set(i);}});});
 frame.append(controls);s.append(frame,detail);root.append(s);set(0);
}
const risks=[
 ['Prompt injection','Untrusted instructions cross a content boundary.','Input isolation · instruction hierarchy enforcement','Adversarial prompt set · model response · policy adherence result'],
 ['Tool misuse','A model requests an action outside its authorization.','Tool allowlist · scoped permissions · confirmation gate','Tool-call trace · authorization decision · action log'],
 ['Data exposure','Protected content is returned to an unauthorized context.','Tenant/session checks · output filtering · data minimization','Synthetic canary test · access log · response capture'],
 ['Unsafe action','A consequential operation occurs without required approval.','Human approval · transaction preview · idempotency guard','Approval record · action state · audit trail'],
 ['Control drift','A previously effective safeguard stops behaving as expected.','Monitoring · regression suite · incident escalation','Versioned test results · alert history · remediation record']
];
function vulnerabilityMap(root){
 const s=section('INTERACTIVE VULNERABILITY & CONTROL MAP','Select a risk to inspect its safeguards','The map connects a vulnerability class to proposed controls and the evidence required to test those controls. These are evaluation design examples, not verified findings about a deployed system.');
 const layout=el('div','vuln-layout');const svgbox=el('div','vuln-graphic');const g=svg('svg',{viewBox:'0 0 700 380',role:'img','aria-label':'Risk categories linked to control objectives'});
 const positions=[[130,65],[350,65],[570,65],[230,290],[470,290]];
 const center=[350,185];
 positions.forEach((p,i)=>g.append(svg('path',{d:'M'+p[0]+' '+p[1]+' L'+center[0]+' '+center[1],class:'vuln-edge','data-risk':i})));
 g.append(svg('rect',{x:267,y:153,width:166,height:64,rx:15,class:'vuln-core'}));const core=svg('text',{x:350,y:190,'text-anchor':'middle',class:'vuln-core-label'});core.textContent='CONTROL LAYER';g.append(core);
 const buttons=[];risks.forEach((r,i)=>{const [x,y]=positions[i];const group=svg('g',{class:'vuln-point','data-risk':i,tabindex:'0',role:'button','aria-label':r[0]});group.append(svg('circle',{cx:x,cy:y,r:48}));const t=svg('text',{x,y:y+4,'text-anchor':'middle'});t.textContent='R'+(i+1);group.append(t);g.append(group);buttons.push(group);});
 svgbox.append(g);
 const list=el('div','vuln-list');const detail=el('article','visual-detail');detail.append(el('div','eyebrow','RISK → CONTROL → EVIDENCE'),el('h3'),el('p'),el('div','visual-evidence'));
 risks.forEach((r,i)=>{const b=el('button','vuln-select');b.type='button';b.textContent='R'+(i+1)+' · '+r[0];b.addEventListener('click',()=>choose(i));list.append(b);buttons[i].addEventListener('click',()=>choose(i));buttons[i].addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();choose(i);}});});
 function choose(i){list.querySelectorAll('button').forEach((b,j)=>b.setAttribute('aria-pressed',String(j===i)));buttons.forEach((b,j)=>b.classList.toggle('active',i===j));g.querySelectorAll('.vuln-edge').forEach((p,j)=>p.classList.toggle('active',i===j));const d=detail.querySelectorAll('h3,p,.visual-evidence');d[0].textContent=risks[i][0];d[1].textContent=risks[i][1];d[2].textContent='Control objective: '+risks[i][2]+'. Evidence to seek: '+risks[i][3]+'.';}
 layout.append(svgbox,list);s.append(layout,detail);root.append(s);choose(0);
}
const timelineItems=[
 ['Test plan approved','Scope, authorization and success criteria recorded.','Planning evidence'],
 ['Test case versioned','Prompt, expected behavior and rubric fixed for the run.','Design evidence'],
 ['Execution captured','Input, output, timestamp and tool trace preserved where available.','Execution evidence'],
 ['Outcome adjudicated','Observed behavior compared with predefined criteria.','Evaluation evidence'],
 ['Finding reviewed','Impact, confidence and limitations documented.','Review evidence'],
 ['Retest recorded','Remediation checked against the original acceptance criteria.','Closure evidence']
];
function evidenceTimeline(root){
 const s=section('INTERACTIVE EVIDENCE TIMELINE','Inspect the evidence lifecycle','Move through the milestones to see what a defensible research record should preserve. These are workflow milestones, not dates or claims that a particular project completed each one.');
 const box=el('div','evidence-timeline');const rail=el('div','timeline-rail');const fill=el('div','timeline-fill');rail.append(fill);
 timelineItems.forEach((item,i)=>{const b=el('button','timeline-stop');b.type='button';b.innerHTML='<span>'+(i+1)+'</span><small>'+item[0]+'</small>';b.addEventListener('click',()=>select(i));rail.append(b);});
 const detail=el('article','visual-detail timeline-detail');detail.append(el('div','eyebrow','MILESTONE'),el('h3'),el('p'),el('span','timeline-kind'));
 const nav=el('div','timeline-controls');const prev=el('button','visual-control','← Earlier');const next=el('button','visual-control','Later →');nav.append(prev,next);let current=0;
 function select(i){current=Math.max(0,Math.min(5,i));rail.querySelectorAll('.timeline-stop').forEach((b,j)=>{b.classList.toggle('active',j===current);b.classList.toggle('done',j<current);b.setAttribute('aria-pressed',String(j===current));});fill.style.width=(current/5*100)+'%';const d=detail.querySelectorAll('h3,p,.timeline-kind');d[0].textContent=timelineItems[current][0];d[1].textContent=timelineItems[current][1];d[2].textContent=timelineItems[current][2];prev.disabled=current===0;next.disabled=current===5;}
 prev.addEventListener('click',()=>select(current-1));next.addEventListener('click',()=>select(current+1));box.append(rail,detail,nav);s.append(box);root.append(s);select(0);
}
function evaluationViz(root){
 const s=section('ANIMATED EVALUATION VISUALIZATION','Turn a test rubric into observable dimensions','The animated bars below are a conceptual rubric view, not measured scores. They show how an evaluation can be decomposed into explicit dimensions without inventing model performance numbers.');
 const dims=[['Instruction hierarchy',84],['Tool authorization',68],['Data boundaries',77],['Secret handling',59],['Action confirmation',73]];
 const panel=el('div','eval-visual');const chart=svg('svg',{viewBox:'0 0 760 300',role:'img','aria-label':'Conceptual animated evaluation dimensions, not performance scores'});
 dims.forEach((d,i)=>{const y=40+i*50;const label=svg('text',{x:8,y:y+5,class:'eval-axis'});label.textContent=d[0];chart.append(label,svg('rect',{x:205,y:y-13,width:510,height:18,rx:9,class:'eval-track'}),svg('rect',{x:205,y:y-13,width:0,height:18,rx:9,class:'eval-bar','data-width':d[1]*5.1}));});
 const note=el('p','eval-disclaimer','Illustrative visual encoding only · no model scores or pass rates represented.');
 const replay=el('button','visual-control','Replay animation');replay.addEventListener('click',()=>animate(true));
 panel.append(chart,note,replay);s.append(panel);root.append(s);
 let observer;if('IntersectionObserver'in window&&!reduce){observer=new IntersectionObserver(entries=>{if(entries.some(e=>e.isIntersecting)){animate(false);observer.disconnect();}},{threshold:.25});observer.observe(panel);}else animate(false);
 function animate(force){chart.querySelectorAll('.eval-bar').forEach((b,i)=>{b.style.transition='none';b.setAttribute('width','0');void b.getBoundingClientRect();if(!reduce)b.style.transition='width '+(650+i*100)+'ms cubic-bezier(.2,.7,.2,1) '+(i*80)+'ms';b.setAttribute('width',b.dataset.width);});}
}
function methodologyDiagram(root){
 const s=section('INTERACTIVE METHODOLOGY','Explore the five-step evidence protocol','Select a phase to inspect its inputs, action and output. The sequence is designed to make each result reproducible and its limitations visible.');
 const data=[['Define','Inputs: system, authorization and research question.','Action: set scope, boundaries and success criteria.','Output: versioned test brief.'],['Design','Inputs: threat hypothesis and expected behavior.','Action: write controlled cases and scoring rubric.','Output: test specification and evaluation criteria.'],['Execute','Inputs: approved test plan and model configuration.','Action: run bounded trials and preserve raw observations.','Output: timestamped run record and artifacts.'],['Adjudicate','Inputs: raw observations and predefined rubric.','Action: classify pass, fail or inconclusive with rationale.','Output: evidence-linked decision.'],['Report','Inputs: adjudicated findings and limitations.','Action: explain impact, confidence and remediation.','Output: report and retest plan.']];
 const panel=el('div','method-map');const svgbox=svg('svg',{viewBox:'0 0 850 170',role:'img','aria-label':'Five connected methodology stages'});svgbox.append(svg('path',{d:'M80 65 H770',class:'method-line'}));const nodes=[];
 data.forEach((d,i)=>{const x=80+i*172;const g=svg('g',{class:'method-node',tabindex:'0',role:'button','aria-label':d[0]});g.append(svg('circle',{cx:x,cy:65,r:25}));const t=svg('text',{x,y:70,'text-anchor':'middle'});t.textContent='0'+(i+1);g.append(t);const l=svg('text',{x,y:118,'text-anchor':'middle',class:'method-label'});l.textContent=d[0];g.append(l);svgbox.append(g);nodes.push(g);});
 const detail=el('article','visual-detail method-detail');detail.append(el('div','eyebrow','PHASE DETAIL'),el('h3'),el('p'),el('p'),el('div','visual-evidence'));
 function choose(i){nodes.forEach((n,j)=>n.classList.toggle('active',i===j));const d=detail.querySelectorAll('h3,p,.visual-evidence');d[0].textContent=data[i][0];d[1].textContent=data[i][1];d[2].textContent=data[i][2];d[3].textContent=data[i][3];}
 nodes.forEach((n,i)=>{n.addEventListener('click',()=>choose(i));n.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();choose(i);}});});panel.append(svgbox,detail);s.append(panel);root.append(s);choose(0);
}
function riskTestControlNetwork(root){
 const s=section('ANIMATED RISK → TEST → CONTROL NETWORK','See how governance connects to evaluation','Select a risk, test or control node. The network highlights its relationships so visitors can follow a traceable assurance path. Relationships are illustrative mappings, not a claim of control effectiveness.');
 const graph=svg('svg',{viewBox:'0 0 900 430',role:'img','aria-label':'Interactive network linking AI risks, security tests and controls'});
 const mobile=matchMedia('(max-width: 700px)').matches;
 const cols=mobile?[180,180,180]:[150,450,750];
 const mobileYs=[120,280,440,650,810,970,1180,1340,1500];
 const desktopYs=[90,210,330];
 const nodeY=i=>mobile?mobileYs[i]:desktopYs[nodes[i][3]];
 if(mobile)graph.setAttribute('viewBox','0 0 360 1600');
 const nodes=[
 ['RISK','Prompt injection',0,0],['RISK','Data exposure',0,1],['RISK','Unsafe action',0,2],
 ['TEST','Indirect injection',1,0],['TEST','Data-boundary probe',1,1],['TEST','Action confirmation',1,2],
 ['CONTROL','Instruction hierarchy',2,0],['CONTROL','Access restrictions',2,1],['CONTROL','Human approval',2,2]
 ];
 const links=[[0,3],[0,6],[1,4],[1,7],[2,5],[2,8],[3,6],[4,7],[5,8],[3,7],[4,6]];
 const edges=[];links.forEach(([a,b])=>{const A=nodes[a],B=nodes[b],ya=nodeY(a),yb=nodeY(b);const curve=mobile?82:100;const p=svg('path',{d:'M'+cols[A[2]]+' '+ya+' C'+(cols[A[2]]+curve)+' '+(ya+(yb-ya)*.35)+' '+(cols[B[2]]-curve)+' '+(yb-(yb-ya)*.35)+' '+cols[B[2]]+' '+yb,class:'network-edge','data-a':a,'data-b':b});graph.append(p);edges.push(p);});
 const groups=[];nodes.forEach((n,i)=>{const g=svg('g',{class:'network-node',tabindex:'0',role:'button','aria-label':n[1]});g.append(svg('rect',{x:cols[n[2]]-(mobile?112:90),y:nodeY(i)-29,width:mobile?224:180,height:58,rx:14}));const t=svg('text',{x:cols[n[2]],y:nodeY(i)+5,'text-anchor':'middle'});t.textContent=n[1];g.append(t);const small=svg('text',{x:cols[n[2]],y:nodeY(i)-38,'text-anchor':'middle',class:'network-kind'});small.textContent=n[0];g.append(small);g.addEventListener('click',()=>select(i));g.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();select(i);}});graph.append(g);groups.push(g);});
 const legend=el('div','network-legend');['RISK','TEST','CONTROL'].forEach(x=>legend.append(el('span','',x)));const detail=el('article','visual-detail network-detail');detail.append(el('div','eyebrow','NETWORK SELECTION'),el('h3'),el('p'));
 function select(i){const connected=new Set([i]);links.forEach(([a,b])=>{if(a===i)connected.add(b);if(b===i)connected.add(a);});groups.forEach((g,j)=>{g.classList.toggle('active',connected.has(j));g.classList.toggle('dimmed',!connected.has(j));});edges.forEach(e=>{const on=Number(e.dataset.a)===i||Number(e.dataset.b)===i;e.classList.toggle('active',on);e.classList.toggle('dimmed',!on);});detail.querySelector('h3').textContent=nodes[i][1];detail.querySelector('p').textContent=nodes[i][0]+' node. Highlighted links show the related '+(nodes[i][0]==='RISK'?'tests and proposed controls':nodes[i][0]==='TEST'?'risk hypotheses and control objectives':'risk hypotheses and evaluation tests')+'. Select another node to trace a different path.';}
 const network=el('div','network-wrap');network.append(graph,legend);panelNetwork(s,network,detail);root.append(s);select(0);
}
function panelNetwork(s,network,detail){const p=el('div','network-panel');p.append(network,detail);s.append(p);}
function pageTransitions(){
 if(reduce||!document.startViewTransition)return;
 document.addEventListener('click',e=>{const a=e.target.closest('a[href]');if(!a||e.defaultPrevented||e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||a.target||a.hasAttribute('download'))return;const u=new URL(a.href,location.href);if(u.origin!==location.origin||u.pathname===location.pathname||u.hash&&u.pathname===location.pathname)return;e.preventDefault();document.startViewTransition(()=>{location.href=u.href;});});
}
const main=$('main');if(main){
 const path=location.pathname;
 if(path.endsWith('/research.html')){const anchor=$('.other-research',main)||$('.arena-research-group',main);if(anchor){attackPath(anchor);vulnerabilityMap(anchor);evidenceTimeline(anchor);evaluationViz(anchor);}}
 if(path.endsWith('/methodology.html')){const anchor=$('.timeline',main)||$('.section .wrap',main);if(anchor)methodologyDiagram(anchor);}
 if(path.endsWith('/governance.html')){const anchor=$('.section .wrap',main);if(anchor)riskTestControlNetwork(anchor);}
}
pageTransitions();
})();