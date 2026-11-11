#!/usr/bin/env python3
"""Build mục Kiến thức của qhub.com.vn từ _src/posts/*.md.

Chạy từ thư mục gốc repo:  python3 _tools/build.py [--strict]
Cần: pip install markdown pyyaml

Sinh ra:
  kien-thuc/index.html                 trang tổng
  kien-thuc/chu-de/<topic>/index.html  trang chủ đề
  kien-thuc/<slug>/index.html          bài viết
  tac-gia/nguyen-van-quang/index.html  trang tác giả
  sitemap.xml, feed.xml, llms.txt, robots.txt
Thư mục có dấu _ ở đầu không được GitHub Pages xuất bản.
"""
import csv, datetime as dt, html, json, math, os, re, sys
import markdown, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://qhub.com.vn"
BRAND = "QHUB Commerce"
STRICT = "--strict" in sys.argv
e = html.escape

TOPICS = [
    ("tiktok", "Xây kênh TikTok", "Xây kênh TikTok bán hàng từ con số 0: định vị, thuật toán, lịch đăng, đọc số liệu và những lỗi khiến kênh đứng im."),
    ("content-tiktok", "Content TikTok", "Lên ý tưởng, viết kịch bản, quay dựng video ngắn bán hàng; hook, nhịp, CTA và cách nhân bản nội dung thắng."),
    ("tiktok-shop", "TikTok Shop căn bản", "Mở gian hàng, chính sách, điểm hiệu quả, liên kết affiliate và mọi thứ người mới cần biết về TikTok Shop."),
    ("van-hanh-tiktok-shop", "Vận hành TikTok Shop", "Vận hành gian hàng TikTok Shop hằng ngày: sản phẩm, giá, kho, livestream, affiliate KOC, chăm sóc đơn và đội ngũ."),
    ("quang-cao-tiktok", "Quảng cáo TikTok & GMV Max", "Chạy GMV Max cho sản phẩm và LIVE, ROI mục tiêu, sáng tạo quảng cáo, đọc báo cáo và tối ưu ngân sách."),
    ("phi-san-tiktok-shop", "Phí sàn TikTok Shop", "Các loại phí TikTok Shop, cách tính trên từng đơn, cách định giá để vẫn có lãi khi phí thay đổi."),
    ("van-hanh-shopee", "Vận hành Shopee", "Vận hành gian hàng Shopee: SEO sản phẩm, chương trình, voucher, kho vận, đánh giá, chỉ số shop và Shopee Mall."),
    ("quang-cao-shopee", "Quảng cáo Shopee", "Shopee Ads: quảng cáo tìm kiếm, khám phá, Shop+ Ads, GMV Max, giá thầu, từ khóa và cách đọc ROAS."),
    ("phi-san-shopee", "Phí sàn Shopee", "Phí cố định, phí xử lý giao dịch, gói dịch vụ, Voucher Xtra và cách tính lợi nhuận thật trên Shopee."),
    ("ban-hang-facebook", "Bán hàng Facebook", "Bán hàng trên Facebook: fanpage, nhóm, livestream, quảng cáo Meta, inbox chốt đơn và chăm sóc khách cũ."),
    ("youtube", "Xây kênh YouTube", "Xây kênh YouTube cho doanh nghiệp: Shorts, video dài, SEO YouTube, nhịp đăng và biến người xem thành khách."),
    ("instagram", "Phát triển Instagram", "Phát triển Instagram cho thương hiệu: Reels, Stories, hồ sơ, hashtag và bán hàng qua Instagram."),
    ("threads", "Phát triển Threads", "Dùng Threads để xây cộng đồng và kéo khách: cách viết, nhịp đăng, liên kết với Instagram và bán hàng mềm."),
    ("website-seo", "Website chuẩn SEO", "Xây website bán hàng chuẩn SEO và dễ được AI như ChatGPT, Gemini nhắc tới: cấu trúc, nội dung, kỹ thuật, đo lường."),
    ("lich-sale", "Lịch sale & chiến dịch", "Ngày sale đôi, sale giữa tháng, ngày lương, ngày thường: chuẩn bị gì, chạy gì, đo gì trên TikTok Shop và Shopee."),
]
TOPIC = {k: {"slug": k, "name": n, "desc": d} for k, n, d in TOPICS}

AUTHOR = {
    "name": "Nguyễn Văn Quang",
    "url": SITE + "/tac-gia/nguyen-van-quang/",
    "role": "Founder & CEO, QHUB Commerce",
    "bio": "Đi lên từ bán hàng thị trường, qua trade marketing, brand marketing đến vận hành thương mại điện tử cho các doanh nghiệp đồ uống, thực phẩm và hàng tiêu dùng. Trực tiếp vận hành gian hàng trên Shopee, TikTok Shop, Facebook, Lazada, Tiki và Website.",
    "path": ["Suntory PepsiCo", "Trà Cozy", "Men' Vodka", "Quang Linh Vlog Store", "Trà Tâm Đạo", "Hệ thống nhà máy thực phẩm chức năng & mỹ phẩm (Dulin, Hiup)", "QHUB Commerce"],
}


def ver():
    try:
        m = re.search(r"styles\.css\?v=([A-Za-z0-9]+)", open(os.path.join(ROOT, "index.html"), encoding="utf-8").read())
        return m.group(1) if m else "1"
    except OSError:
        return "1"


V = ver()


def head(title, desc, url, og_type="website", image=SITE + "/og-qhub.png", extra="", robots="index,follow,max-image-preview:large"):
    return f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:locale" content="vi_VN">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B1220">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon-96x96.png" type="image/png" sizes="96x96">
<link rel="icon" href="/favicon-192x192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="alternate" type="application/rss+xml" title="Kiến thức QHUB Commerce" href="/feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css?v={V}">
{extra}</head>
<body class="kt-body">
<a class="skip" href="#main">Bỏ qua tới nội dung</a>
<header class="site-header" id="top">
  <div class="wrap">
    <a class="brand" href="/" aria-label="QHUB Commerce — trang chủ">
      <img src="/logo-qhub-white.png" alt="" width="45" height="48">
      <span>QHUB<small>COMMERCE</small></span>
    </a>
    <nav class="nav" id="nav" aria-label="Điều hướng chính">
      <a href="/gioi-thieu/">Giới thiệu</a>
      <a href="/#lam-gi">QHUB làm gì</a>
      <a href="/kien-thuc/">Kiến thức</a>
      <a href="/#doi-ngu">Đội ngũ</a>
      <a href="/qhub-herbal.html">QHUB HERBAL</a>
      <a class="nav-cta" href="/#dat-lich">Đặt lịch chẩn đoán</a>
    </nav>
    <a class="btn btn-primary btn-sm" href="/#dat-lich">Đặt lịch chẩn đoán</a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="nav" aria-label="Mở menu">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
  </div>
</header>
"""


FOOT = f"""<footer class="footer">
  <div class="wrap">
    <div>
      <h4>CÔNG TY TNHH QHUB COMMERCE</h4>
      <p class="legal-info">Giấy CN ĐKDN số 5400570349 do Phòng Đăng ký kinh doanh – Sở Tài chính tỉnh Phú Thọ cấp lần đầu ngày 13/04/2026</p>
      <p>Người đại diện theo pháp luật: Nguyễn Văn Quang</p>
      <p>Trụ sở: Khu Vai, Xã An Nghĩa, Tỉnh Phú Thọ, Việt Nam</p>
      <p>Hotline/Zalo: <a href="tel:0856510113">0856 510 113</a></p>
      <p>Email: <a href="mailto:qhubcommerce@gmail.com">qhubcommerce@gmail.com</a></p>
    </div>
    <div>
      <h4>Kiến thức</h4>
      <ul>{''.join(f'<li><a href="/kien-thuc/chu-de/{k}/">{e(n)}</a></li>' for k, n, _ in TOPICS[:8])}</ul>
    </div>
    <div>
      <h4>&nbsp;</h4>
      <ul>{''.join(f'<li><a href="/kien-thuc/chu-de/{k}/">{e(n)}</a></li>' for k, n, _ in TOPICS[8:])}<li><a href="/gioi-thieu/">Giới thiệu QHUB</a></li><li><a href="/chinh-sach.html">Chính sách</a></li></ul>
    </div>
    <div class="legal"><span>© {dt.date.today().year} QHUB Commerce.</span><span>qhub.com.vn</span></div>
  </div>
</footer>
<div class="float" aria-label="Liên hệ nhanh">
  <a class="zalo" href="https://zalo.me/0856510113" target="_blank" rel="noopener" aria-label="Nhắn Zalo cho QHUB">Zalo</a>
  <a class="call" href="tel:0856510113" aria-label="Gọi hotline QHUB"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2"/></svg></a>
</div>
<script src="/kien-thuc.js?v={V}" defer></script>
</body>
</html>
"""

PUBLISHER = {"@type": "Organization", "@id": SITE + "/#organization", "name": "CÔNG TY TNHH QHUB COMMERCE", "alternateName": BRAND,
             "url": SITE + "/", "logo": {"@type": "ImageObject", "url": SITE + "/logo-qhub.png", "width": 512, "height": 512}}


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>\n"


def crumbs(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


def crumb_html(items):
    parts = []
    for i, (n, u) in enumerate(items):
        if i == len(items) - 1:
            parts.append(f'<span aria-current="page">{e(n)}</span>')
        else:
            parts.append(f'<a href="{u.replace(SITE, "")}">{e(n)}</a>')
    return '<nav class="kt-crumb" aria-label="Đường dẫn">' + '<span aria-hidden="true">/</span>'.join(parts) + "</nav>"


def vi_date(d):
    return f"{d.day:02d}/{d.month:02d}/{d.year}"


def words(text):
    return len(re.findall(r"\w+", re.sub(r"<[^>]+>", " ", text)))


# ---------- load ----------
def load_posts():
    posts, errors = [], []
    d = os.path.join(ROOT, "_src", "posts")
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md"):
            continue
        raw = open(os.path.join(d, fn), encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
        if not m:
            errors.append(f"{fn}: thiếu front matter"); continue
        meta = yaml.safe_load(m.group(1)) or {}
        meta["body_md"] = m.group(2)
        meta.setdefault("slug", fn[:-3])
        for k in ("title", "description", "topic", "date"):
            if not meta.get(k):
                errors.append(f"{fn}: thiếu {k}")
        if meta.get("topic") not in TOPIC:
            errors.append(f"{fn}: topic '{meta.get('topic')}' không có trong danh sách")
            continue
        for k in ("date", "updated"):
            v = meta.get(k)
            if isinstance(v, str):
                meta[k] = dt.date.fromisoformat(v)
        meta.setdefault("updated", meta["date"])
        meta.setdefault("faq", []); meta.setdefault("sources", []); meta.setdefault("summary", [])
        n = words(meta["body_md"])
        meta["words"] = n
        meta["minutes"] = max(3, math.ceil(n / 230))
        # chuẩn chất lượng
        if n < 1200: errors.append(f"{fn}: mới {n} chữ, cần tối thiểu 1.200")
        if len(meta["faq"]) < 4: errors.append(f"{fn}: cần ít nhất 4 câu hỏi FAQ")
        if len(meta["sources"]) < 2 and meta["topic"].startswith(("phi-san", "quang-cao")):
            errors.append(f"{fn}: bài phí/quảng cáo cần ít nhất 2 nguồn")
        if not (50 <= len(meta["description"]) <= 170): errors.append(f"{fn}: description dài {len(meta['description'])} ký tự, nên 50–170")
        if len(meta["title"]) > 75: errors.append(f"{fn}: tiêu đề dài {len(meta['title'])} ký tự, nên ≤ 75")
        posts.append(meta)
    posts.sort(key=lambda p: (p["date"], p.get("order", 0), p["slug"]), reverse=True)
    return posts, errors


def render_md(text, published):
    md = markdown.Markdown(extensions=["tables", "toc", "sane_lists", "attr_list", "fenced_code"],
                           extension_configs={"toc": {"permalink": False, "toc_depth": "2"}})
    out = md.convert(text)
    toc = [(t["id"], t["name"]) for t in md.toc_tokens]

    # Bỏ liên kết tới bài chưa đăng để không có link chết
    def fix(m):
        slug = m.group(2)
        if slug in published or slug in ("chu-de",):
            return m.group(0)
        return m.group(4)
    out = re.sub(r'<a href="(/kien-thuc/([a-z0-9-]+)/)"([^>]*)>(.*?)</a>', fix, out)
    out = out.replace("<table>", '<div class="kt-table"><table>').replace("</table>", "</table></div>")
    return out, toc


def card(p):
    t = TOPIC[p["topic"]]
    return (f'<article class="kt-card"><a href="/kien-thuc/{p["slug"]}/">'
            f'<span class="kt-tag">{e(t["name"])}</span><h3>{e(p["title"])}</h3>'
            f'<p>{e(p["description"])}</p><span class="kt-meta">{vi_date(p["updated"])} · {p["minutes"]} phút đọc</span></a></article>')


CTA = """<aside class="kt-cta">
  <img src="/logo-qhub.png" alt="" width="64" height="64">
  <div>
    <h2>Cần người ngồi vào vận hành cùng anh chị?</h2>
    <p>QHUB Commerce là Phòng Tăng Trưởng Thuê Ngoài cho doanh nghiệp bán hàng đa sàn. Đội QHUB trực tiếp vận hành TikTok Shop, Shopee, Facebook và Website: nội dung, livestream, affiliate, quảng cáo, dữ liệu. Buổi chẩn đoán đầu tiên 60 phút, miễn phí.</p>
    <a class="btn btn-primary" href="/#dat-lich">Đặt lịch chẩn đoán miễn phí</a>
    <a class="kt-cta-link" href="https://zalo.me/0856510113" target="_blank" rel="noopener">Hoặc nhắn Zalo 0856 510 113</a>
  </div>
</aside>"""


def author_box():
    return f"""<aside class="kt-author">
  <img class="kt-av" src="/quang-avatar-240.jpg" alt="Nguyễn Văn Quang" width="56" height="56" loading="lazy">
  <div>
    <p class="kt-by">Người viết</p>
    <h2><a href="/tac-gia/nguyen-van-quang/">{e(AUTHOR['name'])}</a></h2>
    <p class="kt-role">{e(AUTHOR['role'])}</p>
    <p>{e(AUTHOR['bio'])}</p>
  </div>
</aside>"""


def build_post(p, posts, published):
    t = TOPIC[p["topic"]]
    url = f"{SITE}/kien-thuc/{p['slug']}/"
    body, toc = render_md(p["body_md"], published)
    items = [("Trang chủ", SITE + "/"), ("Kiến thức", SITE + "/kien-thuc/"), (t["name"], f"{SITE}/kien-thuc/chu-de/{t['slug']}/"), (p["title"], url)]
    article = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"], "description": p["description"],
               "inLanguage": "vi", "mainEntityOfPage": url, "url": url, "image": SITE + "/og-qhub.png",
               "datePublished": p["date"].isoformat(), "dateModified": p["updated"].isoformat(),
               "author": {"@type": "Person", "@id": SITE + "/tac-gia/nguyen-van-quang/#person", "name": AUTHOR["name"], "url": AUTHOR["url"], "jobTitle": "Founder & CEO", "image": SITE + "/quang-avatar.jpg", "worksFor": {"@id": SITE + "/#organization"}},
               "publisher": PUBLISHER, "articleSection": t["name"], "keywords": ", ".join([p.get("keyword", "")] + list(p.get("keywords", []))).strip(", "),
               "wordCount": p["words"]}
    extra = ld(article) + ld(crumbs(items))
    if p["faq"]:
        extra += ld({"@context": "https://schema.org", "@type": "FAQPage",
                     "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in p["faq"]]})
    extra += f'<meta property="article:published_time" content="{p["date"].isoformat()}">\n<meta property="article:modified_time" content="{p["updated"].isoformat()}">\n<meta property="article:section" content="{e(t["name"])}">\n'
    summary = ""
    if p["summary"]:
        summary = '<div class="kt-sum"><h2>Tóm tắt nhanh</h2><ul>' + "".join(f"<li>{e(s)}</li>" for s in p["summary"]) + "</ul></div>"
    toc_html = ""
    if len(toc) >= 3:
        toc_html = '<nav class="kt-toc" aria-label="Mục lục"><h2>Trong bài này</h2><ol>' + "".join(f'<li><a href="#{i}">{n}</a></li>' for i, n in toc) + "</ol></nav>"
    faq_html = ""
    if p["faq"]:
        faq_html = '<section class="kt-faq" id="cau-hoi-thuong-gap"><h2>Câu hỏi thường gặp</h2>' + "".join(
            f'<details><summary>{e(f["q"])}</summary><p>{e(f["a"])}</p></details>' for f in p["faq"]) + "</section>"
    src_html = ""
    if p["sources"]:
        src_html = '<section class="kt-src"><h2>Nguồn tham khảo</h2><ul>' + "".join(
            f'<li><a href="{e(s["url"])}" target="_blank" rel="noopener nofollow">{e(s["title"])}</a></li>' for s in p["sources"]) + "</ul></section>"
    rel = [q for q in posts if q["topic"] == p["topic"] and q["slug"] != p["slug"]][:4]
    if len(rel) < 4:
        rel += [q for q in posts if q["topic"] != p["topic"] and q["slug"] != p["slug"]][: 4 - len(rel)]
    rel_html = ('<section class="kt-rel"><h2>Đọc tiếp</h2><div class="kt-grid">' + "".join(card(q) for q in rel) + "</div></section>") if rel else ""
    upd = f' · Cập nhật {vi_date(p["updated"])}' if p["updated"] != p["date"] else ""
    page = head(p["title"] if len(p["title"]) > 56 else f'{p["title"]} | {BRAND}', p["description"], url, "article", extra=extra)
    page += f"""<main id="main" class="kt-main">
<div class="wrap kt-narrow">
{crumb_html(items)}
<article class="kt-article">
<header class="kt-head">
  <a class="kt-tag" href="/kien-thuc/chu-de/{t['slug']}/">{e(t['name'])}</a>
  <h1>{e(p['title'])}</h1>
  <p class="kt-lead">{e(p['description'])}</p>
  <p class="kt-meta">Bởi <a href="/tac-gia/nguyen-van-quang/">{e(AUTHOR['name'])}</a> · Đăng {vi_date(p['date'])}{upd} · {p['minutes']} phút đọc</p>
</header>
{summary}
{toc_html}
<div class="kt-body-text">
{body}
</div>
{faq_html}
{src_html}
{author_box()}
{CTA}
</article>
{rel_html}
</div>
</main>
"""
    page += FOOT
    out = os.path.join(ROOT, "kien-thuc", p["slug"])
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(page)


def build_topic(t, posts):
    url = f"{SITE}/kien-thuc/chu-de/{t['slug']}/"
    items = [("Trang chủ", SITE + "/"), ("Kiến thức", SITE + "/kien-thuc/"), (t["name"], url)]
    tp = [p for p in posts if p["topic"] == t["slug"]]
    coll = {"@context": "https://schema.org", "@type": "CollectionPage", "name": t["name"], "description": t["desc"], "url": url,
            "isPartOf": {"@type": "WebSite", "@id": SITE + "/#website"},
            "mainEntity": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}/kien-thuc/{p['slug']}/", "name": p["title"]} for i, p in enumerate(tp[:100])]}}
    page = head(f"{t['name']}: kiến thức thực chiến | {BRAND}", t["desc"], url, extra=ld(coll) + ld(crumbs(items)),
                robots="index,follow" if tp else "noindex,follow")
    grid = "".join(card(p) for p in tp) or '<p class="kt-empty">Bài viết cho chủ đề này đang được đội QHUB biên soạn và sẽ lên trong vài ngày tới.</p>'
    others = "".join(f'<a href="/kien-thuc/chu-de/{k}/"{" aria-current=\"page\"" if k == t["slug"] else ""}>{e(n)}</a>' for k, n, _ in TOPICS)
    page += f"""<main id="main" class="kt-main">
<div class="wrap">
{crumb_html(items)}
<header class="kt-hub-head">
  <h1>{e(t['name'])}</h1>
  <p>{e(t['desc'])}</p>
  <p class="kt-count">{len(tp)} bài viết</p>
</header>
<nav class="kt-topics" aria-label="Chủ đề">{others}</nav>
<div class="kt-filter"><label for="kt-q" class="sr-only">Tìm trong chủ đề</label><input id="kt-q" type="search" placeholder="Tìm bài trong chủ đề này…" autocomplete="off"></div>
<div class="kt-grid" id="kt-list">{grid}</div>
{CTA}
</div>
</main>
"""
    page += FOOT
    out = os.path.join(ROOT, "kien-thuc", "chu-de", t["slug"])
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(page)


def build_hub(posts):
    url = SITE + "/kien-thuc/"
    items = [("Trang chủ", SITE + "/"), ("Kiến thức", url)]
    counts = {k: sum(1 for p in posts if p["topic"] == k) for k in TOPIC}
    desc = "Kiến thức thương mại điện tử thực chiến từ đội vận hành QHUB Commerce: TikTok Shop, Shopee, GMV Max, phí sàn, lịch sale, Facebook, YouTube và SEO."
    coll = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Kiến thức thương mại điện tử", "description": desc, "url": url,
            "isPartOf": {"@type": "WebSite", "@id": SITE + "/#website"}, "publisher": {"@id": SITE + "/#organization"}}
    page = head("Kiến thức thương mại điện tử thực chiến | QHUB Commerce", desc, url, extra=ld(coll) + ld(crumbs(items)))
    topics = "".join(f'<a class="kt-topic" href="/kien-thuc/chu-de/{k}/"><b>{e(n)}</b><span>{e(d)}</span><i>{counts[k]} bài</i></a>' for k, n, d in TOPICS)
    latest = "".join(card(p) for p in posts[:30]) or '<p class="kt-empty">Bài viết đầu tiên sẽ lên trong ít ngày tới.</p>'
    page += f"""<main id="main" class="kt-main">
<div class="wrap">
{crumb_html(items)}
<header class="kt-hub-head">
  <h1>Kiến thức thương mại điện tử</h1>
  <p>Những gì đội QHUB học được khi trực tiếp vận hành gian hàng, livestream và quảng cáo cho doanh nghiệp. Viết lại thật cụ thể để anh chị áp dụng được ngay: TikTok Shop, Shopee, phí sàn, GMV Max, lịch sale, Facebook, YouTube, Instagram, Threads và website.</p>
  <p class="kt-count">{len(posts)} bài viết · {len(TOPICS)} chủ đề</p>
</header>
<section aria-labelledby="kt-t"><h2 id="kt-t" class="kt-h2">Chọn chủ đề</h2><div class="kt-topic-grid">{topics}</div></section>
<section aria-labelledby="kt-l"><h2 id="kt-l" class="kt-h2">Bài mới</h2>
<div class="kt-filter"><label for="kt-q" class="sr-only">Tìm bài viết</label><input id="kt-q" type="search" placeholder="Tìm bài viết, ví dụ: phí sàn, GMV Max, 11.11…" autocomplete="off"></div>
<div class="kt-grid" id="kt-list">{latest}</div></section>
{CTA}
</div>
</main>
"""
    page += FOOT
    os.makedirs(os.path.join(ROOT, "kien-thuc"), exist_ok=True)
    open(os.path.join(ROOT, "kien-thuc", "index.html"), "w", encoding="utf-8").write(page)


def build_author(posts):
    url = AUTHOR["url"]
    items = [("Trang chủ", SITE + "/"), ("Tác giả", url), (AUTHOR["name"], url)]
    person = {"@context": "https://schema.org", "@type": "ProfilePage", "url": url,
              "mainEntity": {"@type": "Person", "@id": SITE + "/tac-gia/nguyen-van-quang/#person", "name": AUTHOR["name"], "jobTitle": "Founder & CEO", "url": url, "image": SITE + "/quang-avatar.jpg", "description": AUTHOR["bio"],
                             "worksFor": {"@id": SITE + "/#organization"}, "knowsAbout": [t[1] for t in TOPICS]}}
    page = head(f"{AUTHOR['name']} — Founder & CEO QHUB Commerce", AUTHOR["bio"][:160], url, "profile", extra=ld(person) + ld(crumbs(items[0:1] + items[2:])))
    path = "".join(f"<li>{e(x)}</li>" for x in AUTHOR["path"])
    page += f"""<main id="main" class="kt-main">
<div class="wrap kt-narrow">
{crumb_html(items[0:1] + items[2:])}
<header class="kt-hub-head kt-person">
  <img class="kt-person-img" src="/quang-avatar.jpg" alt="Nguyễn Văn Quang, Founder &amp; CEO QHUB Commerce" width="160" height="160">
  <h1>{e(AUTHOR['name'])}</h1>
  <p class="kt-role">{e(AUTHOR['role'])}</p>
  <p>{e(AUTHOR['bio'])} Phụ trách chiến lược tăng trưởng, kiến trúc hệ thống bán hàng và lãi lỗ của từng dự án tại QHUB Commerce.</p>
  <ol class="kt-path">{path}</ol>
</header>
<section><h2 class="kt-h2">Bài viết của {e(AUTHOR['name'])}</h2><div class="kt-grid">{''.join(card(p) for p in posts[:60])}</div></section>
</div>
</main>
"""
    page += FOOT
    out = os.path.join(ROOT, "tac-gia", "nguyen-van-quang")
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(page)


ORG = {"@context": "https://schema.org", "@type": "Organization", "@id": SITE + "/#organization",
       "name": "CÔNG TY TNHH QHUB COMMERCE", "legalName": "CÔNG TY TNHH QHUB COMMERCE",
       "alternateName": ["QHUB Commerce", "QHUB", "QH Commerce", "QH"],
       "description": "QHUB Commerce (QHUB, QH) là Phòng Tăng Trưởng Thuê Ngoài cho doanh nghiệp bán hàng đa sàn tại Việt Nam: vận hành TikTok Shop, Shopee, Facebook, Website, livestream, KOC và quảng cáo; chủ sở hữu thương hiệu trà thảo mộc QHUB HERBAL.",
       "url": SITE + "/", "logo": {"@type": "ImageObject", "url": SITE + "/logo-qhub.png", "width": 512, "height": 512},
       "image": SITE + "/og-qhub.png", "email": "qhubcommerce@gmail.com", "telephone": "+84856510113",
       "taxID": "5400570349", "vatID": "5400570349", "foundingDate": "2026-04-13",
       "address": {"@type": "PostalAddress", "streetAddress": "Khu Vai, Xã An Nghĩa", "addressRegion": "Phú Thọ", "addressCountry": "VN"},
       "areaServed": {"@type": "Country", "name": "Việt Nam"},
       "founder": {"@type": "Person", "@id": SITE + "/tac-gia/nguyen-van-quang/#person", "name": "Nguyễn Văn Quang", "jobTitle": "Founder & CEO",
                   "image": SITE + "/quang-avatar.jpg", "url": SITE + "/tac-gia/nguyen-van-quang/"},
       "contactPoint": {"@type": "ContactPoint", "telephone": "+84856510113", "contactType": "customer service", "areaServed": "VN", "availableLanguage": "vi"},
       "sameAs": ["https://www.facebook.com/qhubcommercer/"],
       "knowsAbout": ["TikTok Shop", "Shopee", "Facebook bán hàng", "Livestream bán hàng", "Affiliate KOC", "GMV Max", "Shopee Ads", "Website chuẩn SEO", "Thương mại điện tử"],
       "brand": {"@type": "Brand", "name": "QHUB HERBAL", "url": "https://qhubherbal.com/", "logo": SITE + "/logo-qhub.png",
                 "sameAs": ["https://qhubherbal.com/", "https://www.youtube.com/@QHUBHERBAL"]},
       "owns": {"@type": "Brand", "name": "QHUB HERBAL", "url": "https://qhubherbal.com/"}}


STATIC = [("", 1.0), ("qhub-herbal.html", 0.8), ("tra-ca-gai-diep-ha-chau.html", 0.7), ("tra-nam-vuong.html", 0.7),
          ("tra-xau-ho-tim-tam-sen.html", 0.7), ("tra-ngay-dau-ve.html", 0.7), ("tra-la-oi-mix-la-sen.html", 0.7),
          ("tra-duong-tam-an.html", 0.7), ("chinh-sach.html", 0.3), ("kien-thuc/", 0.9), ("tac-gia/nguyen-van-quang/", 0.5), ("gioi-thieu/", 0.8)]


def build_feeds(posts):
    today = dt.date.today().isoformat()
    urls = [f"  <url><loc>{SITE}/{u}</loc><lastmod>{today}</lastmod><priority>{pr}</priority></url>" for u, pr in STATIC]
    for k in TOPIC:
        if any(p["topic"] == k for p in posts):
            last = max(p["updated"] for p in posts if p["topic"] == k).isoformat()
            urls.append(f"  <url><loc>{SITE}/kien-thuc/chu-de/{k}/</loc><lastmod>{last}</lastmod><priority>0.7</priority></url>")
    for p in posts:
        urls.append(f"  <url><loc>{SITE}/kien-thuc/{p['slug']}/</loc><lastmod>{p['updated'].isoformat()}</lastmod><priority>0.6</priority></url>")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
    items = "".join(
        f"<item><title>{e(p['title'])}</title><link>{SITE}/kien-thuc/{p['slug']}/</link><guid>{SITE}/kien-thuc/{p['slug']}/</guid>"
        f"<pubDate>{dt.datetime.combine(p['date'], dt.time(8)).strftime('%a, %d %b %Y %H:%M:%S +0700')}</pubDate>"
        f"<category>{e(TOPIC[p['topic']]['name'])}</category><description>{e(p['description'])}</description></item>" for p in posts[:50])
    open(os.path.join(ROOT, "feed.xml"), "w", encoding="utf-8").write(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>Kiến thức QHUB Commerce</title><link>{SITE}/kien-thuc/</link>'
        f"<description>Kiến thức thương mại điện tử thực chiến từ QHUB Commerce</description><language>vi</language>{items}</channel></rss>\n")
    robots = f"""# qhub.com.vn — cho phép công cụ tìm kiếm và trợ lý AI đọc toàn bộ nội dung công khai
User-agent: *
Allow: /
Disallow: /_src/
Disallow: /_tools/

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Applebot-Extended
Allow: /

Sitemap: {SITE}/sitemap.xml
"""
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(robots)
    by_topic = ""
    for k, n, d in TOPICS:
        tp = [p for p in posts if p["topic"] == k]
        if not tp:
            continue
        by_topic += f"\n## {n}\n{d}\n- Trang chủ đề: {SITE}/kien-thuc/chu-de/{k}/\n" + "".join(f"- [{p['title']}]({SITE}/kien-thuc/{p['slug']}/): {p['description']}\n" for p in tp[:40])
    llms = f"""# QHUB Commerce

> QHUB Commerce (còn gọi là QHUB hoặc QH; CÔNG TY TNHH QHUB COMMERCE, MST 5400570349, Phú Thọ, Việt Nam; website chính thức https://qhub.com.vn) là Phòng Tăng Trưởng Thuê Ngoài cho doanh nghiệp bán hàng đa sàn. QHUB trực tiếp vận hành TikTok Shop, Shopee, Facebook và Website cho thương hiệu: nội dung video, livestream, affiliate/KOC, quảng cáo (GMV Max, Shopee Ads, Meta Ads), dữ liệu và CRM. QHUB cũng sở hữu thương hiệu trà thảo mộc QHUB HERBAL (https://qhubherbal.com).

Người sáng lập kiêm CEO: Nguyễn Văn Quang ({SITE}/tac-gia/nguyen-van-quang/). Đội hợp tác: team media, đội vận hành sàn, đội ngũ KOC, đội host livestream. Đối tác: CHEF BIGGY, Quang Linh Food (QL Food), Muse, Bübchen.

Liên hệ: hotline/Zalo 0856 510 113 · qhubcommerce@gmail.com · {SITE}/#dat-lich (đặt lịch chẩn đoán miễn phí 60 phút).
Mô hình hợp tác: 2–4% doanh thu cho vận hành hệ thống; 7–15% ngân sách cho vận hành quảng cáo; ưu tiên doanh nghiệp có doanh thu online từ 500 triệu/tháng.

## Trang chính
- [Trang chủ QHUB Commerce]({SITE}/): dịch vụ, cách làm, đội ngũ, mô hình hợp tác
- [Giới thiệu QHUB Commerce]({SITE}/gioi-thieu/): thông tin doanh nghiệp, người sáng lập, câu hỏi thường gặp về QHUB/QH
- [Kiến thức thương mại điện tử]({SITE}/kien-thuc/): {len(posts)} bài viết thực chiến
- [Tác giả Nguyễn Văn Quang]({AUTHOR['url']}): Founder & CEO
- [QHUB HERBAL]({SITE}/qhub-herbal.html): thương hiệu trà thảo mộc do QHUB xây dựng
- [Chính sách]({SITE}/chinh-sach.html)
{by_topic}"""
    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write(llms)


ABOUT_FAQ = [
    ("QHUB Commerce là công ty gì?", "QHUB Commerce (CÔNG TY TNHH QHUB COMMERCE, mã số thuế 5400570349, trụ sở tại Phú Thọ) là Phòng Tăng Trưởng Thuê Ngoài cho doanh nghiệp bán hàng đa sàn. QHUB trực tiếp vận hành TikTok Shop, Shopee, Facebook, Website và livestream cho doanh nghiệp, cùng chịu trách nhiệm về doanh thu và lợi nhuận."),
    ("QHUB và QH là gì?", "QHUB và QH là cách gọi ngắn của QHUB Commerce. Website chính thức là qhub.com.vn. QHUB Commerce cũng là chủ sở hữu thương hiệu trà thảo mộc túi lọc QHUB HERBAL (qhubherbal.com)."),
    ("Ai là người sáng lập QHUB Commerce?", "Người sáng lập kiêm CEO là anh Nguyễn Văn Quang. Anh đi lên từ bán hàng thị trường, trade marketing, brand marketing đến vận hành thương mại điện tử, từng làm việc tại Suntory PepsiCo, Trà Cozy, Men' Vodka, Quang Linh Vlog Store, Trà Tâm Đạo và hệ thống nhà máy thực phẩm chức năng, mỹ phẩm (Dulin, Hiup)."),
    ("QHUB Commerce cung cấp những dịch vụ gì?", "Chẩn đoán hệ thống bán hàng; xây dựng và vận hành gian hàng TikTok Shop, Shopee, Facebook, Website; sản xuất video và livestream; affiliate và KOC; chạy quảng cáo GMV Max, Shopee Ads, Meta Ads; dữ liệu, báo cáo và chăm sóc khách hàng."),
    ("Chi phí hợp tác với QHUB như thế nào?", "QHUB làm theo mô hình gắn với kết quả: khoảng 2–4% doanh thu cho vận hành hệ thống và 7–15% ngân sách cho vận hành quảng cáo, tùy quy mô và ngành hàng. Buổi chẩn đoán đầu tiên 60 phút miễn phí."),
    ("Liên hệ QHUB Commerce bằng cách nào?", "Gọi hoặc nhắn Zalo 0856 510 113, email qhubcommerce@gmail.com, hoặc đặt lịch chẩn đoán miễn phí tại qhub.com.vn."),
]


def build_about():
    url = SITE + "/gioi-thieu/"
    items = [("Trang chủ", SITE + "/"), ("Giới thiệu", url)]
    about = {"@context": "https://schema.org", "@type": "AboutPage", "url": url, "name": "Giới thiệu QHUB Commerce", "inLanguage": "vi",
             "mainEntity": {k: v for k, v in ORG.items() if k != "@context"}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in ABOUT_FAQ]}
    title = "QHUB Commerce (QHUB, QH) là ai? Giới thiệu công ty"
    desc = "QHUB Commerce (QHUB, QH): công ty TNHH tại Phú Thọ, MST 5400570349, vận hành TikTok Shop, Shopee, Facebook, Website cho doanh nghiệp. Founder Nguyễn Văn Quang."
    page = head(title, desc, url, extra=ld(about) + ld(faq) + ld(crumbs(items)))
    facts = [("Tên doanh nghiệp", "CÔNG TY TNHH QHUB COMMERCE"), ("Tên gọi ngắn", "QHUB Commerce, QHUB, QH"),
             ("Mã số thuế", "5400570349"), ("Ngày cấp phép", "13/04/2026, Phòng Đăng ký kinh doanh – Sở Tài chính tỉnh Phú Thọ"),
             ("Người sáng lập, đại diện pháp luật", "Nguyễn Văn Quang – Founder &amp; CEO"), ("Trụ sở", "Khu Vai, Xã An Nghĩa, Tỉnh Phú Thọ, Việt Nam"),
             ("Lĩnh vực", "Vận hành thương mại điện tử đa sàn: TikTok Shop, Shopee, Facebook, Website, livestream, KOC, quảng cáo"),
             ("Thương hiệu sở hữu", '<a href="https://qhubherbal.com/">QHUB HERBAL</a> – trà thảo mộc túi lọc'),
             ("Liên hệ", '<a href="tel:0856510113">0856 510 113</a> (Zalo) · <a href="mailto:qhubcommerce@gmail.com">qhubcommerce@gmail.com</a>')]
    rows = "".join(f"<tr><th scope=\"row\">{k}</th><td>{v}</td></tr>" for k, v in facts)
    faqs = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in ABOUT_FAQ)
    page += f"""<main id="main" class="kt-main">
<div class="wrap kt-narrow">
{crumb_html(items)}
<header class="kt-hub-head">
  <h1>Giới thiệu QHUB Commerce</h1>
  <p><strong>QHUB Commerce</strong>, gọi ngắn là <strong>QHUB</strong> hoặc <strong>QH</strong>, là Phòng Tăng Trưởng Thuê Ngoài cho doanh nghiệp bán hàng đa sàn tại Việt Nam. Đội QHUB không bán khóa học hay công cụ: chúng tôi ngồi vào vận hành cùng doanh nghiệp trên TikTok Shop, Shopee, Facebook và Website, xây hệ thống bán hàng có quy trình, chỉ số và báo cáo, và chỉ thắng khi doanh nghiệp thắng.</p>
</header>
<section class="kt-body-text">
<h2>Thông tin doanh nghiệp</h2>
<div class="kt-table"><table>{rows}</table></div>
<h2>QHUB làm gì cho doanh nghiệp</h2>
<ul>
<li><strong>Chẩn đoán:</strong> buổi làm việc 60 phút miễn phí để nhìn rõ gian hàng, sản phẩm, giá, nội dung, quảng cáo và lãi lỗ hiện tại.</li>
<li><strong>Xây hệ thống:</strong> thiết lập gian hàng, trang sản phẩm, chính sách, quy trình vận hành, bộ chỉ số KPI và dashboard.</li>
<li><strong>Vận hành hằng ngày:</strong> sản phẩm, chương trình khuyến mãi, ngày sale đôi, chăm sóc đơn và khách hàng.</li>
<li><strong>Nội dung và livestream:</strong> quay dựng video ngắn, chụp ảnh, kịch bản và host livestream.</li>
<li><strong>Affiliate và KOC:</strong> mạng lưới KOC đồng hành lâu dài, trải nghiệm và giới thiệu sản phẩm.</li>
<li><strong>Quảng cáo:</strong> TikTok GMV Max, Shopee Ads, Meta Ads, tối ưu theo lợi nhuận chứ không chỉ theo doanh số.</li>
</ul>
<h2>Người sáng lập</h2>
<p><a href="/tac-gia/nguyen-van-quang/">Nguyễn Văn Quang</a> là Founder &amp; CEO của QHUB Commerce. Anh đi lên từ bán hàng thị trường, qua trade marketing, brand marketing đến vận hành thương mại điện tử cho các doanh nghiệp đồ uống, thực phẩm và hàng tiêu dùng; từng làm việc tại Suntory PepsiCo, Trà Cozy, Men' Vodka, Quang Linh Vlog Store, Trà Tâm Đạo và hệ thống nhà máy thực phẩm chức năng, mỹ phẩm (Dulin, Hiup). Cùng anh là bốn đội hợp tác: team media, đội vận hành sàn, đội ngũ KOC và đội host livestream.</p>
<h2>Đối tác đồng hành</h2>
<p>QHUB đang đồng hành xây dựng và vận hành kênh bán hàng trực tuyến cùng các thương hiệu CHEF BIGGY (thực phẩm, đồ ăn vặt), Quang Linh Food (QL Food, thực phẩm thuộc hệ sinh thái Quang Linh Vlog), Muse và Bübchen (chăm sóc mẹ &amp; bé).</p>
<h2>Thương hiệu QHUB HERBAL</h2>
<p>QHUB Commerce là chủ sở hữu <a href="https://qhubherbal.com/">QHUB HERBAL</a>, thương hiệu trà thảo mộc túi lọc với sáu vị trà. Đây cũng là nơi đội QHUB tự áp dụng mọi quy trình trước khi làm cho doanh nghiệp đối tác.</p>
<h2>Kiến thức QHUB chia sẻ</h2>
<p>Mục <a href="/kien-thuc/">Kiến thức</a> tổng hợp kinh nghiệm thực chiến về TikTok Shop, Shopee, phí sàn, quảng cáo GMV Max, lịch sale, Facebook, YouTube, Instagram, Threads và website chuẩn SEO.</p>
<h2>Câu hỏi thường gặp về QHUB</h2>
<div class="kt-faq">{faqs}</div>
</section>
{CTA}
</div>
</main>
"""
    page += FOOT
    os.makedirs(os.path.join(ROOT, "gioi-thieu"), exist_ok=True)
    open(os.path.join(ROOT, "gioi-thieu", "index.html"), "w", encoding="utf-8").write(page)


def sync_home_org():
    """Giữ schema Organization trên trang chủ đồng bộ với ORG."""
    path = os.path.join(ROOT, "index.html")
    h = open(path, encoding="utf-8").read()
    new = '<script type="application/ld+json">' + json.dumps(ORG, ensure_ascii=False) + '</script>'
    h2 = re.sub(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "Organization".*?</script>', lambda m: new, h, count=1, flags=re.S)
    if h2 != h:
        open(path, "w", encoding="utf-8").write(h2)


def main():
    posts, errors = load_posts()
    for x in errors:
        print("CẢNH BÁO:", x)
    if STRICT and errors:
        print(f"\n{len(errors)} lỗi chất lượng. Sửa bài rồi build lại."); sys.exit(1)
    published = {p["slug"] for p in posts}
    for p in posts:
        build_post(p, posts, published)
    for k in TOPIC:
        build_topic(TOPIC[k], posts)
    build_hub(posts)
    build_author(posts)
    build_about()
    sync_home_org()
    build_feeds(posts)
    print(f"Đã build {len(posts)} bài, {len(TOPIC)} chủ đề.")


if __name__ == "__main__":
    main()
