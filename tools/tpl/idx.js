
(function(){
  'use strict';

  var events   = Array.prototype.slice.call(document.querySelectorAll('.event'));
  var track    = document.getElementById('tlTrack');
  var viewport = document.getElementById('railViewport');
  var axis     = document.getElementById('tlAxis');
  var fill     = document.getElementById('tlFill');
  var railNow  = document.getElementById('railNow');
  var railIdx  = document.getElementById('railIdx');
  var railBar  = document.getElementById('railBar');
  var topBar   = document.getElementById('topBar');
  var floatTtl = document.getElementById('floatTitle');
  var railEl   = document.getElementById('rail');

  if (!events.length) return;

  /* ---------- 构建时间线节点 ---------- */
  var lastEra = '';
  events.forEach(function(el){
    var era = el.getAttribute('data-era') || '';
    if (era !== lastEra){
      var tag = document.createElement('div');
      tag.className = 'tl-era';
      tag.textContent = era;
      track.appendChild(tag);
      lastEra = era;
    }
    var color = el.getAttribute('data-color') || '#8c2b26';
    var label = el.getAttribute('data-label') || '';
    var seg = label.split(' · ');
    var when = seg[0];
    var place = seg.slice(1).join(' · ');
    var name = el.getAttribute('data-short') || '';
    var sub = name;
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'tl-node';
    btn.setAttribute('data-target', el.id);
    btn.style.setProperty('--c', color);
    btn.innerHTML =
      '<span class="dot"></span>' +
      '<span class="txt"><b>' + when + '</b>' +
      '<i>' + sub + '</i></span>';
    btn.addEventListener('click', function(){
      var y = el.getBoundingClientRect().top + window.pageYOffset - window.innerHeight * 0.16;
      window.scrollTo({ top: Math.max(0, y), behavior: 'smooth' });
    });
    track.appendChild(btn);
  });

  var nodes = Array.prototype.slice.call(track.querySelectorAll('.tl-node'));
  var total = nodes.length;

  /* ---------- 状态 ---------- */
  var active = -1;
  var curY = 0, tgtY = 0, raf = null;
  var railOK = false;

  function nodeCenter(n){ return n.offsetTop + n.offsetHeight / 2; }

  function measure(){
    railOK = viewport && viewport.clientHeight > 80;
    if (!railOK) return null;
    var H = viewport.clientHeight;
    var first = nodeCenter(nodes[0]);
    var lastEl = nodes[total - 1];
    var last = nodeCenter(lastEl);
    axis.style.top = first + 'px';
    axis.style.height = Math.max(0, last - first) + 'px';
    return { H: H, first: first, last: last, trackH: lastEl.offsetTop + lastEl.offsetHeight };
  }

  function loop(){
    raf = null;
    var d = tgtY - curY;
    curY += d * 0.17;
    if (Math.abs(d) < 0.4) curY = tgtY;
    track.style.transform = 'translate3d(0,' + curY.toFixed(2) + 'px,0)';
    if (Math.abs(tgtY - curY) > 0.4) raf = requestAnimationFrame(loop);
  }
  function kick(){ if (!raf) raf = requestAnimationFrame(loop); }

  /* ---------- 渲染 ---------- */
  function render(i){
    var g = measure();

    if (g){
      var center = nodeCenter(nodes[i]);
      var off = g.H * 0.44 - center;
      var minOff = Math.min(0, g.H - g.trackH - 18);
      off = Math.max(minOff, Math.min(0, off));
      tgtY = off;
      kick();

      fill.style.top = g.first + 'px';
      fill.style.height = Math.max(0, center - g.first) + 'px';
      fill.style.setProperty('--fc', events[i].getAttribute('data-color') || '#8c2b26');
    }

    for (var k = 0; k < total; k++){
      nodes[k].classList.toggle('active', k === i);
      nodes[k].classList.toggle('done', k < i);
    }

    var era = events[i].getAttribute('data-era') || '';
    var now = (events[i].getAttribute('data-label') || '').split(' · ')[0];
    if (railNow && railNow.textContent !== now){
      railNow.textContent = now;
      railNow.classList.remove('flip');
      void railNow.offsetWidth;
      railNow.classList.add('flip');
    }
    railIdx.textContent = i + 1 < 10 ? '0' + (i + 1) : String(i + 1);
    railBar.style.width = ((i + 1) / total * 100) + '%';
  }

  /* ---------- 滚动同步 ---------- */
  var ticking = false;

  function onScroll(){
    var docEl = document.documentElement;
    var max = docEl.scrollHeight - window.innerHeight;
    var p = max > 0 ? Math.min(1, Math.max(0, window.pageYOffset / max)) : 0;
    topBar.style.transform = 'scaleX(' + p.toFixed(4) + ')';

    if (railEl) railEl.classList.toggle('away', (max - window.pageYOffset) < 170);

    var line = window.innerHeight * 0.42;
    var idx = 0;
    for (var i = 0; i < total; i++){
      if (events[i].getBoundingClientRect().top <= line) idx = i;
    }
    if (window.innerHeight + window.pageYOffset >= docEl.scrollHeight - 4) idx = total - 1;

    if (idx !== active){ active = idx; render(idx); }
  }

  function requestSync(){
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function(){ ticking = false; onScroll(); });
  }

  window.addEventListener('scroll', requestSync, { passive: true });
  window.addEventListener('resize', function(){
    active = -1;
    curY = 0; tgtY = 0;
    track.style.transform = 'translate3d(0,0,0)';
    requestSync();
  });
  window.addEventListener('load', requestSync);

  /* ---------- 入场动画 ---------- */
  if ('IntersectionObserver' in window){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if (e.isIntersecting){
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.04 });
    events.forEach(function(el){ io.observe(el); });
  } else {
    events.forEach(function(el){ el.classList.add('in'); });
  }

  /* ---------- 初始化 ---------- */
  requestSync();
  if (document.fonts && document.fonts.ready){
    document.fonts.ready.then(function(){ active = -1; requestSync(); });
  }
  setTimeout(function(){ active = -1; requestSync(); }, 400);
})();
