# W1 七天计划（2026-11-16 → 11-22）

> 每天核心 2h；周末 8h = 2h 核心 + 6h 加餐。
> 规则：某天没做完，周日加餐时段补，债不滚到下周。

## Day 1 · 周一 11/16 · 读懂你的第一个服务

- [x] 20min 跑一遍：`uv run pytest -q` → 全绿；`uvicorn` 起来，浏览器开 `/`、`/docs`、`/echo?text=你好`
- [x] 40min 逐行读 `week01/app/main.py`，写 Java 对照表
- [x] 45min 自己加两个接口（不许抄）：`GET /add?a=&b=` 返回和；`GET /time` 返回当前时间
- [ ] 15min 各写一个 pytest 用例

交付：`/add`、`/time` 可调，测试全绿。
自测：如果参数是一段 500 字文本，用 GET 还是 POST？为什么？

## Day 2 · 周二 11/17 · 类型系统与校验

- [ ] 30min 类型标注：`list[str]` ≈ `List<String>`，`dict[str, int]` ≈ `Map<String,Integer>`，`str | None` ≈ `Optional<String>`
- [ ] 50min pydantic：定义 `User` / `Order` / `OrderItem`，加校验（age 1-120、qty ≥ 1、price > 0、email 用 `Field(pattern=...)`，**不要加 email-validator 依赖**）
- [ ] 30min 写 5 个测试，证明非法输入返回 422
- [ ] 10min 笔记

交付：`week01/day02_models.py` + 5 个测试。
自测：Python 的类型注解运行时会检查吗？那 pydantic 为什么能拦下非法输入？

## Day 3 · 周三 11/18 · 列表推导与生成器

- [ ] 20min 列表推导 = `filter + map`：`[x*2 for x in xs if x > 0]`
- [ ] 20min dict / set 推导
- [ ] 30min 生成器 = 惰性流；`yield` ≈ `Iterator`，但只能遍历一次
- [ ] 40min 练习：把你写过的一段 Java Stream 翻成 Python；用生成器读 10 万行日志统计 level 分布，观察内存
- [ ] 10min 笔记

交付：`week01/day03_streams.py`。
自测：什么时候必须用生成器而不是列表？

## Day 4 · 周四 11/19 · async / await 的本质

- [ ] 30min 概念：协程、事件循环、单线程协作式调度；`asyncio.run()` 的作用
- [ ] 50min 练习：`async def work(i)` 里 `await asyncio.sleep(1)`；串行 10 个 vs `asyncio.gather` 10 个，用 `time.perf_counter()` 对比
- [ ] 20min 把 `/echo` 改成 `async def`，观察有无区别（无 IO 时没有）
- [ ] 20min 笔记

交付：`week01/day04_async.py`，能跑出串行≈10s、并发≈1s。
自测：async 能加速 CPU 密集任务吗？

## Day 5 · 周五 11/20 · 并发 HTTP

- [ ] 20min `httpx.AsyncClient` vs `requests` vs Java `HttpClient`
- [ ] 40min 并发请求自己的 `/health` 20 次，用 `asyncio.Semaphore(5)` 限流，统计耗时与成功数
- [ ] 40min 加超时（`httpx.Timeout`）和重试（for 循环 + 指数退避）
- [ ] 20min 笔记，对照线程池 + 信号量

交付：`week01/day05_http.py`。
自测：不加 Semaphore 会怎样？什么场景下必须加？

## Day 6 · 周六 11/21 · 串起来

核心 2h：

- [ ] 写 `week01/day06_cli.py`：读本地文本 → 并发处理 → 输出 top 10 词频
- [ ] 必须用到：类型标注 + 一个 pydantic 模型 + 生成器读文件 + `asyncio` 并发

加餐 6h：

- [ ] 2h 提前进 W2：用 FastAPI 重写一个你熟的 Java 接口（先内存版，不接库）
- [ ] 2h 读 FastAPI 官方文档 Concurrency and async / await 全文
- [ ] 2h 跑 `ruff check .` 和 `ruff format .`，理解 Python 工具链

## Day 7 · 周日 11/22 · 复盘 + 自测

核心 2h：

- [ ] 30min 整理 `week01/NOTES.md`，写 Java → Python 对照表
- [ ] 60min 做 5 道自测题（自己先写答案，再让 Claude 批改）
- [ ] 30min 勾掉 ROADMAP W1，预读 W2

加餐 6h：

- [ ] 2h pydantic 进阶：嵌套模型、`field_validator`、`model_config`
- [ ] 2h 写《Java 程序员看 Python》500 字（发不发都行，先写）
- [ ] 2h 补债 / 休息

---

## W1 验收标准

- [ ] 至少 8 个接口能跑
- [ ] 至少 12 个测试全绿
- [ ] 能不看文档写出列表推导、生成器、`async` 函数
- [ ] 能口述 async 与线程池的三个区别
- [ ] `NOTES.md` 里有 Java 对照表

## 5 道自测题

1. `response_model` 和 Spring 的返回类型，作用差在哪？
2. Python 类型注解运行时不检查，pydantic 为什么能拦？
3. 生成器表达式和列表推导内存差在哪？何时必须用生成器？
4. `asyncio.gather` 和 `CompletableFuture.allOf` 的本质区别是什么？
5. `Semaphore(5)` 不加会怎样？什么场景必须加？
