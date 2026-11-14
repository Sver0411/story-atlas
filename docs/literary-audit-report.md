# Story Atlas 全站文学内容审校报告

审校基线为本地 main 的 7e8d86d。此前的[优化报告](content-optimization-report.md)、[新增书目审查](new-books-content-audit.md)、[审查回应](audit-response.md)、[三体复核](content-review.md)、[分书口径](notes/)和[插画审查](illustration-audit.md)用于确定复核入口。以本轮修改后的实际正文为准。

已盘点59部作品的收录范围、时间线和人物志，每部至少修订一个高风险节点。下表分别记录已改内容、卷章定位及待核事项。能查阅公开原文或译文的，提供文本入口；作者与出版社介绍仅供核对版本或大纲。只有印本定位的条目仍需用指定版复核。本轮未完成逐句原著对读，也未核尽所有既有人物关系与未改节点。

## 修改前后

| 项目 | 基线 | 本轮 |
| --- | ---: | ---: |
| 作品 | 59 | 59 |
| 故事节点 | 1410 | 1414 |
| 人物卡 | 941 | 945 |
| 全站直接人物关系，含《三体》33组 | 1243 | 1243 |
| 数据作品直接关系数 | 1210 | 1210 |
| 有章节出处字段 src 的数据节点 | 137 | 357 |
| 有 src 或 sourceIds 的数据节点 | 311 | 523 |
| 插图事件关联 | 383 | 383 |

58部数据作品有287个事件条目变更，计入新增、正文、时间和分段。共有156张人物卡变更，计入新增、传记、身份及事件关联。《三体》手写页面另改10个事件及歌者人物卡。原有事件 ID 和人物 ID 全部保留。旧统计的1210条关系仅涵盖数据作品，《三体》另有33组。

《时光之轮》新增 tw08a 杜迈井、tw08b 净化阳极力、tw11a 龙山；《飓光志》新增 sa09b 沙兰在营地调查。《基地》新增彭耶茨、里欧斯、密斯及法洛姆，把缺少正文依据的“萨雷什”“肯迪”旧卡改为有明确剧情的钱尼斯与盖尔·多尼克，两个旧锚点继续可用。同步密斯与贝泰、法洛姆与丹尼尔的关系，并重写若干既有关系标签。

首页、目录元数据与 README 核对了节点数、人物数和收录范围。《红楼梦》统一为52个节点。修复了《沙丘》《魔戒》《百年孤独》10个数据节点的分段引用，并校订了仍与改后正文冲突的《沙丘》附段及若干页脚文字。

## 59 部逐书审查

| 作品 · 当前节点 / 人物 | 事件 ID | 问题与实际修订 | 卷章和来源 | 仍待复核 |
| --- | --- | --- | --- | --- |
| [三体](../books/three-body/index.html) · 68 / 32 | e20、e26、e59、e60、e62–e64、e66–e68 | 纠正危机纪年、章北海暗杀、星环城对峙、歌者与太阳系打击和小宇宙尾声；同步歌者人物志。 | 《黑暗森林》上部、《死神永生》第五、六部。[66年太阳系外围](https://www.99csw.com/book/3317/111964.htm)、[67年冥王星](https://www.99csw.com/book/3317/111965.htm) | e25、e27 等仍有原创对白与时间待核。 |
| [三国演义](../books/three-kingdoms/index.html) · 49 / 35 | `tk01`、`tk02`、`tk41`、`tk42` | 压缩桃园与黄巾的重复叙述，改怒鞭督邮、姜维复国失败及晋军入建业。 | 毛宗岗本第1–2、118–120回。[毛宗岗本](https://zh.wikisource.org/wiki/三國志演義) | 近期开出的战役节点需区分章回故事与史书。 |
| [水浒传](../books/water-margin/index.html) · 44 / 128 | `wm33`、`wm34` | 按托梦、墓前相见、自缢、徽宗显灵祭祀重写。 | 一百二十回本第120回。[一百二十回本](https://zh.wikisource.org/wiki/水滸傳_(120回本)) | 招安次序、方腊战役阵亡名单及绰号待核。 |
| [西游记](../books/journey-west/index.html) · 51 / 37 | `xy35`、`xy34` | 先查难簿，再落水晒经书，各保留一个事件。 | 通行本第99回。[章回文本](https://zh.wikisource.org/wiki/西遊記/第099回) | 复核各次过河和妖怪来历。 |
| [红楼梦](../books/red-chamber/index.html) · 52 / 40 | `rc41`、`rc42` | 恢复甄士隐、贾雨村及石头叙事框架，区分贾府将来的预述和人物当时的经历。首页统一为52个节点。 | 程甲本第1、120回。[程甲本末回](https://zh.wikisource.org/wiki/紅樓夢（程甲本）/一百二十) | 程甲、程乙异文与其他人物结局。 |
| [基督山伯爵](../books/monte-cristo/index.html) · 44 / 28 | `mc35b`、`mc36` | 删旧港会海黛及船上对白。恢复梅尔塞苔丝的归处、岛上团聚及最后的信。 | 第112、117章。[公开文本](https://www.gutenberg.org/ebooks/1184) | mc34b 等复仇后心理活动、马赛段落先后。 |
| [百年孤独](../books/solitude/index.html) · 45 / 26 | `so18b`、`so23b`、`so35b`、`so36`、`so37` | 去掉蚂蚁段落复述与镜子，重述母子死亡和羊皮卷破译；纠正3个节点的分段。 | 小说末章。[Penguin 版本信息](https://www.penguin.co.uk/books/57241/one-hundred-years-of-solitude-by-gabriel-garcia-marquez-trans-gregory-rabassa/9780141184999) | so33、so35b 的衰败描写与七代谱系。 |
| [魔戒](../books/lotr/index.html) · 44 / 27 | `lr04b`、`lr06b`、`lr11b`、`lr31b`、`lr33b`、`lr35`、`lr36` | 恢复宴会树、红皮书、灰港与山姆归家；纠正5个节点的分段。 | 《王者归来》第六部第9章。[托尔金遗产机构书目](https://www.tolkienestate.com/writing/the-lord-of-the-rings/) | 魔多、刚铎和洛汗的并行日期，夏尔清洗全线。 |
| [沙丘](../books/dune/index.html) · 40 / 23 | `du24`、`du24b`、`du23`、`du29b`、`du31b`、`du32` | 骑虫重复、戈尼口径冲突及加冕误写已改。恢复政治婚约与杰西卡安慰契妮，同步决斗附段及分段。 | 1965年小说第三篇〈先知〉末段。[Ace 版信息](https://www.penguinrandomhouse.com/books/352036/dune-by-frank-herbert/) | du03b、du05b 与其他附段仍需逐章核对。 |
| [基地](../books/foundation/index.html) · 38 / 22 | fd01–fd30，含带后缀的全部节点 | 38个节点重写，区分数学大会、帝国审判、哈定两次危机、马洛、骡、塔森及崔维兹的选择与解释。补人物并更正两张无出处旧卡。 | 七部小说。《基地》第一至第五部、《基地与帝国》《第二基地》结尾、《基地与地球》第21章。[出版社书目](https://www.penguinrandomhouse.com/series/FOU/foundation/)、[三部曲文本](https://s3.us-west-1.wasabisys.com/luminist/EB/A/Asimov%20-The%20Foundation%20Trilogy.pdf)、[《基地与地球》文本](https://vinaire.me/wp-content/uploads/2024/11/07-isaac-asimov-foundation-and-earth.pdf) | 前传跨年与译名、《基地边缘》各章细节需继续对读。 |
| [地海传奇](../books/earthsea/index.html) · 15 / 7 | `ed01`、`ed02`、`ed03`、`ed04`、`ed05`、`ed06`、`ed07`、`ed08`、`ed09`、`ed10`、`ed11`、`ed13b`、`ed12`、`ed13`、`ed14` | 15个节点改写；纠正贡特授名、柔克放出影子、旱域封缝与失去法力、泰娜收留瑟鲁及古龙来救。 | 前四部。《地海巫师》第1–4、9–10章，《地海孤雏》末章。[作者书目和资料](https://www.ursulakleguin.com/a-wizard-of-earthsea)、[《地海孤雏》](https://www.ursulakleguin.com/tehanu) | 需用同一译本校准真名、岛名和各章节译名。 |
| [冰与火之歌](../books/thrones/index.html) · 34 / 42 | `got01`、`got02`、`got03`、`got04`、`got30`、`got31`、`got32`、`got33`、`got34` | 纠正游骑兵命运、泰莎身份、长城守军及丹妮莉丝第三卷收束；补梅里认出凯特琳。 | 《权力的游戏》序幕、布兰Ⅰ；《冰雨的风暴》提利昂、丹妮莉丝等视角及尾声。[出版社序幕试读](https://www.penguinlibros.com/pe/fantasia/350577-libro-juego-de-tronos-cancion-de-hielo-y-fuego-1-9788466374934/fragmento) | got05–got29 仍有逐句扩写待核，第三卷需对读指定中译。 |
| [纳尼亚传奇](../books/narnia/index.html) · 16 / 16 | nr01–nr15，含 nr07b | 创世与树林分开，删四王共用1900年的标记，重述卡斯宾决斗、瑞利安返家及最后一战。 | 七部原著。创世据《魔法师的外甥》第2–10、13–15章。[加拿大古登堡文本](https://www.gutenbergca.gutenbergcanada.ca/ebooks/lewiscs-magiciansnephew/lewiscs-magiciansnephew-00-h.html) | 采用相对纪年；路易斯的手稿年表和中译各卷译名待统一。 |
| [时光之轮](../books/wheel-of-time/index.html) · 17 / 6 | `tw01`、`tw02`、`tw03`、`tw04`、`tw05`、`tw06`、`tw07`、`tw09`、`tw10`、`tw08a`、`tw08b`、`tw08`、`tw11a`、`tw11`、`tw13`、`tw12`、`tw14` | 纠正至上力和白塔分裂，写回艾雯牺牲、兰德换身和烟斗；新增杜迈井、阳极力净化及龙山。 | 第1、3、4、6、9、12、14卷。末卷第37、47–49章及尾声。[桑德森作品资料](https://www.brandonsanderson.com/pages/the-wheel-of-time-series)、[末卷小说文本入口](https://thepreachersportal.org/wp-content/uploads/2022/02/A_Memory_of_Light_-_Robert_Jordan.pdf)、[作者对尾声归属的说明](https://faq.brandonsanderson.com/knowledge-base/what-did-you-think-of-working-on-wot/) | 十四卷中段仍压缩，佩林、麦特和霄辰政治线需续核。 |
| [飓光志](../books/stormlight/index.html) · 14 / 6 | `sa06`、`sa01`、`sa02`、`sa03`、`sa04`、`sa05`、`sa08`、`sa09`、`sa07`、`sa09b`、`sa10`、`sa11`、`sa12`、`sa13` | 重整前两卷，修正桥四、拜师地点、决斗、纳拉克、誓门及加斯娜回归。新增沙兰在营地调查；赛兹结局采用修订文本。 | 《王道》序章及第59、67–69、75章；《光辉真言》第7、56–58、80–89章及尾声。[作者公开章节](https://www.brandonsanderson.com/blogs/blog/words-of-radiance-sample-chapters)、[终局改版说明](https://www.brandonsanderson.com/blogs/blog/three-stories-in-new-formats) | 需按印本核准章节和译名，特别是光辉骑士誓言译法。 |
| [猎魔人](../books/witcher/index.html) · 16 / 7 | `wt07`、`wt10`、`wt11`、`wt12`、`wt12b`、`wt14`、`wt13`、`wt15` | 纠正沙漠卷次与草叉发生地点，恢复恩希尔身份、雾中小船及加拉哈德框架，删开小屋等续写。 | 《轻蔑时代》第6章；《湖中夫人》第1、9、12章。[Orbit 版本](https://www.hbglibrary.com/titles/andrzej-sapkowski/the-lady-of-the-lake/9780316273770/) | 前卷短篇编年、岛上所见和中译用词需对读。 |
| [第一律法](../books/first-law/index.html) · 12 / 5 | `fl09`、`fl11`、`fl12` | 纠正两条律法，恢复黑道夺权及格洛塔任首席审判官，移除拜亚兹临窗独白。 | 《刀刃本身》及第三部末。[作者第三部书目](https://joeabercrombie.com/books/last-argument-of-kings/) | 需按统一英版精确定位卷末；费罗与种子情节仍需对读。 |
| [索拉里斯星](../books/solaris/index.html) · 16 / 5 | `so05`、`so06`、`so13`、`so14`、`so15`、`so16` | 恢复海若是已故伴侣、第一次火箭与第二次自愿消除，删虚构报告。 | 波兰原著第6、13、14章。[莱姆官网](https://lem.pl/en/works/novels/solaris)、[Bill Johnston 英译文本](https://xxn.org.uk/lib/exe/fetch.php?media=solaris-stanislaw-lem-bill-johnston.pdf) | so07–so12 对白和实验次序仍需复核。 |
| [神经漫游者](../books/neuromancer/index.html) · 14 / 7 | `nm10`、`nm13`、`nm14` | 恢复科托身份、舱体结局、莫莉离开和矩阵中的三个身影。 | 第四部及尾声。[小说文本](https://www.zaco.au/lib/fiction/William%20Gibson%20-%20Neuromancer.pdf) | 冬寂及神经漫游者的行动细节、人工智能术语。 |
| [安德的游戏](../books/enders-game/index.html) · 16 / 7 | `eg13`、`eg14`、`eg15`、`eg16` | 重建殖民航程、发现蜂后和写作《蜂后》《霸主》的因果；纠正彼得政治身份。 | 第9、15章。[Macmillan 版本](https://us.macmillan.com/books/9781429963930/endersgame/)、[第15章文本入口](https://mrhparson.weebly.com/uploads/1/0/7/0/10708100/ender%27s_game_pdf.pdf) | 战斗学校与指挥学校仍需逐章复核。 |
| [海伯利安](../books/hyperion/index.html) · 14 / 9 | `hp08`、`hp09`、`hp10`、`hp11`、`hp12`、`hp13`、`hp14` | 移除伯劳鸟在冢边点名及卡萨德冲入火线，恢复马斯蒂恩失踪和六人唱歌继续前行。 | 第一部第5–6章及尾声。[出版社序章](https://www.penguinrandomhouse.ca/books/167468/hyperion-by-dan-simmons/9780399178610/excerpt) | 马斯蒂恩失踪所在小节及各人较早的回忆需复核。 |
| [一九八四](../books/nineteen-eighty-four/index.html) · 20 / 10 | `n84_18`、`n84_19`、`n84_20` | 恢复获释后重遇茱莉亚、咖啡馆战报与内心屈服；脑后子弹属于想象。 | 第三部第6章。[原著全文](https://www.gutenberg.net.au/ebooks01/0100021h.html) | 真理部文件、果尔德施坦因书稿和心理细节。 |
| [美丽新世界](../books/brave-new-world/index.html) · 18 / 8 | `bn14`、`bn15`、`bn18`、`bn17` | 恢复课堂朗读、流放、约翰与蒙德讨论及灯塔结局，删蒙德发药的续写。 | 第12、15–18章。 | 福特纪元、保留地及琳达死亡段落。 |
| [童年的终结](../books/childhoods-end/index.html) · 15 / 6 | `ce13`、`ce14`、`ce15` | 恢复扬留守观察、播报中断和卡瑞林最后离去，删除“地球只剩荒地”的续写。 | 第23–24章。[原著章节](https://www.thetedkarchive.com/library/arthur-c-clarke-childhood-s-end)、[出版社导读](https://www.penguinrandomhouse.com/books/28158/childhoods-end-by-arthur-c-clarke/9780345444059/teachers-guide/) | 1953年版与后版开篇、前段时距。 |
| [与拉玛相会](../books/rama/index.html) · 15 / 5 | `rm13`、`rm14`、`rm15` | 改为罗德里戈处理武器；删诺顿私人报告，恢复以“三个一组”收尾。 | 第一部末段。[Hachette 核对末句](https://www.hachette.co.uk/authors/2013/09/27/from-the-sfx-book-club-rendezvous-with-rama/) | 探测地形、装备、离去场景的章节定位。 |
| [银河系搭车客指南](../books/hitchhiker/index.html) · 15 / 5 | `hg16`、`hg14` | 恢复马格拉西亚老鼠的动机和重新出发，把指南提示移到开头。 | 第一部开篇及末章。 | 区分小说、广播稿和续作，复查登上黄金之心。 |
| [华氏 451](../books/fahrenheit-451/index.html) · 15 / 6 | `fh14`、`fh15` | 删无依据的书目对白，恢复格兰杰的凤凰比喻和走向被毁城市。 | 第三部〈火光灿烂〉末。 | 前两部分的失踪、搜捕和广播。 |
| [美国众神](../books/american-gods/index.html) · 16 / 6 | `ag15`、`ag14b` | 删冰岛酒馆假对白及收尾说教，恢复另一个奥丁与玻璃眼；把美国段移到冰岛段之前。 | 美国段尾声及冰岛后记。 | 初版和作者首选版须择一，另核 ag11–ag14 和萨姆段动作。 |
| [福尔摩斯探案集](../books/sherlock/index.html) · 23 / 16 | `sh01`、`sh17`、`sh19`、`sh21`、`sh22`、`sh23` | 删墙中尸体，恢复埃文斯假借遗产逼人离开；修订魔鬼之足、王冠宝石案、养蜂与冯·博克行动。 | 〈三个加里德布〉、〈王冠宝石案〉、〈魔鬼之足〉及〈最后致意〉。[《案件簿》](https://gutenberg.ca/ebooks/doyleac-casebookofsherlockholmes/doyleac-casebookofsherlockholmes-00-e.html)、[《最后致意》](https://www.gutenberg.org/files/2350/2350-h/2350-h.htm) | 其余案件故事内部的确切日期仍待核。 |
| [双城记](../books/two-cities/index.html) · 25 / 13 | `tc01`、`tc09`、`tc22`、`tc24`、`tc23`、`tc20`、`tc21`、`tc25` | 侯爵之死移到巴士底狱前，恢复证词、书信、缝衣女工及卡顿牺牲；把未来写回叙述者的假设。 | 第二卷第7–9、15章；第三卷第10、12–15章。[狄更斯原文](https://www.gutenberg.org/files/98/98-h/98-h.htm) | 第二卷中段及恐怖时期的具体日期。 |
| [教父](../books/godfather/index.html) · 14 / 13 | `gf12`、`gf13`、`gf14` | 删电影式洗礼蒙太奇及凯在教堂遇见迈克尔手下，恢复家族清算、康妮质问与弥撒。 | 1969年小说第九部末。[普佐与科波拉访谈，改编背景](https://www.nepm.org/2019-03-08/a-look-back-at-the-godfather-with-mario-puzo-and-francis-ford-coppola?_amp=true) | 维托旧事、清算顺序、汤姆与凯的完整对话。 |
| [傲慢与偏见](../books/pride-prejudice/index.html) · 24 / 15 | `pp23`、`pp24` | 删父女虚构谈话。恢复父亲对婚事的忧虑、达西帮助莉迪亚及彭伯里结局。 | 第59、61章。[奥斯汀原文](https://www.gutenberg.org/ebooks/1342) | pp15–pp21 求婚和私奔的平行时间。 |
| [简·爱](../books/jane-eyre/index.html) · 28 / 14 | `je27`、`je28` | 删婚礼及视力恢复的对白，恢复十年后回顾叙述和末尾圣约翰。 | 第38章。[勃朗特原文](https://www.gutenberg.org/ebooks/1260) | 劳渥德的年序、伯莎身份及原著用语。 |
| [战争与和平](../books/war-peace/index.html) · 21 / 12 | `wp01` | 重写沙龙开场与拿破仑引发的争论，删皮埃尔与安德烈虚构对谈。 | 第一卷第一部第1–6章。[小说全文](https://www.gutenberg.org/ebooks/2600) | 1805与1812两线、人物归宿和尾声日期。 |
| [呼啸山庄](../books/wuthering/index.html) · 20 / 11 | `wh01` | 拆开洛克伍德两次来访，恢复刻字、狗及冒雪再访。 | 第1–2章。[勃朗特原文](https://www.gutenberg.org/cache/epub/768/pg768-images.html) | 耐莉倒叙与洛克伍德叙事现在的关系。 |
| [安娜·卡列尼娜](../books/anna-karenina/index.html) · 20 / 9 | `ak20` | 删列文与基蒂想象中的田间对答，恢复农人谈话、雷雨及末章感悟。 | 第八部第11–19章。[小说全文](https://www.gutenberg.org/ebooks/1399) | 安娜与列文双线、家庭关系和具体日期。 |
| [飘](../books/gone-wind/index.html) · 18 / 11 | `gw18` | 删斯佳丽与父亲相关的无据对白，重述想起塔拉和明天。 | 第63章末。 | 1870标记和不同改编中的对白。 |
| [巴黎圣母院](../books/notre-dame/index.html) · 16 / 8 | `nd16` | 墓窟发现移到行刑后一两年，删填土立碑。 | 第十一卷第4章。[雨果法文原文](https://www.gutenberg.org/files/19657/19657-h/19657-h.htm) | 诉讼及刑场关键次序、改编混入。 |
| [悲惨世界](../books/les-miserables/index.html) · 30 / 14 | `lm27`、`lm28`、`lm29`、`lm30` | 整理衣角证据、银烛台与无名墓碑，删冉阿让死亡场景的旁白添写。 | 第五部第九卷第4–6章。[雨果原文入口](https://www.gutenberg.org/ebooks/135) | 芳汀、街垒、德纳第的时间和经历。 |
| [静静的顿河](../books/quiet-don/index.html) · 12 / 8 | `qd11`、`qd12` | 删临终及父子重逢的扩写，恢复埋葬、投枪和归家抱子。 | 第八部末章。 | 俄文版和中译卷次，前段战事及阵营归属。 |
| [日瓦戈医生](../books/zhivago/index.html) · 14 / 7 | `zh12b`、`zh13` | 删电车中握诗稿、拉拉续写；恢复街头死亡、悼念、塔尼娅和诗篇。 | 第十五部末、第十六及十七部。 | 指定译本、塔尼娅叙述层次和尾声跳年。 |
| [白夜行](../books/byakuyakou/index.html) · 28 / 18 | byx01–byx28 | 二十五年改为自1973年起十九年。28个节点重排并改写，删除黑市账本、虚构婚礼、死亡细节及终章遗言等，区分调查推断与已知事实。 | 第1–13章，重点第6–8、10–13章。[集英社书目](https://www.shueisha.co.jp/books/items/contents_amp.html?isbn=4-08-747439-0)、[小说译本目录](https://read.99csw.com/book/2910/index.html)、[第13章第14节](https://read.99csw.com/book/2910/90910.html) | 指定日文印本对读都子、江利子、美佳的细节及其时间表。 |
| [东方快车谋杀案](../books/orient-express/index.html) · 27 / 21 | `oe25`、`oe26`、`oe27` | 恢复哈德曼与苏珊娜的联系、伯爵代妻及布克特选择；删警方到场和列车放行。 | 第三部第9章。[克里斯蒂官网](https://www.agathachristie.com/stories/murder-on-the-orient-express) | 车厢平面、手帕及证词仍需逐章回看。 |
| [嫌疑人 X 的献身](../books/suspect-x/index.html) · 28 / 12 | `sx27`、`sx28` | 删审讯室对白及汤川后续，重述靖子自首、石神痛哭，点明两名死者。 | 原著末章。 | sx06–sx08、sx21–sx26 的案发时间和反转揭晓时点。 |
| [无人生还](../books/and-then-there-were-none/index.html) · 22 / 13 | `at16`、`at17`、`at19`、`at20`、`at21`、`at22` | 删警方取证续写，改法官假死、漂流瓶、最后自白与岛外莫里斯。 | 第16章、警方尾声、法官手稿。[克里斯蒂作品及改编资料](https://www.agathachristie.com/stories/and-then-there-were-none) | 版本岛名、童谣和各死亡现场的次序。 |
| [漫长的告别](../books/long-goodbye/index.html) · 26 / 13 | `lg25`、`lg26` | 删信件、窗外与心理扩写，恢复换了身份的伦诺克斯来访及最后告别。 | 原著末章。 | 艾琳、罗杰和西尔维亚的证词串联。 |
| [消失的爱人](../books/gone-girl/index.html) · 26 / 13 | `gg25`、`gg26` | 删尼克虚构独白，恢复孩子造成的牵制，结尾回到艾米的叙述。 | 第三部末。 | 全书相对纪日、日记和口供的叙述层次。 |
| [龙纹身的女孩](../books/millennium/index.html) · 24 / 15 | `lg23`、`lg24` | 删藏钱钥匙与换名字搬家，恢复圣诞礼物和莎兰德看到贝里与布隆维斯特。 | 第一部圣诞尾声。 | 银行交易与范耶尔家族年表逐章校准。 |
| [边城](../books/border-town/index.html) · 12 / 6 | `bc08`、`bc09` | 删傩送成家传闻和翠翠拒媒，恢复杨马兵与等待的开放结局。 | 第21章末。 | bc06–bc07c 雷雨、修塔的先后及更多人物动作。 |
| [围城](../books/fortress/index.html) · 16 / 7 | `wch14`、`wch15` | 删报馆改字与出走后没回家，恢复工作挫折和慢五个小时的自鸣钟。 | 第9章。[末章文本](https://mail.99csw.com/book/2619/79461.htm) | 三闾大学各阶段和公历年份。 |
| [平凡的世界](../books/ordinary-world/index.html) · 15 / 8 | `ph13` | 恢复少安修校与秀莲病倒，删除少平返乡观摩的串线。 | 第三部学校落成段。 | ph14–ph15 年份与晓霞、东宝人物线。 |
| [白鹿原](../books/white-deer/index.html) · 15 / 10 | `bl12` | 删除鹿子霖在雪地冻死及手攥土的细节，保留失势与精神失常。 | 小说末段鹿子霖线。 | 需用指定版确认鹿子霖最后的结局以及前后年代。 |
| [活着](../books/to-live/index.html) · 14 / 11 | `tl13`、`tl14` | 删牛的眼泪、价格及多年后对白，恢复采风叙事框架。 | 小说末段。 | 家人死亡次序及福贵家产变化。 |
| [尘埃落定](../books/red-poppies/index.html) · 22 / 11 | `cl21`、`cl22` | 删军队进村和临终虚构对白、未核实的收束年份，重写土司退场。 | 小说末两章。 | 二少爷仇家身份与结尾场景顺序。 |
| [穆斯林的葬礼](../books/muslim-funeral/index.html) · 22 / 10 | `ms22` | 去除墓前爱尔兰民谣、下雪及探访约定，保留楚雁潮悼念。 | 小说尾声。 | ms20–ms21 及家族身份揭示的时间。 |
| [射雕英雄传](../books/legend-condor/index.html) · 19 / 18 | `sd18`、`sd17`、`sd19` | 分清两次论剑，恢复李萍在军营的选择、襄阳遇袭和汗王之死。 | 修订本第38–40回。[第40回文本](https://bailushuyuan.org/novel/traditional/chapters/154) | 指定修订本或新修本，并复核洪七公、欧阳锋传功。 |
| [天龙八部](../books/demi-gods/index.html) · 23 / 17 | `tl22` | 删慕容复与王语嫣的虚构对话，恢复坟地扮朝廷及阿碧陪伴。 | 第50回末。 | 需确定统一版本，核对王语嫣、段誉去向及游坦之线。 |
| [笑傲江湖](../books/swordman/index.html) · 19 / 15 | `xa14`、`xa15` | 删末战、死亡传闻和隐居小屋，恢复任我行战前死讯、教务易手及合奏。 | 第40章〈曲谐〉。[小说文本](https://www.hetubook.com/book2/40/874.html) | 恒山交接次序、琴箫传人的直接关系。 |
| [鹿鼎记](../books/deer-cauldron/index.html) · 18 / 15 | `ld17`、`ld18` | 恢复官船遇袭假消息及回扬州询问生父，删退隐后的自白。 | 第50回末。[小说文本](https://www.99csw.com/book/2175/63872.htm) | 朝廷、天地会及妻儿各线。 |

## 剩余范围

- 《冰与火之歌》中段、《三体》危机纪元等未改节点仍有对白密集、精确日期缺出处的情况。一些作品已有公开原文入口，仍存在未核的人物关系和页脚引语。
- 《天龙八部》《猎魔人》等作品有版本差异。各书待核列保留了需要固定印本、统一译名或对读异文的位置。
- 《时光之轮》增加了关键转折，十四卷逐卷覆盖仍不足。《飓光志》选前两卷，《地海传奇》选前四部，《海伯利安》与《安德的游戏》选第一部。
- fd21 的“贝泰与杜伦走进宫廷”和 fd27b 的“被抹去的星图坐标”图注承袭旧稿；sa11 的插图表现誓门，开启誓门的情节详见紧接的 sa12。保留全部原图及其图注位置。

## 校验

- 使用当前全站生成脚本 python3 tools/rebuild.py 重建58部数据作品的时间线、人物志，并直接更新《三体》现有 HTML。
- python3 tools/check.py 通过，检查120个页面和3310条本地链接及资源。59部作品均有时间线和人物志。
- 额外核对原有锚点、关系端点与重复关系、分段与出处引用，以及本轮修改事件的双向参与者关联。页面插图、图注标记、样式、交互脚本与基线对照通过；未做浏览器像素对比。
- git diff --check 通过。自动检查反映页面和数据的完整性，文学事实的核验范围见各书条目。
