"""W1 骨架：最小的 FastAPI 服务。

Java 类比：
  FastAPI()      ≈ @SpringBootApplication
  @app.get       ≈ @GetMapping
  BaseModel      ≈ DTO + Bean Validation
  Query()        ≈ @RequestParam
  Depends()      ≈ @Autowired
"""

from datetime import datetime

from fastapi import FastAPI, Query
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

from .copy1 import router as copy1_router

# docs_url=None：关掉默认文档页，因为它的 JS 走 cdn.jsdelivr.net，国内打不开会白屏
app = FastAPI(title="AI Learning - Week 01", docs_url=None, redoc_url=None)
app.include_router(copy1_router)

# 换成国内 CDN，/docs 才能正常加载
SWAGGER_VERSION = "5.17.14"
SWAGGER_JS = f"https://cdn.bootcdn.net/ajax/libs/swagger-ui/{SWAGGER_VERSION}/swagger-ui-bundle.js"
SWAGGER_CSS = f"https://cdn.bootcdn.net/ajax/libs/swagger-ui/{SWAGGER_VERSION}/swagger-ui.css"


@app.get("/docs", include_in_schema=False)
def custom_docs() -> HTMLResponse:
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} - Docs",
        swagger_js_url=SWAGGER_JS,
        swagger_css_url=SWAGGER_CSS,
    )


class EchoIn(BaseModel):
    text: str = Field(min_length=1, max_length=500)


class EchoOut(BaseModel):
    text: str
    length: int


# @app.get("/health") getmapping 健康检查接口，返回 {"status": "ok"}，用于监控服务是否正常运行
# def health()定义方法
# dict[str, str]字典反回类型声明，返回一个字典，键和值都是字符串
# {"status": "ok"}字典对象，key和value都是字符串，表示服务状态正常
# name:list[str] = ["张三", "李四", "王五"]
# usr: dict[str, str|int|float] = {"name": "张三", "age": 18, "height": 1.75}
@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


# 查询类接口用 GET：参数在 URL 上，浏览器可直接打开、可收藏
@app.get("/echo", response_model=EchoOut)
def echo_get(
    text: str = Query(min_length=1, max_length=500, description="要回显的文本"),
) -> EchoOut:
    return EchoOut(text=text, length=len(text))


# 提交类接口用 POST：参数在 body 里，适合长文本、敏感数据、有副作用的操作
@app.post("/echo", response_model=EchoOut)
def echo_post(payload: EchoIn) -> EchoOut:
    return EchoOut(text=payload.text, length=len(payload.text))


# 本地测试页：不依赖任何 CDN，离线可用
TEST_PAGE = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>Echo 测试页</title>
<style>
  body { font-family: system-ui, sans-serif; max-width: 640px; margin: 40px auto; padding: 0 16px; }
  input { width: 100%; padding: 10px; font-size: 16px; box-sizing: border-box; }
  button { margin: 12px 12px 0 0; padding: 8px 16px; font-size: 15px; cursor: pointer; }
  pre { background: #f4f4f4; padding: 12px; border-radius: 6px; white-space: pre-wrap; }
</style>
</head>
<body>
  <h2>Echo 测试页</h2>
  <p>GET 和 POST 各点一次，对比返回。</p>
  <input id="text" value="你好" placeholder="输入文本">
  <div>
    <button onclick="callGet()">GET /echo</button>
    <button onclick="callPost()">POST /echo</button>
  </div>
  <pre id="out">等待调用…</pre>
<script>
  const out = document.getElementById('out');
  const text = () => document.getElementById('text').value;

  async function callGet() {
    const r = await fetch('/echo?text=' + encodeURIComponent(text()));
    out.textContent = JSON.stringify(await r.json(), null, 2);
  }

  async function callPost() {
    const r = await fetch('/echo', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({text: text()}),
    });
    out.textContent = JSON.stringify(await r.json(), null, 2);
  }
</script>
</body>
</html>"""


@app.get("/add", response_model=int, summary="加法计算", description="计算两个整数的和")
def add(
    a: int = Query(..., description="第一个加数"), b: int = Query(..., description="第二个加数")
) -> int:
    return a + b


@app.get(
    "/now", response_model=str, summary="获取当前时间", description="返回服务器当前时间的字符串表示"
)
def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def index() -> str:
    return TEST_PAGE
