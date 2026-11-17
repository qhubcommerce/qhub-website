---
title: "Dữ liệu có cấu trúc (schema) cho website bán hàng"
slug: du-lieu-co-cau-truc-schema-cho-website-ban-hang
topic: website-seo
keyword: "schema website"
keywords: ["schema sản phẩm", "json-ld là gì", "schema product offer", "dữ liệu có cấu trúc google", "schema organization"]
description: "Schema website bán hàng cần những loại nào, viết JSON-LD ra sao, kiểm tra ở đâu. Kèm mẫu Product, Organization, Breadcrumb và lỗi hay gặp năm 2026."
date: 2026-11-18
updated: 2026-11-18
summary:
  - "Schema là đoạn mô tả bằng từ vựng chung của schema.org, thường viết dạng JSON-LD, giúp Google và các trợ lý AI hiểu trang đang nói về doanh nghiệp, sản phẩm, giá hay bài viết nào."
  - "Website bán hàng nên có tối thiểu Organization, Product kèm Offer, BreadcrumbList và Article cho bài viết; Product nên khai thêm phí giao hàng và chính sách đổi trả."
  - "Khoảng tháng 5/2026, theo Search Engine Roundtable và Search Engine Land, Google ngừng hiển thị kết quả FAQ dạng mở rộng cho mọi website, nên FAQPage không còn mang lại giao diện nổi bật trên Google."
  - "Kiểm tra schema bằng Rich Results Test, Schema Markup Validator và báo cáo trong Search Console; dữ liệu khai phải khớp với nội dung người xem thấy trên trang."
faq:
  - q: "Schema website là gì?"
    a: "Schema là một đoạn mã mô tả nội dung trang theo bộ từ vựng chung của schema.org, ví dụ đây là sản phẩm, giá bao nhiêu, thương hiệu nào. Người xem không thấy đoạn này, nhưng Google và các trợ lý AI đọc được. Cách viết Google khuyến nghị là JSON-LD đặt trong thẻ script."
  - q: "Website bán hàng nhỏ có cần schema không?"
    a: "Có, và không tốn nhiều công. Chỉ cần Organization ở trang chủ, Product kèm Offer ở trang sản phẩm, BreadcrumbList ở mọi trang con và Article ở bài viết là đã đủ phần cốt lõi. Nhiều nền tảng như WordPress với plugin SEO, Shopify, Haravan đã sinh sẵn một phần, anh chị chỉ cần kiểm tra và bổ sung."
  - q: "Còn nên dùng FAQPage không khi Google đã bỏ kết quả FAQ?"
    a: "Kết quả FAQ dạng mở rộng không còn hiện trên Google từ khoảng tháng 5/2026, theo Search Engine Roundtable. Nhưng phần hỏi đáp viết tốt vẫn giúp người đọc và giúp các trợ lý AI trích dẫn. Đội QHUB giữ phần hỏi đáp hiển thị trên trang; có khai FAQPage hay không là chuyện phụ, miễn nội dung khai khớp với nội dung hiển thị."
  - q: "Có nên tự thêm số sao đánh giá vào schema sản phẩm không?"
    a: "Chỉ khi trang thật sự có đánh giá của người mua, hiển thị công khai và đúng số lượng. Tự điền aggregateRating khi không có đánh giá là khai sai, vi phạm hướng dẫn của Google và có thể bị xử lý thủ công. Website mới chưa có đánh giá thì bỏ trống trường này."
  - q: "Schema có giúp ChatGPT hay Gemini nhắc tới thương hiệu không?"
    a: "Schema không phải công tắc bật lên là được nhắc. Nó giúp máy đọc đúng các dữ kiện như tên công ty, sản phẩm, giá, liên hệ và liên kết các kênh với nhau. Kết hợp với nội dung rõ ràng và được nơi khác nhắc tới, đây là một phần nền của GEO."
sources:
  - title: "Google Search Drops FAQ Rich Results In Search & Search Console – Search Engine Roundtable"
    url: "https://www.seroundtable.com/google-drops-faq-rich-results-41298.html"
  - title: "Google to no longer support FAQ rich results – Search Engine Land"
    url: "https://searchengineland.com/google-to-no-longer-support-faq-rich-results-476957"
  - title: "FAQ (FAQPage, Question, Answer) structured data – Google Search Central"
    url: "https://developers.google.com/search/docs/appearance/structured-data/faqpage"
  - title: "The rise and fall of FAQ schema – and what it means for SEO today – Search Engine Land"
    url: "https://searchengineland.com/faq-schema-rise-fall-seo-today-463993"
  - title: "New Ways to Add Shipping & Return Policies in Google Search (November 2025 Update) – Pemavor"
    url: "https://www.pemavor.com/?p=28384"
---

**Schema website là đoạn mô tả nội dung trang theo bộ từ vựng chung của schema.org, giúp Google và các trợ lý AI hiểu chính xác trang đang nói về doanh nghiệp nào, sản phẩm gì, giá bao nhiêu.** Với website bán hàng, anh chị chỉ cần làm chắc bốn loại: Organization cho doanh nghiệp, Product kèm Offer cho sản phẩm, BreadcrumbList cho đường dẫn, Article cho bài viết. Phần còn lại là kiểm tra định kỳ để dữ liệu khai luôn khớp với thứ người xem thấy.

Bài này đội QHUB viết từ chính việc làm schema cho qhub.com.vn và các trang sản phẩm QHUB HERBAL, kèm đoạn mã mẫu anh chị chép về sửa được ngay. Nếu anh chị đang dựng website từ đầu, có thể đọc trước bài [website bán hàng chuẩn SEO năm 2026](/kien-thuc/website-ban-hang-chuan-seo-nam-2026-huong-dan-tu-a-den-z/).

## Schema website là gì và vì sao web bán hàng cần?

Một trang sản phẩm với người đọc là ảnh, tên, giá, nút mua. Với máy, đó chỉ là một khối chữ. Máy phải đoán đâu là giá, đâu là giá gạch, đâu là tên thương hiệu. Schema bỏ bước đoán đó: anh chị nói thẳng với máy "đây là Product, tên là…, giá là 105.000 VND, còn hàng".

Vài khái niệm cần nắm:

- **schema.org** là bộ từ vựng chung do Google, Microsoft, Yahoo và Yandex cùng khởi xướng. Mỗi loại thông tin có một "kiểu" (type) như Product, Organization, Article, và các "thuộc tính" như name, price, brand.
- **JSON-LD** là cách viết schema thành một khối dữ liệu đặt trong thẻ `<script type="application/ld+json">`. Google khuyến nghị cách này vì tách riêng khỏi giao diện, dễ sửa.
- **Kết quả nhiều định dạng** (rich results) là kiểu hiển thị nổi bật trên Google như giá, tình trạng hàng, đường dẫn breadcrumb. Schema là điều kiện cần, nhưng Google không cam kết hiển thị.

Ba lý do web bán hàng nên làm:

1. **Hiển thị sản phẩm rõ hơn trên Google.** Trang sản phẩm có Product và Offer hợp lệ có cơ hội hiện giá, tình trạng hàng, phí giao.
2. **Máy hiểu đúng thực thể doanh nghiệp.** Organization với `sameAs` nối website, fanpage, gian hàng thành một hệ thống, tránh bị hiểu nhầm với một công ty trùng tên.
3. **Nền cho GEO.** GEO là tối ưu để trợ lý AI như ChatGPT, Gemini nhắc đúng thương hiệu. Dữ kiện có cấu trúc giúp chúng đọc đúng tên, sản phẩm, liên hệ. Đội mình đã viết kỹ phần này trong bài [GEO là gì](/kien-thuc/geo-la-gi-toi-uu-de-chatgpt-gemini-nhac-toi-thuong-hieu/).

## Website bán hàng cần những loại schema nào?

Không cần khai mọi thứ schema.org có. Bảng dưới là bộ tối thiểu đội QHUB dùng cho một web bán hàng vừa và nhỏ.

| Loại schema | Đặt ở trang nào | Thuộc tính quan trọng | Mức ưu tiên |
| --- | --- | --- | --- |
| Organization | Trang chủ, trang giới thiệu | name, url, logo, contactPoint, sameAs, address | Bắt buộc |
| WebSite | Trang chủ | name, url | Nên có |
| Product + Offer | Từng trang sản phẩm | name, image, brand, sku, gtin13, offers (price, priceCurrency, availability) | Bắt buộc |
| OfferShippingDetails | Trong Offer | shippingRate, shippingDestination, deliveryTime | Nên có |
| MerchantReturnPolicy | Trong Offer hoặc Organization | returnPolicyCategory, merchantReturnDays, returnFees | Nên có |
| BreadcrumbList | Mọi trang con | itemListElement theo thứ tự cấp | Nên có |
| Article / BlogPosting | Bài viết | headline, author, datePublished, dateModified, image | Bắt buộc với blog |
| Person | Trang tác giả | name, jobTitle, sameAs | Nên có nếu có tác giả thật |
| FAQPage | Trang có hỏi đáp | mainEntity | Tùy chọn từ 2026 |
| AggregateRating, Review | Trang sản phẩm | chỉ khi có đánh giá thật | Không tự điền |

Về chính sách giao hàng và đổi trả, theo Pemavor (cập nhật 11/2025), Google đã bổ sung cách khai các chính sách này ở cấp tổ chức, không nhất thiết lặp lại trong từng sản phẩm. Website ít sản phẩm như của đội mình vẫn khai thẳng trong Offer cho chắc. Anh chị có nhiều sản phẩm có thể cân nhắc khai một lần ở Organization, rồi kiểm tra lại trong Search Console.

## Mẫu JSON-LD cho trang sản phẩm: ví dụ thật từ QHUB HERBAL

Các trang sản phẩm QHUB HERBAL trên qhub.com.vn, ví dụ [Trà Dưỡng Tâm An](/tra-duong-tam-an.html), đang khai Product, Offer, phí giao, chính sách đổi trả và Breadcrumb. Dưới đây là đoạn rút gọn, đúng cấu trúc đang chạy. Anh chị thay tên, giá, ảnh, đường dẫn của mình.

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Trà Dưỡng Tâm An",
  "image": ["https://qhub.com.vn/g-dta-1.jpg"],
  "description": "Bốn vị tinh gọn: lạc tiên, tâm sen, đinh lăng, hoa cúc.",
  "brand": { "@type": "Brand", "name": "QHUB HERBAL" },
  "category": "Trà thảo mộc túi lọc",
  "offers": {
    "@type": "Offer",
    "url": "https://qhub.com.vn/tra-duong-tam-an.html",
    "priceCurrency": "VND",
    "price": "105000",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition",
    "shippingDetails": {
      "@type": "OfferShippingDetails",
      "shippingRate": { "@type": "MonetaryAmount", "value": "0", "currency": "VND" },
      "shippingDestination": { "@type": "DefinedRegion", "addressCountry": "VN" }
    },
    "hasMerchantReturnPolicy": {
      "@type": "MerchantReturnPolicy",
      "applicableCountry": "VN",
      "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
      "merchantReturnDays": 7
    }
  }
}
```

Vài điều đội mình cân nhắc khi viết đoạn này:

- **Giá trong schema là giá bán 105.000đ**, đúng con số hiển thị lớn nhất trên trang. Giá niêm yết 140.000đ chỉ hiện trên giao diện dạng giá gạch. Ưu đãi theo kênh (trên TikTok Shop và Shopee là mua 3 tặng 1, trên website qhubherbal.com là mua 2 tặng 1) được ghi bằng chữ trên trang, không nhét vào schema để tránh sai lệch.
- **Mô tả chỉ nói thành phần, không nói công dụng.** Trà là thực phẩm thông thường. Thứ gì không được viết trên trang thì cũng không được viết trong schema.
- **Không có aggregateRating.** Trang chưa có hệ thống đánh giá công khai, nên không khai số sao.
- **Có mã vạch thì khai gtin13.** Ví dụ [Trà Dưỡng Nhan](/tra-duong-nhan.html) có mã EAN-13 8936244311836, nên trường `gtin13` giúp Google ghép đúng sản phẩm giữa các nơi bán.

## Mẫu schema Organization và BreadcrumbList

Organization đặt ở trang chủ hoặc trang [giới thiệu](/gioi-thieu/). Đây là "chứng minh thư" của doanh nghiệp với máy.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://example.vn/#organization",
  "name": "Tên công ty đầy đủ",
  "alternateName": "Tên thương hiệu ngắn",
  "url": "https://example.vn/",
  "logo": "https://example.vn/logo.png",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+84-xxx-xxx-xxx",
    "contactType": "customer service",
    "areaServed": "VN",
    "availableLanguage": "vi"
  },
  "sameAs": [
    "https://www.facebook.com/ten-fanpage",
    "https://www.tiktok.com/@ten-kenh"
  ]
}
```

Hai điểm hay sai: `alternateName` chỉ ghi tên người ta thật sự gọi thương hiệu, không nhồi từ khóa; `sameAs` chỉ trỏ tới kênh chính chủ đang hoạt động.

BreadcrumbList mô tả đường dẫn từ trang chủ tới trang hiện tại:

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://example.vn/" },
    { "@type": "ListItem", "position": 2, "name": "Trà thảo mộc", "item": "https://example.vn/tra/" },
    { "@type": "ListItem", "position": 3, "name": "Tên sản phẩm", "item": "https://example.vn/tra/ten-san-pham/" }
  ]
}
```

Thứ tự trong breadcrumb nên khớp với cấu trúc danh mục thật của website. Cách chia danh mục, trang trụ cột, cụm bài, đội mình đã viết trong bài [cấu trúc website chuẩn SEO](/kien-thuc/cau-truc-website-chuan-seo-danh-muc-trang-tru-cot-cum-bai/).

## FAQPage năm 2026 còn đáng làm không?

Đây là câu nhiều anh chị hỏi nhất. Tóm tắt diễn biến:

- Năm 2023, Google thu hẹp kết quả FAQ dạng mở rộng, chỉ còn cho một số website chính phủ và y tế uy tín.
- Khoảng tháng 5/2026, theo Search Engine Roundtable và Search Engine Land, Google ngừng hẳn kết quả FAQ cho mọi website và bỏ báo cáo liên quan trong Search Console.

Nghĩa là khai FAQPage không còn đem lại khối hỏi đáp xổ xuống trên Google. Nhưng phần hỏi đáp hiển thị trên trang vẫn có giá trị: người đọc tìm được câu trả lời nhanh, và các trợ lý AI thường trích những câu trả lời ngắn, rõ. Cách đội QHUB đang làm:

1. Giữ phần hỏi đáp hiển thị ở cuối bài và trang sản phẩm, viết như người thật hỏi.
2. Không coi FAQPage là việc ưu tiên. Website nào đã có sẵn thì để, miễn nội dung khai khớp với nội dung hiển thị.
3. Dồn công sức vào Product, Organization, Article, là những loại vẫn được Google dùng.

Hướng dẫn chính thức về loại này vẫn nằm trên Google Search Central, anh chị đọc bản mới nhất trước khi quyết định.

## Kiểm tra schema ở đâu và bao lâu một lần?

| Công cụ | Dùng để làm gì | Khi nào dùng |
| --- | --- | --- |
| Rich Results Test của Google | Xem trang có đủ điều kiện cho kết quả nhiều định dạng không, báo lỗi và cảnh báo | Mỗi khi sửa mẫu trang |
| Schema Markup Validator (validator.schema.org) | Kiểm tra cú pháp theo schema.org, kể cả loại Google không dùng | Khi viết loại mới |
| Search Console, mục Cải tiến | Theo dõi lỗi trên toàn website theo thời gian | Mỗi tuần một lần |
| Xem mã nguồn trang | Chắc chắn JSON-LD có trong HTML trả về, không chỉ sinh ra sau khi chạy JavaScript | Sau mỗi lần đổi giao diện |

Nhịp đội mình áp dụng: sửa mẫu trang thì chạy Rich Results Test ngay với 2–3 trang đại diện; mỗi thứ Hai mở Search Console xem có lỗi mới không; mỗi lần đổi giá, đổi tình trạng hàng thì chắc chắn schema được cập nhật cùng lúc với giao diện.

## Lỗi hay gặp khi làm schema website bán hàng

- **Giá trong schema khác giá trên trang.** Sửa giá trên giao diện nhưng quên khối JSON-LD viết tay. Google có thể bỏ qua hoặc đánh dấu trang không đáng tin.
- **Tự điền số sao và số đánh giá** khi không có đánh giá thật. Đây là khai sai, rủi ro bị xử lý thủ công.
- **Khai nội dung không hiển thị.** Ví dụ khai FAQPage với câu hỏi không có trên trang, hoặc khai mô tả sản phẩm khác hẳn mô tả người xem đọc.
- **Viết công dụng vào description của Product.** Với thực phẩm, mỹ phẩm, lời gì không được nói trên trang thì cũng không được nói trong schema.
- **Thiếu priceCurrency hoặc viết giá có dấu chấm.** Giá nên là số thuần như `105000`, đơn vị `VND`.
- **Hai plugin cùng sinh schema** làm trang có hai khối Product mâu thuẫn. Kiểm tra mã nguồn để chỉ còn một nguồn.
- **Dùng `availability` InStock mãi** dù đã hết hàng.
- **Quên `@id`** nên Organization ở trang chủ và seller trong Offer không nối được với nhau.

Kinh nghiệm thực tế từ đội vận hành: website của đội QHUB sinh schema từ cùng một nguồn dữ liệu với giao diện. Giá, tên, ảnh nằm một chỗ, build ra cả trang lẫn JSON-LD. Nhờ vậy đổi giá một lần là cả hai cùng đổi. Nếu website của anh chị viết schema tay, hãy ghi vào quy trình: đổi giá trên trang thì đổi luôn trong khối JSON-LD.

## Việc cần làm ngay tuần này

1. Mở Rich Results Test, chạy thử trang chủ, một trang sản phẩm bán chạy và một bài viết. Ghi lại lỗi và cảnh báo.
2. Kiểm tra Product có đủ name, image, brand, offers với price, priceCurrency, availability; bổ sung gtin13 nếu có mã vạch.
3. Thêm phí giao hàng và chính sách đổi trả vào Offer, hoặc khai một lần ở Organization.
4. Xóa aggregateRating nếu trang không có đánh giá thật.
5. Rà Organization: tên, logo, liên hệ, sameAs trỏ đúng kênh chính chủ.
6. Bật lịch kiểm tra Search Console mỗi thứ Hai.

Các bài khác về website, SEO và GEO nằm trong chủ đề [website chuẩn SEO](/kien-thuc/chu-de/website-seo/). QHUB Commerce (qhub.com.vn) là đơn vị vận hành gian hàng đa sàn, có đội media, đội vận hành sàn, đội KOC và đội host livestream, và tự xây website cho chính thương hiệu trà của đội. Anh chị cần người cùng rà website bán hàng thì cứ trao đổi với đội.
