# 学习手册发布指南

页面文件：`docs/index.html`（单文件，无任何外部依赖，可离线）。

## 本地看

直接双击 `docs/index.html`，或：

```bash
cd ai-learning
python -m http.server 8080 --directory docs
# 打开 http://127.0.0.1:8080
```

## 手机上随时看（三种，按省事程度排）

1. **微信文件传输助手**（最快，零部署）
   把 `docs/index.html` 发到文件传输助手，手机点开，加到收藏。离线可用。
2. **GitHub Pages**（长期，push 即更新）
   见下一节。
3. **Cloudflare Pages / 腾讯云静态托管**（国内访问快，免费）
   连上 GitHub 仓库，构建目录填 `docs`，无需构建命令。

## GitHub Pages 首次发布

前提：已装 git，有 GitHub 账号。

```bash
cd ai-learning
git init
git add .
git commit -m "W1 study handbook"
git branch -M main
git remote add origin https://github.com/<你的用户名>/ai-learning.git
git push -u origin main
```

然后在 GitHub 网页上：

1. 仓库 → **Settings** → 左侧 **Pages**
2. **Source** 选 `Deploy from a branch`
3. **Branch** 选 `main`，目录选 `/docs`，点 **Save**
4. 等 1-2 分钟，访问 `https://<你的用户名>.github.io/ai-learning/`

> 如果访问 404，先确认 `docs/index.html` 已经 push 上去，再看 Actions 里 Pages 的构建状态。

## 以后怎么更新

改完 `docs/index.html` 后：

```bash
git add docs/index.html
git commit -m "更新 W1 手册"
git push
```

1 分钟后手机刷新即可。建议手机浏览器「添加到主屏幕」，像 App 一样打开。

## 内容怎么改

| 想改什么 | 怎么做 |
|---|---|
| 改某天的要点 / 题目 | 跟我说「把 D3 的要点改成…」，我直接改文件 |
| 加一周（W2） | 说「把 W2 加进页面」，我加一个 tab |
| 自己动手 | 打开 `docs/index.html`，搜索 `id="d3"` 定位，改完刷新浏览器 |
| 进度清零 | 页面「说明」tab → 重置进度 |

不要让页面内容和 `week01/PLAN.md` 长期分叉。**PLAN.md 是源头，页面是展示。** 改了计划就同步一次。

## 关于打卡进度

进度存在浏览器的 `localStorage` 里：

- 换浏览器、换手机、清缓存都会丢
- 我（Claude）**读不到**你浏览器的本地存储
- 想让我看到进度：页面「说明」tab → **导出进度** → 把文本发给我

导出格式长这样：

```
W1 打卡进度（2026-11-16 ~ 11-22）
D1 4/4
D2 2/4
D3 0/4
D4 0/4
D5 0/4
D6 0/4
```

我拿到后会按你的实际进度调整后面几天的强度。

## 国内访问提示

`*.github.io` 在国内时快时慢，偶尔 DNS 污染。如果长期打不开：

- 用 Cloudflare Pages（免费，国内一般可访问）
- 或把 `index.html` 放腾讯云 COS / 阿里云 OSS 开静态网站
- 最稳的还是微信收藏那个离线文件
