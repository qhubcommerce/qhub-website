import json, re, html, os
SITE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src=open(f'{SITE}/qhub-herbal.html',encoding='utf-8').read()
V=re.search(r'styles\.css\?v=([A-Za-z0-9]+)',open(f'{SITE}/index.html',encoding='utf-8').read()).group(1)
tail=src[src.index('<div class="modal" id="order-modal"'):src.index('<script src="products.js?v=')]

# parse products.js with node for exactness
import subprocess
out=subprocess.check_output(['node','-e',"global.window={};eval(require('fs').readFileSync('%s/products.js','utf8'));console.log(JSON.stringify(window.QHUB_HERBAL))"%SITE])
H=json.loads(out)
P=H['products']
e=html.escape

STORY={
'dhc':["Những đêm thức khuya, bữa tiệc kéo dài, đồ chiên nướng, cay nóng và vài ly cho trọn cuộc vui. Nhịp sống ấy quen thuộc với rất nhiều người, nhất là những ai thường xuyên gặp gỡ, tiếp khách.",
       "Trà Cà Gai – Diệp Hạ Châu phối cà gai leo và diệp hạ châu, hai vị quen thuộc trong y văn phương Đông, cùng xạ đen, an xoa, giảo cổ lam. Cỏ ngọt cho trà hậu ngọt tự nhiên mà không cần thêm đường. Một thói quen nhẹ nhàng để cân bằng lại sau những ngày nhiều cuộc hẹn."],
'nv':["Phong độ là nhất thời, phong thái mới là thứ ở lại. Sự vững vàng của người đàn ông hiện ra trong ánh mắt, dáng đứng và sự tự tin bên người mình thương.",
      "Trà Nam Vương phối bảy vị thảo mộc phương Đông: ba kích, nhục thung dung, nấm ngọc cẩu, kim tiền thảo, dứa dại, mú từn và cỏ ngọt. Đóng túi lọc tiện pha, đây là thói quen chăm sóc bản thân gọn gàng giữa lịch làm việc bận rộn, và cũng là món quà biếu tinh tế."],
'xht':["Giấc ngủ là lúc cơ thể làm những việc quan trọng nhất của một ngày. Một buổi tối được thả lỏng đúng cách thường bắt đầu từ vài thói quen nhỏ: tắt bớt màn hình, giảm ánh sáng, và một tách trà ấm.",
       "Trà Xấu Hổ Tím – Tâm Sen phối xấu hổ tím, tâm sen, lạc tiên cùng đinh lăng và hoa cúc vàng. Hương cúc dịu, vị thanh của tâm sen, hậu ngọt nhẹ từ cỏ ngọt — một tách trà để khép lại ngày dài."],
'ndv':["Những ngày ấy đến đều đặn mỗi tháng. Không tránh được, nhưng có thể đón nhận nhẹ nhàng hơn: giữ ấm cơ thể, nghỉ ngơi nhiều hơn một chút, và một tách trà ấm được chuẩn bị sẵn.",
       "Trà Ngày Dâu Về phối gừng, ngải cứu, táo đỏ — những vị tính ấm — cùng ích mẫu, mâm xôi, cỏ máu, cam thảo và thiên niên kiện. Nếu bạn là người ở bên, một hộp trà là cách quan tâm không cần nhiều lời."],
'loi':["Một bữa tiệc thịnh soạn, một buổi lẩu nướng cùng bạn bè. Những món ngon khó lòng từ chối, và ta thường ăn nhiều hơn dự định.",
       "Trà Lá Ổi Mix Lá Sen có vị thanh mát của lá sen, hương ngũ cốc của gạo lứt rang, cùng lá ổi và giảo cổ lam. Ngọt nhẹ từ cỏ ngọt, không cần thêm đường — một tách trà dễ uống để khép lại bữa ăn."],
'dta':["Deadline, việc nhà, màn hình cả ngày. Tâm trí hiếm khi có lúc được nghỉ.",
       "Trà Dưỡng Tâm An là năm phút cho riêng mình: hương thơm hoa cúc, vị thanh của tâm sen, dịu nhẹ của lạc tiên, cùng đinh lăng. Bốn vị tinh gọn trong mỗi túi trà — một khoảng lặng để lắng lại, rồi bước tiếp nhẹ nhõm hơn."],
'dn':["Nét tươi tắn không đến từ một lớp phấn, mà từ những ngày ngủ đủ, ăn lành và lòng nhẹ nhõm. Giữa lịch làm việc kín, màn hình từ sáng đến tối và những ly trà sữa thay bữa phụ, người phụ nữ hiếm khi có vài phút cho riêng mình.",
      "Trà Dưỡng Nhan gói chín vị hoa và thảo mộc: hoa hồng, kỷ tử, táo đỏ, đông trùng hạ thảo, cùng hoa nhài, tía tô, lá sen, hoa cúc và cỏ ngọt. Hương hoa dịu ngọt, hậu ngọt thanh mà không thêm đường, không caffeine — năm phút mỗi ngày để nâng niu chính mình, và cũng là món quà tinh tế cho mẹ, vợ, bạn gái."],
}
vnd=lambda n:f"{n:,}".replace(',','.')+'đ'
pct=round((1-H['price']/H['priceOld'])*100)

def header():
    return '''<header class="site-header" id="top">
  <div class="wrap">
    <a class="brand" href="./" aria-label="QHUB Commerce — trang chủ">
      <img src="/logo-qhub-white.png" alt="" width="45" height="48">
      <span>QHUB<small>COMMERCE</small></span>
    </a>
    <nav class="nav" id="nav" aria-label="Điều hướng">
      <a href="qhub-herbal.html#san-pham">Bảy vị trà</a>
      <a href="/kien-thuc/">Kiến thức</a>
      <a href="qhub-herbal.html">QHUB HERBAL</a>
      <a href="./#lam-gi">QHUB Commerce làm gì</a>
      <a href="./#dat-lich">Hợp tác cùng QHUB</a>
    </nav>
    <a class="btn btn-primary btn-sm" href="#mua">Mua ngay</a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="nav" aria-label="Mở menu">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
  </div>
</header>'''

def meta_desc(p):
    tail=f" {vnd(H['price'])}/hộp, mua 2 tặng 1, freeship, nhận hàng mới trả tiền."
    first=re.split(r'(?<=[.!?])\s',p['desc'])[0].rstrip('.')
    room=160-len(tail)
    if len(first)>room:
        first=first[:room].rsplit(' ',1)[0].rstrip(' ,:;')+'…'
    else:
        first+='.'
    return first+tail

def page(p):
    i=p['id']; url='https://qhub.com.vn/'+p['slug']
    gal=[(f'g-{i}-{k}.jpg',f"{p['name']} — {H['galleryLabels'][k]}",k==1) for k in range(1,6)]
    thumbs=''.join(f'<button type="button" data-src="{s}" data-alt="{e(a)}"aria-pressed="{"true" if n==0 else "false"}" aria-label="Xem ảnh: {e(a)}"><img src="{s}" alt="" loading="lazy" decoding="async"></button>' for n,(s,a,b) in enumerate(gal))
    ings=''.join((lambda m:f'<li><span>{e(m.group(1))}</span>'+(f'<b>{m.group(2)}</b>' if m.group(2) else '')+'</li>')(re.match(r'(.+?)(?: (\d+%))?$',x)) for x in p['ing'])
    ing_plain=', '.join(p['ing'])
    others=''.join(f'''<a class="mini" href="{o['slug']}" style="--pc:{o['color']};--pt:{o['tint']}"><span class="mi"><img src="g-{o['id']}-2.jpg" alt="" loading="lazy" decoding="async"></span><b>{e(o['name'])}</b><small>{e(o['tagline'])}</small></a>''' for o in P if o['id']!=i)
    ld={"@context":"https://schema.org","@type":"Product","name":p['name'],"sku":"QHH-"+i.upper(),
        "image":['https://qhub.com.vn/'+g[0] for g in gal],"description":p['desc'],
        "brand":{"@type":"Brand","name":"QHUB HERBAL","logo":"https://qhub.com.vn/herbal-symbol-forest.png"},"category":"Trà thảo mộc túi lọc",
        "manufacturer":{"@type":"Organization","name":"CÔNG TY TNHH QHUB COMMERCE","url":"https://qhub.com.vn/"},
        "offers":{"@type":"Offer","url":url,"priceCurrency":"VND","price":str(H['price']),"availability":"https://schema.org/InStock","itemCondition":"https://schema.org/NewCondition",
                  "seller":{"@id":"https://qhub.com.vn/#organization"},
                  "shippingDetails":{"@type":"OfferShippingDetails","shippingRate":{"@type":"MonetaryAmount","value":"0","currency":"VND"},
                      "shippingDestination":{"@type":"DefinedRegion","addressCountry":"VN"},
                      "deliveryTime":{"@type":"ShippingDeliveryTime","handlingTime":{"@type":"QuantitativeValue","minValue":0,"maxValue":1,"unitCode":"DAY"},"transitTime":{"@type":"QuantitativeValue","minValue":2,"maxValue":5,"unitCode":"DAY"}}},
                  "hasMerchantReturnPolicy":{"@type":"MerchantReturnPolicy","applicableCountry":"VN","returnPolicyCategory":"https://schema.org/MerchantReturnFiniteReturnWindow","merchantReturnDays":7,"returnMethod":"https://schema.org/ReturnByMail","returnFees":"https://schema.org/ReturnFeesCustomerResponsibility","merchantReturnLink":"https://qhub.com.vn/chinh-sach.html#doi-tra"}}}
    crumbs={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"QHUB Commerce","item":"https://qhub.com.vn/"},
        {"@type":"ListItem","position":2,"name":"QHUB HERBAL","item":"https://qhub.com.vn/qhub-herbal.html"},
        {"@type":"ListItem","position":3,"name":p['name'],"item":url}]}
    story=''.join(f'<p>{e(s)}</p>' for s in STORY[i])
    return f'''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(p['name'])} – trà thảo mộc QHUB HERBAL, mua 2 tặng 1</title>
<meta name="description" content="{e(meta_desc(p))}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="product">
<meta property="og:title" content="{e(p['name'])} — QHUB HERBAL">
<meta property="og:description" content="{e(p['tagline'])} {vnd(H['price'])}/hộp (giá gốc {vnd(H['priceOld'])}), mua 2 tặng 1.">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="QHUB Commerce">
<meta property="og:image" content="https://qhub.com.vn/g-{i}-1.jpg">
<meta name="theme-color" content="{p['color']}">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon-96x96.png" type="image/png" sizes="96x96">
<link rel="icon" href="/favicon-192x192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css?v={V}">
<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(crumbs,ensure_ascii=False)}</script>
</head>
<body class="h-body pd" style="--pc:{p['color']};--pt:{p['tint']}">
<a class="skip" href="#main">Bỏ qua tới nội dung</a>

{header()}

<main id="main">
<div class="wrap pd-crumb"><nav aria-label="Đường dẫn"><a href="./">QHUB Commerce</a><span aria-hidden="true">/</span><a href="qhub-herbal.html">QHUB HERBAL</a><span aria-hidden="true">/</span><span aria-current="page">{e(p['short'])}</span></nav></div>

<section class="pd-top" id="mua">
  <div class="wrap">
    <div class="pd-gallery">
      <div class="pd-main"><img src="g-{i}-1.jpg" alt="{e(p['name'])} — combo mua 2 tặng 1" width="1080" height="1080" fetchpriority="high"></div>
      <div class="pd-thumbs">{thumbs}</div>
    </div>
    <div class="pd-info">
      <p class="tag">{e(p['tagline'])}</p>
      <h1>{e(p['name'])}</h1>
      <p class="lead">{e(p['desc'])}</p>
      <div class="pd-price"><span class="now">{vnd(H['price'])}</span><span class="old">{vnd(H['priceOld'])}</span><span class="off">-{pct}%</span><span class="unit">/ hộp 30 túi lọc · Giá đã gồm thuế (nếu có), miễn phí giao hàng</span></div>
      <div class="pd-deal"><b>Mua 2 tặng 1</b><span>Cứ 2 hộp được tặng thêm 1 hộp. Hộp tặng được chọn vị khác.</span></div>
      <div class="pd-buy">
        <div class="qty" role="group" aria-label="Số hộp"><button type="button" id="pd-minus" aria-label="Bớt 1 hộp">−</button><input id="pd-qty" type="number" min="1" max="99" value="2" inputmode="numeric" aria-label="Số hộp mua"><button type="button" id="pd-plus" aria-label="Thêm 1 hộp">+</button></div>
        <button class="btn btn-forest" type="button" data-buy="{i}" data-qty="#pd-qty">Đặt mua</button>
      </div>
      <p class="pd-calc" id="pd-calc" aria-live="polite"></p>
      <a class="pd-zalo" href="https://zalo.me/0856510113" target="_blank" rel="noopener">Hoặc nhắn Zalo 0856 510 113 để được tư vấn</a>
      <dl class="pd-facts">
        <div><dt>Giao hàng</dt><dd>Miễn phí toàn quốc</dd></div>
        <div><dt>Thanh toán</dt><dd>Khi nhận hàng</dd></div>
        <div><dt>Đổi trả</dt><dd>Trong 7 ngày</dd></div>
      </dl>
    </div>
  </div>
</section>

<section class="pd-sec pd-inside">
  <div class="wrap pd-two">
    <div>
      <h2>Bên trong một túi trà</h2>
      <p class="sub">{len(p['ing'])} nguyên liệu thảo mộc. {"Thành phần và tỷ lệ được ghi rõ trên hộp." if any('%' in x for x in p['ing']) else "Thành phần được ghi rõ trên hộp."}</p>
      <ul class="pd-ing">{ings}</ul>
    </div>
    <figure class="pd-fig"><img src="g-{i}-2.jpg" alt="Thành phần {e(p['name'])}" loading="lazy" decoding="async" width="1080" height="1080"></figure>
  </div>
</section>

<section class="pd-sec pd-story">
  <div class="wrap pd-two rev">
    <figure class="pd-fig"><img src="g-{i}-3.jpg" alt="Lý do nên chọn {e(p['name'])}" loading="lazy" decoding="async" width="1080" height="1080"></figure>
    <div>
      <h2>{e(p['tagline'])}</h2>
      {story}
      <p class="pd-fit"><b>Phù hợp với</b>{e(p['fit'])}</p>
    </div>
  </div>
</section>

<section class="pd-sec pd-brew">
  <div class="wrap">
    <h2>Cách pha</h2>
    <ol class="pd-steps">
      <li><b>1 túi lọc</b><span>Cho vào cốc</span></li>
      <li><b>200 ml nước sôi</b><span>Ở 95–100 °C</span></li>
      <li><b>Hãm 5 phút</b><span>Cho trà ngấm đều</span></li>
      <li><b>Thưởng thức</b><span>Ngon nhất khi còn ấm</span></li>
    </ol>
  </div>
</section>

<section class="pd-sec pd-spec-wrap">
  <div class="wrap pd-two top">
    <div>
      <h2>Thông tin sản phẩm</h2>
      <dl class="pd-spec">
        <div><dt>Tên sản phẩm</dt><dd>{e(p['name'])}</dd></div>
        <div><dt>Loại</dt><dd>Trà thảo mộc túi lọc</dd></div>
        <div><dt>Thành phần</dt><dd>{e(ing_plain)}</dd></div>
        <div><dt>Quy cách</dt><dd>Hộp 30 gói × 3 g, khối lượng tịnh 90 g</dd></div>
        <div><dt>Cách dùng</dt><dd>Hãm 1 túi lọc với 200 ml nước sôi 95–100 °C trong 5 phút</dd></div>
        <div><dt>Bảo quản</dt><dd>Nơi khô ráo, thoáng mát, tránh ánh nắng trực tiếp</dd></div>
        <div><dt>Hạn sử dụng</dt><dd>24 tháng kể từ ngày sản xuất. Số lô, NSX, HSD in dưới đáy hộp</dd></div>
        <div><dt>Số tự công bố</dt><dd>{e(p['tcb'])}</dd></div>
        <div><dt>Xuất xứ</dt><dd>Việt Nam</dd></div>
        <div><dt>Thương hiệu</dt><dd>QHUB HERBAL — CÔNG TY TNHH QHUB COMMERCE</dd></div>
      </dl>
    </div>
    <aside class="pd-side">
      <div class="pd-note"><h3>Lưu ý khi dùng</h3><p>{e(p['note'])}</p><p class="dis">Sản phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh.</p></div>
      <div class="pd-promise">
        <h3>QHUB HERBAL cam kết</h3>
        <ul>
          <li><b>Chính hãng</b>Đúng bao bì, đúng thành phần in trên nhãn</li>
          <li><b>Miễn phí giao hàng toàn quốc</b>Thanh toán khi nhận hàng, được kiểm hàng trước khi trả tiền</li>
          <li><b>Hạn dùng rõ ràng</b>Số lô, ngày sản xuất, hạn dùng in dưới đáy hộp</li>
          <li><b>Đóng gói cẩn thận</b>Hộp cứng, chèn kỹ trước khi giao</li>
          <li><b>Đổi trả trong 7 ngày</b>Khi lỗi sản xuất, hộp móp méo, giao sai, hoặc khi đổi ý nếu hộp còn nguyên seal. <a href="chinh-sach.html#doi-tra">Xem chính sách</a></li>
          <li><b>Tư vấn tận tình</b>Giải đáp cách dùng trước và sau khi mua</li>
        </ul>
      </div>
    </aside>
  </div>
</section>

<section class="pd-sec pd-more-wrap">
  <div class="wrap">
    <div class="pd-more-head"><h2>Các vị khác của QHUB HERBAL</h2><a class="link-forest" href="qhub-herbal.html#san-pham">Xem cả bảy vị</a></div>
    <div class="pd-more">{others}</div>
  </div>
</section>
</main>

{tail}<script src="products.js?v={V}"></script>
<script src="main.js?v={V}"></script>
</body>
</html>
'''
for p in P:
    open(f"{SITE}/{p['slug']}",'w',encoding='utf-8').write(page(p))
    print('wrote',p['slug'])
