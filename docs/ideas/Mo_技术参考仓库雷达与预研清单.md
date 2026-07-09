# Mo 技术参考仓库雷达与预研清单

版本：Draft 1.0  
适用项目：MarkOrbit / Mo / Lite 1.1-2.0  
定位：技术总监主动维护的开源项目雷达、选型框架与 Codex 预研任务清单  
核心目标：围绕 Mo 的 Artifact、Render、Edit、Publish 能力，主动寻找、筛选、验证、归档可参考或可集成的技术仓库。

---

## 0. 执行摘要

MarkOrbit / Mo 不能只被动评价用户刷到的工具，而应主动建立一套长期维护的 **Mo 技术参考仓库雷达**。

雷达的目标不是“看到开源项目就集成”，而是：

> **围绕 Mo 的长期架构，主动寻找最适合的开源仓库、最低风险的集成路径、最可控的技术路线，并转化为 Codex 可执行的预研任务。**

当前 Mo 的新增关键方向包括：

```text
Mo Artifact｜业务成果物层
Mo Render｜结果渲染层
Mo Edit｜视频/素材后处理层
Mo Publish｜内容发布分发层
Mo Stock Asset Connector｜外部素材库连接器
```

技术参考仓库雷达要覆盖：

1. 程序化视频渲染；
2. PDF / 文档生成；
3. 图文 / 海报生成；
4. TTS / 音频生成；
5. 字幕 / Caption Engine；
6. 视频剪辑后处理；
7. 外部免费可商用素材库连接；
8. 本地发布插件 / MCP 发布；
9. Agent Workflow / Skills；
10. 数字人 / 口播增强，后置。

---

## 1. 技术雷达职责

### 1.1 技术总监职责

技术总监需要主动做四件事：

1. **发现技术仓库**：主动寻找适合 Mo 的开源项目、技术框架和参考实现。
2. **判断适配价值**：判断它属于 Mo 的哪一层，是主链路、参考架构、插件能力，还是只值得借鉴思路。
3. **控制风险边界**：检查 license、维护状态、部署难度、中文支持、商用限制、平台风控和数据合规。
4. **转化为预研任务**：把技术判断转成 Codex 可执行的 POC 任务，而不是停留在概念评价。

---

## 2. 技术参考仓库评分表

每个候选仓库必须按以下维度评分。

| 维度 | 评估问题 | 评分说明 |
|---|---|---|
| 业务匹配度 | 是否服务 Mo 的明确模块 | 1-5 |
| 技术匹配度 | 是否适合 Next.js / TypeScript / Python / Worker 架构 | 1-5 |
| License 风险 | MIT / Apache / GPL / AGPL / 商业限制 | 1-5，分数越高风险越低 |
| 活跃度 | 最近是否维护，社区是否活跃 | 1-5 |
| 可替换性 | 是否可做 Provider / Adapter，不锁死主系统 | 1-5 |
| 部署难度 | 是否依赖 GPU、浏览器、ffmpeg、Docker | 1-5，分数越高越易部署 |
| 中文支持 | 中文字体、字幕、TTS、断句是否可行 | 1-5 |
| 批量能力 | 是否支持队列、批量任务、Worker 调用 | 1-5 |
| 数据合规 | 是否涉及用户隐私、账号、版权、素材授权 | 1-5，分数越高风险越低 |
| Mo 集成成本 | 是否能接 Workspace / Asset / Marks / Global / Leads | 1-5 |

### 2.1 分级规则

| 等级 | 含义 | 处理方式 |
|---|---|---|
| A | 可进入技术预研 | 做 POC，写报告 |
| B | 可作为参考架构 | 研究设计，不急于集成 |
| C | 只借鉴思路 | 归档，不进入开发 |
| D | 暂不考虑 | 记录原因，暂停 |

---

## 3. Mo 技术雷达分层

### 3.1 Mo Render 层

目标：把结构化业务成果物渲染成 PDF / PNG / MP3 / MP4。

包括：

- Document Renderer；
- Graphic Renderer；
- Audio Renderer；
- Video Renderer；
- Page Renderer。

候选方向：

- Remotion；
- HyperFrames；
- Playwright PDF；
- Satori；
- resvg；
- Sharp；
- Piper；
- Coqui TTS；
- Short Video Maker。

### 3.2 Mo Edit 层

目标：对已有视频、音频、素材进行剪辑、字幕、调色、删停顿和包装。

候选方向：

- Video Cut Skills；
- Video Use；
- Silenci / Silence-Cutter；
- Auto-Editor；
- Jumpcutter；
- FFmpeg workflow；
- Whisper / faster-whisper。

### 3.3 Mo Publish 层

目标：辅助用户把 Mo 生成的成果物发布到外部平台。

候选方向：

- AiToEarn；
- MCP publish tools；
- Browser automation；
- Chrome extension boilerplate；
- Local agent frameworks。

### 3.4 Mo Stock Asset Connector 层

目标：按任务检索外部免费可商用素材库，作为 Mo Asset Hub 的补充。

候选方向：

- Pexels Video；
- Pixabay；
- Unsplash；
- MotionElements Free；
- 素材授权记录；
- 素材风险标记；
- 素材导入 Mo Asset Hub。

---

## 4. 首批重点候选仓库清单

---

## 4.1 Remotion

### 定位

React 程序化视频渲染框架。

### 对应 Mo 模块

- Mo Video Renderer；
- Mo Render；
- Mo Artifact；
- Mo Marks 视频；
- Mo Global 报价视频；
- Mo Content 知识视频。

### 适合场景

- 单商标推荐视频；
- 多商标合集视频；
- 商标排行榜；
- 全球报价说明视频；
- 商标知识栏目；
- 数据周报；
- 固定栏目批量出片。

### 优势

- React 组件化；
- 与 Next.js 技术栈契合；
- 模板化能力强；
- 适合变量驱动批量视频；
- 适合商标数据套版。

### 风险

- 商业 license 需要重点核查；
- 渲染可能依赖 Chromium / ffmpeg；
- 批量渲染需要 Worker；
- 中文字体需要测试；
- 长视频渲染性能需评估。

### 初步等级

A：进入技术预研。

### POC 任务

1. 本地安装 Remotion；
2. 渲染 10 秒竖屏 9:16 MP4；
3. 使用中文字体；
4. 加入商标 logo；
5. 加入 3 个商标字段；
6. 加入字幕；
7. 加入 TTS 音频占位；
8. 输出 MP4；
9. 记录部署依赖和渲染耗时。

---

## 4.2 HyperFrames

### 定位

HTML / CSS / JS → MP4 的视频渲染工具。

### 对应 Mo 模块

- Mo Video Renderer；
- Mo Render；
- Mo Marks 视频；
- Mo Content 短视频；
- Mo Global 报价说明视频。

### 适合场景

- 商标推荐短视频；
- 多商标合集视频；
- 商标流程说明；
- Section 8 / 续展提醒视频；
- 商标驳回解释视频；
- 报价说明视频；
- 字幕卡片视频。

### 优势

- HTML/CSS/JS 思路直观；
- 适合 Agent 编写模板；
- 可作为“视频打印机”；
- 内容和文字可控；
- 商标名、类别、价格、状态可精准展示。

### 风险

- 成熟度需要验证；
- 中文字体需要测试；
- Worker 部署需要验证；
- 与现有 Next.js 集成方式需设计；
- 示例素材不可直接商用。

### 初步等级

A：进入技术预研。

### POC 任务

1. 本地 clone 并运行；
2. 渲染 10 秒 HTML 视频；
3. 插入中文标题；
4. 插入商标 logo；
5. 插入价格、类别、国家；
6. 加入简单动画；
7. 合成音频占位；
8. 输出 MP4；
9. 与 Remotion 对比开发体验。

---

## 4.3 Playwright / Chromium PDF

### 定位

HTML → PDF 文档渲染方案。

### 对应 Mo 模块

- Mo Document Renderer；
- Mo Render；
- Mo Global；
- Mo Marks；
- Mo Client Delivery。

### 适合场景

- 报价方案 PDF；
- 商标推荐报告；
- 商标销售资料；
- 客户确认表；
- POA 预览；
- OA 分析报告；
- 续展 / 宣誓提醒函；
- 材料清单。

### 优势

- PDF 是商标业务高频刚需；
- 技术风险低于视频；
- 和 Next.js / HTML/CSS 思路一致；
- 可复用分享页模板；
- 适合先落地商业价值。

### 风险

- 中文字体嵌入；
- 分页控制；
- 页眉页脚；
- Docker Chromium 依赖；
- PDF 文件存储和权限。

### 初步等级

A：第一优先预研。

### POC 任务

1. 用 HTML 模板生成报价单；
2. 支持中文；
3. 支持 logo；
4. 支持多国家报价表；
5. 支持分页；
6. 输出 PDF；
7. 保存到本地或对象存储占位；
8. 对比浏览器打印效果。

---

## 4.4 Satori + resvg

### 定位

HTML/SVG → 图片的图文渲染方案。

### 对应 Mo 模块

- Mo Graphic Renderer；
- Mo Render；
- Mo Content；
- Mo Marks；
- Mo Global；
- Mo Leads。

### 适合场景

- 小红书封面；
- 朋友圈图；
- 商标推荐图；
- 报价图；
- 风险提示卡；
- 流程图；
- 视频封面；
- 私聊解释图。

### 优势

- 文字精准；
- 适合中文长文案排版；
- 比 AI 生图可靠；
- 可模板化；
- 适合批量生成。

### 风险

- 中文字体处理；
- 复杂 CSS 支持有限；
- SVG 转 PNG 性能；
- 字体版权；
- 设计模板质量需要人工设计。

### 初步等级

A：进入技术预研。

### POC 任务

1. 生成 1080x1440 小红书封面；
2. 插入中文标题；
3. 插入商标 logo；
4. 插入 3 个卖点；
5. 输出 PNG；
6. 测试中文字体；
7. 测试不同模板变量。

---

## 4.5 Piper / TTS Provider

### 定位

文本 → 音频的本地或云端 TTS 方案。

### 对应 Mo 模块

- Mo Audio Renderer；
- Mo Video Renderer；
- Mo Content；
- Mo Marks；
- Mo Global。

### 适合场景

- 商标推荐配音；
- 商标知识口播；
- 报价说明口播；
- 视频伪口播；
- 多语言基础配音。

### 优势

- 本地低成本；
- 可做 POC；
- 与模板视频结合价值高；
- 有助于形成“伪口播”。

### 风险

- 中文声音质量；
- voice model 许可证；
- 商业使用限制；
- 语速和断句；
- 字幕对齐。

### 初步等级

A/B：先做 Provider 抽象，再测试不同 TTS。

### POC 任务

1. 生成中文 20 秒音频；
2. 输出 MP3 / WAV；
3. 测试音质；
4. 记录 voice license；
5. 生成字幕时间轴基础版；
6. 与视频模板合成。

---

## 4.6 Short Video Maker

### 定位

文本 + TTS + 字幕 + 背景视频的短视频生成流水线参考。

### 对应 Mo 模块

- Mo Video Pipeline；
- Mo Render；
- Mo Audio Renderer；
- Caption Engine；
- Stock Asset Connector。

### 适合场景

- 知识短视频；
- 商标常识视频；
- 报价说明视频；
- 内容主题视频。

### 优势

- 工作流接近 Mo Video；
- 可参考脚本、TTS、字幕、背景素材组合方式；
- 适合借鉴 pipeline。

### 风险

- 不一定适合商标精准信息；
- 模板质量需重做；
- License 需核查；
- 不应直接成为主链路。

### 初步等级

B：参考架构。

### 预研任务

1. 阅读项目结构；
2. 梳理 pipeline；
3. 提取可借鉴的数据结构；
4. 判断是否可改成 Mo Video Worker；
5. 不直接集成主仓库。

---

## 4.7 Silenci / Silence-Cutter

### 定位

自动去除视频静音、生成字幕的剪辑后处理工具。

### 对应 Mo 模块

- Mo Edit；
- Video Post-Processor；
- 中文口播剪辑；
- 用户素材后处理。

### 适合场景

- 用户上传口播；
- 自动删停顿；
- 自动字幕；
- 长视频切短；
- 教程视频粗剪。

### 优势

- 适合口播剪辑；
- 与代理人个人 IP 场景相关；
- 可后置增强内容生产。

### 风险

- 中文断句需测试；
- 转写质量；
- 剪辑准确性；
- 依赖 ffmpeg / AI 转写；
- 不适合主渲染链路。

### 初步等级

B：参考 Mo Edit 架构。

### 预研任务

1. 测试 1 分钟中文口播；
2. 自动去静音；
3. 生成字幕；
4. 输出视频；
5. 记录质量和部署依赖。

---

## 4.8 Auto-Editor / Jumpcutter

### 定位

自动删除静音、压缩视频节奏的基础剪辑工具。

### 对应 Mo 模块

- Mo Edit；
- Video Cut；
- 口播剪辑。

### 适合场景

- 商标知识口播删停顿；
- 教程视频压缩；
- 长视频切短；
- 视频素材粗剪。

### 优势

- 简单；
- 可用 ffmpeg 流水线实现；
- 适合做内部基础能力。

### 风险

- 不懂中文语义；
- 容易误剪；
- 需要和转写、字幕结合；
- 只是 Mo Edit 的基础能力。

### 初步等级

B/C：参考思路。

---

## 4.9 AiToEarn

### 定位

AI 内容营销和多平台分发参考项目。

### 对应 Mo 模块

- Mo Publish；
- Lite Local Publish Plugin；
- MCP Publish Agent；
- PublishPackage。

### 适合场景

- 多平台发布任务结构；
- 本地发布助手；
- MCP 工具；
- 发布状态回写；
- 自媒体运营自动化。

### 优势

- 对 Mo Publish 有启发；
- 可能支持 MCP；
- 可能有平台发布适配思路；
- 适合本地插件方向。

### 风险

- 平台风控；
- 账号安全；
- Cookie / 登录态；
- 页面规则变化；
- 合规风险高；
- 不适合云端直接代发。

### 初步等级

B：作为 Mo Publish 参考，不进入 Lite 1.1 主线。

### 预研任务

1. 阅读 MCP 调用方式；
2. 阅读发布任务结构；
3. 判断是否适合改成本地插件；
4. 梳理账号安全风险；
5. 不做云端代发。

---

## 4.10 Pexels API / Pexels SDK

### 定位

外部免费可商用素材库连接器第一候选。

### 对应 Mo 模块

- Mo Stock Asset Connector；
- Mo Asset Hub；
- Mo Video；
- Mo Content。

### 适合场景

- 商标知识视频 B-roll；
- 跨境电商视频素材；
- 办公 / 合同 / 物流 / 品牌场景；
- 服装 / 餐饮 / 科技行业视频素材；
- 商标推荐视频背景素材。

### 优势

- 视频素材丰富；
- 适合 B-roll；
- 可按关键词检索；
- 适合 Mo Video 质感提升。

### 风险

- 需要 API key；
- 授权记录必须保存；
- 不可全量搬运；
- 人物 / logo / 品牌风险；
- 素材被删除后的使用证据。

### 初步等级

A/B：Lite 1.3 进入预研。

### POC 任务

1. 按关键词搜索视频；
2. 获取缩略图；
3. 获取下载链接；
4. 保存 sourceUrl / author / license；
5. 标记 containsPeople / containsLogo；
6. 导入 Mo Asset Hub；
7. 用于一个 30 秒模板视频。

---

## 5. 技术路线优先级

当前建议优先级：

```text
第一优先：PDF Renderer
  Playwright / Chromium HTML → PDF

第二优先：Graphic Renderer
  Satori + resvg / Playwright screenshot

第三优先：Video Renderer
  Remotion vs HyperFrames POC

第四优先：TTS + Caption
  Piper / 云 TTS Provider + 字幕时间轴

第五优先：Stock Asset Connector
  Pexels Video API

第六优先：Mo Edit
  Silenci / Auto-Editor / FFmpeg

第七优先：Mo Publish
  AiToEarn / 本地发布插件

第八优先：Digital Human
  数字人口播，后置
```

---

## 6. Lite 版本规划映射

### 6.1 Lite 1.1

保持主线，不接入复杂渲染和发布。

只保留字段和结构：

- `ContentDraft.videoBrief`
- `ContentDraft.scenePlan`
- `ContentDraft.captionText`
- `MediaAsset.sourceUrl`
- `MediaAsset.sourceName`
- `MediaAsset.rightsNote`
- `TemplateAsset`
- `AssetUsageLog`

不做：

- Remotion；
- HyperFrames；
- PDF 渲染；
- TTS；
- 视频成片；
- 发布插件；
- Pexels 自动检索。

### 6.2 Lite 1.2：Mo Render MVP

重点：

1. PDF Renderer；
2. Graphic Renderer；
3. Video Renderer POC；
4. TTS Provider；
5. Caption Engine；
6. Manual Publish Tracking。

### 6.3 Lite 1.3：Mo Stock + Mo Edit

重点：

1. Pexels Video Connector；
2. 外部素材来源记录；
3. 素材风险标记；
4. 用户选择素材；
5. 导入 Mo Asset Hub；
6. 视频后处理；
7. 中文口播剪辑。

### 6.4 Lite 1.5：Mo Publish Local Plugin

重点：

1. Chrome Extension 本地分发插件；
2. 读取 PublishPackage；
3. 打开小红书 / 抖音 / 视频号等平台；
4. 自动填表；
5. 用户确认发布；
6. 回写发布记录；
7. MCP Local Agent 预研。

### 6.5 Lite 2.0：Mo Persona Digital Human

重点：

1. 代理人数字人；
2. 机构统一数字人；
3. 个人 IP 口播形象；
4. 声音授权；
5. 肖像授权；
6. 多语言数字人视频。

---

## 7. Codex 预研任务总表

### 7.1 POC-001：Playwright PDF

目标：

> 验证 MarkOrbit 能否用 HTML/CSS 模板生成中文报价 PDF。

任务：

1. 新建独立 POC 目录；
2. 使用 Playwright 渲染 HTML；
3. 生成中文 PDF；
4. 插入 logo；
5. 插入报价表；
6. 支持分页；
7. 输出示例 PDF；
8. 写预研报告。

验收：

- 可生成 PDF；
- 中文正常；
- 表格正常；
- 页眉页脚可控；
- Docker 依赖记录清楚。

### 7.2 POC-002：Satori / resvg 图文

目标：

> 验证 HTML/SVG 模板生成商标推荐 PNG。

任务：

1. 生成 1080x1440 PNG；
2. 插入中文标题；
3. 插入商标 logo；
4. 插入卖点；
5. 测试字体；
6. 输出 3 套模板变体。

验收：

- PNG 清晰；
- 中文不乱码；
- 文字不变形；
- logo 不失真。

### 7.3 POC-003：Remotion 商标视频

目标：

> 验证 React 模板生成 10 秒竖屏商标推荐视频。

任务：

1. 安装 Remotion；
2. 创建 9:16 视频；
3. 插入商标名；
4. 插入 logo；
5. 插入类别/国家/价格；
6. 加入字幕；
7. 合成音频占位；
8. 输出 MP4。

验收：

- 可输出 MP4；
- 中文正常；
- logo 正常；
- 渲染耗时记录；
- license 风险记录。

### 7.4 POC-004：HyperFrames 商标视频

目标：

> 验证 HTML/CSS/JS 模板生成 10 秒商标推荐视频。

任务：

1. 安装 HyperFrames；
2. 创建 HTML 视频模板；
3. 插入中文；
4. 插入商标 logo；
5. 插入动画；
6. 输出 MP4；
7. 与 Remotion 对比。

验收：

- 可输出 MP4；
- 中文正常；
- 动画正常；
- 渲染方式可理解；
- 部署依赖记录。

### 7.5 POC-005：TTS + Caption

目标：

> 验证中文口播音频和基础字幕时间轴。

任务：

1. 用 Piper 或云 TTS 生成中文音频；
2. 输出 MP3/WAV；
3. 按句子生成字幕时间轴；
4. 输出 SRT；
5. 记录音质和授权。

验收：

- 音频可播放；
- 字幕可用；
- 语速可控；
- Provider 抽象建议明确。

### 7.6 POC-006：Pexels Video Connector

目标：

> 验证按关键词检索并下载视频素材，保存来源和授权信息。

任务：

1. 使用 Pexels API；
2. 搜索关键词；
3. 获取候选视频；
4. 下载一个短视频；
5. 保存 sourceUrl / author / license；
6. 标记风险字段；
7. 导入 Mo Asset Hub 结构草案。

验收：

- 可搜索；
- 可下载；
- 来源可记录；
- 不做全量搬运；
- 合规字段明确。

### 7.7 POC-007：Video Edit 去停顿

目标：

> 验证中文口播视频自动删停顿和生成字幕。

任务：

1. 使用 Silenci / Auto-Editor / FFmpeg；
2. 输入 1 分钟中文口播；
3. 自动检测静音；
4. 输出删停顿视频；
5. 生成字幕；
6. 记录误剪情况。

验收：

- 可输出视频；
- 停顿删除有效；
- 字幕可用；
- 中文断句质量记录。

### 7.8 POC-008：PublishPackage 手动发布

目标：

> 验证 Mo Publish 的最小数据结构和手动发布流程。

任务：

1. 定义 PublishPackage JSON；
2. 生成标题、正文、标签、媒体列表；
3. 提供复制按钮；
4. 提供下载按钮；
5. 提供打开平台链接；
6. 提供标记已发布；
7. 记录 publishedUrl。

验收：

- 不接平台账号；
- 不自动发布；
- 可记录发布状态；
- 可后续接本地插件。

---

## 8. 仓库归档规范

每个技术参考仓库应归档到：

```text
docs/research/tech-radar/
```

建议文件：

```text
docs/research/tech-radar/README.md
docs/research/tech-radar/render/remotion.md
docs/research/tech-radar/render/hyperframes.md
docs/research/tech-radar/render/playwright-pdf.md
docs/research/tech-radar/render/satori-resvg.md
docs/research/tech-radar/audio/piper.md
docs/research/tech-radar/video-edit/silenci.md
docs/research/tech-radar/publish/aitoearn.md
docs/research/tech-radar/stock-assets/pexels.md
```

每个仓库归档内容：

```text
项目名称
仓库地址
License
最后活跃时间
技术栈
Mo 对应模块
核心能力
不适合做什么
POC 任务
风险
结论
```

---

## 9. 技术选型原则

### 9.1 工具不能反向定义 Mo

Mo 决定业务，工具只负责加工。

不要因为某个工具很火，就改变产品主线。

### 9.2 主系统与 Renderer 解耦

视频、PDF、TTS、素材检索都应优先 Worker 化 / Provider 化。

不应全部塞进 Next.js 主请求流程。

### 9.3 优先做确定性输出

商标行业要求准确。

优先采用：

- HTML → PDF；
- SVG → PNG；
- React → MP4；
- 模板变量渲染。

谨慎采用：

- AI 直接生成含文字图片；
- AI 直接生成完整视频；
- AI 直接修改商标 logo。

### 9.4 所有素材要保留来源

外部素材必须保存：

- sourceName；
- sourceUrl；
- authorName；
- licenseUrl；
- downloadedAt；
- rightsNote；
- riskLevel。

### 9.5 发布优先本地化

不要先做云端代发。

优先：

- 复制；
- 下载；
- 打开平台；
- 用户确认；
- 本地插件；
- 状态回写。

---

## 10. 当前建议结论

当前第一批应进入正式预研的技术仓库 / 技术方向：

1. Playwright PDF；
2. Satori + resvg；
3. Remotion；
4. HyperFrames；
5. Piper / TTS Provider；
6. Pexels Video API；
7. Silenci / Auto-Editor；
8. AiToEarn；
9. Short Video Maker。

当前最重要的开发判断：

> **Lite 1.1 不接这些工具，只预留字段；Lite 1.2 以 Mo Render MVP 的方式开始落地 PDF、图片、视频、TTS；Lite 1.3 再接外部素材库和视频剪辑；Lite 1.5 再做本地发布插件。**

---

## 11. 后续文档建议

建议继续输出：

1. `Mo Render 架构设计文档.md`
2. `Remotion vs HyperFrames 技术选型报告.md`
3. `Lite 1.2 Mo Render MVP PRD.md`
4. `Mo Stock Asset Connector 设计文档.md`
5. `Mo Publish Local Plugin 产品方案.md`
6. `Codex 技术预研任务包：Mo Render POC.md`

---

## 12. 一句话总结

> **Mo 技术参考仓库雷达的核心任务，不是追热点，而是把合适的开源技术转化为 MarkOrbit 可控、可替换、可审计、可商业化的行业成果物生产能力。**
