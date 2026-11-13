# 故事图谱 · Story Atlas

六部作品的原创图文导读，在同一个书架中沿时间线阅读故事、沿关系网查阅人物。

[在线阅读](https://sver0411.github.io/story-atlas/) · [GitHub](https://github.com/Sver0411/story-atlas)

每本书只保留 **图文版、人物志** 两个页面；纯文字版及原《三体》精简版已移除。本站包含完整剧透，内容是独立撰写的情节概述，不是小说全文。

## 书架

| 作品 | 收录范围 | 故事节点 | 人物 | 直接关系 |
| --- | --- | ---: | ---: | ---: |
| [三体](books/three-body/index.html) | 小说三部曲 | 68 | 32 | 33 |
| [基督山伯爵](books/monte-cristo/index.html) | 小说完整主线与结局 | 36 | 24 | 40 |
| [百年孤独](books/solitude/index.html) | 布恩迪亚家族七代 | 37 | 24 | 40 |
| [魔戒](books/lotr/index.html) | 小说三部曲，含夏尔清洗与灰港 | 36 | 22 | 37 |
| [沙丘](books/dune/index.html) | 第一部小说，不含后续作品 | 32 | 22 | 40 |
| [红楼梦](books/red-chamber/index.html) | 通行120回本，区分前80回、后40回 | 42 | 30 | 48 |
| 合计 | | 251 | 154 | 238 |

书架支持题材筛选、书名与作者搜索。新增五本书的图文页支持节点搜索、章节跳转与阅读位置保存；人物志支持姓名/别名搜索、直接关系探索及对应故事跳转。阅读位置保存在当前浏览器本地，不上传服务器。

## 插图与内容依据

保留《三体》原有26幅插图，新增其余五本书共16幅 AI 场景插图。图注区分概念设计与原作明确的设定，原著没有规定的容貌、服饰细节和建筑造型属于视觉想象；未以影视改编补全小说情节。

- [新增插图与完整生成提示词](docs/anthology-images.json)
- [三体插图与提示词](docs/image-generation.json) · [配图核对记录](docs/illustration-audit.md) · [正文与人物修订记录](docs/content-review.md)
- [基督山伯爵内容口径](docs/notes/monte-cristo.md)
- [百年孤独内容口径](docs/notes/solitude.md)
- [魔戒与沙丘内容口径](docs/notes/fantasy.md)
- [红楼梦版本与结局说明](books/red-chamber/NOTES.md)

各新增作品页末附阅读范围和核对来源，节点的“出处”可跳到相应资料。《红楼梦》不把后四十回视作曹雪芹确定原稿，也不采用其他续书推测结局。

## 本地使用与维护

纯静态 HTML、CSS、JavaScript，可直接打开首页，也可启动本地服务：

```sh
python3 -m http.server 8765
```

访问 `http://localhost:8765/`。网站不依赖服务端、数据库或在线构建。

新增五本书的内容保存在 `books/<book-id>/data.js`，插图配置在 `assets/illustrations.json`，生成后的 HTML 已提交。修改内容或模板后运行（Node.js 18+、Python 3）：

```sh
node tools/build.mjs
python3 tools/check.py
```

构建检查数据 ID、人物引用、事件引用、来源与关系唯一性；页面检查覆盖本地链接、资源、锚点、重复 ID 和每本书的两个页面限制。《三体》原有两页保留其页面实现，不由模板重写。

## GitHub Pages

仓库从 `main` 分支根目录发布，`.nojekyll` 确保按静态文件提供。所有站内路径均为相对路径，适配项目型 Pages 地址。

原根目录 `characters.html#c-…` 继续跳转到《三体》人物志，首页 `#e…` 深链接继续指向《三体》原节点。原纯文字版、精简版 URL 已删除。仓库改名后请使用上述新的 Pages 地址。
