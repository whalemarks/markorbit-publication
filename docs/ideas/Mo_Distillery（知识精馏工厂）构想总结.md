# Mo Distillery（知识精馏工厂）构想总结

> 版本：Draft v0.1
> 定位：Mo 2.x 核心能力预研

## 一、背景

仓颉.Skill 最大的启发不是“读书摘要”，而是**把知识蒸馏成 Agent 可以调用的能力**。

一本优秀的书，是作者多年实践、验证后的方法论。如果 AI 真正学会其中的方法，而不是仅生成摘要，这些知识就能成为 Mo 的长期能力资产。

---

## 二、为什么 Mo 需要 Distillery

Mo Brain 负责存储知识。

Mo Distillery 负责生产知识。

建议架构：

Mo Data
↓
Mo Distillery
↓
Mo Brain
↓
Mo Intelligence
↓
Capability Catalog
↓
Skill Library
↓
Guide / Flow / Lite

---

## 三、Mo Distillery 的定位

它不是：

- PDF 摘要工具
- AI 读书笔记

而是：

**Knowledge Factory（知识制造工厂）**

负责把任何知识载体转换为：

- Knowledge Unit
- Wiki
- Rule
- FAQ
- Capability
- Skill
- Workflow Fragment
- Marketing Topic
- Case Library

---

## 四、支持蒸馏的知识来源

- 书籍
- 官方指南
- 法律法规
- 法院判决
- OA 文书
- 律师意见
- 培训 PPT
- 视频字幕
- GitHub 文档
- 行业报告
- 企业 SOP
- 客户案例
- 白皮书
- 最佳实践

---

## 五、建议流水线

导入知识

↓

整体理解

↓

结构分析

↓

五维提取（框架 / 原则 / 案例 / 反例 / 术语）

↓

三重验证

↓

Knowledge Unit

↓

Wiki

↓

Capability

↓

Skill

↓

Workflow

↓

Marketing Topic

---

## 六、商标行业应用

例如《USPTO TMEP》可蒸馏出：

- LikelihoodAnalysis
- GoodsRewrite
- OfficeActionReply
- DescriptivenessAnalysis
- ExaminerIntentAnalysis
- DeadlineCalculation
- Section8Checklist

Guide 调用这些 Capability，而不是简单回答问题。

---

## 七、Lite 的角色

Lite 不负责生产知识。

Lite 负责消费知识。

Guide 根据用户意图调用：

Capability → Workflow → Flow。

---

## 八、与仓颉.Skill 的区别

仓颉.Skill：

- Book-centric
- 面向单本书

Mo Distillery：

- Knowledge-centric
- 面向所有知识载体
- 与 Mo Brain、Capability、Workflow 深度融合

---

## 九、长期价值

Mo Distillery 将成为：

- Mo Brain 的知识入口
- Capability Catalog 的生产线
- Skill Library 的来源
- Workflow Catalog 的知识来源
- Marketing Engine 的主题来源

它不是附属工具，而是整个 Mo 持续成长的知识制造工厂。
