# MarkOrbit / Mo lite 新想法讨论总结：Mo Artifact、Mo Render、Mo Edit、Mo Publish

版本：Draft 1.0  
整理范围：HyperFrames、Remotion、TTS、PDF、AiToEarn、本地发布插件、视频剪辑 Skills、数字人、免费商用素材库工作流  
核心结论：Mo lite 不应只是 AI 工作台，而应升级为 **商标行业业务成果物自动生产系统**

---

## 0. 执行摘要

本轮讨论的核心发现是：

> **MarkOrbit / Mo lite 的长期价值，不只是生成文案，而是把商标行业的数据、知识、素材、模板、AI 能力和工作流，自动加工成可交付、可传播、可转化的业务成果物。**

因此，需要在原有 Mo 架构中新增或强化四个概念：

```text
Mo Artifact｜业务成果物层
Mo Render｜结果渲染层
Mo Edit｜视频/素材后处理层
Mo Publish｜内容发布分发层
```

新的完整链路为：

```text
Mo Data / Mo Brain / Mo Workspace
  ↓
Mo Assistant / Mo Guide
  ↓
Mo Artifact
  ↓
Mo Render
  ↓
Mo Edit
  ↓
Mo Publish
  ↓
客户触达 / 内容分发 / 商机转化 / 订单成交
```

Mo lite 未来不只是帮助代理人“想清楚、写出来”，还要进一步帮助代理人：

- 生成 PDF；
- 生成图片；
- 生成音频；
- 生成短视频；
- 整理素材；
- 剪辑口播；
- 生成发布包；
- 辅助发布到自媒体；
- 记录发布结果；
- 反哺商机转化。

最终目标：

> **MarkOrbit / Mo lite = 商标行业的智能业务成果物生产与分发系统。**

---

## 1. 新增核心架构概念

---

## 1.1 Mo Artifact｜业务成果物层

### 定义

Mo Artifact 是 Mo 生成出来的业务成果物，不等于普通内容草稿。

它可以是：

- ContentDraft；
- GraphicPost；
- VideoProject；
- QuoteProposal；
- TrademarkListing；
- TrademarkRecommendationPage；
- PDF Report；
- POA；
- FilingChecklist；
- CustomerEmail；
- MessageDraft；
- PublishPackage；
- Order；
- CaseReport。

### 为什么需要 Artifact 概念

过去系统容易停留在“AI 生成一段文字”。  
但商标代理业务真正需要的是：

- 可以发给客户的报价单；
- 可以分享的商标推荐页；
- 可以发布的视频；
- 可以下载的 PDF；
- 可以复制的微信话术；
- 可以归档的客户确认表；
- 可以转化的订单。

因此，Mo 的输出应统一抽象为 Artifact。

### 标准链路

```text
Mo Capability
  ↓
Mo Skill
  ↓
Mo Workflow
  ↓
Mo Artifact
  ↓
Mo Render
  ↓
User Delivery
```

---

## 1.2 Mo Render｜结果渲染层

### 定义

Mo Render 负责把结构化 Artifact 加工成用户可直接使用的文件或页面。

它不是 AI 生成逻辑，而是“结果加工层”。

### Mo Render 包含

```text
Mo Render
  ├── Graphic Renderer：HTML / SVG / React → PNG / SVG
  ├── Document Renderer：HTML / React / Markdown → PDF / DOCX
  ├── Audio Renderer：Text → MP3 / WAV
  ├── Video Renderer：HTML / React / JS + Assets + Audio → MP4
  └── Page Renderer：结构化数据 → 分享页 / 落地页
```

### 关键原则

> **Mo lite 决定内容、数据、模板、业务规则；Renderer 只负责把结果加工成文件。**

例如：

- HyperFrames：HTML/CSS/JS → MP4；
- Remotion：React Component → MP4；
- Playwright：HTML → PDF；
- Piper / TTS：文本 → 音频；
- Satori / resvg / Sharp：HTML/SVG → 图片。

---

## 1.3 Mo Edit｜视频/素材后处理层

### 定义

Mo Edit 不是从数据生成视频，而是对已有素材进行整理、剪辑、字幕、调色、包装。

适用于：

- 用户上传口播视频；
- 用户上传产品视频；
- 用户上传商标介绍录屏；
- 外部素材库下载的 B-roll；
- 已生成视频的二次包装。

### 典型能力

- 删除停顿；
- 中文断句；
- 自动加字幕；
- 调色；
- 添加片头片尾；
- 添加 logo；
- 添加 CTA；
- 分割成多条短视频；
- 将长口播切成短视频。

### Mo Edit 和 Mo Render 的区别

| 层 | 输入 | 输出 | 典型场景 |
|---|---|---|---|
| Mo Render | 结构化数据 + 模板 | PDF / PNG / MP4 | 商标推荐视频、报价 PDF |
| Mo Edit | 已有视频 / 音频 / 素材 | 剪辑后视频 | 口播剪辑、删停顿、加字幕 |

---

## 1.4 Mo Publish｜内容发布分发层

### 定义

Mo Publish 负责把 Mo Render / Mo Edit 生成的成果物辅助发布到各内容平台。

它不是内容生成，也不是视频渲染，而是分发层。

### 支持对象

- ContentDraft；
- GraphicPost；
- VideoProject；
- QuoteProposal；
- TrademarkRecommendationPage；
- TrademarkListing；
- MessageDraft；
- PDF；
- MP4；
- PNG。

### 支持平台方向

- 小红书；
- 抖音；
- 视频号；
- B站；
- 公众号；
- TikTok；
- YouTube；
- Facebook；
- Instagram；
- X；
- LinkedIn。

### 重要原则

> **第一阶段不做云端代发，优先做本地分发插件 / 半自动发布助手。**

---

## 2. HyperFrames 的判断

---

## 2.1 定位

HyperFrames 的本质是：

> **HTML / CSS / JS → MP4 的视频渲染工具。**

它像一个“视频打印机”。

```text
商标数据 + 文案 + 素材 + 模板 + 音频
        ↓
生成 HTML/CSS/JS 视频页面
        ↓
HyperFrames 渲染
        ↓
MP4 视频
```

### 它负责什么

- 渲染 HTML；
- 渲染动画；
- 合成视频画面；
- 输出 MP4。

### 它不负责什么

- 不懂商标；
- 不写商标销售话术；
- 不生成商标数据；
- 不管理素材；
- 不生成 TTS；
- 不做发布；
- 不做计费；
- 不做权限；
- 不做商机转化。

---

## 2.2 对 Mo 的价值

HyperFrames 很适合作为：

> **Mo Video Renderer 的底层渲染引擎候选。**

它适合：

- 商标推荐短视频；
- 多商标合集视频；
- 商标流程讲解视频；
- Section 8 / 续展提醒视频；
- 商标驳回解释视频；
- 全球报价说明视频；
- 私域客户定制推荐视频。

---

## 2.3 与 Mo Marks 的结合

每个待售商标可以生成：

- 单商标推荐视频；
- 多商标合集视频；
- 行业推荐视频；
- 客户定制推荐视频；
- 稀缺好名视频；
- 价格提醒视频。

链路：

```text
TrademarkAsset
  ↓
TrademarkListing
  ↓
AI 包装卖点
  ↓
选择视频模板
  ↓
TTS 配音
  ↓
HyperFrames 渲染
  ↓
MP4
```

---

## 2.4 重要结论

HyperFrames 不是完整视频生成产品，只是加工环节。

正确关系：

```text
Mo 决定业务结构
Mo 决定数据
Mo 决定模板变量
Mo 决定用户场景
Mo 决定输出结果
HyperFrames 只负责把其中一种结果渲染成视频
```

---

## 3. 再售商标展示视频模板

---

## 3.1 核心想法

如果设计几套“再售商标展示模板”，就可以快速生产大量看起来定制化的商标推荐视频。

标准公式：

```text
商标数据
  + AI 销售文案
  + 模板
  + 素材
  + TTS 音频
  + 字幕
  = 定制化商标推荐短视频
```

---

## 3.2 推荐模板类型

### 模板 A：高端品牌推荐型

适合：

- 服装；
- 美妆；
- 珠宝；
- 家居；
- 轻奢品牌。

结构：

1. 商标 logo 出场；
2. 品牌名大字展示；
3. 一句话卖点；
4. 适用行业；
5. 类别 / 国家 / 状态；
6. 推荐客户；
7. 咨询 CTA。

---

### 模板 B：商标房源卡片型

类比链家房源视频。

结构：

1. 今日推荐商标；
2. 商标名；
3. 类别；
4. 注册国家；
5. 有效状态；
6. 价格区间；
7. 三个卖点；
8. 适合做什么品牌。

---

### 模板 C：行业合集型

适合一次推 5-10 个商标。

结构：

1. 适合某行业的商标合集；
2. 每个商标展示 3-5 秒；
3. 行业定位；
4. 类别 / 国家；
5. 统一 CTA。

---

### 模板 D：稀缺资源型

适合：

- 好名字；
- 短词；
- 双拼；
- 英文词；
- 稀缺类别商标。

结构：

1. “这个名字还在吗？”
2. 商标大字展示；
3. 注册信息；
4. 稀缺点；
5. 使用方向；
6. “先到先得”。

---

### 模板 E：客户定制推荐型

适合给具体客户私域跟进。

结构：

1. 为您筛选了 X 个适合某项目的商标；
2. 客户行业；
3. 多个商标逐一展示；
4. 推荐理由；
5. 下一步确认。

---

## 3.3 标准变量

每个商标视频模板可使用：

```text
trademarkName
logoUrl
country
classNumbers
goodsServices
registrationNumber
status
validUntil
askingPrice
recommendedIndustries
targetCustomers
sellingPoints
brandStory
riskNotes
cta
contactBlock
```

AI 负责生成：

```text
hook
voiceoverScript
scenePlan
captionText
sellingPoints
cta
```

Renderer 负责输出视频。

---

## 3.4 “伪口播”逻辑

伪口播分三层。

### Level 1：字幕 + 背景音乐

只有动态字幕、商标展示、背景音乐。  
适合快速批量生成。

### Level 2：AI 配音 + 字幕

这是最适合 MarkOrbit 的阶段。

```text
商标数据
  ↓
AI 生成口播稿
  ↓
TTS 生成音频
  ↓
模板视频渲染
  ↓
字幕同步
  ↓
MP4
```

### Level 3：数字人 / 真人口型

后置。  
可考虑 HeyGen、可灵数字人、火山数字人、本地数字人方案。

---

## 4. Remotion 的判断

---

## 4.1 定位

Remotion 是用 React 程序化生成视频的框架。

它和 HyperFrames 的思想类似，但更 React 化。

如果 HyperFrames 是：

```text
HTML/CSS/JS → MP4
```

Remotion 更像：

```text
React Component → MP4
```

---

## 4.2 对 Mo 的价值

MarkOrbit 是 Next.js / React 技术栈，因此 Remotion 对 Mo 可能比 HyperFrames 更自然。

适合：

- 排行榜视频；
- 数据周报；
- 商标推荐视频；
- 多商标合集视频；
- 报价说明视频；
- 商标流程讲解视频；
- 固定栏目批量出片。

---

## 4.3 推荐判断

Remotion 应作为 **Mo Video Renderer 的重点预研对象**。

建议和 HyperFrames 并行预研：

| 对比项 | HyperFrames | Remotion |
|---|---|---|
| 核心方式 | HTML/CSS/JS | React |
| 与 Next.js 契合 | 中 | 高 |
| 模板开发 | 前端通用 | React 组件化 |
| 适合批量视频 | 高 | 高 |
| 商标数据套版 | 高 | 高 |
| 成熟度 | 需预研 | 较成熟 |
| Mo 适配潜力 | 高 | 很高 |

---

## 5. TTS 与 Mo Audio Renderer

---

## 5.1 定位

TTS 是：

> **文本 → 音频 的渲染器。**

在 Mo 中应定义为：

# Mo Audio Renderer

---

## 5.2 作用

用于：

- 商标推荐口播；
- 商标知识口播；
- 报价说明口播；
- 私域跟进语音稿；
- 视频伪口播；
- 多语言语音说明。

---

## 5.3 推荐技术方向

可预研：

- Piper：本地、低成本、适合原型；
- Coqui TTS：能力强，但维护和许可证需评估；
- eSpeak NG：轻量备用；
- 云 TTS Provider：OpenAI、Azure、火山、阿里云、ElevenLabs 等。

### 建议架构

不要绑定某一个 TTS。

应设计为 Provider：

```text
TtsProvider
  ├── LocalPiperProvider
  ├── CloudTtsProvider
  ├── OpenAiTtsProvider
  ├── AzureTtsProvider
  └── DisabledTtsProvider
```

---

## 5.4 与视频关系

TTS 是 Mo Video 的关键前置能力。

```text
VideoScript
  ↓
TTS
  ↓
Caption Engine
  ↓
Video Renderer
```

没有 TTS，模板视频更像动态 PPT；有了 TTS，才接近短视频口播。

---

## 6. PDF 与 Mo Document Renderer

---

## 6.1 定位

PDF 是商标业务中最刚需的成果物之一。

Mo Document Renderer 负责：

```text
HTML / React / Markdown + Data → PDF
```

---

## 6.2 适合生成的 PDF

优先级很高：

- 报价方案 PDF；
- 商标推荐报告；
- 商标销售资料；
- 客户确认表；
- POA 预览；
- 申请材料清单；
- OA 分析报告；
- 商标检索报告；
- 续展 / 宣誓提醒函。

---

## 6.3 推荐技术路线

### 第一优先：Playwright / Chromium PDF

原因：

- MarkOrbit 是 Next.js；
- 可以复用前端 HTML/CSS 思路；
- 渲染效果可控；
- 对复杂报告、报价单、分享页转 PDF 友好。

### 可选路线

- WeasyPrint：适合 Python Worker；
- Paged.js：适合长文档和手册；
- React PDF：适合纯 React 组件 PDF；
- Stirling PDF：适合 PDF 后处理，不适合作为主生成器。

---

## 6.4 结论

PDF Renderer 应该比视频更早落地。

原因：

1. 商标业务刚需；
2. 客户更容易接受；
3. 技术风险低；
4. 变现更直接；
5. 与报价、推荐页、销售页强相关。

---

## 7. Graphic Renderer

---

## 7.1 定位

Graphic Renderer 负责：

```text
HTML / SVG / React + Data → PNG / SVG
```

---

## 7.2 适合场景

- 朋友圈图；
- 小红书封面；
- 私聊解释图；
- 商标推荐图；
- 报价图；
- 风险提示卡；
- 流程图；
- 商标销售海报；
- 视频封面。

---

## 7.3 推荐工具

可研究：

- Satori；
- resvg；
- Sharp；
- Vercel OG 思路；
- Playwright screenshot。

### 设计原则

不要让 AI 图片模型直接生成包含中文长文本的成品图。

正确方式：

```text
AI 生成结构化内容
  ↓
HTML/SVG 模板精确排版
  ↓
PNG 输出
```

---

## 8. AiToEarn 与 Mo Publish

---

## 8.1 定位

AiToEarn 更像：

> **内容分发 / 自媒体运营层。**

不是渲染器，也不是视频生成器。

对应 Mo 架构：

# Mo Publish

---

## 8.2 对 Mo 的价值

AiToEarn 类项目对 Mo 的价值包括：

- 多平台发布工作流；
- MCP 化发布接口；
- 发布任务结构；
- 浏览器插件 / 本地插件思路；
- 平台适配器；
- 发布状态回写；
- 内容运营自动化。

---

## 8.3 不建议云端直接代发

云端全平台代发风险高：

- 用户账号安全；
- Cookie / 登录态；
- 验证码；
- 平台风控；
- 内容审核；
- 规则变化；
- SaaS 合规责任。

---

## 8.4 建议做成本地分发插件

定义：

# Lite Local Publish Plugin  
中文：**Lite 本地分发插件 / Mo 发布助手**

定位：

> 在用户本地电脑上，帮助用户把 Lite 生成的图文、视频、PDF、话术，一键整理并辅助发布到小红书、抖音、视频号、B站、公众号、TikTok、YouTube 等平台。

---

## 8.5 本地插件工作流

```text
Lite 生成 PublishPackage
  ↓
本地插件接收任务
  ↓
打开平台创作中心
  ↓
自动填标题、正文、标签、上传视频/图片
  ↓
用户检查
  ↓
用户确认发布
  ↓
回写发布记录
```

核心原则：

- Cookie 不上传；
- 登录在用户本地；
- 不自动点击最终发布；
- 用户确认；
- 失败可降级为复制粘贴。

---

## 8.6 分阶段路线

### Phase A：Lite 内手动发布助手

- 复制标题；
- 复制正文；
- 下载图片；
- 下载视频；
- 打开平台发布页；
- 标记已发布。

适合 Lite 1.2。

### Phase B：Chrome Extension 本地插件

- 读取 Lite 发布包；
- 自动填表；
- 上传媒体；
- 用户确认发布；
- 回写状态。

适合 Lite 1.5。

### Phase C：Local Agent / MCP 插件

本地运行：

```text
markorbit-publish-agent
```

支持 MCP 或本地 API。  
适合 Mo 2.0。

---

## 9. Video Use / Video Cut Skills / 中文口播剪辑

---

## 9.1 定位

这类工具更适合 Mo Edit，而不是 Mo Render。

它们处理的是：

```text
已有视频素材 → 剪辑整理 → 包装成片
```

而不是：

```text
商标数据 → 模板 → 渲染 MP4
```

---

## 9.2 适合能力

- 删除停顿；
- 口播节奏；
- 中文断句；
- 自动字幕；
- 剪辑包装；
- 调色；
- 添加动效；
- 素材自动整理。

---

## 9.3 对 Mo 的应用场景

### 代理人真人口播

用户上传一段口播视频：

```text
3 分钟原始口播
  ↓
自动转写
  ↓
删除停顿
  ↓
中文断句
  ↓
加字幕
  ↓
加重点词
  ↓
加 logo / CTA
  ↓
输出 30-60 秒短视频
```

### 课程 / 教程剪辑

适合：

- 商标申请教程；
- OA 讲解；
- 商标交易流程；
- 全球报价说明；
- 续展宣誓提醒。

---

## 9.4 推荐位置

放在：

```text
Lite 1.3 / Lite 1.5：Mo Video Edit
```

优先级低于：

1. PDF Renderer；
2. Graphic Renderer；
3. Video Renderer；
4. TTS；
5. Caption Engine。

---

## 10. AI 视频生成 Skill

---

## 10.1 定位

AI 视频生成 Skill 适合做素材补充，不适合作为最终商标视频主链路。

原因：

商标视频中很多内容必须准确：

- 商标名；
- logo；
- 类别；
- 国家；
- 价格；
- 期限；
- 风险提示；
- 联系方式。

AI 视频模型容易生成错误文字或扭曲 logo。

---

## 10.2 正确用途

适合生成：

- 背景 B-roll；
- 氛围镜头；
- 抽象品牌画面；
- 科技感画面；
- 场景素材；
- 转场片段。

位置：

```text
Mo Asset Hub
  ↓
AI B-roll Generator
  ↓
Mo Video Renderer
```

---

## 11. 数字人 / Meta Human

---

## 11.1 定位

数字人适合未来做：

```text
Mo Persona
  ↓
数字人形象
  ↓
TTS / 口型驱动
  ↓
品牌统一口播视频
```

---

## 11.2 应用场景

- 代理人个人 IP 数字人；
- 机构统一数字人；
- 商标知识口播；
- 报价讲解；
- 客户定制推荐；
- 多语言讲解。

---

## 11.3 为什么后置

风险和复杂度较高：

- 肖像权；
- 声音权；
- 授权；
- 效果稳定性；
- 渲染成本；
- 内容审核；
- 用户接受度。

推荐放在：

```text
Lite 2.0 / Mo Persona Digital Human
```

---

## 12. 免费可商用素材库工作流

---

## 12.1 核心想法

可以借用“调用高清可商用素材库来制作视频”的工作流。

但建议借用工作流，不要直接照搬素材库或代码。

---

## 12.2 适合 Mo 的工作流

```text
Mo 生成脚本
  ↓
提取关键词
  ↓
检索免费可商用素材库
  ↓
下载候选素材
  ↓
筛选匹配片段
  ↓
导入 Mo Asset Hub
  ↓
套入视频模板
  ↓
TTS + 字幕
  ↓
渲染成 MP4
```

---

## 12.3 建议新增模块

# Mo Stock Asset Connector｜素材库连接器

属于：

```text
Mo Asset Hub
  ↓
Mo Stock Asset Connector
  ↓
Mo Render / Mo Video
```

它不是视频生成器，而是外部素材补充能力。

---

## 12.4 可接素材库

优先级建议：

1. Pexels Video；
2. Pixabay；
3. Unsplash，主要用于图片；
4. MotionElements Free，视 API 和授权情况。

### 第一阶段建议

先接 Pexels Video。

理由：

- 视频质量较高；
- 适合商业、办公、生活方式、跨境电商场景；
- 对短视频 B-roll 友好。

---

## 12.5 合规原则

不要全量抓取素材库。

正确方式：

```text
按任务检索
  ↓
用户选择 / 系统推荐
  ↓
保存素材引用和来源
  ↓
生成视频时使用
  ↓
记录 sourceUrl / sourceName / licenseSnapshot / downloadedAt
```

禁止：

```text
全量抓取外部素材库
  ↓
变成自己的素材库
```

---

## 12.6 素材合规护栏

必须过滤或标记：

- 明显第三方商标；
- 品牌门头；
- 可识别 logo；
- 人物肖像；
- 水印；
- 敏感场景；
- 授权不清晰素材。

每个素材应保存：

```text
title
sourceName
sourceUrl
sourceAssetId
licenseType
licenseUrl
authorName
authorUrl
downloadedAt
fileUrl
thumbnailUrl
tags
usageScope
rightsNote
containsPeople
containsLogo
riskLevel
```

---

## 13. 对 Mo 架构的整体调整

---

## 13.1 更新后的 Mo 业务成果物链路

```text
Mo Data
  ↓
Mo Brain
  ↓
Mo Intelligence
  ↓
Capability
  ↓
Skill
  ↓
Workflow
  ↓
Mo Guide / Mo Assistant
  ↓
Mo Artifact
  ↓
Mo Render
  ↓
Mo Edit
  ↓
Mo Publish
  ↓
Applications / 客户 / 内容平台 / 商机 / 订单
```

---

## 13.2 各层职责

| 层 | 职责 |
|---|---|
| Mo Data | 获取和管理商标、客户、报价、素材等数据 |
| Mo Brain | 理解法律、规则、流程、知识 |
| Mo Intelligence | 发现机会、推荐主题、推荐客户 |
| Capability | 定义可执行能力 |
| Skill | 实现具体能力 |
| Workflow | 编排多个能力 |
| Mo Guide / Assistant | 理解用户意图并调用能力 |
| Mo Artifact | 形成业务成果物 |
| Mo Render | 渲染成 PDF / PNG / MP3 / MP4 |
| Mo Edit | 对已有素材进行剪辑、字幕、包装 |
| Mo Publish | 发布分发和状态回写 |
| Applications | Lite、MarkReg、客户端、小程序、插件 |

---

## 14. 对 Lite 版本路线的调整建议

---

## 14.1 Lite 1.1：保持主线，不做渲染和发布

Lite 1.1 继续做：

- Mo Workspace；
- Mo Content；
- Mo Asset Hub；
- Mo Assistant；
- Mo Marks；
- Mo Global；
- Mo Leads；
- ContentDraft.videoBrief；
- scenePlan；
- captionText；
- TemplateAsset；
- MediaAsset；
- AssetUsageLog。

不要做：

- HyperFrames 接入；
- Remotion 接入；
- TTS；
- 视频成片；
- PDF 渲染；
- 发布插件；
- 外部素材库自动检索。

Lite 1.1 只预留字段和结构。

---

## 14.2 Lite 1.2：Mo Render MVP

Lite 1.2 应重点做：

### 第一优先：PDF Renderer

- 报价方案 PDF；
- 商标推荐 PDF；
- 商标销售资料 PDF；
- 客户确认表 PDF。

### 第二优先：Graphic Renderer

- 朋友圈图；
- 小红书封面；
- 商标推荐图；
- 报价图。

### 第三优先：Video Renderer

- Remotion / HyperFrames 二选一或并行预研；
- 单商标推荐视频；
- 多商标合集视频；
- 商标知识视频；
- 报价说明视频。

### 第四优先：TTS + Caption Engine

- 伪口播；
- 自动字幕；
- 字幕时间轴；
- 字幕样式。

### 第五优先：Manual Publish Tracking

- 生成发布包；
- 复制标题；
- 复制正文；
- 下载成果物；
- 标记已发布；
- 记录发布链接。

---

## 14.3 Lite 1.3：Mo Stock Asset Connector + Mo Video Edit

Lite 1.3 可做：

- Pexels Video Connector；
- 外部素材检索；
- 素材来源记录；
- 素材风险标记；
- 用户选择素材；
- 导入 Mo Asset Hub；
- 视频后处理；
- 中文口播剪辑；
- 自动加字幕；
- 删除停顿。

---

## 14.4 Lite 1.5：Mo Publish Local Plugin

Lite 1.5 可做：

- Chrome Extension 本地分发插件；
- 小红书 / 抖音 / 视频号 1-2 个平台优先；
- 读取 PublishPackage；
- 自动填表；
- 用户确认发布；
- 回写发布记录；
- MCP Local Agent 预研。

---

## 14.5 Lite 2.0：Mo Persona Digital Human

Lite 2.0 可做：

- 代理人数字人；
- 机构统一数字人；
- 个人 IP 口播形象；
- 多语言数字人视频；
- 数字人授权管理；
- 声音授权管理。

---

## 15. 建议新增数据模型方向

---

## 15.1 Mo Artifact 通用模型，后置

可先不建通用 Artifact 表，但设计上要统一。

未来可考虑：

```text
Artifact
ArtifactVersion
ArtifactUsage
ArtifactRenderJob
```

短期先用具体业务表：

- ContentDraft；
- QuoteProposal；
- TrademarkListing；
- RecommendationPage；
- VideoProject；
- PublishPackage。

---

## 15.2 VideoProject

未来 Lite 1.2 可新增：

```text
VideoProject
  id
  userId
  sourceObjectType
  sourceObjectId
  templateId
  title
  script
  voiceoverText
  scenePlan
  captionTrackId
  status
  duration
  aspectRatio
  outputUrl
  coverUrl
  metadata
```

---

## 15.3 VideoRenderJob

```text
VideoRenderJob
  id
  videoProjectId
  rendererType
  status
  inputJson
  outputJson
  errorMessage
  startedAt
  completedAt
```

rendererType：

```text
remotion
hyperframes
ffmpeg
manual
```

---

## 15.4 TtsJob

```text
TtsJob
  id
  userId
  provider
  text
  voiceId
  language
  status
  audioUrl
  duration
  errorMessage
```

---

## 15.5 CaptionTrack

```text
CaptionTrack
  id
  sourceObjectType
  sourceObjectId
  language
  segmentsJson
  styleJson
```

---

## 15.6 RenderArtifact

```text
RenderArtifact
  id
  userId
  artifactType
  sourceObjectType
  sourceObjectId
  fileUrl
  thumbnailUrl
  format
  status
  metadata
```

artifactType：

```text
pdf
png
mp3
mp4
srt
html
```

---

## 15.7 PublishPackage

```text
PublishPackage
  id
  userId
  sourceObjectType
  sourceObjectId
  title
  body
  hashtags
  mediaJson
  targetPlatforms
  cta
  contactBlock
  status
```

---

## 15.8 PublishPost

```text
PublishPost
  id
  publishPackageId
  platform
  title
  body
  mediaJson
  status
  scheduledAt
  publishedAt
  publishedUrl
  errorMessage
```

---

## 15.9 StockAssetSource

```text
StockAssetSource
  id
  provider
  sourceAssetId
  sourceUrl
  authorName
  authorUrl
  licenseType
  licenseUrl
  downloadedAt
  riskLevel
  containsPeople
  containsLogo
  metadata
```

---

## 16. 产品命名建议

---

## 16.1 对内命名

- Mo Artifact｜业务成果物层；
- Mo Render｜结果渲染层；
- Mo Edit｜视频后处理层；
- Mo Publish｜内容分发层；
- Mo Video Renderer；
- Mo Audio Renderer；
- Mo Document Renderer；
- Mo Graphic Renderer；
- Mo Stock Asset Connector；
- Mo Publish Assistant；
- Lite Local Publish Plugin。

---

## 16.2 对用户命名

不要使用太技术化的词。

可以叫：

- AI 商标视频；
- 商标推荐视频；
- 商标讲解视频；
- AI 配音短视频；
- 商标销售资料；
- 商标推荐报告；
- 一键生成报价单；
- 一键生成发布包；
- 本地发布助手。

---

## 17. 风险与边界

---

## 17.1 不要让工具反向定义产品

HyperFrames、Remotion、AiToEarn、Video Cut Skills 都只是候选工具。

正确关系：

```text
Mo 决定业务
工具负责加工
```

不要为了某个工具调整核心产品。

---

## 17.2 不要过早做真实全平台发布

发布平台风控高、维护成本高。

优先：

- 复制；
- 下载；
- 打开平台；
- 标记已发布；
- 本地插件；
- 用户确认。

---

## 17.3 不要直接搬运免费素材库

禁止全量抓取外部素材库。

只做：

- 按任务检索；
- 用户选择；
- 保存来源；
- 记录授权；
- 合规提示。

---

## 17.4 不要让 AI 直接生成含精确文字的视频画面

商标名、价格、国家、期限、联系方式必须由模板渲染控制。

AI 可生成：

- 脚本；
- 卖点；
- 分镜；
- 图像提示词；
- B-roll 建议。

最终文字应由 Renderer 精准排版。

---

## 17.5 数字人后置

数字人有价值，但不是当前核心。

前期先做：

- 模板视频；
- TTS；
- 字幕；
- 素材；
- PDF；
- 图文。

---

## 18. 最终战略判断

本轮新想法最重要的战略意义是：

> **Mo 不应只做“AI 帮代理人写东西”，而应做“AI 帮代理人生产业务成果物并分发转化”。**

未来 MarkOrbit 的能力可以概括为：

```text
结构化数据
  ↓
结构化知识
  ↓
结构化内容
  ↓
结构化模板
  ↓
自动渲染
  ↓
本地分发
  ↓
客户转化
```

这使 MarkOrbit 相比普通 AI 写作工具、普通视频工具、普通素材工具具备独特优势：

- 它懂商标；
- 它有商标数据；
- 它有商标资产；
- 它有报价逻辑；
- 它有客户和商机；
- 它有代理人 Persona；
- 它有素材库；
- 它能生成可交付成果物；
- 它能追踪使用和转化。

最终方向：

> **MarkOrbit / Mo = 商标行业的智能业务成果物生产与分发系统。**

---

## 19. 建议后续文档

下一步建议补充以下文档：

1. `Mo Render 架构设计文档`
2. `Mo Artifact 数据模型设计`
3. `Lite 1.2 Mo Render MVP PRD`
4. `Mo Video Renderer 技术预研任务书`
5. `Remotion vs HyperFrames 技术选型报告`
6. `Mo Stock Asset Connector 设计文档`
7. `Mo Publish Local Plugin 产品方案`
8. `商标再售视频模板库设计文档`

---

## 20. 当前执行建议

当前 Lite 1.1 不改主线。

但应在 Lite 1.1 的数据模型中继续保留：

- `ContentDraft.videoBrief`
- `ContentDraft.scenePlan`
- `ContentDraft.captionText`
- `MediaAsset.sourceUrl`
- `MediaAsset.sourceName`
- `MediaAsset.rightsNote`
- `TemplateAsset`
- `AssetUsageLog`

并在 V1.2 前启动以下技术预研：

1. Remotion 本地渲染 10 秒视频；
2. HyperFrames 本地渲染 10 秒视频；
3. Playwright HTML 转 PDF；
4. Satori / Playwright 截图转 PNG；
5. Piper / 云 TTS 生成中文音频；
6. 字幕时间轴生成；
7. Pexels Video API 检索和下载；
8. 简单 PublishPackage 结构设计。

结论：

> **现在不是立刻把这些工具塞进 Sprint 0，而是把它们纳入 Mo 的长期成果物生产架构，并在 Lite 1.2 以 Mo Render MVP 的方式开始落地。**
