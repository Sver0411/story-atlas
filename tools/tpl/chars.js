
(function(){
  var DATA = {"zhe": {"name": "叶哲泰", "role": "理论物理学教授 · 叶文洁之父", "deeds": "理论物理学教授，叶文洁的父亲。在批斗会上坚持科学判断，遭到殴打而死。他的遭遇深刻影响了叶文洁对人类社会的看法。", "quote": "", "camp": "红岸", "campKey": "hongan", "color": "#8c2b26", "link": "e3", "linkName": "父亲的死", "rel": [["ye", "叶文洁", "父女"]], "quoteSource": "", "quoteSourceName": ""}, "shao": {"name": "绍琳", "role": "叶文洁之母", "deeds": "叶哲泰的妻子，叶文洁的母亲。她在批斗会上揭发丈夫，后来改嫁。家庭的破裂成为叶文洁早年经历的一部分。", "quote": "", "camp": "红岸", "campKey": "hongan", "color": "#8c2b26", "link": "e3", "linkName": "父亲的死", "rel": [["ye", "叶文洁", "母女"]], "quoteSource": "", "quoteSourceName": ""}, "bai": {"name": "白沐霖", "role": "《大生产报》记者", "deeds": "在大兴安岭采访时与叶文洁相识，把《寂静的春天》借给她阅读。反映林场问题的信件受到追查后，他把责任推给叶文洁，使她遭到关押与审查。", "quote": "", "camp": "红岸", "campKey": "hongan", "color": "#8c2b26", "link": "e4", "linkName": "寂静的春天", "rel": [["ye", "叶文洁", "诬陷"]], "quoteSource": "", "quoteSourceName": ""}, "ye": {"name": "叶文洁", "role": "天体物理学家 · ETO 创始人", "deeds": "在红岸基地发现利用太阳放大电波的方法，收到三体监听员警告后仍向其回答，邀请三体文明介入地球。她制造接地线故障并锯断绳索，导致雷志成与杨卫宁死亡；后来成为 ETO 的精神领袖，并启发罗辑研究宇宙社会学。", "quote": "", "camp": "红岸", "campKey": "hongan", "color": "#8c2b26", "link": "e8", "linkName": "叶文洁的回答", "rel": [["zhe", "叶哲泰", "父女"], ["shao", "绍琳", "母女"], ["yang", "杨卫宁", "夫妻 · 杀夫"], ["dong", "杨冬", "母女"], ["bai", "白沐霖", "诬陷"], ["lei", "雷志成", "灭口"], ["wang", "汪淼", "接触 ETO"], ["yiwen", "伊文斯", "共创 ETO"], ["luo", "罗辑", "传授公理"], ["l1379", "1379 号", "警告"]], "quoteSource": "", "quoteSourceName": ""}, "yang": {"name": "杨卫宁", "role": "红岸基地工程师 · 叶文洁之夫", "deeds": "红岸基地工程师，叶哲泰的学生，后来与叶文洁结婚。他在雷志成下崖检修接地线时前去帮忙，因叶文洁锯断绳索而与雷志成一同坠亡。", "quote": "", "camp": "红岸", "campKey": "hongan", "color": "#8c2b26", "link": "e9", "linkName": "杀夫", "rel": [["ye", "叶文洁", "夫妻 · 杀夫"]], "quoteSource": "", "quoteSourceName": ""}, "lei": {"name": "雷志成", "role": "红岸基地政委", "deeds": "红岸基地政委，通过秘密通信备份发现外星信号，试图把这项发现据为己有。叶文洁制造接地线故障，引他下崖检修，再锯断绳索将其杀害。", "quote": "", "camp": "红岸", "campKey": "hongan", "color": "#8c2b26", "link": "e9", "linkName": "杀夫", "rel": [["ye", "叶文洁", "灭口"]], "quoteSource": "", "quoteSourceName": ""}, "dong": {"name": "杨冬", "role": "理论物理学家 · 叶文洁之女", "deeds": "理论物理学家，叶文洁与杨卫宁的女儿、丁仪的恋人。高能物理实验失去可重复的规律后，她陷入对物理学根基的绝望并自杀，其死亡成为汪淼参与调查的线索之一。", "quote": "", "camp": "红岸", "campKey": "hongan", "color": "#8c2b26", "link": "e19", "linkName": "逮捕", "rel": [["ye", "叶文洁", "母女"], ["ding", "丁仪", "恋人"]], "quoteSource": "", "quoteSourceName": ""}, "ding": {"name": "丁仪", "role": "理论物理学家", "deeds": "理论物理学家，杨冬的恋人。曾与汪淼讨论实验异常；两个世纪后随螳螂号检查水滴，发现其外壳的异常结构，并在水滴开始攻击时遇难。", "quote": "", "camp": "红岸", "campKey": "hongan", "color": "#8c2b26", "link": "e41", "linkName": "末日之战", "rel": [["dong", "杨冬", "恋人"]], "quoteSource": "", "quoteSourceName": ""}, "yiwen": {"name": "伊文斯", "role": "ETO 降临派领袖 · 审判日号主人", "deeds": "物种共产主义的信奉者，与叶文洁共同推动 ETO 发展，领导降临派。他以审判日号为通信基地，掌握与三体世界的联系，最终死于古筝行动。", "quote": "", "camp": "ETO", "campKey": "eto", "color": "#7a5a38", "link": "e11", "linkName": "内奸", "rel": [["ye", "叶文洁", "共创 ETO"], ["shen", "申玉菲", "同组织"], ["pan", "潘寒", "上下级"]], "quoteSource": "", "quoteSourceName": ""}, "shen": {"name": "申玉菲", "role": "ETO 拯救派 · 科学边界成员", "deeds": "ETO 拯救派成员，支持丈夫魏成研究三体问题，希望帮助三体文明摆脱灾难，并避免其入侵地球。她与降临派发生冲突，最终被潘寒杀害。", "quote": "", "camp": "ETO", "campKey": "eto", "color": "#7a5a38", "link": "e13", "linkName": "内斗", "rel": [["pan", "潘寒", "暗杀"], ["yiwen", "伊文斯", "同组织"]], "quoteSource": "", "quoteSourceName": ""}, "pan": {"name": "潘寒", "role": "ETO 降临派", "deeds": "ETO 降临派成员，杀害拯救派的申玉菲。后来在组织聚会上被叶文洁指责违背 ETO 的共同目标，遭组织成员处死。", "quote": "", "camp": "ETO", "campKey": "eto", "color": "#7a5a38", "link": "e13", "linkName": "内斗", "rel": [["shen", "申玉菲", "暗杀"], ["yiwen", "伊文斯", "上下级"]], "quoteSource": "", "quoteSourceName": ""}, "wang": {"name": "汪淼", "role": "纳米材料科学家 · 飞刃发明者", "deeds": "纳米材料科学家，因科学家自杀事件参与调查。他经历照片与视野中的倒计时、宇宙背景辐射闪烁，通过三体游戏接触 ETO；其研发的飞刃成为古筝行动的关键材料。", "quote": "", "camp": "军方与科学界", "campKey": "mil", "color": "#2f4a6b", "link": "e14", "linkName": "倒计时", "rel": [["ye", "叶文洁", "接触 ETO"], ["shi", "史强", "搭档"]], "quoteSource": "", "quoteSourceName": ""}, "shi": {"name": "史强", "role": "警官", "deeds": "参与三体相关案件调查的警官，常被称为大史。他保护并协助汪淼，参与突袭 ETO 聚会和策划古筝行动；冬眠来到未来后，再次承担罗辑的保护工作。", "quote": "", "camp": "军方与科学界", "campKey": "mil", "color": "#2f4a6b", "link": "e25", "linkName": "拒绝", "rel": [["wang", "汪淼", "搭档"], ["luo", "罗辑", "保护"]], "quoteSource": "", "quoteSourceName": ""}, "chang": {"name": "常伟思", "role": "太空军首任司令员", "deeds": "太空军首任司令员，主持早期组建与研究工作，重视章北海等军官，并支持通过冬眠向未来输送人才。他在危机纪元早期去世，没有亲历两个世纪后的末日之战。", "quote": "", "camp": "军方与科学界", "campKey": "mil", "color": "#2f4a6b", "link": "e30", "linkName": "增援未来", "rel": [["zhang", "章北海", "上下级"]], "quoteSource": "", "quoteSourceName": ""}, "zhang": {"name": "章北海", "role": "太空军政委 · 自然选择号执行舰长", "deeds": "以陨石子弹暗杀阻碍无工质推进路线的航天界元老，随后通过冬眠来到未来。他利用临时执行舰长权限带走自然选择号，试图为人类保留火种，最终与东方延绪等人死于黑暗战役。", "quote": "没关系的，都一样。", "camp": "军方与科学界", "campKey": "mil", "color": "#2f4a6b", "link": "e43", "linkName": "黑暗战役", "rel": [["chang", "常伟思", "上下级"], ["dongfang", "东方延绪", "接管指挥"], ["chu", "褚岩", "星舰地球"]], "quoteSource": "https://www.bidutuijian.com/books/heiansenlin/045.html", "quoteSourceName": "《黑暗森林》黑暗战役"}, "dongfang": {"name": "东方延绪", "role": "自然选择号舰长", "deeds": "自然选择号舰长。章北海获授临时执行舰长权限并控制飞船出逃后，她曾试图制止；末日之战后参与星舰地球的决策，最终死于终极规律号的次声波攻击。", "quote": "", "camp": "军方与科学界", "campKey": "mil", "color": "#2f4a6b", "link": "e42", "linkName": "前进四", "rel": [["zhang", "章北海", "接管指挥"]], "quoteSource": "", "quoteSourceName": ""}, "chu": {"name": "褚岩", "role": "蓝色空间号舰长", "deeds": "蓝色空间号舰长。在黑暗战役前令全员穿航天服，将舱内抽成真空，避免次声波杀伤，保住全舰人员并反击终极规律号。后来与万有引力号船员合作，探索四维碎片。", "quote": "", "camp": "军方与科学界", "campKey": "mil", "color": "#2f4a6b", "link": "e43", "linkName": "黑暗战役", "rel": [["zhang", "章北海", "星舰地球"]], "quoteSource": "", "quoteSourceName": ""}, "luo": {"name": "罗辑", "role": "面壁者 · 第一任执剑人", "deeds": "由叶文洁的启发研究宇宙社会学，以恒星坐标检验黑暗森林推论。危机纪元末期，他在墓前以雪地工程的反触发系统威胁发出广播，建立威慑；长期担任执剑人后，又成为冥王星文明博物馆的守护者。", "quote": "", "camp": "面壁者", "campKey": "mian", "color": "#3f5f86", "link": "e44", "linkName": "执剑人", "rel": [["zhuang", "庄颜", "夫妻"], ["shi", "史强", "保护"], ["tai", "泰勒", "同为面壁者"], ["lei2", "雷迪亚兹", "同为面壁者"], ["xi", "希恩斯", "同为面壁者"], ["ye", "叶文洁", "传授公理"], ["cheng", "程心", "交接执剑"], ["zhizi", "智子", "对峙"]], "quoteSource": "", "quoteSourceName": ""}, "zhuang": {"name": "庄颜", "role": "罗辑之妻", "deeds": "罗辑行使面壁者权力寻找的理想伴侣，后来成为他的妻子，与他在庄园共同生活并育有女儿。她与女儿进入冬眠，促使罗辑重新面对面壁者的责任。", "quote": "", "camp": "面壁者", "campKey": "mian", "color": "#3f5f86", "link": "e27", "linkName": "梦中的姑娘", "rel": [["luo", "罗辑", "夫妻"]], "quoteSource": "", "quoteSourceName": ""}, "tai": {"name": "泰勒", "role": "面壁者 · 前美国国防部长", "deeds": "计划用宏原子武器把地球舰队变为量子幽灵，借此与三体舰队作战。破壁人在其住所揭露目标后，他陷入面壁者无法证明自己真意的困境，最终在罗辑庄园湖边自杀。", "quote": "", "camp": "面壁者", "campKey": "mian", "color": "#3f5f86", "link": "e33", "linkName": "破壁 · 泰勒", "rel": [["luo", "罗辑", "同为面壁者"]], "quoteSource": "", "quoteSourceName": ""}, "lei2": {"name": "雷迪亚兹", "role": "面壁者 · 委内瑞拉总统", "deeds": "计划用恒星型氢弹使水星坠入太阳，以连锁灾变毁掉太阳系，威胁三体文明。破壁人揭露计划及资源障碍后，他借假冒反触发装置脱身，返回委内瑞拉并被愤怒人群杀害。", "quote": "", "camp": "面壁者", "campKey": "mian", "color": "#3f5f86", "link": "e34", "linkName": "破壁 · 雷迪亚兹", "rel": [["luo", "罗辑", "同为面壁者"]], "quoteSource": "", "quoteSourceName": ""}, "xi": {"name": "希恩斯", "role": "面壁者 · 英国物理学家", "deeds": "与山杉惠子研究大脑思维，发展出思想钢印。其设备表面固化胜利信念，实际植入失败主义；在未来的听证会上，妻子揭示了这一秘密及隐匿的设备，引发对钢印族的追查。", "quote": "", "camp": "面壁者", "campKey": "mian", "color": "#3f5f86", "link": "e35", "linkName": "破壁 · 希恩斯", "rel": [["shan", "山杉惠子", "夫妻"], ["luo", "罗辑", "同为面壁者"]], "quoteSource": "", "quoteSourceName": ""}, "shan": {"name": "山杉惠子", "role": "脑科学家 · 希恩斯之妻 · 破壁人", "deeds": "与希恩斯合作研究脑科学，也是他的妻子和破壁人。在危机纪元 205 年的听证会上，她揭示思想钢印的真实作用与秘密设备，打破了丈夫对外展示的胜利主义形象。", "quote": "", "camp": "面壁者", "campKey": "mian", "color": "#3f5f86", "link": "e35", "linkName": "破壁 · 希恩斯", "rel": [["xi", "希恩斯", "夫妻"]], "quoteSource": "", "quoteSourceName": ""}, "wei": {"name": "维德", "role": "PIA 局长 · 光速飞船推动者", "deeds": "危机纪元初期主持 PIA，推动程心提出的阶梯计划。后来领导星环城秘密研究曲率驱动，准备以反物质武器对抗联邦政府；在程心要求其履行承诺后停止抵抗，随后被处决。", "quote": "", "camp": "威慑之后", "campKey": "hou", "color": "#5a3a6b", "link": "e59", "linkName": "反物质子弹", "rel": [["cheng", "程心", "决裂"], ["yun", "云天明", "阶梯计划"]], "quoteSource": "", "quoteSourceName": ""}, "cheng": {"name": "程心", "role": "第二任执剑人 · 星环公司", "deeds": "参与阶梯计划并推荐云天明成为候选人。后来接任执剑人，却未在水滴袭击时启动广播；在星环城危机中要求维德停止抵抗。太阳系二维化时，她与艾 AA 乘星环号逃离，最终与关一帆进入小宇宙。", "quote": "", "camp": "威慑之后", "campKey": "hou", "color": "#5a3a6b", "link": "e49", "linkName": "十分钟", "rel": [["yun", "云天明", "暗恋"], ["wei", "维德", "决裂"], ["aa", "艾 AA", "挚友"], ["guan", "关一帆", "同行"], ["luo", "罗辑", "交接执剑"]], "quoteSource": "", "quoteSourceName": ""}, "yun": {"name": "云天明", "role": "阶梯计划 · 三个童话的作者", "deeds": "在身患绝症时买下 DX3906 恒星赠给程心，后来成为阶梯计划的最终人选。他的大脑被三体舰队截获并恢复生存，在受监视的远程会面中，用三个童话向程心传递关键情报；此后与艾 AA 在蓝星相伴。", "quote": "", "camp": "威慑之后", "campKey": "hou", "color": "#5a3a6b", "link": "e37", "linkName": "阶梯计划", "rel": [["aa", "艾 AA", "相伴一生"], ["cheng", "程心", "暗恋"], ["wei", "维德", "阶梯计划"]], "quoteSource": "", "quoteSourceName": ""}, "aa": {"name": "艾 AA", "role": "天文学研究者 · 程心之友", "deeds": "威慑时代的天文学研究者，后来成为程心的朋友与事业伙伴。她与程心共同经历大移民、解读童话和逃离太阳系；程心与关一帆离开蓝星后，她留在那里并与到访的云天明相伴。", "quote": "", "camp": "威慑之后", "campKey": "hou", "color": "#5a3a6b", "link": "e46", "linkName": "六十年后", "rel": [["yun", "云天明", "相伴一生"], ["cheng", "程心", "挚友"]], "quoteSource": "", "quoteSourceName": ""}, "guan": {"name": "关一帆", "role": "宇宙学研究者 · 万有引力号船员", "deeds": "万有引力号上的宇宙学研究者，曾与褚岩等人探索四维碎片。后来在 DX3906 与程心相遇，两人乘穿梭机前往灰星，因死线扩散错过云天明与艾 AA，最终进入 647 号小宇宙。他是原船员本人。", "quote": "", "camp": "威慑之后", "campKey": "hou", "color": "#5a3a6b", "link": "e65", "linkName": "黑域", "rel": [["cheng", "程心", "同行"]], "quoteSource": "", "quoteSourceName": ""}, "shou": {"name": "三体元首", "role": "三体世界统治者", "deeds": "三体世界的最高统治者，主持入侵太阳系的远征与智子工程，为身处三恒星系统中的文明寻找稳定家园。小说中的不同时期不能简单理解为同一位统治者一直在位。", "quote": "", "camp": "三体与宇宙", "campKey": "san", "color": "#1f5d57", "link": "e10", "linkName": "舰队与智子", "rel": [["zhizi", "智子", "智子工程"]], "quoteSource": "", "quoteSourceName": ""}, "l1379": {"name": "1379 号", "role": "三体世界监听员", "deeds": "三体世界的一名监听员。收到地球信号后，他冒着被惩罚的风险发出警告，希望地球不再回答，使三体方面无法确认其位置。后来他与罗辑有过交流，仍表达了对不同文明间善意的期待。", "quote": "不要回答！不要回答！不要回答！！！", "camp": "三体与宇宙", "campKey": "san", "color": "#1f5d57", "link": "e7", "linkName": "不要回答", "rel": [["ye", "叶文洁", "警告"]], "quoteSource": "https://www.bidutuijian.com/books/santi/032.html", "quoteSourceName": "《三体》监听员"}, "zhizi": {"name": "智子", "role": "三体世界的超级计算机与使者", "deeds": "经低维展开与电路蚀刻制成的质子计算机，负责干扰人类高能物理实验和监视地球。后来三体方面通过名为智子的女性仿生机器人与人类交流；机器人的外形不等同于微观质子本身。", "quote": "", "camp": "三体与宇宙", "campKey": "san", "color": "#1f5d57", "link": "e10", "linkName": "舰队与智子", "rel": [["shou", "三体元首", "智子工程"], ["luo", "罗辑", "对峙"]], "quoteSource": "", "quoteSourceName": ""}, "ge": {"name": "歌者", "role": "宇宙清理者", "deeds": "种子飞船上的清理员。他检查暴露文明的坐标与太阳系的行星布局，判断质量点难以清理全部目标，向长老申请并投出二向箔。他与程心没有直接交往。", "quote": "", "camp": "三体与宇宙", "campKey": "san", "color": "#1f5d57", "link": "e62", "linkName": "歌者", "rel": [], "quoteSource": "", "quoteSourceName": ""}};

  var nodes = [].slice.call(document.querySelectorAll('.pnode'));
  var links = [].slice.call(document.querySelectorAll('.plink'));
  var labels = [].slice.call(document.querySelectorAll('.rlabel'));
  var panel = document.getElementById('pdetail');

  // 邻接表
  var adj = {};
  nodes.forEach(function(n){ adj[n.dataset.id] = []; });
  links.forEach(function(l){
    var a = l.dataset.a, b = l.dataset.b;
    if (adj[a] && adj[a].indexOf(b) < 0) adj[a].push(b);
    if (adj[b] && adj[b].indexOf(a) < 0) adj[b].push(a);
  });

  // 原始坐标
  var pos = {}, orig = {};
  nodes.forEach(function(n){
    var mm = n.getAttribute('transform').match(/translate\(([-\d.]+),([-\d.]+)\)/);
    var x = parseFloat(mm[1]), y = parseFloat(mm[2]);
    pos[n.dataset.id] = { x: x, y: y };
    orig[n.dataset.id] = { x: x, y: y };
  });

  var CX = 620, CY = 350;
  var raf = null;

  function apply(){
    nodes.forEach(function(n){
      var p = pos[n.dataset.id];
      n.setAttribute('transform', 'translate(' + p.x.toFixed(1) + ',' + p.y.toFixed(1) + ')');
    });
    links.forEach(function(l){
      var a = pos[l.dataset.a], b = pos[l.dataset.b];
      if (!a || !b) return;
      l.setAttribute('x1', a.x.toFixed(1));
      l.setAttribute('y1', a.y.toFixed(1));
      l.setAttribute('x2', b.x.toFixed(1));
      l.setAttribute('y2', b.y.toFixed(1));
    });
    labels.forEach(function(t){
      var a = pos[t.dataset.a], b = pos[t.dataset.b];
      if (!a || !b) return;
      t.setAttribute('x', ((a.x + b.x) / 2).toFixed(1));
      t.setAttribute('y', ((a.y + b.y) / 2 - 4).toFixed(1));
    });
  }

  function animateTo(targets, dur){
    if (raf) cancelAnimationFrame(raf);
    var start = {};
    Object.keys(targets).forEach(function(id){ start[id] = { x: pos[id].x, y: pos[id].y }; });
    var t0 = performance.now();
    dur = dur || 620;

    function step(t){
      var k = Math.min(1, (t - t0) / dur);
      var e = 1 - Math.pow(1 - k, 3);
      Object.keys(targets).forEach(function(id){
        var s0 = start[id], tg = targets[id];
        pos[id] = { x: s0.x + (tg.x - s0.x) * e, y: s0.y + (tg.y - s0.y) * e };
      });
      apply();
      if (k < 1) raf = requestAnimationFrame(step);
      else raf = null;
    }
    raf = requestAnimationFrame(step);
  }

  var cur = null;

  function resetStyles(){
    nodes.forEach(function(n){
      n.style.opacity = '';
      n.style.pointerEvents = '';
      n.removeAttribute('aria-hidden');
      n.classList.remove('dim','sel');
      n.querySelector('circle').setAttribute('r', 27);
      n.querySelector('.pname').style.fontSize = '';
    });
    links.forEach(function(l){ l.classList.remove('dim','hot'); });
    labels.forEach(function(t){ t.classList.remove('show','dim'); });
  }

  // 以某人为中心重排
  function layoutEgo(id){
    resetStyles();
    var nbrs = (adj[id] || []).slice();

    // 二阶：一阶的邻居，排除中心和一阶
    var seen = {};
    seen[id] = 1;
    nbrs.forEach(function(n){ seen[n] = 1; });
    var second = [];
    nbrs.forEach(function(n){
      (adj[n] || []).forEach(function(k){
        if (!seen[k]){ seen[k] = 1; second.push(k); }
      });
    });
    second = second.slice(0, 14);

    var targets = {};

    // 其余节点收拢到中心（几乎不可见），避免飞出画面
    nodes.forEach(function(n){
      if (n.dataset.id !== id && nbrs.indexOf(n.dataset.id) < 0 && second.indexOf(n.dataset.id) < 0){
        targets[n.dataset.id] = { x: CX, y: CY };
        n.style.opacity = 0;
        n.style.pointerEvents = 'none';
        n.setAttribute('aria-hidden', 'true');
      }
    });

    // 中心
    targets[id] = { x: CX, y: CY };
    var nc = nodes.filter(function(x){ return x.dataset.id === id; })[0];
    nc.style.opacity = 1;
    nc.classList.add('sel');
    nc.querySelector('circle').setAttribute('r', 34);
    nc.querySelector('.pname').style.fontSize = '13px';

    // 一阶
    var R1 = 180;
    nbrs.forEach(function(nid, i){
      var ang = (i / Math.max(1, nbrs.length)) * Math.PI * 2 - Math.PI / 2;
      targets[nid] = { x: CX + Math.cos(ang) * R1, y: CY + Math.sin(ang) * R1 };
      var g = nodes.filter(function(x){ return x.dataset.id === nid; })[0];
      g.style.opacity = 1;
      g.querySelector('circle').setAttribute('r', 25);
    });

    // 二阶
    var R2 = 300;
    second.forEach(function(nid, i){
      var ang = (i / Math.max(1, second.length)) * Math.PI * 2 - Math.PI / 2 + 0.22;
      targets[nid] = { x: CX + Math.cos(ang) * R2, y: CY + Math.sin(ang) * R2 };
      var g = nodes.filter(function(x){ return x.dataset.id === nid; })[0];
      g.style.opacity = 0.5;
      g.querySelector('circle').setAttribute('r', 18);
      g.querySelector('.pname').style.fontSize = '9px';
    });

    // 线：只保留中心相关的 + 一阶之间的
    links.forEach(function(l){
      var a = l.dataset.a, b = l.dataset.b;
      var on = (a === id || b === id) || (nbrs.indexOf(a) >= 0 && nbrs.indexOf(b) >= 0);
      l.classList.toggle('hot', a === id || b === id);
      l.classList.toggle('dim', !on);
      l.style.opacity = on ? '' : 0.04;
    });
    labels.forEach(function(t){
      var a = t.dataset.a, b = t.dataset.b;
      var on = (a === id || b === id) || (nbrs.indexOf(a) >= 0 && nbrs.indexOf(b) >= 0);
      t.classList.toggle('show', on);
      t.classList.toggle('dim', !on);
    });

    animateTo(targets);
  }

  function layoutAll(){
    resetStyles();
    cur = null;
    CX = 620;
    var targets = {};
    nodes.forEach(function(n){
      targets[n.dataset.id] = orig[n.dataset.id];
      n.style.opacity = '';
      n.querySelector('circle').setAttribute('r', 27);
      n.querySelector('.pname').style.fontSize = '';
    });
    links.forEach(function(l){ l.style.opacity = ''; });
    labels.forEach(function(t){ t.classList.remove('show','dim'); });
    panel.classList.remove('on');
    animateTo(targets);
  }

  function openDetail(id){
    var d = DATA[id];
    if (!d) return;
    cur = id;
    // 面板占据右侧，把网络重心左移，避免任何节点被压住
    CX = window.innerWidth > 1080 ? 450 : 620;
    layoutEgo(id);

    var camp = document.getElementById('pdCamp');
    camp.textContent = d.camp;
    camp.style.color = d.color;
    camp.style.boxShadow = 'inset 0 0 0 1px ' + d.color + '55';
    camp.style.background = 'rgba(0,0,0,0.025)';

    document.getElementById('pdName').textContent = d.name;
    document.getElementById('pdRole').textContent = d.role;
    document.getElementById('pdDeeds').textContent = d.deeds;
    var quote = document.getElementById('pdQuote');
    quote.textContent = d.quote;
    quote.hidden = !d.quote;
    var source = document.getElementById('pdQuoteSource');
    source.hidden = !d.quoteSource;
    source.href = d.quoteSource || '#';
    source.textContent = d.quoteSource ? '原文出处 · ' + d.quoteSourceName + ' ↗' : '';
    var lk = document.getElementById('pdLink');
    lk.href = 'index.html#' + d.link;
    lk.textContent = '时间线 · ' + d.linkName + ' →';

    var rel = document.getElementById('pdRel');
    rel.innerHTML = '';
    (d.rel || []).forEach(function(r){
      var b = document.createElement('button');
      b.innerHTML = '<b>' + r[1] + '</b><i>' + r[2] + '</i>';
      b.addEventListener('click', function(){ openDetail(r[0]); });
      rel.appendChild(b);
    });
    panel.classList.add('on');
  }

  nodes.forEach(function(n){
    n.addEventListener('click', function(){
      if (cur === n.dataset.id) return;
      openDetail(n.dataset.id);
    });
  });

  document.getElementById('pdClose').addEventListener('click', layoutAll);

  document.getElementById('allBtn').addEventListener('click', function(){
    var btns = [].slice.call(document.querySelectorAll('.fbtn'));
    btns.forEach(function(x){ x.classList.remove('on'); });
    document.getElementById('allBtn').classList.add('on');
    layoutAll();
  });

  // 阵营筛选（不改变布局，只淡化）
  var btns = [].slice.call(document.querySelectorAll('.fbtn'));
  btns.forEach(function(b){
    if (b.id === 'allBtn') return;
    b.addEventListener('click', function(){
      btns.forEach(function(x){ x.classList.remove('on'); });
      b.classList.add('on');
      layoutAll();
      var camp = b.dataset.camp;
      nodes.forEach(function(n){
        var d = DATA[n.dataset.id];
        if (!(d && d.campKey === camp)) n.style.opacity = 0.1;
      });
    });
  });
})();
