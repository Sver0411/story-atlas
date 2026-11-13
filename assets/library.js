(function(){
  'use strict';
  var cards=[].slice.call(document.querySelectorAll('.book-card')),input=document.getElementById('librarySearch'),buttons=[].slice.call(document.querySelectorAll('[data-filter]')),filter='all';
  function render(){var q=input.value.trim().toLocaleLowerCase(),count=0;cards.forEach(function(card){var on=(filter==='all'||card.dataset.category===filter)&&(!q||card.dataset.search.toLocaleLowerCase().includes(q));card.hidden=!on;if(on)count++;});document.getElementById('bookCount').textContent=count+' / '+cards.length+' 部作品';document.getElementById('libraryEmpty').hidden=count>0;buttons.forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.filter===filter));});}
  input.addEventListener('input',render);buttons.forEach(function(b){b.addEventListener('click',function(){filter=b.dataset.filter;render();});});
  cards.forEach(function(card){try{var state=JSON.parse(localStorage.getItem('story-atlas:'+card.dataset.book)||'null');if(!state||!state.event)return;var link=card.querySelector('.continue-link');if(link){link.href=card.dataset.url+'#'+state.event;link.textContent='继续阅读 · '+state.title;link.hidden=false;}}catch(e){}});
  // 兼容最初三体首页的事件深链接。
  if(/^#e\d+$/.test(location.hash))location.replace('books/three-body/index.html'+location.hash);
})();
