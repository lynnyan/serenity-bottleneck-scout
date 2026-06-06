# Serenity 研报包（Thesis Pack）— tesla-optimus-robot-us-china

日期：2026-06-05  
市场：US / CN  
周期：1-3y  
候选：002050.SZ（三花智控）— watchlist（Tesla 供应商状态：Rumor）；688017.SH（绿的谐波）— watchlist（Tesla 供应商状态：Rumor）

## 0）范围与假设

- 覆盖/不覆盖：
  - 覆盖：以 Tesla Optimus（人形机器人）作为**需求锚**；结合美国与中国的产业政策与供给侧背景；将**关节执行/传动栈**作为核心的*瓶颈（bottleneck）*候选节点（精密减速器 → 机电一体关节/执行器）。
  - 不覆盖：完整估值；详尽 TAM；对每个“人形机器人项目”的全量竞品拆解。
- 关键假设（必须可证伪）：
  - Tesla 持续将“Bots（含 Optimus）”作为产品线，并在 1–3 年周期内推进到“量产”。[R1]
  - Tesla 在 2026 财年内持续在季度材料中披露与机器人产线/工厂准备相关的制造意图（产线安装、工厂准备等）。[R2] [R3]
  - 人形机器人在可预见架构下需要高精度关节执行（减速器 + 电机 + 驱动 + 传感），这些硬件的制造/可靠性/验证是早期规模化的潜在瓶颈（而不仅是“AI 演示”）。[R4]
  - 跨境采购与本地化不确定；本报告中提及的公司不等于 Tesla 已确认供应商，除非按规则标注为 **Anchor-confirmed**。
- 会推翻我的证据（反证线索）：
  - Tesla 对 Optimus 降级/转向（例如在财报中不再提“Bots/Optimus”，资本计划与时间表消失，或关键里程碑推迟到 2027 之后）。[R1] [R3]
  - Tesla 快速垂直整合关键节点（例如明确宣称并展示“自研/自制减速器或执行器”的产线与扩产证据），导致外部供应商难以获得利润池。
  - 明确替代：Tesla（或主流 OEM）转向不同关节方案（例如直驱/不同类型减速技术/不同执行器封装），在成本与精度上足以替代当前路径。

## 1）供应链地图（必须物理闭环）

原材料 → 工艺/半成品 → 器件 → 模组 → 系统 → 终端客户

- 地图（以关节执行/传动栈为焦点；从头到尾）：
  - 原材料：合金钢（齿轮/轴类）、铜（绕组）、永磁体（电机）、铝（壳体）、润滑材料。
  - 工艺/过程：锻造/铸造、热处理、精密机加工、磨削/珩磨、涂层、计量/检测（metrology）。
  - 器件（关节关键件）：
    - 精密减速器要素（例如“应变波/谐波”类；轴承；柔轮/刚轮等）
    - 高功率密度电机 + 热设计
    - 伺服驱动/功率器件 + 控制芯片
    - 关节传感（位置/力矩：编码器 + 力/力矩传感）
  - 模组：
    - 机电一体关节/执行器：减速器 + 电机 + 驱动 + 传感的一体化“关节”
    - 线束、电源分配与安全互锁
  - 系统：
    - 人形机器人（Optimus 级别）+ 车队软件 + 训练/仿真管线
  - 终端客户：
    - Tesla 内部先行部署，后续若商业化则面向企业/消费者
    - 中国侧：政策驱动下的多场景人形机器人产业化推进。[R4]
- chokepoint vs bottleneck（必经口 vs 供给瓶颈）：
  - **Chokepoint（跨生态“必经门槛”）：目前公开信息不足，NOT PROVEN。** 不能把减速器/执行器当作跨生态“标准门槛/平台入口”。这些部件通常在足够时间与资本投入下可做二供/多供。
  - **Bottleneck（产能/工艺/验证摩擦）：** 精密减速器与机电一体执行器制造依赖专用设备（精密加工、热处理、计量检测）与可靠性验证；良率爬坡可能慢。本报告按“瓶颈假设”写作，而非已证实 chokepoint。[R4]
- 供给侧“物理约束”应如何量化：
  - 专用设备的供给与交付周期（精密磨齿/磨削、计量检测、热处理能力）与良率学习曲线。
  - 公差与可靠性测试产能（加速寿命、安全测试）。
  - 需求锚是否在材料中点名“component supply / supply chain readiness”等约束。[R2] [R3]
- 地理/政策单点（US + CN）：
  - 美国：Tesla 在 Q1 2026 更新中提到 Fremont 与 Texas 的机器人产线准备。[R3]
  - 中国：政策文件明确强调关键零部件突破（含减速器/电机/驱动）与 2027 年前形成“安全可靠的产业链供应链体系”。[R4]
  - 跨境：关税/出口管制与本地化激励会改变二供节奏与验证周期（需持续跟踪财报与政策更新）。

## 2）候选表（标准字段）

| 字段 | 内容 |
|---|---|
| 主题 | Tesla Optimus（人形机器人）— US + CN |
| 产业层级 | 器件 → 模组（精密减速器 / 机电一体执行器） |
| 核心产品（瓶颈节点） | 关节执行/传动栈：精密减速器 + 电机 + 驱动 + 传感的一体化执行器，关键在制造公差、可靠性与验证吞吐。 |
| “不可绕开”的物理原因 | 在高 DOF 人形架构下，关节必须完成大减速比、高刚度/低背隙、力矩控制与安全冗余；没有执行/传动栈就无法实现可用的运动控制。 |
| chokepoint 结论 | NOT PROVEN（本报告不把该节点当作跨生态标准门槛）。 |
| bottleneck 结论 | 假设成立的必要条件：出现>12 个月交期/在手订单/产能抢占/扩产资本化等可追踪证据（目前缺口较大）。 |
| 价值捕获路径 | 若瓶颈成立，价值捕获应体现在：减速器/执行器厂商的收入结构、ASP、毛利率、产能利用率、backlog/订单质量等公开指标上（目前未完成绑定）。 |
| 主要风险 | 架构替代、Tesla 垂直整合、二供加速、政策导致的价格竞争/过度扩产、可靠性验证拖累良率与利润。 |

## 3）评分（100 分制；按阈值扣分）

- 需求锚（25）：18（Tesla 产线意图清晰，但缺少可重复的“产量/部署”数据；中国侧用 UBTECH/Unitree 作为行业需求侧补充）。[R2] [R3] [R6] [R7]
- chokepoint（20）：0（NOT PROVEN）
- bottleneck（20）：8（物理合理，但缺少交期/backlog 等硬证据）
- 价值捕获（15）：4（尚未把“瓶颈→财报指标”绑定到单一上市主体）
- 催化剂（10）：8（10‑Q 窗口与 2026-12-31 二元里程碑较清晰）
- 风险/反证（10）：8

**合计：46 / 100（watchlist / 研究计划型包，不满足高确信度阈值）**

## 4）证据表（每条关键主张对应来源/缺口）

| 主张 | 结论 | 证据渠道 | 一手证据/链接 | 缺口（如何补齐） |
|---|---|---|---|---|
| Tesla 机器人产线意图明确 | PASS | IR/财报更新 | Q1 2026 Update（p6）提到“1M/10M 产线设计”；Q4 2025 Update（p8）提到 2026 年前量产计划。[R2 p8] [R3 p6] | 需要跨季度的“单位/部署/产量”可重复指标 |
| 中国侧人形需求/产业化信号 | PASS（行业层面） | 交易所公告/公司披露 | UBTECH FY2025（p1–p2）披露人形业务收入快速增长并提及量产交付；Unitree 上交所披露（p25）提及人形相关趋势。[R6 p25] [R7 p1] [R7 p2] | 需要证明这些需求同样约束在“精密减速/执行器”而非仅软件 |
| 节点为跨生态 chokepoint | FAIL | 标准/认证/平台/资格认证 | 目前无可用一手证据证明跨生态“标准门槛” | 若要通过：需要标准/认证/平台入口型证据；否则换节点 |
| 交期>12个月（瓶颈硬证据） | FAIL | backlog/交期/设备交付 | 目前缺少与该节点绑定的日期化交期/backlog 证据 | 需要：供应商财报/设备 OEM 声明/经销商报价（含时间戳） |
| 供应商集中≤3 或切换/认证摩擦很大 | FAIL | 客户集中/teardown/认证周期 | 未识别 Tesla 的具体供应链；也未证明行业集中度阈值 | 需要：BOM/拆解归因、客户集中披露、认证周期披露 |
| 价值捕获 4–8 季度内可见 | FAIL | 分部/毛利/ASP/backlog | 未绑定到单一上市主体的可观察 KPI | 选择 1 家候选并定义 KPI + 阈值（毛利、ASP、利用率等） |

## 5）催化剂时钟

- 硬催化（自 2026-06-05 起 3–9 个月）：
  - Tesla Q2 2026 披露窗口：约 **2026-08-10** 附近的 10‑Q（看是否新增量化信息：产线状态、capex、部署规模）。
  - Tesla Q3 2026 披露窗口：约 **2026-11-09** 附近的 10‑Q（验证 Q2 是否兑现；是否再次确认 2026 年底里程碑）。
  - 中国侧政策落地：将“2026 H2”细化为具体文件类型/发布部门/发布时间窗（当前不够具体）。[R4]
- 确认催化（12–18 个月）：
  - **到 2026-12-31：** Tesla “2026 年底前量产”是否实现（强二元）。[R2 p8]
  - **到 2027-06-30：** 是否出现持续的试产/部署规模化数据（多季度连续披露），以及关节执行模块是否出现“代际冻结”的资格认证壁垒。

## 6）风险与反证

- 替代路径：直驱/其他减速方案/不同执行器封装，降低“谐波/应变波”减速方案的重要性。
- 政策/地理：
  - 本地化与二供加速可能压缩供应商议价权；反之跨境摩擦也可能拉长认证周期。
  - 政策指向不等于利润（可能过度扩产、价格竞争）。
- 周期/估值/流动性（一般研究提示）：工业自动化资本开支具有周期性，不应把政策或演示当作线性增长。
- 质量/可靠性：可靠性/安全认证拖慢爬坡；良率学习可能侵蚀利润。

## 7）审判结论（Verifier Judge）

- 结论（第 2 轮）：**REVISE**（仍未满足该 skill 的“chokepoint/bottleneck 通过阈值”）。
- 审判文件：/Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/judge/round_2/judge_verdict.md
- 要达到 APPROVE 的必做修订：
  - 证明（或更换）跨生态 **must-pass gate**（标准/认证/资格门槛等一手证据），否则 chokepoint 相关阈值无法通过。
  - 补齐**日期化交期/backlog**证据（绑定到减速器/执行器或关键设备）。
  - 补齐**供应商集中度/切换摩擦**证据（BOM/拆解、认证周期、客户集中披露）。
  - 将**价值捕获**绑定到至少一家上市公司的可观测 KPI（4–8 季度内验证）。
- 重点监控反证：
  - Tesla “2026 年底前量产”是否软化/延后。[R2 p8] [R3 p6]
  - 中国侧快速多供与价格战（关注利用率、ASP、毛利语言）。[R5]
  - 关节架构替代。

## References

- [R1] Tesla 2025 10‑K HTML 片段（抽取）：/Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/filing_snippets_tsla_10k.md
- [R2] Tesla Q4 2025 Update（PDF）：/Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/TSLA-Q4-2025-Update.pdf
- [R3] Tesla Q1 2026 Update（PDF）：/Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/TSLA-Q1-2026-Update.pdf
- [R4] 《人形机器人创新发展指导意见》（工信部科〔2023〕193号，2023‑10‑20；PDF）：https://www.ncsti.gov.cn/kjdt/tzgg/202311/P020231103479626066804.pdf
- [R5] 绿的谐波 2025 年年度报告（PDF）：/Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/688017_2025_annual_report_2026-04-23.pdf
- [R6] 宇树科技（Unitree）上交所披露文件（PDF，2026‑03‑20）：/Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/Unitree_SSE_2026-03-20.pdf
- [R7] UBTECH FY2025 业绩披露（HKEX，PDF，2026‑03‑31）：/Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/UBTECH_HKEX_2026-03-31_FY2025_results.pdf
- [R8] 三花智控 2025 年年度报告全文（巨潮资讯，PDF，2026‑03‑24）：/Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/sanhua_002050_annual_2025_2026-03-24_cninfo.pdf
- [R9] 三花智控 2026‑05‑26 投资者关系活动记录表（编号：2026‑004，巨潮 PDF）：/Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/sanhua_002050_investor_activity_2026-05-26_cninfo_1225332276.pdf
- [R10] 36Kr（EU）文章：称 Tesla 向三花下达执行器大单，并在 Optimus 供应链语境中提及“harmonic reducers（如 Green Harmonic）”（2025‑10‑15）：https://eu.36kr.com/en/p/3510288514980998（快照：/Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/rumor_36kr_sanhua_685m_order.html）
- [R11] 东方财富财富号：称三花为 Optimus“核心供应商”（2025年12月12日）：https://caifuhao.eastmoney.com/news/20251212090942688077930（快照：/Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/rumor_caifuhao_sanhua_core_supplier_2025-12-12.html）
- [R12] 东方财富财富号：称绿的谐波进入 Optimus 供应链（2025年12月25日）：https://caifuhao.eastmoney.com/news/20251225133947133551540（快照：/Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/rumor_caifuhao_greenharmonic_tesla.html）
- [R13] 界面新闻：讨论“50亿订单”传闻，并提到公司对机器人业务细节不便回复（2026年2月28日）：https://www.jiemian.com/article/13508755.html（快照：/Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/rumor_jiemian_sanhua_50b_rumor.html）
- [R14] Rumor dossier（整理，非一手）：/Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/rumor_dossier.md
- [R15] Tesla 专利（一手）— “ACTUATOR AND ACTUATOR DESIGN METHODOLOGY”（WO2024072984A1）：https://patents.google.com/patent/WO2024072984A1/en（PDF 快照：/Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/tesla_patent_WO2024072984A1_actuator_design.pdf）
- [R16] Tesla 专利（一手）— “Systems and methods for a robot knee joint assembly”（WO2024073135A1 / EP4594165A1）：https://patents.google.com/patent/WO2024073135A1/en

## 附录：组件优先候选池（含供应商确认标记）

> 这不是已确认供应商清单。每个公司都必须标注是否为 **Anchor-confirmed**。
> 允许的标注：**Anchor-confirmed / Not confirmed / Rumor / Unknown**，并给出证据说明（URL 或文件）。
>
> 需求锚（Anchor company）：Tesla（Optimus / “Bots”项目）[R1]

| 节点 | 公司 | 市场 | Tesla 供应商状态 | 证据说明 | 重要性 |
|---|---|---|---|---|---|
| 下游人形 OEM（行业需求信号） | UBTECH | CN/HK | Not confirmed | FY2025 业绩披露提及人形业务收入增长与量产交付（p1–p2）。[R7 p1] [R7 p2] | 独立的一手行业需求/商业化信号（非 Tesla 专属）。 |
| 下游人形 OEM（行业需求信号） | Unitree | CN | Not confirmed | 上交所披露文件中提及人形相关趋势（p25）。[R6 p25] | 独立的一手行业需求/商业化信号（非 Tesla 专属）。 |
| 机电一体执行器/总成（候选） | 三花智控（002050.SZ） | CN | Rumor | 多个二手渠道声称其为 Optimus 执行器/关节供应链相关方，但缺少 Tesla/公司一手点名：见 [R10] [R11] 与整理 [R14]。同时，官方 2026‑05‑26 投资者关系活动记录表未出现 Tesla/Optimus/关节等关键词。[R9] | 若人形规模化，执行器总成的集成与验证可能成为早期产能/良率瓶颈；与 Tesla 的供应关系仍未被一手证据证实。 |
| 精密减速器（应变波/谐波类） | 绿的谐波（688017.SH） | CN | Rumor | 二手渠道声称其进入 Optimus 供应链：见 [R10] [R12] 与整理 [R14]。但公司年报未点名 Tesla/Optimus。[R5] | 若人形关节需求扩张，可能成为产能杠杆，但与 Tesla 的供应关系仍未被一手证据证实。 |
| 精密减速器（全球 incumbents 示例） | Harmonic Drive Systems / Nabtesco | Non‑US/CN | Unknown | 未在此报告中核验 Tesla 关联（无一手证据） | 对标竞争格局；潜在供给替代。 |
| 机电一体执行器（减速器+电机+驱动） | 绿的谐波（机电一体化） | CN | Unknown | 年报提及机电一体化产品；无 Tesla 一手确认。[R5] | 执行器封装与验证可能构成瓶颈。 |
| 电机（高功率密度） |（示例）Nidec / 国内电机厂商 | Mixed | Unknown | 无 Tesla 一手确认 | 电机影响力矩密度与热边界。 |
| 伺服驱动/功率器件 |（示例）TI / Infineon / 国内驱动厂商 | Mixed | Unknown | 无 Tesla 一手确认 | 体量放大时可能成为约束。 |
| 传感（视觉/力/编码器） |（示例）国内传感厂商/全球计量厂商 | Mixed | Unknown | 政策强调“专用传感器”；无 Tesla 一手确认。[R4] | 传感质量影响操作、安全与验证难度。 |

## 变更记录

- 将节点从“chokepoint”降级为**仅瓶颈假设**，并明确 chokepoint 为 **NOT PROVEN**。
- 增补 Tesla 关于 1M/10M 产线意图与“2026 年底前量产”目标的可审计引用（含页码）。[R2 p8] [R3 p6]
- 增补中国侧两个独立的一手行业需求信号（UBTECH + Unitree，含页码）。[R6 p25] [R7 p1] [R7 p2]
- 将交期、供应商集中度、价值捕获等缺口明确标注为 **FAIL / evidence gaps**。
