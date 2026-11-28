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
 const s=section('INTERACTIVE RISK → TEST → CONTROL MAP','Explore the assurance process by phase','Switch between risks, evaluation tests and controls. Select any item to see what it means, how it connects to the other phases and what evidence would help assess it.');
 const phases=[
  {key:'RISK',title:'01 · Identify risks',intro:'Start with the failure mode: what could go wrong, and what boundary might be crossed?',items:[
   ['Prompt injection','Untrusted content may influence the model’s governing instructions.','Indirect prompt-injection scenario','Instruction hierarchy and untrusted-input isolation','Adversarial input set · model response · instruction-following assessment'],
   ['Data exposure','The model may disclose information outside the permitted context.','Data-boundary probe','Scoped access and data minimization','Synthetic canary test · response capture · access-control logs'],
   ['Unsafe action','The model may take a consequential action without appropriate approval.','Action-confirmation scenario','Human approval and constrained tool permissions','Tool-call trace · approval record · resulting action state']
  ]},
  {key:'TEST',title:'02 · Evaluate behavior',intro:'Turn each risk hypothesis into a bounded test with observable pass/fail criteria.',items:[
   ['Indirect injection','Place untrusted instructions in content the model is asked to process.','Targets: Prompt injection','Expected: untrusted content is treated as data, not authority','Test input · model output · tool trace where applicable'],
   ['Data-boundary probe','Ask for synthetic information outside the permitted session or scope.','Targets: Data exposure','Expected: protected information is not disclosed','Synthetic canary · response capture · access decision'],
   ['Action confirmation','Request a consequential tool action and observe whether approval is required.','Targets: Unsafe action','Expected: action is held until required confirmation','Tool arguments · confirmation event · action state']
  ]},
  {key:'CONTROL',title:'03 · Assess controls',intro:'A control objective is a claim to test, not proof that a safeguard is effective.',items:[
   ['Instruction hierarchy','Keep higher-priority instructions authoritative and isolate untrusted content.','Addresses: Prompt injection','Test: Indirect injection','Versioned test cases · response samples · evaluator rationale'],
   ['Access restrictions','Constrain data and tool access to the user, session and task authorization.','Addresses: Data exposure','Test: Data-boundary probe','Permission configuration · access logs · synthetic data test'],
   ['Human approval','Require explicit review before consequential or sensitive actions.','Addresses: Unsafe action','Test: Action confirmation','Approval trail · tool-call record · action-state verification']
  ]}
 ];
 const panel=el('div','phase-explorer');
 const tabs=el('div','phase-tabs');tabs.setAttribute('role','tablist');tabs.setAttribute('aria-label','Risk, test and control phases');
 const content=el('div','phase-content');
 const left=el('div','phase-items');const detail=el('article','phase-detail');
 const detailEyebrow=el('div','eyebrow','SELECT AN ITEM');const title=el('h3','');const desc=el('p','');const relation=el('div','phase-relation');const evidence=el('div','visual-evidence');
 detail.append(detailEyebrow,title,desc,relation,evidence);
 let activePhase=0,activeItem=0;
 function render(){
  const phase=phases[activePhase];
  tabs.replaceChildren();
  phases.forEach((p,i)=>{const b=el('button','phase-tab');b.type='button';b.setAttribute('role','tab');b.setAttribute('aria-selected',String(i===activePhase));b.textContent=p.title;b.addEventListener('click',()=>{activePhase=i;activeItem=0;render();});tabs.append(b);});
  left.replaceChildren(el('p','phase-intro',phase.intro));
  phase.items.forEach((item,i)=>{const b=el('button','phase-item');b.type='button';b.setAttribute('aria-pressed',String(i===activeItem));b.append(el('span','phase-index','0'+(i+1)),el('strong','',item[0]),el('span','phase-chevron','↗'));b.addEventListener('click',()=>{activeItem=i;renderDetail();left.querySelectorAll('.phase-item').forEach((x,j)=>x.setAttribute('aria-pressed',String(j===i)));});left.append(b);});
  content.replaceChildren(left,detail);
  renderDetail();
 }
 function renderDetail(){
  const phase=phases[activePhase],item=phase.items[activeItem];
  detailEyebrow.textContent=phase.key+' PHASE · ITEM '+(activeItem+1);
  title.textContent=item[0];desc.textContent=item[1];
  relation.replaceChildren(el('div','phase-relation-label','CONNECTED WORK'));
  relation.append(el('div','phase-chip-row',item[2]),el('div','phase-chip-row',item[3]));
  evidence.textContent='EVIDENCE TO PRESERVE · '+item[4];
 }
 panel.append(tabs,content);s.append(panel);root.append(s);render();
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