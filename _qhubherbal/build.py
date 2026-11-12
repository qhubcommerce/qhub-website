# -*- coding: utf-8 -*-
"""Build website tĩnh qhubherbal.com từ data.py + templates/ -> dist/
   Chạy: python3 build.py
   Thêm sản phẩm: thêm 1 mục vào PRODUCTS trong data.py + ảnh site/assets/img/products/<slug>.webp và <slug>-3d.webp
   (+ tùy chọn ảnh thư viện site/assets/img/gallery/<slug>/*.webp, ảnh nguyên liệu site/assets/img/ing/<key>.webp)."""
import os, json, shutil, datetime, glob
from jinja2 import Environment, FileSystemLoader
import data
vnd_s = lambda n: f"{n:,}".replace(',', '.')

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'site'); OUT = os.path.join(ROOT, 'dist')
FORM = json.load(open(os.path.join(ROOT, 'form_config.json'), encoding='utf-8'))
NOW = datetime.datetime.now()
VERSION = NOW.strftime('%Y%m%d%H%M%S')
site = data.SITE
products = data.PRODUCTS
bys = {p['slug']: p for p in products}
cats = []
for p in products:
    if p['cat'] not in cats: cats.append(p['cat'])
    GAL = [('thanh-phan','Thành phần thảo mộc'),('ly-do','Lý do nên chọn'),('dong-y','Công dụng theo quan niệm phương Đông'),('cach-pha','Cách pha'),('trong-hop','Trong mỗi hộp có gì'),('thong-tin-hop','Thông tin trên hộp'),('hoi-dap','Hỏi đáp nhanh')]
    p['gallery'] = [(f"{site['media']}/gallery/{p['slug']}-{k}.webp" + ("?v=2" if k == 'thong-tin-hop' else ''), f"{p['name']} – {t}") for k,t in GAL if os.path.exists(os.path.join(ROOT,'media/gallery',f"{p['slug']}-{k}.webp"))]
    for k in ('ings',):
        for ing in p[k]:
            assert os.path.exists(os.path.join(SRC, 'assets/img/ing', ing[0] + '.webp')), ing[0]
    for suf in ('', '-3d'):
        assert os.path.exists(os.path.join(SRC, 'assets/img/products', p['slug'] + suf + '.webp')), p['slug'] + suf

env = Environment(loader=FileSystemLoader(os.path.join(ROOT, 'templates')), autoescape=True, trim_blocks=True, lstrip_blocks=True)
SHIP_LD = {"@type": "OfferShippingDetails", "shippingRate": {"@type": "MonetaryAmount", "value": 0, "currency": "VND"},
    "shippingDestination": {"@type": "DefinedRegion", "addressCountry": "VN"},
    "deliveryTime": {"@type": "ShippingDeliveryTime",
        "handlingTime": {"@type": "QuantitativeValue", "minValue": site['ship_handling'][0], "maxValue": site['ship_handling'][1], "unitCode": "DAY"},
        "transitTime": {"@type": "QuantitativeValue", "minValue": site['ship_transit'][0], "maxValue": site['ship_transit'][1], "unitCode": "DAY"}}}
RETURN_LD = {"@type": "MerchantReturnPolicy", "applicableCountry": "VN", "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
    "merchantReturnDays": site['return_days'], "returnMethod": "https://schema.org/ReturnByMail",
    "returnFees": "https://schema.org/ReturnFeesCustomerResponsibility", "merchantReturnLink": site['domain'] + "/chinh-sach-doi-tra/"}
org_ld = json.dumps({
    "@context": "https://schema.org", "@type": "Organization", "name": "QHUB HERBAL",
    "legalName": site['company'], "url": site['domain'], "logo": site['domain'] + "/assets/img/logo-forest.png",
    "email": site['email'], "telephone": "+84" + site['hotline_raw'][1:],
    "address": {"@type": "PostalAddress", "streetAddress": "Khu Vai, xã An Nghĩa", "addressRegion": "Phú Thọ", "addressCountry": "VN"},
    "taxID": site['mst'], "alternateName": "QHUB Herbal", "slogan": "Tinh hoa trà thảo mộc phương Đông",
    "description": "Thương hiệu trà thảo mộc kế thừa tinh hoa y học thảo mộc phương Đông, 100% thiên nhiên.",
    "hasMerchantReturnPolicy": RETURN_LD,
    "contactPoint": {"@type": "ContactPoint", "telephone": "+84" + site['hotline_raw'][1:], "contactType": "customer service", "areaServed": "VN", "availableLanguage": "vi"},
    "sameAs": [u for u in list(site.get('social', {}).values()) + list(site.get('marketplaces', {}).values()) if u]}, ensure_ascii=False)
site_ld = json.dumps({"@context": "https://schema.org", "@type": "WebSite", "name": "QHUB HERBAL", "alternateName": ["QHUB Herbal", "qhubherbal.com"], "url": site['domain'] + "/"}, ensure_ascii=False)

# ================= BLOG / KIẾN THỨC =================
import re, markdown as md
CATS = {'cam-nang': 'Cẩm nang sống khỏe', 'thao-moc': 'Thảo mộc', 'san-pham': 'Sản phẩm & cách dùng', 'cau-chuyen': 'Câu chuyện', 'top': 'Top & so sánh'}
CAT_INTRO = {'cam-nang': 'Hiểu đúng những phiền toái thường gặp – nóng trong, mỏi lưng, khó ngủ, đầy bụng, những ngày ấy, căng thẳng – và những thói quen nhỏ giúp cơ thể nhẹ nhõm hơn.', 'thao-moc': 'Từng vị thảo mộc Việt: cách nhận biết, tính vị theo quan niệm phương Đông, cách dùng và những lưu ý.', 'san-pham': 'Thành phần, cách pha, thời điểm uống và cách chọn đúng trà QHUB HERBAL cho bạn.', 'cau-chuyen': 'Những câu chuyện đời thường (nhân vật minh họa) về sức khỏe, gia đình và những tách trà ấm.', 'top': 'Tổng hợp, so sánh các loại trà thảo mộc theo nhu cầu – minh bạch tiêu chí, dễ chọn.'}
def load_posts():
    out = []
    for fn in sorted(glob.glob(os.path.join(ROOT, 'content/posts/*.md'))):
        txt = open(fn, encoding='utf-8').read()
        for m in re.finditer(r'^\+\+\+\n(.*?)\n\+\+\+\n(.*?)(?=^\+\+\+\n|\Z)', txt, re.S | re.M):
            meta, body = m.group(1), m.group(2).strip()
            a = {'faq': []}
            for line in meta.split('\n'):
                if line.startswith('- ') and '::' in line:
                    q, ans = line[2:].split('::', 1); a['faq'].append((q.strip(), ans.strip())); continue
                if ':' in line:
                    k, v = line.split(':', 1); a[k.strip()] = v.strip()
            a['body'] = body
            a.setdefault('_seq', len(out))
            out.append(a)
    return out
POSTS = load_posts()
# Bài dài (viết lại): content/long/<slug>.md – thay thân bài; khối +++ đầu file (tùy chọn) ghi đè desc/title/seo_title và FAQ
LONG_DONE = 0
for a in POSTS:
    fn = os.path.join(ROOT, 'content/long', a['slug'] + '.md')
    if not os.path.exists(fn): continue
    txt = open(fn, encoding='utf-8').read().strip()
    m = re.match(r'^\+\+\+\n(.*?)\n\+\+\+\n(.*)$', txt, re.S)
    if m:
        faq = []
        for line in m.group(1).split('\n'):
            if line.startswith('- ') and '::' in line:
                q, ans = line[2:].split('::', 1); faq.append((q.strip(), ans.strip()))
            elif ':' in line:
                k, v = line.split(':', 1); a[k.strip()] = v.strip()
        if faq: a['faq'] = faq
        txt = m.group(2).strip()
    a['body'] = txt; a['long'] = True; LONG_DONE += 1
print('long posts:', LONG_DONE, '/', len(POSTS))
def slugify_vn(t):
    import unicodedata
    t = t.replace('đ', 'd').replace('Đ', 'D')
    t = unicodedata.normalize('NFD', t); t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')
def inbuy(slug):
    p = bys[slug]
    return (f'<div class="inbuy" style="--c:{p["color"]}"><img src="/assets/img/products/thumb/{slug}.webp" alt="{p["name"]}" width="110" height="158" loading="lazy">'
            f'<div><b>{p["name"]}</b><p>{p["tagline"]} {p["when_see"]}. Hộp 30 túi lọc × 3 g – <strong style="color:var(--sale)">{vnd_s(site["price_sale"])}đ</strong> <s>{vnd_s(site["price_list"])}đ</s> · <span class="promo-tag">Mua 2 tặng 1</span></p>'
            f'<div class="btns"><a class="btn btn--sm" href="#dat-hang" data-order="{slug}" data-qty="2">Mua 2 tặng 1</a><a class="btn btn--sm btn--ghost" href="/san-pham/{slug}/">Xem chi tiết</a></div></div></div>')
herb_post = {}
for a in POSTS:
    a['cat_slug'] = a.get('cat', 'thao-moc'); a['cat'] = CATS[a['cat_slug']]
    a['products'] = [bys[x.strip()] for x in a.get('products', '').split(',') if x.strip() in bys]
    if 'order' not in a: a['order'] = str(100 + a['_seq'])
    if not a.get('cover'):
        ks = ['thanh-phan', 'ly-do', 'cach-pha', 'trong-hop', 'thong-tin-hop', 'hoi-dap', 'dong-y']
        if a['products']:
            ps = a['products'][0]['slug']; cand = [k for k in ks if os.path.exists(os.path.join(ROOT, 'media/gallery', f'{ps}-{k}.webp'))]
            a['cover'] = f"gallery/{ps}-{cand[sum(map(ord, a['slug'])) % len(cand)]}.webp"
        else:
            a['cover'] = '/assets/img/lineup.webp'
    cov = a.get('cover', '')
    a['cover_url'] = cov if cov.startswith('/') else f"{site['media']}/{cov}"
    a['date'] = a.get('date', NOW.strftime('%Y-%m-%d'))
    y, mo, d = a['date'].split('-'); a['date_vn'] = f'{d}/{mo}/{y}'
    body = a['body']
    if a.get('long') and '## Nguồn tham khảo' not in body:
        import refs as _refs; body = body + _refs.refs_md(body)
    body = re.sub(r'\[\[buy:([\w-]+)\]\]', lambda m: '\n\n' + inbuy(m.group(1)) + '\n\n', body)
    toc = []
    def h2(m):
        t = m.group(1).strip(); i = slugify_vn(t)[:60]; toc.append((i, t)); return f'<h2 id="{i}">{t}</h2>'
    html = md.markdown(body, extensions=['tables', 'sane_lists'])
    html = re.sub(r'<h2>(.*?)</h2>', h2, html)
    a['html'] = html; a['toc'] = toc
    words = len(re.sub('<[^>]+>', ' ', html).split()); a['minutes'] = max(3, round(words / 220))
    if a.get('herb'): herb_post[a['herb']] = a['slug']
if 'hoa-cuc-vang' in herb_post: herb_post.setdefault('hoa-cuc', herb_post['hoa-cuc-vang'])
POSTS.sort(key=lambda a: (bool(a.get('long')), a['date'], int(a.get('order', 0))), reverse=True)  # bài dài lên trước
env.globals['herb_post'] = herb_post
_sv = lambda d: f'<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
env.globals['icons'] = [
  _sv('<path d="M3 21h18M5 21V9l5-3v15M10 21V4l9 5v12"/><path d="M14 13h2M14 17h2"/>'),
  _sv('<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13l2 2 4-4"/>'),
  _sv('<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3M8 11h6M11 8v6"/>'),
  _sv('<path d="M12 3s7 7.2 7 12a7 7 0 0 1-14 0c0-4.8 7-12 7-12z"/>'),
  _sv('<path d="M4 9h13v5a6 6 0 0 1-6 6h-1a6 6 0 0 1-6-6z"/><path d="M17 11h1.5a2.5 2.5 0 0 1 0 5H17M8 2v3M12 2v3"/>'),
  _sv('<path d="M3 5v14M7 5v14M11 5v14M15 5v14M19 5v14"/>')]
env.globals['leaf'] = _sv('<path d="M5 19c0-8 6-14 15-14 0 9-6 15-14 15"/><path d="M5 19 13 11"/>')
env.globals['herb_img'] = lambda key: f'/assets/img/ing/{key}.webp'

COMMON = dict(site=site, products=products, bys=bys, cats=cats, year=NOW.year, version=VERSION, org_ld=org_ld, site_ld=site_ld,
              form=dict(action=FORM['action'], fields_json=json.dumps(FORM['fields'])),
              faq=data.FAQ, day=data.DAY, gifts=data.GIFTS, trust=data.TRUST, warn=data.WARN_PACK)

if os.path.exists(OUT): shutil.rmtree(OUT)
shutil.copytree(SRC, OUT)
os.makedirs(os.path.join(OUT,'assets/css'), exist_ok=True)
open(os.path.join(OUT,'assets/css/site.css'),'w',encoding='utf-8').write(open(os.path.join(ROOT,'css/fonts.css'),encoding='utf-8').read()+open(os.path.join(ROOT,'css/main.css'),encoding='utf-8').read())
pages = []

MOVE = ('products/', 'ing/', 'og/', 'hero', 'lineup', 'leaf-blur', 'leaf-fresh', 'leaf-p-', 'herb-', 'zalo-qr')
def relocate(html):
    for m in MOVE:
        html = html.replace('/assets/img/' + m, site['media_img'] + '/img/' + m)
    html = html.replace(site['domain'] + site['media_img'], site['media_img'])
    html = re.sub(r'(qhubherbal-img\.pages\.dev/img/og/[\w-]+\.jpg)(?!\?)', r'\1?v=3', html)
    html = re.sub(r'(qhubherbal-media\.pages\.dev/(?:gallery|herbs)/[\w-]+\.webp)(?:\?v=\d+)?', r'\1?v=3', html)
    return re.sub(r'(qhubherbal-img\.pages\.dev/img/products/(?:thumb/)?[\w-]+\.webp)(?!\?)', r'\1?v=4', html)
def render(tpl, path, **kw):
    ctx = dict(COMMON); ctx.update(kw); ctx['path'] = path
    _t = ctx.get('title') or ''
    if len(_t) > 62 and _t.endswith(' | QHUB HERBAL'):
        ctx['title'] = _t[:-len(' | QHUB HERBAL')]
    _d = ctx.get('description') or ''
    if len(_d) > 160:
        _c = _d[:157]; ctx['description'] = _c[:_c.rfind(' ')].rstrip(' ,.;:–-') + '…'
    html = relocate(env.get_template(tpl).render(**ctx))
    fn = os.path.join(OUT, path.strip('/'), 'index.html') if path.endswith('/') else os.path.join(OUT, path.strip('/'))
    os.makedirs(os.path.dirname(fn), exist_ok=True)
    open(fn, 'w', encoding='utf-8').write(html)
    if not kw.get('noindex'): pages.append(path)

_sp=[a for a in POSTS if a['cat_slug']=='san-pham'][:3]; _tm=[a for a in POSTS if a['cat_slug']=='thao-moc'][:3]
def _pick(items, k):
    items = sorted(items, key=lambda a: (not a.get('long'), ), reverse=False)
    return items[:k]
_groups = [_pick([a for a in POSTS if p in a['products'] and a['cat_slug'] != 'top'], 3) for p in products]
_groups.append(_pick([a for a in POSTS if a['cat_slug'] == 'top'], 4))
_groups.append(_pick([a for a in POSTS if a['cat_slug'] == 'thao-moc'], 3))
slider, _seen = [], set()
for i in range(4):
    for g in _groups:
        if i < len(g) and g[i]['slug'] not in _seen: slider.append(g[i]); _seen.add(g[i]['slug'])
_vid = site.get('video_youtube', '').strip()
_m = re.search(r'(?:v=|youtu\.be/|embed/|shorts/)([\w-]{11})', _vid)
video_id = _m.group(1) if _m else (_vid if re.fullmatch(r'[\w-]{11}', _vid) else '')
render('index.html', '/', slider=slider, posts_total=len(POSTS), video_id=video_id, latest=[x for pair in zip(_sp,_tm) for x in pair], title='QHUB HERBAL – Trà thảo mộc túi lọc 100% thiên nhiên',
       description=f"Kế thừa tinh hoa y học thảo mộc phương Đông ngàn đời, đúc kết cùng các nghiên cứu khoa học hiện đại, QHUB HERBAL chắt lọc {len(products)} công thức trà thảo mộc tinh túy, 100% thiên nhiên – an yên trong từng tách trà.")
render('list.html', '/san-pham/', section='sp', title='Tất cả sản phẩm – Trà thảo mộc túi lọc QHUB HERBAL',
       description=f"Danh sách trà thảo mộc túi lọc QHUB HERBAL, hộp 30 túi × 3 g, không thêm đường. Giá niêm yết {vnd_s(site['price_list'])}đ, giá ưu đãi {vnd_s(site['price_sale'])}đ/hộp.")
for p in products:
    ld = json.dumps({"@context": "https://schema.org", "@type": "Product", "name": p['name'], "brand": {"@type": "Brand", "name": "QHUB HERBAL"},
        "image": [site['domain'] + f"/assets/img/products/{p['slug']}.webp", site['domain'] + f"/assets/img/products/{p['slug']}-3d.webp"],
        "description": p['intro'], "gtin13": p['gtin'], "sku": p['gtin'], "category": "Trà thảo mộc túi lọc",
        "offers": {"@type": "Offer", "priceCurrency": "VND", "price": site['price_sale'], "availability": "https://schema.org/InStock",
                   "itemCondition": "https://schema.org/NewCondition", "priceValidUntil": f"{NOW.year + 1}-12-31",
                   "priceSpecification": [{"@type": "UnitPriceSpecification", "price": site['price_sale'], "priceCurrency": "VND", "validFrom": "2026-11-11"},
                                          {"@type": "UnitPriceSpecification", "priceType": "https://schema.org/StrikethroughPrice", "price": site['price_list'], "priceCurrency": "VND"}],
                   "url": site['domain'] + f"/san-pham/{p['slug']}/", "seller": {"@type": "Organization", "name": site['company']},
                   "shippingDetails": SHIP_LD, "hasMerchantReturnPolicy": RETURN_LD}}, ensure_ascii=False)
    bc_ld = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": site['domain'] + "/"},
        {"@type": "ListItem", "position": 2, "name": "Sản phẩm", "item": site['domain'] + "/san-pham/"},
        {"@type": "ListItem", "position": 3, "name": p['name'], "item": site['domain'] + f"/san-pham/{p['slug']}/"}]}, ensure_ascii=False)
    others = [o for o in products if o['slug'] != p['slug']]
    render('product.html', f"/san-pham/{p['slug']}/", p=p, others=others[:4] if len(others) > 4 else others,
           title=f"{p['name']} – {p['tagline'].rstrip('.')} | QHUB HERBAL",
           description=f"{p['name']}: {p['when_see'].lower()}. {', '.join(p['keys'])}. Hộp 30 túi lọc × 3 g, không thêm đường. Giá ưu đãi {vnd_s(site['price_sale'])}đ (niêm yết {vnd_s(site['price_list'])}đ).",
           og_type='product', og_image=f"{site['domain']}/assets/img/og/{p['slug']}.jpg", product_ld=ld, bc_ld=bc_ld, section='sp',
           posts_for=[a for a in POSTS if p in a['products']][:6], posts_n=sum(1 for a in POSTS if p in a['products']))

post_cats = [(k, v, sum(1 for a in POSTS if a['cat_slug'] == k)) for k, v in CATS.items()]
post_cats = [c for c in post_cats if c[2]]
PER = 24
def paged(items, base, **kw):
    n = max(1, -(-len(items) // PER))
    for i in range(n):
        url = base if i == 0 else f"{base}trang/{i+1}/"
        pager = [(j + 1, base if j == 0 else f"{base}trang/{j+1}/") for j in range(n)] if n > 1 else []
        t = kw['title'] if i == 0 else kw['title'].replace(' | QHUB HERBAL', f' – Trang {i+1} | QHUB HERBAL')
        render('blog.html', url, posts=items[i*PER:(i+1)*PER], total=len(items), page=i+1, pager=pager, post_cats=post_cats,
               section='kt', **{**kw, 'title': t})
paged(POSTS, '/kien-thuc/', h1='Hiểu cây cỏ, thương cơ thể', cur='all',
      intro=f'{len(POSTS)} bài viết về từng vị thảo mộc Việt, những phiền toái thường gặp của cơ thể, cách pha – cách dùng trà túi lọc và những thói quen nhỏ giúp mỗi ngày nhẹ nhõm hơn.',
      title='Kiến thức thảo mộc – Hiểu cây cỏ, thương cơ thể | QHUB HERBAL',
      description='Bài viết về thảo mộc Việt (cà gai leo, ba kích, tâm sen, ích mẫu, lá ổi…), cẩm nang sống khỏe, top trà thảo mộc theo nhu cầu và cách chọn trà túi lọc phù hợp.')
for k, v, nn in post_cats:
    paged([a for a in POSTS if a['cat_slug'] == k], f'/kien-thuc/chu-de/{k}/', h1=v, cur=k, crumb=v, intro=CAT_INTRO.get(k, ''),
          title=f'{v} – Kiến thức thảo mộc | QHUB HERBAL', description=CAT_INTRO.get(k, v))
for p in products:
    items = [a for a in POSTS if p in a['products']]
    if items:
        paged(items, f"/kien-thuc/tra/{p['slug']}/", h1=f"Tất cả bài viết về {p['name']}", cur='', crumb=p['name'], prod=p,
              intro=f"{len(items)} bài viết liên quan đến {p['name']}: {p['when_see'].lower()} – hiểu đúng nguyên nhân, thói quen nên có và cách dùng trà.",
              title=f"{p['name']}: kiến thức và cách dùng | QHUB HERBAL", description=f"Tổng hợp bài viết về {p['name']} và những vấn đề liên quan: {p['when_see'].lower()}.")
for a in POSTS:
    same = [r for r in POSTS if r is not a and (set(map(id, r['products'])) & set(map(id, a['products'])))]
    rel = ([r for r in same if r.get('long')] + [r for r in POSTS if r is not a and r.get('long') and r not in same] + same)[:3]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": a['title'], "description": a['desc'], "image": a['cover_url'], "datePublished": a['date'], "dateModified": a['date'],
         "author": {"@type": "Organization", "name": "QHUB HERBAL"}, "publisher": {"@type": "Organization", "name": "QHUB HERBAL", "logo": {"@type": "ImageObject", "url": site['domain'] + "/assets/img/logo-forest.png"}},
         "mainEntityOfPage": site['domain'] + f"/kien-thuc/{a['slug']}/", "inLanguage": "vi"},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": site['domain'] + "/"},
            {"@type": "ListItem", "position": 2, "name": "Kiến thức", "item": site['domain'] + "/kien-thuc/"},
            {"@type": "ListItem", "position": 3, "name": a['title'], "item": site['domain'] + f"/kien-thuc/{a['slug']}/"}]}]}
    _rv = site.get('reviewer') or {}
    if _rv.get('name'):
        _p = {"@type": "Person", "name": _rv['name'], "jobTitle": _rv.get('title', '')}
        if _rv.get('url'): _p['url'] = _rv['url']
        ld["@graph"].append({"@type": "WebPage", "@id": site['domain'] + f"/kien-thuc/{a['slug']}/", "url": site['domain'] + f"/kien-thuc/{a['slug']}/", "name": a['title'], "reviewedBy": _p, "lastReviewed": a['date']})
    if a['faq']:
        ld["@graph"].append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in a['faq']]})
    render('post.html', f"/kien-thuc/{a['slug']}/", noindex=not a.get('long'), a=a, related=rel, section='kt', og_type='article', og_image=a['cover_url'],
           title=a.get('seo_title', a['title']) + ' | QHUB HERBAL', description=a['desc'], post_ld=json.dumps(ld, ensure_ascii=False))

_contact = f"Hotline/Zalo <a href=\"tel:{site['hotline_raw']}\">{site['hotline']}</a> · Email <a href=\"mailto:{site['email']}\">{site['email']}</a>"
_owner = site['company'] + f" · Mã số doanh nghiệp/MST {site['mst']}" + (f" do {site['dkdn_place']} cấp lần đầu ngày {site['dkdn_date']}" if site.get('dkdn_date') and site.get('dkdn_place') else '') + f" · Trụ sở: {site['address']}" + (f" · Người đại diện theo pháp luật: {site['legal_rep']} – {site['legal_rep_title']}" if site.get('legal_rep') else '')
PRIVACY = f"""<p class="eyebrow">Chính sách</p><h1>Chính sách bảo mật và bảo vệ dữ liệu cá nhân</h1>
<p>Cập nhật: {NOW.strftime('%d/%m/%Y')}. Website qhubherbal.com do {site['company']} (MST {site['mst']}, {site['address']}) sở hữu và vận hành cho thương hiệu QHUB HERBAL. Chúng tôi là bên kiểm soát và xử lý dữ liệu cá nhân bạn cung cấp trên website.</p>
<h2>1. Dữ liệu chúng tôi thu thập</h2><ul><li><b>Khi bạn đặt hàng:</b> họ tên, số điện thoại, địa chỉ nhận hàng, sản phẩm và số lượng.</li><li><b>Thông tin kỹ thuật:</b> trang bạn truy cập trước khi đặt hàng và nguồn giới thiệu (lưu tạm trong trình duyệt của bạn, gửi kèm đơn để chúng tôi biết bạn đến từ đâu).</li></ul><p>Chúng tôi không thu thập dữ liệu cá nhân nhạy cảm, không thu thập thông tin thẻ ngân hàng.</p>
<h2>2. Mục đích xử lý</h2><ul><li>Liên hệ xác nhận đơn hàng, tư vấn cách dùng sản phẩm.</li><li>Đóng gói, giao hàng, thu tiền khi giao hàng (COD), đổi trả và hoàn tiền.</li><li>Tiếp nhận, giải quyết phản ánh, khiếu nại.</li><li>Thực hiện nghĩa vụ kế toán, thuế theo quy định pháp luật.</li></ul><p>Chúng tôi không bán, cho thuê hoặc trao đổi dữ liệu của bạn cho bên thứ ba vì mục đích quảng cáo.</p>
<h2>3. Cơ sở xử lý – sự đồng ý của bạn</h2><p>Chúng tôi chỉ xử lý dữ liệu khi bạn đánh dấu đồng ý với chính sách này trước khi gửi đơn hàng. Bạn có quyền rút lại sự đồng ý bất kỳ lúc nào bằng cách liên hệ với chúng tôi; việc rút lại không ảnh hưởng đến các xử lý đã thực hiện trước đó.</p>
<h2>4. Thời gian lưu trữ</h2><p>Dữ liệu đơn hàng được lưu tối đa <b>24 tháng</b> kể từ đơn hàng gần nhất để phục vụ chăm sóc khách hàng, đổi trả, bảo hành; chứng từ kế toán được lưu theo thời hạn pháp luật quy định. Hết thời hạn, dữ liệu được xóa hoặc ẩn danh hóa.</p>
<h2>5. Những ai được tiếp cận dữ liệu</h2><ul><li>Nhân sự phụ trách đơn hàng, chăm sóc khách hàng của {site['company']}.</li><li>Đơn vị vận chuyển: chỉ họ tên, số điện thoại, địa chỉ nhận hàng và số tiền thu hộ.</li><li>Nhà cung cấp hạ tầng lưu trữ: hệ thống biểu mẫu và bảng tính Google (Google LLC) dùng để tiếp nhận đơn hàng.</li><li>Cơ quan nhà nước có thẩm quyền khi có yêu cầu theo quy định pháp luật.</li></ul>
<h2>6. Biện pháp bảo vệ</h2><p>Website sử dụng kết nối mã hóa HTTPS. Dữ liệu đơn hàng được lưu trong tài khoản quản trị có xác thực, chỉ cấp quyền cho nhân sự cần thiết. Trường hợp xảy ra sự cố lộ lọt dữ liệu, chúng tôi sẽ thông báo cho bạn và cơ quan có thẩm quyền theo quy định.</p>
<h2>7. Quyền của bạn và cách thực hiện</h2><p>Bạn có quyền được biết, xem, chỉnh sửa, yêu cầu xóa, hạn chế xử lý dữ liệu, rút lại sự đồng ý và khiếu nại về việc xử lý dữ liệu. Để thực hiện, vui lòng liên hệ {_contact}, nêu rõ số điện thoại đã dùng khi đặt hàng. Chúng tôi phản hồi trong vòng <b>72 giờ</b> và hoàn tất yêu cầu chỉnh sửa, xóa trong vòng <b>7 ngày làm việc</b> (trừ dữ liệu pháp luật yêu cầu phải lưu giữ).</p>
<h2>8. Cookie và lưu trữ trình duyệt</h2><p>Website chỉ dùng bộ nhớ tạm của trình duyệt (sessionStorage) để ghi nhớ trang bạn đến và nội dung đơn hàng đang điền; dữ liệu này tự xóa khi bạn đóng trình duyệt.</p>
<h2>9. Liên hệ</h2><p>{_owner}. {_contact}.</p>"""
render('page.html', '/chinh-sach-bao-mat/', content=PRIVACY, title='Chính sách bảo mật | QHUB HERBAL', description='Chính sách bảo mật thông tin khách hàng của QHUB HERBAL.')



# ---- Chính sách vận chuyển / đổi trả / điều khoản (yêu cầu của Google Merchant Center) ----
_upd = NOW.strftime('%d/%m/%Y')
_contact = f"Hotline/Zalo <a href=\"tel:{site['hotline_raw']}\">{site['hotline']}</a> · Email <a href=\"mailto:{site['email']}\">{site['email']}</a>"
SHIP = f"""<p class="eyebrow">Chính sách</p><h1>Chính sách vận chuyển</h1>
<p>Cập nhật: {_upd}. Áp dụng cho đơn hàng đặt trên qhubherbal.com, qua hotline hoặc Zalo của QHUB HERBAL.</p>
<h2>1. Phí giao hàng</h2><p><b>Miễn phí giao hàng toàn quốc</b> cho mọi đơn hàng, không yêu cầu giá trị tối thiểu.</p>
<h2>2. Phạm vi giao hàng</h2><p>Giao đến tất cả tỉnh, thành phố trên lãnh thổ Việt Nam thông qua các đơn vị vận chuyển đối tác.</p>
<h2>3. Thời gian giao hàng</h2>
<table><thead><tr><th>Bước</th><th>Thời gian</th></tr></thead><tbody>
<tr><td>Xác nhận và đóng gói đơn hàng</td><td>Trong vòng 1 ngày làm việc kể từ khi QHUB HERBAL gọi xác nhận đơn</td></tr>
<tr><td>Vận chuyển</td><td>1–4 ngày tùy khu vực</td></tr>
<tr><td><b>Tổng thời gian dự kiến</b></td><td><b>2–5 ngày</b></td></tr></tbody></table>
<p>Thời gian có thể kéo dài hơn vào dịp lễ, Tết, thời tiết xấu hoặc khu vực vùng sâu, vùng xa. Chúng tôi sẽ chủ động báo nếu đơn hàng bị chậm.</p>
<h2>4. Quy trình</h2><ol><li>Bạn đặt hàng trên website (hoặc gọi/nhắn Zalo).</li><li>QHUB HERBAL gọi điện xác nhận đơn, địa chỉ nhận hàng.</li><li>Đơn được đóng gói và bàn giao cho đơn vị vận chuyển.</li><li>Bạn kiểm tra hàng khi nhận và thanh toán theo phương thức đã thống nhất khi xác nhận đơn.</li></ol>
<h2>5. Kiểm tra hàng khi nhận</h2><p>Bạn được kiểm tra tình trạng bên ngoài của kiện hàng và hộp trà khi nhận. Nếu hộp móp méo, rách, ẩm ướt hoặc giao sai sản phẩm, vui lòng từ chối nhận hoặc chụp ảnh và báo ngay cho chúng tôi để được đổi mới miễn phí.</p>
<h2>6. Liên hệ</h2><p>{_owner}. {_contact}.</p>"""
RET = f"""<p class="eyebrow">Chính sách</p><h1>Chính sách đổi trả và hoàn tiền</h1>
<p>Cập nhật: {_upd}. QHUB HERBAL mong bạn hài lòng với từng tách trà. Nếu chưa ưng ý, bạn có thể đổi trả theo chính sách dưới đây.</p>
<h2>1. Thời hạn</h2><p>Bạn được đổi hoặc trả hàng trong vòng <b>{site['return_days']} ngày</b> kể từ ngày nhận hàng.</p>
<h2>2. Trường hợp được đổi trả</h2>
<table><thead><tr><th>Trường hợp</th><th>Điều kiện</th><th>Phí vận chuyển đổi trả</th></tr></thead><tbody>
<tr><td><b>Hàng lỗi</b>: hộp móp méo, rách, ẩm mốc, hết hạn, giao sai sản phẩm hoặc thiếu hàng</td><td>Chụp ảnh tình trạng sản phẩm, báo cho chúng tôi trong {site['return_days']} ngày</td><td><b>QHUB HERBAL chịu toàn bộ</b></td></tr>
<tr><td><b>Đổi ý</b>: không còn nhu cầu, muốn đổi sang sản phẩm khác</td><td>Hộp còn nguyên tem, nguyên màng co, chưa mở, chưa sử dụng</td><td>Khách hàng chịu phí gửi trả</td></tr>
</tbody></table>
<h2>3. Trường hợp không áp dụng</h2><ul><li>Quá {site['return_days']} ngày kể từ khi nhận hàng.</li><li>Sản phẩm đã mở màng co, đã sử dụng (trừ trường hợp hàng lỗi).</li><li>Quà tặng kèm trong chương trình khuyến mại (trừ khi lỗi).</li></ul>
<h2>4. Cách thức đổi trả</h2><ol><li>Liên hệ {_contact}, cung cấp mã đơn hoặc số điện thoại đặt hàng và ảnh sản phẩm.</li><li>QHUB HERBAL xác nhận và hướng dẫn gửi trả qua đơn vị vận chuyển.</li><li>Sau khi nhận lại hàng và kiểm tra, chúng tôi gửi sản phẩm thay thế hoặc hoàn tiền.</li></ol>
<h2>5. Hoàn tiền</h2><p>Hoàn tiền bằng chuyển khoản ngân hàng trong vòng <b>3–7 ngày làm việc</b> kể từ khi chúng tôi nhận lại hàng. Với đơn đổi ý mua theo chương trình "mua 2 tặng 1", số tiền hoàn được tính theo giá trị thực tế của sản phẩm trả lại sau ưu đãi.</p>
<h2>6. Liên hệ</h2><p>{_owner}. {_contact}.</p>"""
TERMS = f"""<p class="eyebrow">Điều khoản</p><h1>Điều khoản mua hàng và sử dụng website</h1>
<p>Cập nhật: {_upd}. Website qhubherbal.com là nền tảng thương mại điện tử kinh doanh trực tiếp có chức năng đặt hàng trực tuyến của <b>{site['company']}</b>, bán sản phẩm mang thương hiệu QHUB HERBAL do công ty phân phối.</p>
<h2>1. Thông tin chủ sở hữu website</h2><p>{_owner}. {_contact}.</p>
<h2>2. Hàng hóa kinh doanh</h2><p>Trà thảo mộc túi lọc QHUB HERBAL (thực phẩm), sản xuất tại {site['manufacturer']} – {site['iso']}. Mỗi trang sản phẩm công bố tên sản phẩm, thành phần, quy cách, cách dùng, đối tượng lưu ý, giá bán. {site['disclaimer']} Thông tin về thảo mộc trên website mang tính giới thiệu, tham khảo, không thay thế tư vấn của bác sĩ.</p>
<h2>3. Giá và khuyến mại</h2><p>Giá niêm yết {vnd_s(site['price_list'])}đ/hộp, giá bán ưu đãi {vnd_s(site['price_sale'])}đ/hộp. Giá bán <b>đã bao gồm thuế giá trị gia tăng (nếu có)</b> và <b>đã bao gồm phí giao hàng</b> (miễn phí giao hàng toàn quốc); không phát sinh chi phí nào khác. Chương trình khuyến mại (như "mua 2 tặng 1") áp dụng theo thời hạn công bố trên website; giá trị cuối cùng của đơn hàng được thông báo lại cho bạn khi xác nhận đơn.</p>
<h2>4. Quy trình đặt hàng và xác nhận</h2><ol><li>Chọn sản phẩm, số lượng trong khung đặt hàng; hệ thống hiển thị số hộp, số hộp được tặng và tạm tính để bạn kiểm tra.</li><li>Nhập họ tên, số điện thoại, địa chỉ nhận hàng; đánh dấu đồng ý Chính sách bảo mật và Điều khoản; bấm "Gửi đơn đặt hàng".</li><li>Trong giờ làm việc, QHUB HERBAL gọi điện hoặc nhắn Zalo để xác nhận lại sản phẩm, số lượng, tổng tiền, địa chỉ. Bạn có thể sửa hoặc hủy đơn tại bước này.</li><li>Đơn hàng được coi là giao kết khi hai bên xác nhận qua điện thoại/Zalo. Chúng tôi có thể từ chối đơn có thông tin không chính xác hoặc không liên lạc được.</li></ol>
<h2>5. Thanh toán, giao hàng, đổi trả</h2><p>Xem chi tiết tại <a href="/chinh-sach-thanh-toan/">Chính sách thanh toán</a> (thanh toán khi nhận hàng – COD), <a href="/chinh-sach-van-chuyen/">Chính sách vận chuyển</a> (miễn phí toàn quốc, 2–5 ngày) và <a href="/chinh-sach-doi-tra/">Chính sách đổi trả và hoàn tiền</a> ({site['return_days']} ngày).</p>
<h2>6. Điều kiện, giới hạn cung cấp</h2><ul><li>Phạm vi: giao hàng trên lãnh thổ Việt Nam.</li><li>Đơn số lượng lớn, đơn đại lý vui lòng liên hệ hotline để được tư vấn và báo giá riêng.</li><li>Tình trạng còn hàng được xác nhận khi gọi xác nhận đơn; nếu hết hàng, chúng tôi thông báo và bạn có quyền đổi sản phẩm hoặc hủy đơn.</li><li>Một số sản phẩm không dùng cho phụ nữ mang thai, cho con bú (ghi rõ trên trang sản phẩm và bao bì).</li></ul>
<h2>7. Quyền và nghĩa vụ của {site['company']}</h2><ul><li>Cung cấp đầy đủ, trung thực thông tin về hàng hóa, giá, điều kiện giao dịch; giao đúng sản phẩm, đúng số lượng, còn hạn sử dụng.</li><li>Bảo vệ dữ liệu cá nhân của khách hàng theo Chính sách bảo mật.</li><li>Tiếp nhận và giải quyết phản ánh, khiếu nại theo <a href="/giai-quyet-khieu-nai/">Cơ chế giải quyết khiếu nại</a>; thực hiện đổi trả, hoàn tiền theo chính sách đã công bố.</li><li>Xuất hóa đơn điện tử theo quy định khi khách hàng yêu cầu.</li><li>Được từ chối hoặc hủy đơn hàng có dấu hiệu giả mạo, đặt hàng ảo, thông tin không chính xác.</li></ul>
<h2>8. Quyền và nghĩa vụ của khách hàng</h2><ul><li>Được cung cấp thông tin đầy đủ, chính xác về sản phẩm; được kiểm tra hàng khi nhận; được đổi trả, hoàn tiền, khiếu nại theo chính sách.</li><li>Được yêu cầu xem, sửa, xóa dữ liệu cá nhân của mình.</li><li>Cung cấp thông tin đặt hàng chính xác, nghe máy xác nhận đơn, nhận hàng và thanh toán đúng như đã xác nhận.</li><li>Đọc kỹ thành phần, hướng dẫn sử dụng và lưu ý trên bao bì trước khi dùng; tham khảo ý kiến bác sĩ nếu đang mang thai, cho con bú, có bệnh lý hoặc đang dùng thuốc.</li></ul>
<h2>9. Giải quyết tranh chấp</h2><p>Mọi tranh chấp được ưu tiên giải quyết bằng thương lượng, hòa giải. Trường hợp không đạt được thỏa thuận, các bên có quyền yêu cầu cơ quan bảo vệ quyền lợi người tiêu dùng, trọng tài hoặc tòa án có thẩm quyền giải quyết theo quy định pháp luật Việt Nam.</p>
<h2>10. Sở hữu trí tuệ</h2><p>Nội dung, hình ảnh, logo QHUB HERBAL trên website thuộc quyền của {site['company']}. Vui lòng ghi nguồn khi trích dẫn.</p>"""

PAY = f"""<p class="eyebrow">Chính sách</p><h1>Chính sách thanh toán</h1>
<p>Cập nhật: {_upd}. Áp dụng cho đơn hàng đặt trên qhubherbal.com, qua hotline hoặc Zalo của QHUB HERBAL.</p>
<h2>1. Phương thức thanh toán</h2><p><b>Thanh toán khi nhận hàng (COD):</b> bạn kiểm tra hàng rồi thanh toán bằng tiền mặt cho nhân viên giao hàng. Website không yêu cầu đặt cọc, không thu thập thông tin thẻ ngân hàng hay tài khoản thanh toán của bạn.</p>
<h2>2. Số tiền thanh toán</h2><p>Bằng tổng giá bán các sản phẩm trong đơn đã được hai bên xác nhận qua điện thoại/Zalo. Giá đã bao gồm thuế giá trị gia tăng (nếu có) và phí giao hàng (miễn phí toàn quốc) – không phát sinh khoản thu nào khác. Hộp tặng trong chương trình khuyến mại không tính tiền.</p>
<h2>3. Chứng từ</h2><p>Mỗi kiện hàng kèm phiếu giao hàng ghi rõ sản phẩm, số lượng, số tiền thu hộ. Hóa đơn điện tử được xuất theo quy định; nếu cần hóa đơn ghi thông tin doanh nghiệp, vui lòng báo khi xác nhận đơn.</p>
<h2>4. Hoàn tiền</h2><p>Trường hợp đổi trả theo <a href="/chinh-sach-doi-tra/">Chính sách đổi trả và hoàn tiền</a>, chúng tôi hoàn tiền bằng chuyển khoản vào tài khoản ngân hàng do bạn cung cấp trong vòng 3–7 ngày làm việc kể từ khi nhận lại hàng.</p>
<h2>5. Cảnh báo giả mạo</h2><p>QHUB HERBAL không bao giờ yêu cầu bạn chuyển khoản trước qua tin nhắn từ số lạ hay cung cấp mã OTP. Khi nghi ngờ, vui lòng gọi hotline <a href="tel:{site['hotline_raw']}">{site['hotline']}</a>.</p>
<h2>6. Liên hệ</h2><p>{_owner}. {_contact}.</p>"""
CMP = f"""<p class="eyebrow">Chăm sóc khách hàng</p><h1>Cơ chế tiếp nhận và giải quyết phản ánh, khiếu nại</h1>
<p>Cập nhật: {_upd}. QHUB HERBAL trân trọng mọi góp ý và cam kết xử lý phản ánh, khiếu nại một cách nhanh chóng, minh bạch.</p>
<h2>1. Kênh tiếp nhận</h2><ul><li><b>Trực tuyến:</b> Zalo <a href="{site['zalo_url']}" target="_blank" rel="noopener">{site['hotline']}</a> · Email <a href="mailto:{site['email']}">{site['email']}</a>.</li><li><b>Điện thoại:</b> hotline <a href="tel:{site['hotline_raw']}">{site['hotline']}</a>.</li><li><b>Văn bản:</b> gửi về {site['company']}, {site['address']}.</li></ul>
<h2>2. Thông tin cần cung cấp</h2><p>Họ tên, số điện thoại đặt hàng, sản phẩm, ngày nhận hàng, nội dung phản ánh và hình ảnh, video (nếu có).</p>
<h2>3. Thời hạn xử lý</h2>
<table><thead><tr><th>Bước</th><th>Thời hạn</th></tr></thead><tbody>
<tr><td>Xác nhận đã tiếp nhận</td><td>Trong vòng 24 giờ</td></tr>
<tr><td>Phản hồi phương án giải quyết</td><td>Trong vòng 3 ngày làm việc</td></tr>
<tr><td>Hoàn tất (đổi hàng, hoàn tiền…)</td><td>Trong vòng 7 ngày làm việc kể từ khi thống nhất phương án</td></tr></tbody></table>
<h2>4. Nguyên tắc giải quyết</h2><ul><li>Ưu tiên thương lượng, hòa giải, bảo đảm quyền lợi hợp pháp của người tiêu dùng.</li><li>Lỗi do QHUB HERBAL (giao sai, hàng lỗi, hết hạn): đổi mới hoặc hoàn tiền 100%, chịu toàn bộ chi phí vận chuyển.</li><li>Phản ánh về sức khỏe khi sử dụng: khuyến nghị ngừng dùng và đến cơ sở y tế; chúng tôi phối hợp cung cấp thông tin thành phần, lô sản xuất.</li></ul>
<h2>5. Khi chưa đạt thỏa thuận</h2><p>Bạn có quyền yêu cầu cơ quan quản lý nhà nước về bảo vệ quyền lợi người tiêu dùng, Sở Công Thương nơi bạn sinh sống, trọng tài hoặc tòa án có thẩm quyền giải quyết theo quy định pháp luật.</p>
<h2>6. Đơn vị chịu trách nhiệm</h2><p>{_owner}.</p>"""
render('page.html', '/chinh-sach-thanh-toan/', content=PAY, title='Chính sách thanh toán – Thanh toán khi nhận hàng | QHUB HERBAL', description='Thanh toán khi nhận hàng (COD), giá đã gồm VAT và phí giao hàng, hoàn tiền 3–7 ngày làm việc.')
render('page.html', '/giai-quyet-khieu-nai/', content=CMP, title='Cơ chế giải quyết khiếu nại | QHUB HERBAL', description='Kênh tiếp nhận phản ánh, khiếu nại của QHUB HERBAL và thời hạn xử lý: xác nhận 24 giờ, phản hồi 3 ngày làm việc.')
render('page.html', '/chinh-sach-van-chuyen/', content=SHIP, title='Chính sách vận chuyển – Miễn phí giao hàng toàn quốc | QHUB HERBAL', description='QHUB HERBAL miễn phí giao hàng toàn quốc mọi đơn, thời gian giao dự kiến 2–5 ngày. Kiểm tra hàng khi nhận.')
render('page.html', '/chinh-sach-doi-tra/', content=RET, title=f"Chính sách đổi trả {site['return_days']} ngày | QHUB HERBAL", description=f"Đổi trả trong {site['return_days']} ngày kể từ khi nhận hàng. Hàng lỗi QHUB HERBAL chịu phí; đổi ý khi hộp còn nguyên tem. Hoàn tiền 3–7 ngày làm việc.")
render('page.html', '/dieu-khoan/', content=TERMS, title='Điều khoản mua hàng | QHUB HERBAL', description='Điều khoản mua hàng, giá, khuyến mại, giao hàng, đổi trả và sử dụng website qhubherbal.com.')
# ---- Trang Giới thiệu / thông tin thương hiệu (cho người đọc và công cụ AI) ----
rows = ''.join(f"<tr><td><a href=\"/san-pham/{p['slug']}/\">{p['name']}</a></td><td>{p['when_see']}</td><td>{', '.join(i[1] for i in p['ings'])}</td><td>{p['time']}</td></tr>" for p in products)
spec = ''.join(f"<tr><td>{p['name']}</td><td>{p['tcb']}</td><td>{p['gtin']}</td></tr>" for p in products)
ABOUT = f"""<p class="eyebrow">Về chúng tôi</p><h1>QHUB HERBAL là gì? Thông tin thương hiệu trà thảo mộc QHUB HERBAL</h1>
<p><b>QHUB HERBAL</b> là thương hiệu trà thảo mộc túi lọc của {site['company']} (MST {site['mst']}, {site['address']}). Các công thức được phối theo nguyên tắc <b>Quân – Thần – Tá – Sứ</b> của người xưa phương Đông, từ thảo mộc Việt quen thuộc, đóng gói túi lọc 3 g tiện pha trong 5 phút.</p>
<h2>Thông tin nhanh</h2><ul>
<li><b>Sản phẩm:</b> {len(products)} dòng trà thảo mộc túi lọc, mỗi dòng cho một nhu cầu: thanh lọc, phái mạnh, giấc ngủ, phái đẹp, tiêu hóa, thư thái.</li>
<li><b>Quy cách:</b> hộp 30 túi lọc × 3 g (90 g). Không thêm đường, không caffeine, vị ngọt dịu từ thảo mộc (cỏ ngọt, cam thảo, táo đỏ).</li>
<li><b>Giá:</b> giá niêm yết {vnd_s(site['price_list'])}đ/hộp, giá ưu đãi <b>{vnd_s(site['price_sale'])}đ/hộp</b>.</li>
<li><b>Sản xuất:</b> {site['manufacturer']}. {site['iso']}.</li>
<li><b>Pháp lý:</b> mỗi sản phẩm có hồ sơ tự công bố riêng và mã vạch GS1 riêng (bảng dưới).</li>
<li><b>Đặt hàng & tư vấn:</b> form trên website, hotline/Zalo <a href="tel:{site['hotline_raw']}">{site['hotline']}</a>, email {site['email']}. QHUB gọi điện xác nhận đơn trước khi giao.</li>
</ul>
<h2>Chọn trà theo nhu cầu</h2>
<div class="tablewrap"><table class="ptable"><thead><tr><th>Sản phẩm</th><th>Dành cho khi</th><th>Thành phần</th><th>Thời điểm uống</th></tr></thead><tbody>{rows}</tbody></table></div>
<h2>Hồ sơ sản phẩm</h2>
<div class="tablewrap"><table class="ptable"><thead><tr><th>Sản phẩm</th><th>Số tự công bố</th><th>Mã vạch (GTIN)</th></tr></thead><tbody>{spec}</tbody></table></div>
<h2>Điều QHUB HERBAL cam kết</h2><ul>
<li>Ghi rõ thành phần và tỷ lệ vị chủ đạo trên từng hộp.</li>
<li>Không thêm đường, không hương liệu tổng hợp.</li>
<li>Nói đúng về sản phẩm: trà thảo mộc là thực phẩm dùng hằng ngày, <b>không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh</b>. Khi có dấu hiệu bất thường về sức khỏe, hãy đi khám bác sĩ.</li>
<li>Tư vấn chọn trà trung thực theo nhu cầu, kể cả khi sản phẩm không phù hợp với bạn.</li>
</ul>
<h2>Đọc thêm</h2><p><a href="/kien-thuc/">Kiến thức thảo mộc</a> · <a href="/kien-thuc/chu-de/top/">Top trà thảo mộc theo nhu cầu</a> · <a href="/san-pham/">Tất cả sản phẩm</a></p>"""
render('page.html', '/gioi-thieu/', content=ABOUT, title='QHUB HERBAL là gì? Thông tin thương hiệu, nhà máy, giá, liên hệ | QHUB HERBAL',
       description=f"QHUB HERBAL – thương hiệu trà thảo mộc túi lọc của {site['company']}. {len(products)} dòng trà theo quan niệm phương Đông, nhà máy ISO 22000:2018, giá ưu đãi {vnd_s(site['price_sale'])}đ/hộp.")

THANKS = f"""<div class="thanks"><img src="/assets/img/symbol-forest.png" alt="" width="120" height="120">
<p class="eyebrow" style="justify-content:center">Đặt hàng thành công</p><h1>Cảm ơn bạn đã tin chọn QHUB HERBAL!</h1>
<p id="tksum">QHUB đã nhận được đơn của bạn và sẽ gọi điện xác nhận trong thời gian sớm nhất.</p>
<p>Cần thay đổi đơn hoặc muốn được tư vấn ngay? Gọi/nhắn Hotline/Zalo <a href="{site['zalo_url']}" target="_blank" rel="noopener"><b>{site['hotline']}</b></a>.</p>
<p style="margin-top:28px"><a class="btn" href="/">Về trang chủ</a> <a class="btn btn--ghost" href="/san-pham/">Xem thêm sản phẩm</a></p></div>
<script>try{{var d=JSON.parse(sessionStorage.getItem('qh_last')||'null');if(d){{var e=document.getElementById('tksum');e.textContent='';var b=document.createElement('span');b.textContent='Cảm ơn '+d.ten+'. Đơn của bạn: '+d.sp.join(', ')+' ('+d.tong+'). QHUB sẽ gọi điện xác nhận trong thời gian sớm nhất.';e.appendChild(b);}}}}catch(x){{}}</script>"""
render('page.html', '/cam-on/', content=THANKS, title='Cảm ơn bạn đã đặt hàng | QHUB HERBAL', description='Đặt hàng thành công.', noindex=True)

NOTFOUND = """<div class="thanks"><img src="/assets/img/symbol-forest.png" alt="" width="120" height="120"><h1>Không tìm thấy trang</h1>
<p>Trang bạn tìm có thể đã đổi địa chỉ. Mời bạn xem các sản phẩm của QHUB HERBAL.</p><p><a class="btn" href="/san-pham/">Xem sản phẩm</a></p></div>"""
render('page.html', '/404.html', content=NOTFOUND, title='Không tìm thấy trang | QHUB HERBAL', description='Không tìm thấy trang.', noindex=True)


render('fragment_order.html', '/assets/order.html', noindex=True)
# llms.txt – tóm tắt cho các trợ lý AI
L = [f"# QHUB HERBAL", "", f"> Thương hiệu trà thảo mộc túi lọc Việt Nam của {site['company']} (MST {site['mst']}). {len(products)} công thức theo quan niệm phương Đông, hộp 30 túi × 3 g, không thêm đường, không caffeine. Giá ưu đãi {vnd_s(site['price_sale'])}đ/hộp (niêm yết {vnd_s(site['price_list'])}đ). Đang có chương trình mua 2 tặng 1 (mua 2 hộp bất kỳ tặng 1 hộp tự chọn, cộng dồn). Sản xuất tại nhà máy đạt ISO 22000:2018. Đặt hàng: {site['domain']} · hotline/Zalo {site['hotline']}.", "",
     "Lưu ý: sản phẩm là thực phẩm, không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh.", "", "## Sản phẩm"]
for p in products:
    L.append(f"- [{p['name']}]({site['domain']}/san-pham/{p['slug']}/): {p['tagline']} Dành cho: {p['when_see'].lower()}. Thành phần: {', '.join(i[1] for i in p['ings'])}. Uống: {p['time'].lower()}.")
_ch = {'youtube': 'Kênh YouTube', 'facebook': 'Fanpage Facebook', 'tiktok': 'Kênh TikTok'}
L += ["", "## Thông tin thương hiệu", f"- [Giới thiệu QHUB HERBAL]({site['domain']}/gioi-thieu/)"] + [f"- [{_ch[k]} chính thức]({u})" for k, u in site.get('social', {}).items() if u] + ["", "## Kiến thức"]
L += [f"- [{v}]({site['domain']}/kien-thuc/chu-de/{k}/)" for k, v, n in post_cats]
L += [f"- [Bài viết về {p['name']}]({site['domain']}/kien-thuc/tra/{p['slug']}/)" for p in products]
L += ["", "## Bài viết nổi bật"] + [f"- [{a['title']}]({site['domain']}/kien-thuc/{a['slug']}/): {a['desc']}" for a in POSTS if a['cat_slug'] in ('top', 'san-pham')][:80]
open(os.path.join(OUT, 'llms.txt'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')

# chuyển ảnh nặng sang project media (giữ zip web chính nhỏ)
MI = os.path.join(ROOT, 'imgsite/img'); os.makedirs(MI, exist_ok=True)
for fn in os.listdir(os.path.join(OUT, 'assets/img')):
    full = os.path.join(OUT, 'assets/img', fn)
    if any(fn.startswith(m.rstrip('/')) for m in MOVE):
        dst = os.path.join(MI, fn)
        if os.path.isdir(full):
            if os.path.exists(dst): shutil.rmtree(dst)
            shutil.copytree(full, dst); shutil.rmtree(full)
        else:
            shutil.copy2(full, dst); os.remove(full)

# ---- Google Merchant Center feed ----
from xml.sax.saxutils import escape as _x
_fi = ['<?xml version="1.0" encoding="UTF-8"?>', '<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0"><channel>',
       f'<title>QHUB HERBAL</title><link>{site["domain"]}/</link><description>Trà thảo mộc túi lọc QHUB HERBAL</description>']
for p in products:
    _d = f"{p['name']} – {p['tagline']} Thành phần: {', '.join(i[1] for i in p['ings'])}. Hộp 30 túi lọc × 3 g, không thêm đường. {site['disclaimer']}"
    _fi.append('<item>' + ''.join([
        f"<g:id>{p['gtin']}</g:id>", f"<title>{_x(p['name'] + ' – Trà thảo mộc túi lọc QHUB HERBAL hộp 30 túi')}</title>",
        f"<description>{_x(_d)}</description>", f"<link>{site['domain']}/san-pham/{p['slug']}/</link>",
        f"<g:image_link>{site['media_img']}/img/products/{p['slug']}.webp</g:image_link>",
        f"<g:additional_image_link>{site['media_img']}/img/products/{p['slug']}-3d.webp</g:additional_image_link>",
        "<g:availability>in_stock</g:availability>", "<g:condition>new</g:condition>",
        f"<g:price>{site['price_list']} VND</g:price>", f"<g:sale_price>{site['price_sale']} VND</g:sale_price>",
        "<g:brand>QHUB HERBAL</g:brand>", f"<g:gtin>{p['gtin']}</g:gtin>", "<g:identifier_exists>yes</g:identifier_exists>",
        "<g:google_product_category>2073</g:google_product_category>",
        "<g:product_type>Trà thảo mộc &gt; Trà túi lọc</g:product_type>",
        "<g:shipping><g:country>VN</g:country><g:price>0 VND</g:price>"
        f"<g:min_handling_time>{site['ship_handling'][0]}</g:min_handling_time><g:max_handling_time>{site['ship_handling'][1]}</g:max_handling_time>"
        f"<g:min_transit_time>{site['ship_transit'][0]}</g:min_transit_time><g:max_transit_time>{site['ship_transit'][1]}</g:max_transit_time></g:shipping>",
    ]) + '</item>')
_fi.append('</channel></rss>')
open(os.path.join(OUT, 'google-merchant-feed.xml'), 'w', encoding='utf-8').write('\n'.join(_fi) + '\n')
# sitemap, robots, headers
today = NOW.strftime('%Y-%m-%d')
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for pth in pages: sm.append(f'  <url><loc>{site["domain"]}{pth}</loc><lastmod>{today}</lastmod></url>')
sm.append('</urlset>')
open(os.path.join(OUT, 'sitemap.xml'), 'w').write('\n'.join(sm) + '\n')
open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nDisallow: /cam-on/\nSitemap: {site["domain"]}/sitemap.xml\n')
open(os.path.join(OUT, '_headers'), 'w').write("""/assets/fonts/*
  Cache-Control: public, max-age=31536000, immutable
/assets/img/*
  Cache-Control: public, max-age=2592000
/assets/css/*
  Cache-Control: public, max-age=3600
/assets/js/*
  Cache-Control: public, max-age=3600
/assets/order.html
  Cache-Control: public, max-age=600
/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
https://:project.pages.dev/*
  X-Robots-Tag: noindex
""")
# ---- Tách trang bài viết sang 2 dự án phụ (qhubherbal-kt1, qhubherbal-kt2) để zip web chính < 3,8 MB ----
NSHARD = 2
for i in range(NSHARD):
    d = os.path.join(ROOT, f'ktsite{i+1}')
    if os.path.exists(d): shutil.rmtree(d)
    os.makedirs(os.path.join(d, 'kien-thuc'))
    open(os.path.join(d, '_headers'), 'w').write("/*\n  X-Robots-Tag: noindex\n")
    open(os.path.join(d, 'index.html'), 'w').write('<!doctype html><meta charset="utf-8"><title>QHUB</title>')
    open(os.path.join(d, '404.html'), 'w').write('<!doctype html><meta charset="utf-8"><title>404</title>')
for a in POSTS:
    k = sum(map(ord, a['slug'])) % NSHARD
    src = os.path.join(OUT, 'kien-thuc', a['slug'])
    shutil.move(src, os.path.join(ROOT, f'ktsite{k+1}', 'kien-thuc', a['slug']))
open(os.path.join(OUT, '_routes.json'), 'w').write(json.dumps({"version": 1, "include": ["/kien-thuc/*"], "exclude": ["/kien-thuc/", "/kien-thuc/trang/*", "/kien-thuc/chu-de/*", "/kien-thuc/tra/*"]}))
open(os.path.join(OUT, '_worker.js'), 'w').write("""// Trang bài viết nằm ở dự án phụ; web chính chỉ chuyển tiếp nội bộ (URL giữ nguyên qhubherbal.com)
const SHARDS = ['https://qhubherbal-kt1.pages.dev', 'https://qhubherbal-kt2.pages.dev'];
export default {
  async fetch(request, env) {
    const res = await env.ASSETS.fetch(request);
    if (res.status !== 404) return res;
    const url = new URL(request.url);
    const m = url.pathname.match(/^\\/kien-thuc\\/([a-z0-9-]+)\\/?$/);
    if (!m) return res;
    let sum = 0; for (const ch of m[1]) sum += ch.charCodeAt(0);
    const origin = SHARDS[sum % SHARDS.length];
    const r = await fetch(origin + '/kien-thuc/' + m[1] + '/', { cf: { cacheTtl: 600, cacheEverything: true } });
    if (!r.ok) return res;
    const h = new Headers(r.headers); h.delete('x-robots-tag'); h.set('cache-control', 'public, max-age=600');
    return new Response(r.body, { status: 200, headers: h });
  }
};
""")
print('built', len(pages), 'pages ->', OUT)
