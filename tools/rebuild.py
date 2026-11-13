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
    'and-then-there-were-none': '一个小士兵，落单孤零零，悬梁了此生，一个也不剩。',
    'orient-express': '我荣幸地退出这个案子。',
    'long-goodbye': '说一声再见，就是死去一点点。',
    'sherlock': '排除一切不可能，剩下的即使再不可能，也是真相。',
    'millennium': '恨女人的男人。',
    'gone-girl': '每当我想起我的妻子，我总是先想起她的脑袋。',
    'two-cities': '这是最好的时代，也是最坏的时代。',
    'les-miserables': '比天空更宽阔的，是人的心灵。',
    'pride-prejudice': '凡是有钱的单身汉，总想娶位太太，这已经成了一条举世公认的真理。',
    'jane-eyre': '你以为我穷、低微、不美、矮小，我就没有灵魂没有心吗。',
    'wuthering': '我对他的爱，就像脚下恒久不变的岩石。',
    'war-peace': '我要活，要爱，要相信。',
    'anna-karenina': '幸福的家庭都是相似的，不幸的家庭各有各的不幸。',
    'gone-wind': '明天又是新的一天。',
    'godfather': '我会给他一个不能拒绝的条件。',
    'notre-dame': '美与丑，只隔着一层皮。',
    'quiet-don': '我们这儿的人，一辈子就守着一条河。',
    'zhivago': '喧哗静了，我走上台。',
    'fortress': '城外的人想冲进去，城里的人想逃出来。',
    'white-deer': '这地还是这地，人换了几茬了。',
    'ordinary-world': '即使是最平凡的人，也要为他那个世界的存在而战斗。',
    'border-town': '这个人也许永远不回来了，也许明天回来。',
}


DECOR = {
'white-deer': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <path d="M60 440 Q300 360 540 440" fill="none" stroke="#b3a184" stroke-width="1"/>
  <path d="M60 470 Q300 400 540 470" fill="none" stroke="#c2b096" stroke-width=".5"/>
  <path d="M170 428 V330 L200 306 L230 330 V428" fill="none" stroke="#8f7f66" stroke-width="1"/>
  <path d="M206 428 V392 H226 V428" fill="none" stroke="#8f7f66" stroke-width=".6"/>
  <path d="M380 428 V352 L402 334 L424 352 V428" fill="none" stroke="#8f7f66" stroke-width=".8"/>
  <path d="M300 250 l10 -16 l10 16 l-10 14Z" fill="none" stroke="#8c3a34" stroke-width=".9"/>
  <path d="M120 520 H480" stroke="#b3a184" stroke-width=".4" stroke-dasharray="2 9"/>
</svg>''',
'ordinary-world': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <path d="M60 470 Q180 420 300 460 T540 450" fill="none" stroke="#b6a077" stroke-width="1"/>
  <path d="M60 500 Q180 452 300 490 T540 480" fill="none" stroke="#c4b08a" stroke-width=".5"/>
  <g stroke="#8d7a58" stroke-width=".8">
    <path d="M200 470 V380 M180 380 H220"/><path d="M180 380 L200 344 L220 380"/>
    <path d="M380 460 V390 M364 390 H396"/><path d="M364 390 L380 360 L396 390"/>
  </g>
  <path d="M296 470 V410 H304 V470" stroke="#8c3a34" stroke-width=".9"/>
  <path d="M120 530 H480" stroke="#b6a077" stroke-width=".4" stroke-dasharray="2 9"/>
</svg>''',
'border-town': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <path d="M60 400 Q180 384 300 400 T540 400" fill="none" stroke="#8fa79a" stroke-width="1"/>
  <path d="M60 434 Q180 418 300 434 T540 434" fill="none" stroke="#a0b6a9" stroke-width=".6"/>
  <path d="M60 468 Q180 452 300 468 T540 468" fill="none" stroke="#b0c4b8" stroke-width=".4"/>
  <path d="M250 400 L300 344 L350 400" fill="none" stroke="#6f8a7c" stroke-width=".9"/>
  <path d="M120 400 V430 M480 400 V430" stroke="#6f8a7c" stroke-width=".8"/>
  <circle cx="300" cy="300" r="10" fill="none" stroke="#8c3a34" stroke-width=".9"/>
  <path d="M300 310 V344" stroke="#8c3a34" stroke-width=".6"/>
</svg>''',
'quiet-don': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <path d="M60 380 Q160 364 260 380 T460 380 T560 380" fill="none" stroke="#8f8a75" stroke-width="1"/>
  <path d="M60 420 Q160 404 260 420 T460 420 T560 420" fill="none" stroke="#a09a84" stroke-width=".6"/>
  <path d="M60 460 Q160 444 260 460 T460 460 T560 460" fill="none" stroke="#b0aa94" stroke-width=".4"/>
  <path d="M200 380 V300 L230 276 L260 300 V380" fill="none" stroke="#7d7864" stroke-width=".9"/>
  <path d="M360 380 V330 L382 312 L404 330 V380" fill="none" stroke="#7d7864" stroke-width=".7"/>
  <circle cx="486" cy="214" r="30" fill="none" stroke="#8c3a34" stroke-width="1.4"/>
  <path d="M120 520 H480" stroke="#a09a84" stroke-width=".4" stroke-dasharray="2 9"/>
</svg>''',
'zhivago': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <path d="M180 470 V300 L240 240 L300 300 V470" fill="none" stroke="#8d929a" stroke-width="1"/>
  <path d="M300 470 V330 L360 280 L420 330 V470" fill="none" stroke="#8d929a" stroke-width=".8"/>
  <path d="M240 470 V400 H270 V470" fill="none" stroke="#a5aab2" stroke-width=".5"/>
  <g stroke="#b8bcc4" stroke-width=".4"><path d="M120 500 H480 M120 522 H480"/></g>
  <path d="M300 150 V210" stroke="#8c3a34" stroke-width=".8"/>
  <circle cx="300" cy="140" r="8" fill="none" stroke="#8c3a34" stroke-width="1"/>
</svg>''',
'fortress': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <rect x="176" y="230" width="248" height="240" fill="none" stroke="#a3967c" stroke-width="1"/>
  <path d="M176 230 H424 M176 300 H424 M176 370 H424" stroke="#a3967c" stroke-width=".4"/>
  <path d="M212 470 V380 H252 V470 M348 470 V380 H388 V470" fill="none" stroke="#8f8368" stroke-width=".8"/>
  <path d="M300 470 V410 Q300 380 330 380" fill="none" stroke="#8f8368" stroke-width=".6"/>
  <circle cx="300" cy="330" r="14" fill="none" stroke="#8c3a34" stroke-width="1"/>
  <path d="M120 500 H480" stroke="#b0a48c" stroke-width=".4" stroke-dasharray="2 9"/>
</svg>''',
'gone-wind': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <path d="M120 470 H480" stroke="#a97f6c" stroke-width="1"/>
  <path d="M300 470 V300 M300 300 L200 250 M300 300 L400 250" stroke="#8f6a58" stroke-width="1.1"/>
  <path d="M186 258 q14 -30 28 0 q-14 18 -28 0Z" fill="none" stroke="#8c3a34" stroke-width=".9"/>
  <path d="M386 258 q14 -30 28 0 q-14 18 -28 0Z" fill="none" stroke="#8c3a34" stroke-width=".9"/>
  <g stroke="#c19a86" stroke-width=".5"><path d="M150 420 q40 -14 80 0 M370 420 q40 -14 80 0"/></g>
  <path d="M60 520 H540" stroke="#b58a76" stroke-width=".4" stroke-dasharray="2 9"/>
</svg>''',
'godfather': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <path d="M300 200 q-52 0 -52 40 q0 30 24 40 q-20 8 -20 28 h96 q0 -20 -20 -28 q24 -10 24 -40 q0 -40 -52 -40Z" fill="none" stroke="#9a9186" stroke-width="1.1"/>
  <path d="M300 200 q-40 -18 -62 6 M300 200 q40 -18 62 6" fill="none" stroke="#8a8176" stroke-width=".8"/>
  <path d="M214 330 H386 M228 350 H372" stroke="#8a8176" stroke-width=".6"/>
  <circle cx="300" cy="278" r="2.6" fill="#8c3a34"/>
  <path d="M150 470 H450" stroke="#a9a096" stroke-width=".8"/>
  <path d="M120 512 H480" stroke="#b9b0a6" stroke-width=".4" stroke-dasharray="2 9"/>
</svg>''',
'notre-dame': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <path d="M300 180 V470" stroke="#a08b6a" stroke-width="1.1"/>
  <path d="M300 200 L240 470 M300 200 L360 470" fill="none" stroke="#a08b6a" stroke-width=".8"/>
  <circle cx="300" cy="300" r="46" fill="none" stroke="#8f7a5a" stroke-width="1.1"/>
  <circle cx="300" cy="300" r="30" fill="none" stroke="#8f7a5a" stroke-width=".5" stroke-dasharray="2 7"/>
  <path d="M254 300 H346 M300 254 V346" stroke="#8f7a5a" stroke-width=".4"/>
  <path d="M120 470 H480" stroke="#a08b6a" stroke-width="1"/>
  <path d="M150 500 H450" stroke="#c0ab8a" stroke-width=".4" stroke-dasharray="2 9"/>
</svg>''',
'wuthering': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <path d="M120 500 Q220 460 300 500 T480 500" fill="none" stroke="#9a9aa4" stroke-width=".7"/>
  <path d="M150 500 V330 L190 300 L230 330 V500" fill="none" stroke="#8a8a94" stroke-width="1.1"/>
  <path d="M300 500 V300 L360 256 L420 300 V500" fill="none" stroke="#8a8a94" stroke-width="1.1"/>
  <path d="M330 500 V420 H390 V500" fill="none" stroke="#8a8a94" stroke-width=".6"/>
  <path d="M340 330 H380 M340 366 H380" stroke="#b0b0ba" stroke-width=".5"/>
  <path d="M470 470 q18 -40 0 -80 q-18 40 0 80Z" fill="none" stroke="#8c3a34" stroke-width=".9"/>
  <path d="M60 540 H540" stroke="#a5a5ae" stroke-width=".4" stroke-dasharray="2 9"/>
</svg>''',
'war-peace': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <path d="M120 430 Q300 360 480 430" fill="none" stroke="#a3ab99" stroke-width="1"/>
  <path d="M300 250 V430" stroke="#8f9785" stroke-width="1.1"/>
  <path d="M262 250 H338" stroke="#8f9785" stroke-width="1.4"/>
  <circle cx="300" cy="222" r="26" fill="none" stroke="#8c3a34" stroke-width="1.2"/>
  <path d="M286 222 H314 M300 208 V236" stroke="#8c3a34" stroke-width=".7"/>
  <g stroke="#b6bdab" stroke-width=".5">
    <path d="M150 470 V430 M180 470 V440 M210 470 V434 M400 470 V436 M430 470 V442 M460 470 V430"/>
  </g>
  <path d="M60 470 H540" stroke="#a3ab99" stroke-width="1"/>
</svg>''',
'anna-karenina': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <g stroke="#b09a9a" stroke-width=".6">
    <path d="M60 400 H540"/><path d="M60 424 H540"/>
    <path d="M120 400 V424 M180 400 V424 M240 400 V424 M300 400 V424 M360 400 V424 M420 400 V424 M480 400 V424"/>
  </g>
  <path d="M60 460 Q140 440 220 460 T380 460 T540 460" fill="none" stroke="#c0aaaa" stroke-width=".5"/>
  <g fill="none" stroke="#8c3a34" stroke-width="1.1">
    <path d="M300 250 q-14 -22 0 -44 q14 22 0 44Z"/>
    <path d="M300 250 V330" stroke-width=".8"/>
    <path d="M282 330 H318" stroke-width="1"/>
  </g>
  <circle cx="300" cy="206" r="3" fill="#8c3a34"/>
</svg>''',
'jane-eyre': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <path d="M300 470 V250" stroke="#a89478" stroke-width="1.1"/>
  <path d="M232 470 V300 Q232 214 300 186 Q368 214 368 300 V470" fill="none" stroke="#a89478" stroke-width="1"/>
  <path d="M248 470 V306 Q248 236 300 214 Q352 236 352 306 V470" fill="none" stroke="#a89478" stroke-width=".4" stroke-dasharray="2 8"/>
  <g fill="none" stroke="#8c3a34" stroke-width="1">
    <path d="M300 250 q-9 -16 0 -30 q9 14 0 30Z"/>
    <path d="M290 254 q-14 -8 -12 -20 M310 254 q14 -8 12 -20" stroke-width=".6"/>
  </g>
  <path d="M120 470 H480" stroke="#c0b39c" stroke-width="1"/>
  <path d="M120 512 H480" stroke="#c9bca6" stroke-width=".4" stroke-dasharray="2 9"/>
</svg>''',
'pride-prejudice': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <path d="M180 240 H420 V400 L300 460 L180 400 Z" fill="none" stroke="#b3a08a" stroke-width="1.1"/>
  <path d="M180 240 L300 330 L420 240" fill="none" stroke="#b3a08a" stroke-width=".9"/>
  <path d="M212 300 H388 M212 330 H388 M212 360 H330" stroke="#c2b19c" stroke-width=".5"/>
  <circle cx="392" cy="416" r="26" fill="none" stroke="#8c3a34" stroke-width="1.2"/>
  <path d="M378 416 q14 -18 28 0 q-14 16 -28 0Z" fill="none" stroke="#8c3a34" stroke-width=".8"/>
  <path d="M120 520 H480" stroke="#c0b39c" stroke-width=".4" stroke-dasharray="2 9"/>
</svg>''',
'les-miserables': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <g fill="none" stroke="#b09a7e" stroke-width="1.1">
    <path d="M246 470 V330 M234 330 H258"/>
    <path d="M234 330 V300 H258 V330"/>
    <path d="M354 470 V330 M342 330 H366"/>
    <path d="M342 330 V300 H366 V330"/>
  </g>
  <g fill="none" stroke="#8c3a34" stroke-width="1">
    <path d="M246 300 q-8 -14 0 -26 q8 12 0 26Z"/>
    <path d="M354 300 q-8 -14 0 -26 q8 12 0 26Z"/>
  </g>
  <path d="M246 274 V246 M354 274 V246" stroke="#c08a72" stroke-width=".6" stroke-dasharray="2 6"/>
  <path d="M120 470 H480" stroke="#a08b76" stroke-width="1"/>
  <path d="M120 512 H480" stroke="#b9a894" stroke-width=".4" stroke-dasharray="2 9"/>
</svg>''',
'two-cities': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <g fill="none" stroke="#b09a86" stroke-width=".9">
    <path d="M96 420 V300 M112 420 V262 L120 248 L128 262 V420"/>
    <path d="M146 420 V330 M160 420 V286 M176 420 V340"/>
    <path d="M440 420 V276 L450 258 L460 276 V420"/>
    <path d="M476 420 V320 M492 420 V300 M508 420 V352"/>
  </g>
  <path d="M60 420 H540" stroke="#a08b76" stroke-width="1"/>
  <g fill="none" stroke="#8e7a66" stroke-width=".6">
    <path d="M60 462 Q110 448 160 462 T260 462 T360 462 T460 462 T560 462"/>
    <path d="M60 486 Q110 472 160 486 T260 486 T360 486 T460 486 T560 486"/>
  </g>
  <path d="M300 150 V214" stroke="#7a6656" stroke-width="1.1"/>
  <path d="M268 214 H332" stroke="#7a6656" stroke-width="1.1"/>
  <path d="M284 214 L300 258 L316 214" fill="none" stroke="#8c3a34" stroke-width="1.2"/>
</svg>''',
'gone-girl': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <rect x="196" y="150" width="208" height="248" fill="none" stroke="#a09396" stroke-width="1"/>
  <rect x="212" y="166" width="176" height="216" fill="none" stroke="#a09396" stroke-width=".5" stroke-dasharray="2 7"/>
  <circle cx="300" cy="256" r="34" fill="none" stroke="#6f6468" stroke-width="1.1"/>
  <path d="M278 292 q22 20 44 0" fill="none" stroke="#6f6468" stroke-width="1.1"/>
  <path d="M262 244 q10 -8 20 0 M318 244 q10 -8 20 0" fill="none" stroke="#6f6468" stroke-width=".8"/>
  <path d="M232 344 H368" stroke="#8c8184" stroke-width=".5"/>
  <path d="M140 430 H460" stroke="#b0a5a7" stroke-width=".4" stroke-dasharray="2 9"/>
</svg>''',
'millennium': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <g fill="none" stroke="#8d97a1" stroke-width="1.1">
    <path d="M300 300 m0 -14 a14 14 0 1 1 -14 14 a28 28 0 1 1 28 -28 a42 42 0 1 1 -42 42 a56 56 0 1 1 56 -56 a70 70 0 1 1 -70 70"/>
  </g>
  <g fill="none" stroke="#8d97a1" stroke-width=".5" opacity=".65">
    <path d="M300 300 m0 -84 a84 84 0 1 0 84 84 a98 98 0 1 0 -98 -98"/>
  </g>
  <g stroke="#6f7982" stroke-width=".8">
    <path d="M392 254 q10 -14 22 -12"/><path d="M404 286 q12 -10 22 -6"/>
  </g>
  <path d="M120 512 H480" stroke="#a9b1b8" stroke-width=".5" stroke-dasharray="2 9"/>
</svg>''',
'sherlock': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <circle cx="286" cy="266" r="92" fill="none" stroke="#a08b6c" stroke-width="1.4"/>
  <circle cx="286" cy="266" r="82" fill="none" stroke="#a08b6c" stroke-width=".5" stroke-dasharray="2 9"/>
  <path d="M348 330 L424 414" stroke="#a08b6c" stroke-width="5" stroke-linecap="round"/>
  <path d="M348 330 L424 414" stroke="#c9bca6" stroke-width="1.4" stroke-dasharray="3 5"/>
  <g fill="#8a7355">
    <ellipse cx="252" cy="242" rx="5" ry="9" transform="rotate(-24 252 242)"/>
    <ellipse cx="282" cy="230" rx="5" ry="9" transform="rotate(-18 282 230)"/>
    <ellipse cx="312" cy="222" rx="5" ry="9" transform="rotate(-12 312 222)"/>
  </g>
  <path d="M120 520 H480" stroke="#c0b39c" stroke-width=".6" stroke-dasharray="2 8"/>
</svg>''',
'long-goodbye': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <path d="M212 232 H388 L300 358 Z" fill="none" stroke="#8d8b82" stroke-width="1.1"/>
  <path d="M300 358 V470" stroke="#8d8b82" stroke-width="1.1"/>
  <path d="M258 470 H342" stroke="#8d8b82" stroke-width="1.1"/>
  <path d="M228 262 H372" stroke="#8d8b82" stroke-width=".5" stroke-dasharray="2 6"/>
  <circle cx="314" cy="290" r="6" fill="none" stroke="#8c3a34" stroke-width="1"/>
  <path d="M314 284 q6 -10 14 -8" fill="none" stroke="#8c3a34" stroke-width=".8"/>
  <path d="M120 508 H480" stroke="#a5a29a" stroke-width=".8"/>
  <path d="M170 496 V520 M430 496 V520" stroke="#a5a29a" stroke-width=".5"/>
  <g fill="none" stroke="#b5b2a8" stroke-width=".6">
    <path d="M392 210 q26 -34 0 -68"/><path d="M378 214 q22 -30 0 -60"/>
  </g>
</svg>''',
'orient-express': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <g stroke="#b9a894" stroke-width=".6">
    <path d="M40 400 L560 300"/><path d="M40 430 L560 322"/>
  </g>
  <g stroke="#a08c76" stroke-width=".9">
    <path d="M120 414 V438 M180 405 V428 M240 395 V417 M300 386 V407 M360 376 V396 M420 366 V386 M480 356 V375"/>
  </g>
  <g fill="#d8cec0">
    <circle cx="150" cy="180" r="2.2"/><circle cx="214" cy="140" r="1.6"/><circle cx="284" cy="196" r="2"/>
    <circle cx="352" cy="132" r="1.8"/><circle cx="418" cy="188" r="2.2"/><circle cx="470" cy="150" r="1.5"/>
    <circle cx="196" cy="236" r="1.8"/><circle cx="330" cy="248" r="1.6"/><circle cx="440" cy="242" r="2"/>
  </g>
  <rect x="248" y="286" width="104" height="34" fill="none" stroke="#8c6a50" stroke-width="1"/>
  <path d="M248 303 H352" stroke="#8c6a50" stroke-width=".6"/>
  <circle cx="286" cy="320" r="14" fill="none" stroke="#8c6a50" stroke-width=".8"/>
  <circle cx="322" cy="320" r="14" fill="none" stroke="#8c6a50" stroke-width=".8"/>
  <circle cx="300" cy="303" r="2" fill="#8c3a34"/>
</svg>''',
'and-then-there-were-none': '''<svg viewBox="0 0 600 600" aria-hidden="true">
  <g stroke="#9aa8a0" stroke-width="1">
    <path d="M60 470 H540"/>
    <path d="M150 470 Q300 372 450 470" fill="none" stroke-width=".7" stroke-dasharray="2 7"/>
  </g>
  <g fill="none" stroke="#6b7b72" stroke-width="1">
    <circle cx="165" cy="300" r="7"/><circle cx="204" cy="300" r="7"/><circle cx="243" cy="300" r="7"/>
    <circle cx="282" cy="300" r="7"/><circle cx="321" cy="300" r="7"/><circle cx="360" cy="300" r="7"/>
    <circle cx="399" cy="300" r="7"/><circle cx="438" cy="300" r="7"/><circle cx="477" cy="300" r="7"/>
  </g>
  <g stroke="#6b7b72" stroke-width=".9">
    <path d="M165 307 V326 M204 307 V326 M243 307 V326 M282 307 V326 M321 307 V326 M360 307 V326 M399 307 V326 M438 307 V326 M477 307 V326"/>
  </g>
  <circle cx="410" cy="360" r="11" fill="none" stroke="#8c3a34" stroke-width="1.2"/>
  <path d="M410 349 V318" stroke="#8c3a34" stroke-width="1.2"/>
  <path d="M120 512 H480" stroke="#9aa8a0" stroke-width=".5" stroke-dasharray="2 8"/>
</svg>''',
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
