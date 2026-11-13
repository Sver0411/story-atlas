# -*- coding: utf-8 -*-
import io, json, os, re, math, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subs_data import SUBS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDX_CSS = io.open(os.path.join(ROOT,'tools/tpl/idx.css'), encoding='utf-8').read()
IDX_JS = io.open(os.path.join(ROOT,'tools/tpl/idx.js'), encoding='utf-8').read()
CH_CSS = io.open(os.path.join(ROOT,'tools/tpl/chars.css'), encoding='utf-8').read()
CH_JS = io.open(os.path.join(ROOT,'tools/tpl/chars.js'), encoding='utf-8').read()

BOOKS = sorted([d for d in os.listdir(os.path.join(ROOT, 'books'))
                if d != 'three-body' and os.path.exists(os.path.join(ROOT, 'books', d, 'data.js'))])

QUOTES = {
    'monte-cristo': '人类的一切智慧，就包含在这四个字里面：等待和希望。',
    'solitude': '注定经受百年孤独的家族，不会有第二次机会在大地上出现。',
    'lotr': '道路不停向前延伸，从我脚下一直伸向远方。',
    'dune': '恐惧是思维的杀手。',
    'red-chamber': '满纸荒唐言，一把辛酸泪。都云作者痴，谁解其中味。',
    'three-kingdoms': '天下大势，分久必合，合久必分。',
    'water-margin': '太平本是将军定，不许将军见太平。',
    'journey-west': '心生，种种魔生；心灭，种种魔灭。',
    'to-live': '少年去游荡，中年想掘藏，老年做和尚。',
    'foundation': '暴力是无能者的最后手段。',
    'thrones': '在权力的游戏里，你不赢就得死。',
    'byakuyakou': '我的人生，从来就没有太阳，所以不怕失去。',
    'suspect-x': '有时候，一个人只要好好活着，就足以拯救某个人。',
}


DECOR = {
'suspect-x': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <g stroke="#9aa79c" stroke-width=".4" opacity=".55">
    <path d="M120 180 H480 M120 240 H480 M120 300 H480 M120 360 H480 M120 420 H480"/>
    <path d="M180 120 V480 M240 120 V480 M300 120 V480 M360 120 V480 M420 120 V480"/>
  </g>
  <path d="M100 300 H500" stroke="#7c8b80" stroke-width=".9"/>
  <path d="M300 110 V490" stroke="#7c8b80" stroke-width=".9"/>
  <path d="M150 440 Q225 200 300 300 Q375 400 450 160" fill="none" stroke="#4a5a52" stroke-width="1.3"/>
  <circle cx="300" cy="300" r="3.2" fill="#4a5a52"/>
  <path d="M352 348 l18 18 M370 348 l-18 18" stroke="#8c3a34" stroke-width="1.6"/>
</svg>''',
'byakuyakou': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <circle cx="300" cy="282" r="128" fill="none" stroke="#8e97a6" stroke-width="1"/>
  <circle cx="300" cy="282" r="128" fill="none" stroke="#8e97a6" stroke-width=".5" stroke-dasharray="2 10" transform="rotate(26 300 282)"/>
  <path d="M300 116 V66" stroke="#8e97a6" stroke-width=".7"/>
  <path d="M300 512 V462" stroke="#8e97a6" stroke-width=".7"/>
  <path d="M214 430 L292 316" stroke="#6f7787" stroke-width="1.2"/>
  <path d="M386 430 L308 316" stroke="#6f7787" stroke-width="1.2"/>
  <circle cx="207" cy="437" r="10" fill="none" stroke="#6f7787" stroke-width="1"/>
  <circle cx="393" cy="437" r="10" fill="none" stroke="#6f7787" stroke-width="1"/>
  <path d="M300 282 V196" stroke="#6f7787" stroke-width=".6" stroke-dasharray="3 8"/>
</svg>''',
'monte-cristo': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <g fill="none" stroke="#c2b9a8" stroke-width="1">
    <path d="M20 400 Q120 356 220 400 T420 400 T620 400"/>
    <path d="M20 452 Q120 408 220 452 T420 452 T620 452"/>
    <path d="M20 504 Q120 460 220 504 T420 504 T620 504"/>
  </g>
  <circle cx="352" cy="330" r="6" fill="#7a4d35"/>
  <path d="M118 206 Q236 262 352 330" fill="none" stroke="#7a4d35" stroke-width="1" stroke-dasharray="3 7"/>
  <circle cx="118" cy="206" r="11" fill="none" stroke="#7a4d35" stroke-width="1"/>
  <text x="118" y="180" text-anchor="middle" font-size="11" fill="#a89f8e" letter-spacing="3">MARSEILLE</text>
  <text x="352" y="306" text-anchor="middle" font-size="11" fill="#a89f8e" letter-spacing="3">IF</text>
</svg>''',
'solitude': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <g fill="none" stroke="#8f9a86" stroke-width="1">
    <circle cx="300" cy="300" r="58" stroke-dasharray="300 64"/>
    <circle cx="300" cy="300" r="108" stroke-dasharray="560 118" transform="rotate(38 300 300)"/>
    <circle cx="300" cy="300" r="158" stroke-dasharray="820 172" transform="rotate(76 300 300)"/>
    <circle cx="300" cy="300" r="208" stroke-dasharray="1080 226" transform="rotate(114 300 300)"/>
    <circle cx="300" cy="300" r="258" stroke-dasharray="1340 280" transform="rotate(152 300 300)"/>
  </g>
  <circle cx="300" cy="300" r="3" fill="#53664a"/>
</svg>''',
'lotr': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <path d="M110 540 L300 300 L490 540 Z" fill="none" stroke="#c0b39c" stroke-width="1"/>
  <path d="M170 540 L300 372 L430 540" fill="none" stroke="#c0b39c" stroke-width=".6" opacity=".6"/>
  <circle cx="300" cy="212" r="88" fill="none" stroke="#a8823c" stroke-width="1.4"/>
  <circle cx="300" cy="212" r="76" fill="none" stroke="#a8823c" stroke-width=".7" stroke-dasharray="2 7" opacity=".8"/>
  <path d="M300 246 Q316 222 300 196 Q284 222 300 246 Z" fill="none" stroke="#a8823c" stroke-width="1.1"/>
  <path d="M300 142 V96" stroke="#a8823c" stroke-width=".7" stroke-dasharray="2 8"/>
</svg>''',
'dune': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <circle cx="410" cy="176" r="52" fill="none" stroke="#c9a46a" stroke-width="1.2"/>
  <circle cx="410" cy="176" r="62" fill="none" stroke="#c9a46a" stroke-width=".6" opacity=".5"/>
  <g fill="none" stroke="#b79b74" stroke-width="1">
    <path d="M-20 392 Q120 316 260 392 T540 392 T820 392"/>
    <path d="M-20 448 Q140 372 300 448 T580 448 T860 448"/>
    <path d="M-20 506 Q160 430 340 506 T620 506 T900 506"/>
  </g>
</svg>''',
'red-chamber': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <circle cx="330" cy="300" r="172" fill="none" stroke="#c3a2a6" stroke-width="1.2"/>
  <circle cx="330" cy="300" r="160" fill="none" stroke="#c3a2a6" stroke-width=".6" opacity=".6"/>
  <path d="M330 472 V300" fill="none" stroke="#c3a2a6" stroke-width=".8" stroke-dasharray="2 8"/>
  <path d="M330 300 Q368 246 424 232" fill="none" stroke="#984b53" stroke-width="1.1"/>
  <g fill="#984b53">
    <circle cx="424" cy="232" r="4"/><circle cx="404" cy="252" r="3"/><circle cx="442" cy="252" r="3"/>
    <circle cx="392" cy="272" r="2.6"/>
  </g>
  <path d="M330 300 Q300 262 268 256" fill="none" stroke="#984b53" stroke-width="1" opacity=".7"/>
</svg>''',
}

PALETTE = ['#8c2b26', '#7a5a38', '#2f4a6b', '#5a3a6b', '#1f5d57', '#a8823c', '#4a4a58', '#6b645a']

# 每本书的插图：文件名, 图注, 插入到第几个事件（0-based）
IMAGES = {
    'monte-cristo': [
        ('monte-cristo.jpg', '马赛港 · 法老号归来的清晨'),
        ('monte-faria.jpg', '伊夫堡 · 法里亚神甫与那场漫长的授课'),
        ('monte-paris.jpg', '巴黎 · 客厅里的清算'),
    ],
    'solitude': [
        ('solitude.jpg', '马孔多 · 建村时的雨季与荒地'),
        ('solitude-rain.jpg', '下了四年十一个月零两天的雨'),
        ('solitude-train.jpg', '香蕉公司 · 驶向马孔多的列车'),
    ],
    'lotr': [
        ('lotr.jpg', '夏尔 · 出发前的最后一个清晨'),
        ('lotr-moria.jpg', '墨瑞亚 · 矿坑深处的黑暗'),
        ('lotr-volcano.jpg', '末日火山 · 最后一段路'),
        ('lotr-havens.jpg', '灰港 · 最后的船'),
    ],
    'dune': [
        ('dune.jpg', '厄拉科斯 · 沙海与香料'),
        ('dune-worm.jpg', '沙虫 · 沙漠深处的震动'),
        ('dune-water.jpg', '水 · 弗雷曼人最贵的东西'),
    ],
    'red-chamber': [
        ('red-chamber.jpg', '大观园 · 花影与回廊'),
        ('red-chamber-snow.jpg', '雪中的园子 · 盛景之后'),
        ('red-chamber-flowers.jpg', '葬花 · 花谢花飞'),
    ],
}


def load(book_id):
    s = io.open('%s/books/%s/data.js' % (ROOT, book_id), encoding='utf-8').read()
    body = s[s.index('{'):s.rindex('}') + 1]
    return json.loads(body)


def esc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


def subs_html(book_id, event_id):
    items = SUBS.get(book_id, {}).get(event_id)
    if not items:
        return ''
    out = []
    for i, (t, text) in enumerate(items):
        tag = ['其一', '其二', '其三', '其四'][i] if len(items) > 1 else '深读'
        out.append('<div class="ev-sub"><h3><span>%s</span>%s</h3><p>%s</p></div>' % (tag, esc(t), text))
    return ''.join(out)


def build_index(b):
    era_label = {e['id']: e['label'] for e in b['eras']}
    total = len(b['events'])
    people = len(b['people'])

    # 插图分配：均分到事件序列
    imgs = IMAGES.get(b['id'], [])
    slots = {}
    if imgs:
        step = max(1, total // (len(imgs) + 1))
        for i, (fn, cap) in enumerate(imgs):
            idx = min(total - 1, step * (i + 1))
            slots[idx] = (fn, cap)

    parts = []
    last_era = None
    for i, ev in enumerate(b['events']):
        era = ev['era']
        if era != last_era:
            parts.append(
                '\n    <div class="era-divider">\n      <span class="era-name">%s</span>\n'
                '      <span class="era-sub">%s</span>\n    </div>\n'
                % (esc(era_label.get(era, '')), '%02d — %02d' % (i + 1, total)))
            last_era = era
        label = ev['when'] + (' · ' + ev['place'] if ev.get('place') else '')
        parts.append(
            '\n    <section class="event" id="%s" style="--c:%s"\n'
            '      data-color="%s" data-era="%s" data-short="%s" data-label="%s">\n'
            '      <div class="ev-when">%s<em>%s</em></div>\n'
            '      <h2>%s</h2>\n      <p>%s</p>%s\n    </section>\n'
            % (ev['id'], b['accent'], b['accent'], esc(era_label.get(era, '')),
               esc(ev['title']), esc(label), esc(ev['when']), esc(ev.get('place', '')),
               esc(ev['title']), ev['text'], subs_html(b['id'], ev['id'])))
        if i in slots:
            fn, cap = slots[i]
            parts.append(
                '\n      <figure class="ev-fig"><img src="../../img/anthology/%s" alt="%s" loading="lazy">'
                '<figcaption>%s · 概念配图</figcaption></figure>\n' % (fn, esc(cap), esc(cap)))

    hero = '''<header class="masthead">
  <div class="hero-deco">%s</div>
  <div class="mast-inner">
    <p class="hero-kicker">%s</p>
    <h1><em>%s</em><span>时间线</span></h1>
    <p class="hero-deck">%s<br>%d 个时间点，从「%s」到「%s」。</p>
    <div class="hero-rule"></div>
    <div class="hero-meta">
      <span>%d 个时间点 · %d 位人物</span><i></i>
      <span>%s</span><i></i>
      <span>向下滚动</span>
    </div>
  </div>
  <div class="scroll-hint">SCROLL</div>
</header>''' % (DECOR.get(b['id'], ''), esc(b['author'].split('；')[0]), esc(b['title']), esc(b['description']),
                 total, esc(b['events'][0]['title']), esc(b['events'][-1]['title']),
                 total, people, esc(b['scope']))

    html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s · 时间线 | %(n)d 个故事节点</title>
<meta name="description" content="%(desc)s">
<style>%(css)s.foot-nav{display:flex;gap:26px;justify-content:center;margin-top:26px}
.foot-nav a{
  font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;
  color:var(--ink-3);text-decoration:none;border-bottom:1px solid transparent;
  padding-bottom:2px;transition:.3s;
}
.foot-nav a:hover{color:var(--ink);border-bottom-color:var(--ink)}
</style>
</head>
<body id="top">

<div class="top-progress"><i id="topBar"></i></div>
<nav class="topnav">
  <span class="nav-ind" aria-hidden="true"></span>
  <a href="../../index.html">书架</a>
  <a href="index.html" class="on">时间线</a>
  <a href="characters.html">人物志</a>
</nav>

%(hero)s

<main class="layout">
  <article class="content" id="content">
%(body)s
  </article>

  <aside class="rail" id="rail">
    <div class="rail-inner">
      <div class="rail-head">
        <div class="rail-topline">
          <span class="kicker">Current</span>
          <span class="rail-count"><b id="railIdx">01</b> / %(n)d</span>
        </div>
        <div class="rail-era" id="railNow">%(first)s</div>
      </div>
      <div class="rail-viewport" id="railViewport">
        <div class="tl-track" id="tlTrack">
          <div class="tl-axis" id="tlAxis"></div>
          <div class="tl-fill" id="tlFill"></div>
        </div>
      </div>
      <div class="rail-foot">
        <div class="rail-bar"><i id="railBar"></i></div>
        <div class="rail-hint">CHRONOLOGICAL ORDER</div>
      </div>
    </div>
  </aside>
</main>

<footer class="site-foot">
  <p class="q">“%(quote)s”</p>
  <p class="tiny">%(title)s · %(author)s　·　%(n)d 个时间点，%(people)d 位人物</p>
  <nav class="foot-nav">
    <a href="#top">回到开头</a>
    <a href="characters.html">看人物志</a>
    <a href="../../index.html">回书架</a>
  </nav>
</footer>

<script>%(js)s</script>
<script>
(function(){
  var nav=document.querySelector('.topnav');
  if(!nav) return;
  var on=nav.querySelector('.on'), ind=nav.querySelector('.nav-ind');
  if(!on||!ind) return;
  function place(){
    ind.style.width=on.offsetWidth+'px';
    ind.style.transform='translateX('+on.offsetLeft+'px)';
    ind.style.opacity='1';
  }
  requestAnimationFrame(function(){ requestAnimationFrame(place); });
  window.addEventListener('resize',place);
})();
</script>
</body>
</html>''' % dict(title=esc(b['title']), author=esc(b['author']), desc=esc(b['description']),
                  n=total, css=IDX_CSS, js=IDX_JS, hero=hero, body=''.join(parts),
                  first=esc(b['events'][0]['when']), quote=QUOTES.get(b['id'], ''), people=people)

    out = '%s/books/%s/index.html' % (ROOT, b['id'])
    io.open(out, 'w', encoding='utf-8').write(html)
    return len(html)


def layout_positions(people):
    """分簇布局：每个 group 聚成一团，簇心分布在大圆上。"""
    groups = []
    for p in people:
        g = p.get('group', '')
        if g not in groups:
            groups.append(g)
    buckets = {g: [p['id'] for p in people if p.get('group', '') == g] for g in groups}

    cx, cy = 620.0, 440.0
    K = len(groups)
    ring = 250.0 if K >= 5 else 225.0
    pos = {}
    meta = []

    for gi, g in enumerate(groups):
        ids = buckets[g]
        n = len(ids)
        # 簇心：大圆上均匀分布，从正上方开始
        ang = -math.pi / 2 + (gi / K) * math.pi * 2
        gx = cx + math.cos(ang) * ring
        gy = cy + math.sin(ang) * ring

        cr = max(48.0, min(172.0, 30 + n * 8))   # 簇半径随人数增长
        if n == 1:
            pos[ids[0]] = (gx, gy)
        elif n > 10:
            # 人数多的组走双圈：内圈 6 人，外圈其余
            inner, outer = ids[:6], ids[6:]
            for i, pid in enumerate(inner):
                a2 = -math.pi / 2 + (i / len(inner)) * math.pi * 2
                pos[pid] = (gx + math.cos(a2) * cr * 0.54, gy + math.sin(a2) * cr * 0.54)
            for i, pid in enumerate(outer):
                a2 = -math.pi / 2 + (i / len(outer)) * math.pi * 2 + 0.22
                pos[pid] = (gx + math.cos(a2) * cr, gy + math.sin(a2) * cr)
        else:
            for i, pid in enumerate(ids):
                a2 = -math.pi / 2 + (i / n) * math.pi * 2
                pos[pid] = (gx + math.cos(a2) * cr, gy + math.sin(a2) * cr)

        ly = gy - cr - 22
        meta.append(dict(name=g, x=gx, y=ly, count=n))
    return pos, meta


def short_name(name):
    if '·' in name:
        part = name.split('·')[-1].strip()
        if len(part) <= 5:
            return part
    return name if len(name) <= 5 else name[:5]


def name_size(name):
    n = len(name)
    if n <= 3:
        return 11
    if n == 4:
        return 10
    if n == 5:
        return 9
    return 8


def build_chars(b):
    people = b['people']
    by_id = {p['id']: p for p in people}

    # 人数过多时，关系网只取核心人物（每组按事件数排序取前若干），卡片仍列全部
    net_people = people
    if len(people) > 56:
        buckets = {}
        for p in people:
            buckets.setdefault(p.get('group', ''), []).append(p)
        for g in buckets:
            buckets[g].sort(key=lambda x: (-len(x.get('events') or []), x['name']))
        net_people = []
        quota = 6
        while len(net_people) < 52 and quota > 0:
            added = False
            for g, lst in buckets.items():
                for p in lst:
                    if p in net_people:
                        continue
                    if len([x for x in net_people if x.get('group') == g]) >= quota:
                        continue
                    net_people.append(p)
                    added = True
                    break
                if len(net_people) >= 52:
                    break
            if not added:
                quota -= 1
    net_ids = {p['id'] for p in net_people}
    pos, gmeta = layout_positions(net_people)

    # 分组颜色
    groups = []
    for p in people:
        g = p.get('group', '')
        if g not in groups:
            groups.append(g)
    color = {g: PALETTE[i % len(PALETTE)] for i, g in enumerate(groups)}

    group_tags = []
    for m in gmeta:
        group_tags.append('<text class="gtag" x="%.0f" y="%.0f" text-anchor="middle">%s</text>'
                          % (m['x'], m['y'], esc(m['name'])))

    links = []
    labels = []
    for rel in b['relations']:
        a, bb = rel['a'], rel['b']
        if a not in pos or bb not in pos:
            continue
        x1, y1 = pos[a]
        x2, y2 = pos[bb]
        links.append('<line class="plink" data-a="%s" data-b="%s" x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" '
                     'stroke="%s" stroke-width="0.9" opacity="0.32"/>'
                     % (a, bb, x1, y1, x2, y2, color[by_id[a].get('group', '')]))
        labels.append('<text class="rlabel" x="%.0f" y="%.0f" data-a="%s" data-b="%s">%s</text>'
                      % ((x1 + x2) / 2, (y1 + y2) / 2 - 4, a, bb, esc(rel['label'])))

    nodes = []
    for p in net_people:
        x, y = pos[p['id']]
        sn = short_name(p['name'])
        nodes.append('<g class="pnode" data-id="%s" transform="translate(%.0f,%.0f)">'
                     '<title>%s · %s</title>'
                     '<circle r="26" fill="#f7f4ed" stroke="%s" stroke-width="1.1"/>'
                     '<text class="pname" y="4" style="font-size:%dpx">%s</text></g>'
                     % (p['id'], x, y, esc(p['name']), esc(p['role']), color[p.get('group', '')], name_size(sn), esc(sn)))

    group_cards = []
    for g in groups:
        cards = []
        for p in [x for x in people if x.get('group', '') == g]:
            evs = p.get('events') or []
            first_ev = evs[0] if evs else ''
            ev_title = ''
            for e in b['events']:
                if e['id'] == first_ev:
                    ev_title = e['title']
                    break
            aliases = '、'.join(p.get('aliases', [])[:3])
            cards.append(
                '''      <article class="pcard" id="c-%(id)s" style="--c:%(c)s">
        <div class="pcard-top"><h3>%(name)s</h3></div>
        <p class="role">%(role)s</p>
        <p class="deeds">%(deeds)s</p>
        %(jump)s
      </article>''' % dict(
                    id=p['id'], c=color[g], name=esc(p['name']), role=esc(p['role']),
                    deeds=esc(p.get('deeds', '')),
                    jump=('<a class="jump" href="index.html#%s">时间线 · %s →</a>' % (first_ev, esc(ev_title)))
                    if first_ev else ''))
        group_cards.append('''    <section class="pgroup">
      <div class="pgroup-head"><h2 style="--c:%s">%s</h2></div>
      <div class="pgrid">
%s
      </div>
    </section>''' % (color[g], esc(g), '\n'.join(cards)))

    DATA = {}
    for p in people:
        rel = []
        for r in b['relations']:
            if r['a'] == p['id']:
                rel.append([r['b'], by_id[r['b']]['name'] if r['b'] in by_id else r['b'], r['label']])
            elif r['b'] == p['id']:
                rel.append([r['a'], by_id[r['a']]['name'] if r['a'] in by_id else r['a'], r['label']])
        evs = p.get('events') or []
        ev_title = ''
        for e in b['events']:
            if e['id'] == (evs[0] if evs else ''):
                ev_title = e['title']
                break
        DATA[p['id']] = dict(name=p['name'], role=p['role'], deeds=p.get('deeds', ''),
                             quote=(p.get('aliases') or [''])[0],
                             camp=p.get('group', ''), campKey=p.get('group', ''),
                             color=color[p.get('group', '')],
                             link=(evs[0] if evs else ''), linkName=ev_title, rel=rel)

    js = CH_JS
    js = js.replace('var CX = 620, CY = 350;', 'var CX = 620, CY = 440;')
    js = js.replace("""  function resetStyles(){
    nodes.forEach""", """  function resetStyles(){
    [].forEach.call(document.querySelectorAll('.gtag'), function(t){ t.style.opacity = 0; });
    nodes.forEach""")
    js = js.replace("""    panel.classList.remove('on');
    animateTo(targets);""", """    panel.classList.remove('on');
    [].forEach.call(document.querySelectorAll('.gtag'), function(t){ t.style.opacity = ''; });
    animateTo(targets);""")
    js = js.replace('quote.hidden = !d.quote;', 'if (quote) quote.hidden = !d.quote;')
    js = js.replace('source.hidden = !d.quoteSource;', 'if (source) source.hidden = !d.quoteSource;')
    js = re.sub(r'var DATA = \{.*?\};\n', 'var DATA = %s;\n' % json.dumps(DATA, ensure_ascii=False), js, count=1, flags=re.S)

    filters = '<button class="fbtn on" id="allBtn">全览</button>' + ''.join(
        '<button class="fbtn" data-camp="%s">%s</button>' % (g, esc(g)) for g in groups)

    extra_css = '''
.foot-nav{display:flex;gap:26px;justify-content:center;margin-top:26px}
.foot-nav a{
  font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;
  color:var(--ink-3);text-decoration:none;border-bottom:1px solid transparent;
  padding-bottom:2px;transition:.3s;
}
.foot-nav a:hover{color:var(--ink);border-bottom-color:var(--ink)}
.gtag{
  font-family:var(--sans);font-size:12px;letter-spacing:.08em;
  fill:var(--ink-2);opacity:.9;
}
'''
    html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s · 人物志 | %(n)d 个人物</title>
<meta name="description" content="%(desc)s">
<style>%(css)s</style>
<style>%(extra)s.foot-nav{display:flex;gap:26px;justify-content:center;margin-top:26px}
.foot-nav a{
  font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;
  color:var(--ink-3);text-decoration:none;border-bottom:1px solid transparent;
  padding-bottom:2px;transition:.3s;
}
.foot-nav a:hover{color:var(--ink);border-bottom-color:var(--ink)}
</style>
</head>
<body id="top">

<nav class="topnav">
  <span class="nav-ind" aria-hidden="true"></span>
  <a href="../../index.html">书架</a>
  <a href="index.html">时间线</a>
  <a href="characters.html" class="on">人物志</a>
</nav>

<header class="masthead">
  <div class="wrap">
    <p class="kicker">%(author)s / CHARACTERS</p>
    <h1 class="big">%(title)s · 人物</h1>
    <p class="deck">%(desc)s</p>
    <div class="rule"></div>
  </div>
</header>

<main class="wrap">
  <section class="netwrap">
    <div class="nethead">
      <h2>关系网</h2>
      <p>点击人物 · 查看羁绊</p>
    </div>
    <div class="netbar">%(filters)s</div>
    <div class="netbox">
      <svg class="net" viewBox="0 0 1240 900" role="img" aria-label="%(title)s人物关系网">
        <g class="gtags">%(gtags)s</g>
        <g class="links">%(links)s</g>
        <g class="labels">%(labels)s</g>
        <g class="nodes">%(nodes)s</g>
      </svg>
      <aside class="pdetail" id="pdetail">
        <button class="pd-close" id="pdClose" aria-label="关闭">×</button>
        <div class="pd-camp" id="pdCamp"></div>
        <h3 id="pdName"></h3>
        <p class="pd-role" id="pdRole"></p>
        <p class="pd-deeds" id="pdDeeds"></p>
        <blockquote id="pdQuote"></blockquote>
        <a id="pdQuoteSource" hidden></a>
        <div class="pd-rel-title">羁绊</div>
        <div class="pd-rel" id="pdRel"></div>
        <a class="pd-link" id="pdLink" href="#">在时间线中查看 →</a>
      </aside>
    </div>
  </section>

%(groups)s

</main>

<footer class="site-foot">
  <p class="q">“%(quote)s”</p>
  <p class="tiny">%(title)s · %(author)s　·　%(n)d 位人物，%(evcount)d 个时间点</p>
  <nav class="foot-nav">
    <a href="index.html">看时间线</a>
    <a href="#top">回到开头</a>
    <a href="../../index.html">回书架</a>
  </nav>
</footer>

<script>%(js)s</script>
<script>
(function(){
  var nav=document.querySelector('.topnav');
  if(!nav) return;
  var on=nav.querySelector('.on'), ind=nav.querySelector('.nav-ind');
  if(!on||!ind) return;
  function place(){
    ind.style.width=on.offsetWidth+'px';
    ind.style.transform='translateX('+on.offsetLeft+'px)';
    ind.style.opacity='1';
  }
  requestAnimationFrame(function(){ requestAnimationFrame(place); });
  window.addEventListener('resize',place);
})();
</script>
</body>
</html>''' % dict(title=esc(b['title']), author=esc(b['author']), desc=esc(b['description']),
                  n=len(people), evcount=len(b['events']), quote=QUOTES.get(b['id'], ''), css=CH_CSS, extra=extra_css, js=js, filters=filters,
                  gtags='\n        '.join(group_tags),
                  links='\n        '.join(links), labels='\n        '.join(labels), nodes='\n        '.join(nodes),
                  groups='\n'.join(group_cards))

    out = '%s/books/%s/characters.html' % (ROOT, b['id'])
    io.open(out, 'w', encoding='utf-8').write(html)
    return len(html)


for bid in BOOKS:
    b = load(bid)
    a = build_index(b)
    c = build_chars(b)
    print('%-14s index %6d  chars %6d  (%d events, %d people)' % (bid, a, c, len(b['events']), len(b['people'])))
