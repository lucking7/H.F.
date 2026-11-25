const indexes = [
  ["Routing-Policy.json", "网络策略组"],
  ["Routing-Policy144px.json", "网络策略组 · 144 px"],
  ["Apps.json", "应用与品牌"],
  ["Apps144px.json", "应用 · 144 px"],
  ["Flags.json", "旗帜"],
  ["UI.json", "UI 合集"],
  ["UI-Handdrawn-Ink.json", "手绘墨线"],
  ["REX.json", "REX 图标"],
  ["REX-Platforms.json", "REX 平台徽标"],
  ["REX-Runtime.json", "REX 运行时标志"],
];

const glass = new Map([
  ["qwen-brandmark", ["Qwen", "三段蓝色折带组成千问的品牌标记", "brandmarks 品牌标识 通义千问 Qwen Brandmark macOS 26"]],
  ["openrouter-combine", ["OpenRouter", "石墨色玻璃上，荧光绿 OR 标记与白色字标上下排列", "ProviderCombine 供应商 图文组合 OpenRouter Stacked macOS 26"]],
  ["ollama-provider", ["Ollama", "浅色玻璃上的羊驼线稿", "ProviderIcon 供应商 标记 羊驼 Ollama Provider macOS 26"]],
  ["kimi-avatar", ["Kimi", "黑色头像上的白色 K 与蓝点", "Avatar 头像 月之暗面 Moonshot Kimi Avatar macOS 26"]],
  ["cursor-agent", ["Cursor", "立方体顶面独立受光，中央保留三角形留白", "AgentIcon 智能体 立方体 Cursor Faceted macOS 26"]],
  ["mistral-combine", ["Mistral AI", "五色像素图形与 Mistral 字标横向排列", "IconCombine 图文组合 像素 Mistral AI Lockup macOS 26"]],
  ["ai", ["AI", "青瓷色玻璃上的深玉色 AI 字标", "通用 AI 人工智能 总览 全部模型 青玉 Jade Glass"]],
  ["ai-symbol", ["AI 符号", "靛蓝玻璃上的双脑叶浮雕", "通用 AI 人工智能 符号 大脑 脑纹 蛋白石 AI Symbol Opal Glass"]],
  ["claude", ["Claude", "铜色星芒与暖瓷玻璃", "琥珀橙 星芒 铜 暖瓷"]],
  ["openai", ["OpenAI", "珍珠色绳结与烟熏石墨玻璃", "珍珠 绳结 烟熏石墨 ChatGPT"]],
  ["codex", ["Codex", "钴蓝终端云与折射玻璃", "钴蓝 终端 云 命令行"]],
  ["ai-silicon", ["AI Silicon", "裸露计算晶粒、堆叠显存和金色走线", "真实 AI 实体芯片 硅片 显存 加速器"]],
  ["claude-code-light", ["Claude Code Light", "导入原图 · 浅色底与橙色徽标", "浅色 白底 Claude Code 原图"]],
  ["claude-code-white", ["Claude Code White", "导入原图 · 橙色底与浅色徽标", "白色 橙底 Claude Code 原图"]],
  ["gemini", ["Gemini", "棱镜玻璃中的四芒星", "Google 谷歌 双子座 光谱 棱镜 Prism"]],
  ["deepseek", ["DeepSeek", "潮汐玻璃中的鲸鱼", "深度求索 深蓝 潮汐 鲸鱼 Tidal"]],
  ["mistral", ["Mistral", "余烬玻璃中的像素 M", "暖橙 余烬 像素 Ember Le Chat"]],
]);

const assetDirectories = new Set(["flags", "logo", "rex-icons", "signal"]);
const psdPaths = new Set([
  "signal/flash00001.png",
  "logo/apple/apple_store00008.png",
  "logo/apple/apple_store00009.png",
  "logo/apple/apple_store00010.png",
]);
const statusLabels = { unreviewed: "未审核", pass: "通过", revise: "需调整" };
const rawPrefix = "https://raw.githubusercontent.com/lucking7/H.F./main/";
const storageKey = "h.f-icon-review-v1";
const pageSize = 12;
const repoUrl = new URL("../", location.href);

const ids = [
  "collection", "search", "filter", "grid", "results-count", "page-position", "page-prev", "page-next",
  "stage", "stage-img", "tone-dark", "tone-light", "size-fit", "size-144", "size-32", "item-title",
  "item-subtitle", "item-path", "item-dims", "item-count", "item-format", "open-png", "open-icns", "open-psd",
  "prev-item", "next-item", "mark-pass", "mark-revise", "mark-summary", "reviewed-count", "export", "notice",
  "inspector", "empty", "empty-message", "collection-title", "collection-info", "progress-fill",
];
const ui = Object.fromEntries(ids.map(id => [id, document.getElementById(id)]));
const collections = new Map();
let reviewed = new Map();
let assets = new Map();
let matches = [];
let selected = null;
let page = 0;
let storageAvailable = true;
let noticeTimer;

function assetUrl(path) {
  return new URL(path.split("/").map(encodeURIComponent).join("/"), repoUrl).href;
}

function localPath(url) {
  if (typeof url !== "string" || !url.startsWith(rawPrefix)) return null;
  const path = decodeURIComponent(url.slice(rawPrefix.length));
  const segments = path.split("/");
  if (!assetDirectories.has(segments[0]) || !path.toLowerCase().endsWith(".png") || path.includes("\\")) return null;
  if (segments.some(segment => !segment || segment === "." || segment === "..")) return null;
  return path;
}

async function loadIndex([filename, title]) {
  const response = await fetch(assetUrl(filename), { cache: "no-cache" });
  if (!response.ok) throw new Error(`无法读取 ${filename}（${response.status}）`);
  const { icons } = await response.json();
  if (!Array.isArray(icons)) throw new Error(`${filename} 缺少图标列表`);
  const items = icons.map(({ name, url }) => {
    const path = localPath(url);
    if (!path || typeof name !== "string") throw new Error(`${filename} 包含无法读取的图标路径`);
    const glassFile = path.match(/^logo\/ai-glass\/(png|144px)\/([a-z-]+)\.png$/);
    const detail = glassFile && glass.get(glassFile[2]);
    const psd = psdPaths.has(path);
    const basename = path.slice(path.lastIndexOf("/") + 1);
    const preview = psd ? `review/previews/${basename}` : path;
    const thumbnail = detail
      ? `logo/ai-glass/144px/${glassFile[2]}.png`
      : preview.replace(/^signal\/routing-policy\/1024\//, "signal/routing-policy/144/");
    return {
      name,
      path,
      filename,
      keywords: detail ? `${detail[0]} ${detail[1]} ${detail[2]}` : "",
      icns: detail ? `logo/ai-glass/icns/${glassFile[2]}.icns` : null,
      psdFilename: psd ? basename.replace(/\.png$/, ".psd") : null,
      preview,
      thumbnail,
    };
  });
  return { filename, title, items };
}

function setText(id, text) {
  ui[id].textContent = text;
}

function notice(text, { temporary = false } = {}) {
  clearTimeout(noticeTimer);
  setText("notice", text);
  ui.notice.hidden = !text;
  if (temporary) noticeTimer = setTimeout(() => notice(""), 3000);
}

function readReviews() {
  if (!storageAvailable) return null;
  try {
    const saved = Object.entries(JSON.parse(localStorage.getItem(storageKey) || "{}"));
    return new Map(saved.filter(([path, entry]) => assets.has(path) && ["pass", "revise"].includes(entry?.status)));
  } catch {
    storageAvailable = false;
    notice("无法读取本地审核记录，当前标记可在刷新前导出。");
    return null;
  }
}

function statusOf(path) {
  return reviewed.get(path)?.status || "unreviewed";
}

function updateProgress() {
  setText("reviewed-count", `${reviewed.size} / ${assets.size}`);
  ui["progress-fill"].style.width = `${assets.size ? reviewed.size / assets.size * 100 : 0}%`;
  ui.export.disabled = !reviewed.size;
}

function createThumb(item) {
  const mark = statusOf(item.path);
  const button = document.createElement("button");
  button.type = "button";
  button.className = "thumb";
  button.dataset.path = item.path;
  button.title = `${item.name} · ${statusLabels[mark]}`;
  button.setAttribute("aria-label", button.title);

  const art = document.createElement("span");
  art.className = "thumb-art";
  const image = document.createElement("img");
  image.alt = "";
  image.loading = "lazy";
  image.decoding = "async";
  image.addEventListener("error", () => {
    image.hidden = true;
    art.textContent = "无法预览";
  }, { once: true });
  image.src = assetUrl(item.thumbnail);
  art.append(image);

  const name = document.createElement("span");
  name.className = "thumb-name";
  name.textContent = item.name;
  button.append(art, name);
  if (mark !== "unreviewed") {
    const badge = document.createElement("span");
    badge.className = "thumb-status";
    badge.dataset.status = mark;
    badge.textContent = statusLabels[mark];
    button.append(badge);
  }
  button.addEventListener("click", event => {
    showItem(item);
    if (event.detail > 0 && matchMedia("(max-width: 800px)").matches) {
      const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;
      ui.inspector.scrollIntoView({ block: "start", behavior: reducedMotion ? "auto" : "smooth" });
    }
  });
  return button;
}

function updateSelection() {
  for (const thumb of ui.grid.children) {
    const active = thumb.dataset.path === selected?.path;
    thumb.classList.toggle("is-selected", active);
    thumb.setAttribute("aria-pressed", String(active));
  }
}

function renderGrid() {
  const pageCount = Math.ceil(matches.length / pageSize);
  const visible = matches.slice(page * pageSize, (page + 1) * pageSize);
  const focusedPath = ui.grid.contains(document.activeElement) ? document.activeElement.dataset.path : null;
  ui.grid.replaceChildren(...visible.map(createThumb));
  updateSelection();
  if (focusedPath) {
    const focused = [...ui.grid.children].find(thumb => thumb.dataset.path === focusedPath);
    (focused || ui.grid.querySelector(".is-selected") || ui.search).focus({ preventScroll: true });
  }
  setText("results-count", `${matches.length} 项`);
  setText("page-position", pageCount ? `${page + 1} / ${pageCount}` : "0 / 0");
  ui["page-prev"].disabled = page <= 0;
  ui["page-next"].disabled = page + 1 >= pageCount;
}

function updateMark() {
  const status = statusOf(selected?.path);
  for (const value of ["pass", "revise"]) {
    const button = ui[`mark-${value}`];
    button.setAttribute("aria-pressed", String(status === value));
    button.disabled = !selected;
  }
  setText("mark-summary", statusLabels[status]);
  ui["mark-summary"].dataset.status = status;
}

function setPreview(item) {
  const image = ui["stage-img"];
  const url = assetUrl(item.preview);
  image.alt = item.name;
  if (image.src === url) return;
  setText("item-dims", "…");
  image.hidden = false;
  image.src = url;
  if (image.complete && image.naturalWidth) updateDimensions();
}

function updateDimensions() {
  const image = ui["stage-img"];
  if (selected && image.src === assetUrl(selected.preview) && image.naturalWidth) {
    setText("item-dims", `${image.naturalWidth} × ${image.naturalHeight} px`);
  }
}

function renderInspector() {
  ui.inspector.hidden = !selected;
  ui.empty.hidden = !!selected;
  updateMark();
  if (!selected) {
    ui["stage-img"].removeAttribute("src");
    return;
  }

  const position = matches.indexOf(selected);
  setText("item-title", selected.name);
  setText("item-subtitle", selected.subtitle || selected.filename);
  setText("item-path", selected.path);
  setText("item-count", `${position + 1} / ${matches.length}`);
  let format = "PNG";
  if (selected.icns) format = "PNG · ICNS";
  if (selected.psdFilename) format = "PSD · PNG 预览";
  setText("item-format", format);
  ui["open-png"].href = assetUrl(selected.preview);
  ui["open-png"].title = selected.psdFilename ? "打开 PNG 预览" : "打开原尺寸 PNG";
  ui["open-png"].firstChild.textContent = selected.psdFilename ? "PNG 预览" : "原图";
  ui["open-icns"].hidden = !selected.icns;
  if (selected.icns) ui["open-icns"].href = assetUrl(selected.icns);
  else ui["open-icns"].removeAttribute("href");
  ui["open-psd"].hidden = !selected.psdFilename;
  if (selected.psdFilename) {
    ui["open-psd"].href = assetUrl(selected.path);
    ui["open-psd"].download = selected.psdFilename;
  } else {
    ui["open-psd"].removeAttribute("href");
  }
  ui["prev-item"].disabled = position <= 0;
  ui["next-item"].disabled = position + 1 >= matches.length;
  setPreview(selected);
}

function showItem(item) {
  selected = item;
  const nextPage = Math.floor(matches.indexOf(item) / pageSize);
  if (nextPage !== page) {
    page = nextPage;
    renderGrid();
  } else {
    updateSelection();
  }
  renderInspector();
}

function updateResults({ retain = false } = {}) {
  const collection = collections.get(ui.collection.value);
  const query = ui.search.value.trim().toLocaleLowerCase();
  const filter = ui.filter.value;
  const oldPosition = matches.indexOf(selected);
  const previous = retain && selected?.path;

  matches = collection.items.filter(item => {
    const searchable = `${item.name} ${item.path} ${item.keywords}`.toLocaleLowerCase();
    return searchable.includes(query) && (filter === "all" || statusOf(item.path) === filter);
  });

  selected = previous && matches.find(item => item.path === previous);
  selected ||= matches[Math.min(retain ? Math.max(oldPosition, 0) : 0, Math.max(matches.length - 1, 0))] || null;
  page = selected ? Math.floor(matches.indexOf(selected) / pageSize) : 0;
  setText("collection-title", collection.title);
  if (collection.filename === "All.json") {
    const link = document.createElement("a");
    link.href = assetUrl(collection.filename);
    link.textContent = collection.filename;
    link.target = "_blank";
    link.rel = "noopener";
    ui["collection-info"].replaceChildren(link);
  } else {
    setText("collection-info", collection.filename || collection.info);
  }
  if (["Routing-Policy.json", "Routing-Policy144px.json"].includes(ui.collection.value)) {
    const comparison = document.createElement("a");
    comparison.href = assetUrl("signal/routing-policy/comparison.png");
    comparison.target = "_blank";
    comparison.rel = "noopener";
    comparison.textContent = "新旧对照";
    ui["collection-info"].append(" · ", comparison);
  }
  setText("empty-message", query ? "没有匹配的图标。试试其他名称或文件路径。" : "当前筛选下没有图标。");
  renderGrid();
  renderInspector();
}

function changeMark(status) {
  const item = selected;
  if (!item) return;
  reviewed = readReviews() || reviewed;
  const clear = statusOf(item.path) === status;
  if (clear) reviewed.delete(item.path);
  else reviewed.set(item.path, { status, updatedAt: new Date().toISOString() });
  if (storageAvailable) {
    try {
      localStorage.setItem(storageKey, JSON.stringify(Object.fromEntries(reviewed)));
    } catch {
      storageAvailable = false;
    }
  }
  if (storageAvailable) {
    notice(clear ? `已清除 ${item.name} 的标记。` : `${item.name} 已标记为${statusLabels[status]}。`, { temporary: true });
  } else {
    notice("当前浏览器无法保存标记，刷新前可以导出审核记录。");
  }
  const wasMarkFocused = [ui["mark-pass"], ui["mark-revise"]].includes(document.activeElement);
  updateProgress();
  updateResults({ retain: true });
  if (!selected && wasMarkFocused) ui.filter.focus();
}

function syncReviews(event) {
  if (event.key !== storageKey && event.key !== null) return;
  const latest = readReviews();
  if (!latest) return;
  reviewed = latest;
  updateProgress();
  updateResults({ retain: true });
}

function exportReviews() {
  const reviews = [...reviewed].map(([path, entry]) => ({ path, name: assets.get(path).name, ...entry }));
  const data = { version: 1, reviews };
  const url = URL.createObjectURL(new Blob([JSON.stringify(data, null, 2) + "\n"], { type: "application/json" }));
  const link = document.createElement("a");
  link.href = url;
  link.download = "hf-icon-review.json";
  document.body.append(link);
  link.click();
  link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
  if (storageAvailable) notice(`已导出 ${reviews.length} 条审核记录。`, { temporary: true });
}

function setAppearance(kind, value, options) {
  ui.stage.dataset[kind] = value;
  for (const option of options) ui[`${kind}-${option}`].setAttribute("aria-pressed", String(option === value));
}

function wireEvents() {
  ui.collection.addEventListener("change", () => updateResults());
  ui.search.addEventListener("input", () => updateResults());
  ui.filter.addEventListener("change", () => updateResults());
  ui["stage-img"].addEventListener("load", updateDimensions);
  ui["stage-img"].addEventListener("error", () => {
    if (!selected) return;
    setText("item-dims", "无法读取图像");
    ui["stage-img"].hidden = true;
  });

  for (const [direction, offset] of [["prev", -1], ["next", 1]]) {
    ui[`page-${direction}`].addEventListener("click", () => showItem(matches[(page + offset) * pageSize]));
    ui[`${direction}-item`].addEventListener("click", () => showItem(matches[matches.indexOf(selected) + offset]));
  }
  for (const [kind, options] of [["tone", ["light", "dark"]], ["size", ["fit", "144", "32"]]]) {
    const initial = ui.stage.dataset[kind];
    setAppearance(kind, options.includes(initial) ? initial : options[0], options);
    for (const val of options) ui[`${kind}-${val}`].addEventListener("click", () => setAppearance(kind, val, options));
  }
  ui["mark-pass"].addEventListener("click", () => changeMark("pass"));
  ui["mark-revise"].addEventListener("click", () => changeMark("revise"));
  ui.export.addEventListener("click", exportReviews);
  window.addEventListener("storage", syncReviews);
}

async function start() {
  const controls = [ui.collection, ui.search, ui.filter];
  for (const control of controls) control.disabled = true;
  try {
    const catalogs = [["All.json", "综合订阅"], ...indexes];
    const [combined, ...loaded] = await Promise.all(catalogs.map(loadIndex));
    const unique = new Map(combined.items.map(item => [item.path, item]));
    for (const index of loaded) {
      for (const item of index.items) {
        const canonical = unique.get(item.path);
        if (!canonical) unique.set(item.path, item);
        else if (canonical.name !== item.name) canonical.keywords += ` ${item.name}`;
      }
    }
    const featured = [];
    for (const [slug, [name, subtitle]] of glass) {
      const item = unique.get(`logo/ai-glass/png/${slug}.png`);
      if (item) featured.push({ ...item, name, subtitle });
    }
    assets = unique;
    collections.set("glass", { title: "AI 玻璃", info: "1024 px · 144 px · macOS ICNS", items: featured });
    collections.set("all", combined);
    for (const index of loaded) collections.set(index.filename, index);
    ui.collection.replaceChildren(...[...collections].map(([key, { title }]) => new Option(title, key)));
    const requestedCollection = new URLSearchParams(location.search).get("collection");
    const key = requestedCollection === "All.json" ? "all" : requestedCollection;
    ui.collection.value = collections.has(key) ? key : "glass";
    for (const control of controls) control.disabled = false;
    reviewed = readReviews() || reviewed;
    updateProgress();
    wireEvents();
    updateResults();
  } catch (error) {
    ui.inspector.hidden = true;
    ui.empty.hidden = false;
    setText("empty-message", location.protocol === "file:" ? "请用本地 HTTP 地址打开审核页。" : "无法载入图标索引，请检查本地服务器后刷新页面。");
    if (location.protocol !== "file:") notice(error.message);
  }
}

start();
