# AI 转型学习仓库

南京 · 10 年 Java 后端 · 目标 2027-04 前拿到 AI 应用 / Agent / RAG 岗 offer。

> 📱 手机版学习手册：`docs/index.html`（打卡 + 抽背 + 速查）。发布与更新见 `DEPLOY.md`。

## 目录结构

```
ai-learning/
├── ROADMAP.md          # 20 周计划，每周勾选进度
├── pyproject.toml      # 依赖与环境
├── .env.example        # API key 模板
├── week01/             # 每周一个目录，可独立运行
│   ├── app/main.py
│   └── test_main.py
└── projects/           # 三个主打项目（W6 起陆续创建）
    ├── p01-llm-feature/
    ├── p02-rag-kb/
    └── p03-agent-ops/
```

## 每周节奏（26h）

| 时间 | 做什么 | 时长 |
|---|---|---|
| 周一 ~ 周三 | 输入：读文档、写 20-50 行小练习 | 6h |
| 周四 ~ 周五 | 消化：整理笔记、让 agent 出题 | 4h |
| 周六 | 项目主攻，分 4 个 2h 块 | 8h |
| 周日 | 4h 项目收尾 + 2h 复盘 + 2h 缓冲 | 8h |

**铁律：每周结束时必须有一个能跑的东西。** 哪怕只是一个接口、一个脚本。不允许连续两周只看不写。

## 环境

```bash
cd ai-learning
uv sync
cp .env.example .env      # 填入你的 key
```

跑起来：

```bash
uv run python -m uvicorn week01.app.main:app --reload
# 打开 http://127.0.0.1:8000/docs
```

跑测试：

```bash
uv run pytest -q
```

## 用 Claude Code 的正确姿势

1. 在这个目录启动 Claude Code，它会自动读根目录的 `claude.md`。
2. 每周开始：让它读 `ROADMAP.md` 当前周，拆成 7 天任务。
3. 写代码时：自己先写，卡住只问「这个报错怎么理解」，不要让它代写。
4. 写完：`让它 review 这个文件`，要求给出问题 + 改法 + 一个追问。
5. 周日：`出 5 道本周自测题，我答完你批改`。
6. 每两周：把 10 个目标 JD 丢给它做差距分析，更新下周计划。

## 项目记录要求（面试素材）

每个项目根目录必须有：

- `README.md`：解决什么问题、架构图、技术选型理由、踩坑记录
- `EVAL.md`：评测集规模、指标、优化前后对比
- `COST.md`：QPS、P99 延迟、单次调用成本、优化手段
- 一个可访问的演示地址（或录屏）
