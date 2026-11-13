(function(){
  'use strict';
  var book=window.BOOK;if(!book)return;
  var motion=matchMedia('(prefers-reduced-motion: reduce)');
  var switcher=document.getElementById('bookSwitch');
  if(switcher)switcher.addEventListener('change',function(){location.href=switcher.value;});
  var storeKey='story-atlas:'+book.id,previousProgress=null;
  try{previousProgress=JSON.parse(localStorage.getItem(storeKey)||'null');}catch(e){}
  function save(id){try{localStorage.setItem(storeKey,JSON.stringify({event:id,title:(book.events.find(function(e){return e.id===id;})||{}).title,updated:Date.now()}));}catch(e){}}
  var events=[].slice.call(document.querySelectorAll('.event'));
  if(events.length){
    var nav=[].slice.call(document.querySelectorAll('.chapter-rail a')),bar=document.getElementById('readingProgress'),active='',lastSaved='';
    function sync(){
      var target=innerHeight*.3,now=events[0];events.forEach(function(e){if(!e.hidden&&e.getBoundingClientRect().top<=target)now=e;});
      if(now.getBoundingClientRect().top<innerHeight*.8&&now.id!==lastSaved){lastSaved=now.id;save(now.id);}
      if(now.id!==active){active=now.id;nav.forEach(function(n){var on=n.hash==='#'+active;n.classList.toggle('active',on);if(on)n.setAttribute('aria-current','location');else n.removeAttribute('aria-current');});}
      if(bar){var max=document.documentElement.scrollHeight-innerHeight;bar.style.transform='scaleX('+Math.max(0,Math.min(1,max>0?scrollY/max:0))+')';}
    }
    var ticking=false;function requestSync(){if(ticking)return;ticking=true;requestAnimationFrame(function(){ticking=false;sync();});}
    addEventListener('scroll',requestSync,{passive:true});addEventListener('resize',requestSync);addEventListener('load',requestSync);requestSync();
    var jump=document.getElementById('chapterJump');if(jump)jump.addEventListener('change',function(){var el=document.getElementById(jump.value);if(el){save(el.id);el.scrollIntoView({behavior:motion.matches?'auto':'smooth',block:'start'});history.replaceState(null,'','#'+el.id);}});
    var search=document.getElementById('eventSearch');if(search)search.addEventListener('input',function(){
      var q=search.value.trim().toLocaleLowerCase(),count=0;
      events.forEach(function(el){var on=!q||el.textContent.toLocaleLowerCase().includes(q);el.hidden=!on;if(on)count++;});
      document.querySelectorAll('.era-divider[data-era]').forEach(function(el){el.hidden=!events.some(function(ev){return ev.dataset.era===el.dataset.era&&!ev.hidden;});});
      document.getElementById('eventSearchCount').textContent=count+' / '+events.length+' 个节点';document.getElementById('eventEmpty').hidden=count>0;
    });
    var resume=document.getElementById('resumeReading');if(resume&&previousProgress&&document.getElementById(previousProgress.event)){resume.href='#'+previousProgress.event;resume.textContent='继续上次：'+previousProgress.title;resume.hidden=false;}
  }
  var graph=document.getElementById('relationshipGraph');if(!graph)return;
  var NS='http://www.w3.org/2000/svg',byId={},nodes={},links=[],labels=[],current=null,trail=[],query='';
  book.people.forEach(function(p){byId[p.id]=p;});
  var adjacency={};book.people.forEach(function(p){adjacency[p.id]=[];});
  book.relations.forEach(function(r){adjacency[r.a].push({id:r.b,label:r.label});adjacency[r.b].push({id:r.a,label:r.label});});
  function svg(tag,attrs,text){var el=document.createElementNS(NS,tag);Object.keys(attrs).forEach(function(k){el.setAttribute(k,attrs[k]);});if(text)el.textContent=text;return el;}
  var edgeLayer=svg('g',{'aria-hidden':'true'}),labelLayer=svg('g',{'aria-hidden':'true'}),nodeLayer=svg('g',{});graph.append(edgeLayer,labelLayer,nodeLayer);
  book.relations.forEach(function(r){var line=svg('line',{'class':'relation-edge'}),label=svg('text',{'class':'relation-label'},r.label);edgeLayer.appendChild(line);labelLayer.appendChild(label);links.push(line);labels.push(label);});
  book.people.forEach(function(p){
    var g=svg('g',{'class':'person-node','data-id':p.id,role:'button',tabindex:'0','aria-label':p.name+'，'+p.role,'aria-pressed':'false'});g.appendChild(svg('circle',{r:'25'}));g.appendChild(svg('text',{y:'4'},p.name));g.addEventListener('click',function(){select(p.id);});g.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();select(p.id);}});nodeLayer.appendChild(g);nodes[p.id]=g;
  });
  function match(p){return !query||[p.name,p.role,p.deeds,(p.aliases||[]).join(' ')].join(' ').toLocaleLowerCase().includes(query);}
  function filterPeople(){document.querySelectorAll('.person-card').forEach(function(card){card.hidden=!match(byId[card.dataset.person]);});document.querySelectorAll('.people-group').forEach(function(group){group.hidden=!group.querySelector('.person-card:not([hidden])');});var count=book.people.filter(match).length;document.getElementById('peopleCount').textContent=count+' / '+book.people.length+' 位人物';document.getElementById('peopleEmpty').hidden=count>0;}
  function layout(){
    var positions={},visible={},neighbors=current?adjacency[current].map(function(r){return r.id;}):[];
    var list=current?neighbors:book.people.filter(match).map(function(p){return p.id;});
    if(current){positions[current]=[450,325];visible[current]=true;}
    list.forEach(function(id,i){var a=i/Math.max(1,list.length)*Math.PI*2-Math.PI/2,r=current?215:255;positions[id]=[450+Math.cos(a)*r,325+Math.sin(a)*r];visible[id]=true;});
    book.people.forEach(function(p){var node=nodes[p.id],on=!!visible[p.id],pos=positions[p.id]||[450,325];node.setAttribute('transform','translate('+pos[0]+','+pos[1]+')');node.style.display=on?'':'none';node.style.pointerEvents=on?'auto':'none';node.setAttribute('aria-hidden',String(!on));node.setAttribute('tabindex',on?'0':'-1');node.setAttribute('aria-pressed',String(current===p.id));node.classList.toggle('selected',current===p.id);node.querySelector('circle').setAttribute('r',current===p.id?34:current?28:25);});
    book.relations.forEach(function(r,i){var a=positions[r.a]||[450,325],b=positions[r.b]||[450,325],on=visible[r.a]&&visible[r.b],direct=current&&(r.a===current||r.b===current);links[i].setAttribute('x1',a[0]);links[i].setAttribute('y1',a[1]);links[i].setAttribute('x2',b[0]);links[i].setAttribute('y2',b[1]);links[i].style.display=on?'':'none';links[i].classList.toggle('direct',!!direct);labels[i].setAttribute('x',(a[0]+b[0])/2);labels[i].setAttribute('y',(a[1]+b[1])/2-8);labels[i].style.display=on&&direct?'':'none';});
    document.getElementById('graphCaption').textContent=current?byId[current].name+' · '+neighbors.length+' 位直接关联人物。点击相邻人物继续探索。':'选择一位人物，查看本页收录的直接关系。手机上可横向滑动关系图。';
  }
  var detail=document.getElementById('personDetail');
  function select(id,options){
    if(!byId[id])return;options=options||{};if(current&&current!==id&&!options.back)trail.push(current);if(!match(byId[id])){query='';personSearch.value='';filterPeople();}current=id;
    var person=byId[id];detail.replaceChildren();
    var role=document.createElement('div');role.className='role';role.textContent=person.group+' · '+person.role;
    var name=document.createElement('h2');name.textContent=person.name;name.tabIndex=-1;
    var deeds=document.createElement('p');deeds.textContent=person.deeds;detail.append(role,name,deeds);
    var rels=document.createElement('div');rels.className='person-relations';
    adjacency[id].forEach(function(r){var button=document.createElement('button'),label=document.createElement('span');button.type='button';button.appendChild(document.createTextNode(byId[r.id].name));label.textContent=r.label;button.appendChild(label);button.addEventListener('click',function(){select(r.id);});rels.appendChild(button);});
    if(!adjacency[id].length){var note=document.createElement('p');note.textContent='本页未收录其他直接关系。';rels.appendChild(note);}detail.appendChild(rels);
    var foot=document.createElement('div');foot.className='detail-links';
    var event=book.events.find(function(e){return (person.events||[]).includes(e.id);});if(event){var link=document.createElement('a');link.href='index.html#'+event.id;link.textContent='时间线 · '+event.title+' →';foot.appendChild(link);}
    var card=document.createElement('a');card.href='#p-'+id;card.textContent='人物卡片 ↓';foot.appendChild(card);
    if(trail.length){var back=document.createElement('button');back.type='button';back.textContent='← 上一人物';back.addEventListener('click',function(){select(trail.pop(),{back:true});});foot.appendChild(back);}detail.appendChild(foot);
    document.querySelectorAll('.person-card').forEach(function(c){c.classList.toggle('selected',c.id==='p-'+id);});
    history.replaceState(null,'','#p-'+id);layout();document.getElementById('peopleLive').textContent='已选择'+person.name+'，'+adjacency[id].length+'位关联人物';
    if(options.scroll){document.getElementById('relationMap').scrollIntoView({behavior:motion.matches?'auto':'smooth',block:'start'});}
  }
  function resetDetail(){detail.innerHTML='<div class="eyebrow">人物关系</div><h2>从一个人开始</h2><p>点选图中的人物，沿着亲缘、同盟与冲突，了解故事如何发生。</p>';document.querySelectorAll('.person-card').forEach(function(c){c.classList.remove('selected');});}
  document.getElementById('resetGraph').addEventListener('click',function(){current=null;trail=[];query='';personSearch.value='';filterPeople();layout();resetDetail();history.replaceState(null,'',location.pathname+location.search);});
  document.querySelectorAll('[data-show-person]').forEach(function(button){button.addEventListener('click',function(){select(button.dataset.showPerson,{scroll:true});});});
  var personSearch=document.getElementById('personSearch');personSearch.addEventListener('input',function(){query=personSearch.value.trim().toLocaleLowerCase();current=null;trail=[];filterPeople();resetDetail();layout();history.replaceState(null,'',location.pathname+location.search);});
  personSearch.addEventListener('keydown',function(e){if(e.key==='Enter'){var first=book.people.find(match);if(first)select(first.id,{scroll:true});}if(e.key==='Escape'){personSearch.value='';personSearch.dispatchEvent(new Event('input'));}});
  layout();var initial=location.hash.replace(/^#p-/,'');if(byId[initial])select(initial);
})();
