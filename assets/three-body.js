(function(){
  'use strict';
  var events=[].slice.call(document.querySelectorAll('.event')),last='',queued=false;
  function sync(){queued=false;if(!events.length||events[0].getBoundingClientRect().top>innerHeight*.8)return;var active=events[0];events.forEach(function(e){if(e.getBoundingClientRect().top<=innerHeight*.3)active=e;});if(last===active.id)return;last=active.id;try{localStorage.setItem('story-atlas:three-body',JSON.stringify({event:active.id,title:active.querySelector('h2').textContent,updated:Date.now()}));}catch(e){}}
  function queue(){if(!queued){queued=true;requestAnimationFrame(sync);}}
  addEventListener('scroll',queue,{passive:true});addEventListener('load',queue);queue();
})();
