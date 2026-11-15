---
title: "Cấu trúc website chuẩn SEO: danh mục, trang trụ cột, cụm bài"
slug: cau-truc-website-chuan-seo-danh-muc-trang-tru-cot-cum-bai
topic: website-seo
keyword: "cấu trúc website seo"
keywords: ["cấu trúc website chuẩn seo", "trang trụ cột là gì", "cụm chủ đề topic cluster", "cấu trúc url chuẩn seo", "breadcrumb là gì"]
description: "Cấu trúc website SEO gồm trang chủ, danh mục, trang trụ cột và cụm bài nối nhau bằng liên kết nội bộ. Hướng dẫn theo Google, kèm sơ đồ mẫu và ví dụ thật."
date: 2026-11-16
updated: 2026-11-16
summary:
  - "Cấu trúc website SEO tốt là cách xếp trang theo tầng (trang chủ, danh mục, trang trụ cột, bài con) và nối chúng bằng liên kết nội bộ để Google lẫn khách đều hiểu trang nào nói về gì."
  - "Theo tài liệu Google Search Central, Google dùng liên kết để tìm trang mới và hiểu quan hệ giữa các trang, nên trang quan trọng phải được liên kết từ trang chủ hoặc menu."
  - "Google khuyên URL dùng từ dễ đọc, nối bằng dấu gạch ngang; breadcrumb nên phản ánh đường đi thường gặp của người dùng, không bắt buộc trùng cấu trúc URL."
  - "Mục Kiến thức của qhub.com.vn dùng URL phẳng /kien-thuc/<bài>/ và 15 trang chủ đề làm trang trụ cột, chủ đề được thể hiện qua breadcrumb và liên kết."
faq:
  - q: "Cấu trúc website SEO là gì?"
    a: "Là cách sắp xếp các trang của website thành từng tầng rõ ràng (trang chủ, danh mục, trang trụ cột, bài viết, sản phẩm) và nối chúng bằng menu, breadcrumb, liên kết trong bài. Cấu trúc tốt giúp Google tìm thấy trang nhanh hơn, hiểu trang nào quan trọng, và giúp khách không bị lạc."
  - q: "Trang trụ cột (pillar page) khác bài viết thường thế nào?"
    a: "Trang trụ cột nói tổng quan một chủ đề lớn và dẫn tới tất cả bài con trong chủ đề đó. Bài con đi sâu vào một câu hỏi cụ thể và liên kết ngược về trang trụ cột. Một chủ đề chỉ nên có một trang trụ cột."
  - q: "URL có nên chứa tên danh mục không?"
    a: "Không bắt buộc. Google chỉ khuyên URL đơn giản, dễ đọc, dùng dấu gạch ngang giữa các từ. URL phẳng (không lồng danh mục) giúp đổi chủ đề mà không phải đổi địa chỉ bài; URL có danh mục giúp người đọc nhìn là biết trang thuộc nhóm nào. Chọn một kiểu và giữ ổn định."
  - q: "Website nhỏ vài chục trang có cần làm cụm chủ đề không?"
    a: "Có, và càng làm sớm càng nhẹ. Chỉ cần 3–5 chủ đề, mỗi chủ đề một trang trụ cột và vài bài con liên kết qua lại. Khi website lớn lên, khung này giữ cho mọi bài mới đều có chỗ đứng."
  - q: "Breadcrumb có còn tác dụng khi Google không hiện trên điện thoại nữa?"
    a: "Vẫn có. Từ tháng 1/2025 Google chỉ rút gọn phần URL hiển thị trên kết quả di động, còn breadcrumb trên trang vẫn giúp khách quay lại danh mục và giúp Google hiểu thứ bậc trang. Dữ liệu có cấu trúc BreadcrumbList vẫn được Google hỗ trợ."
sources:
  - title: "Help Google understand your ecommerce website structure – Google Search Central"
    url: "https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure"
  - title: "URL structure best practices for Google Search – Google Search Central"
    url: "https://developers.google.com/search/docs/crawling-indexing/url-structure"
  - title: "Link best practices for Google – Google Search Central"
    url: "https://developers.google.com/search/docs/crawling-indexing/links-crawlable"
  - title: "Breadcrumb (BreadcrumbList) structured data – Google Search Central"
    url: "https://developers.google.com/search/docs/appearance/structured-data/breadcrumb"
  - title: "Simplifying the visible URL element on mobile search results – Google Search Central Blog (01/2025)"
    url: "https://developers.google.com/search/blog/2025/01/simplifying-breadcrumbs"
  - title: "SEO Starter Guide – Google Search Central"
    url: "https://developers.google.com/search/docs/fundamentals/seo-starter-guide"
---

**Cấu trúc website SEO là cách xếp các trang thành từng tầng rõ ràng (trang chủ, danh mục, trang trụ cột, bài con, sản phẩm) rồi nối chúng bằng menu, breadcrumb và liên kết nội bộ, để Google và khách hàng đều hiểu trang nào nói về gì, trang nào quan trọng.** Không có một sơ đồ "chuẩn" duy nhất. Nhưng có vài nguyên tắc Google viết rõ trong tài liệu chính thức, và có một khung đơn giản mà doanh nghiệp nào cũng áp dụng được.

Bài này đội QHUB viết từ chính việc dựng hai website đang chạy: mục Kiến thức của qhub.com.vn và web bán hàng của thương hiệu trà QHUB HERBAL. Mình sẽ đi qua từng tầng, cách đặt URL, cách nối bài, và những lỗi hay gặp khi website lớn dần.

## Cấu trúc website SEO là gì và vì sao Google quan tâm?

Google không "đọc" website theo kiểu lật từng trang trong sổ. Nó đi theo liên kết. Trong tài liệu hướng dẫn cho website thương mại điện tử, Google Search Central viết rằng Google dựa vào liên kết giữa các trang để tìm trang mới và đoán trang nào là nội dung quan trọng nhất. Menu, liên kết chéo giữa các trang vì thế ảnh hưởng trực tiếp tới cách Google hiểu website của anh chị.

Từ đó có ba hệ quả rất thực tế:

- **Trang không có liên kết trỏ tới thì gần như vô hình.** Tài liệu "Link best practices" của Google nói rõ mỗi trang anh chị quan tâm nên có ít nhất một liên kết từ trang khác trên chính website.
- **Trang càng gần trang chủ, càng được coi là quan trọng.** Google khuyên các trang quan trọng nhất (danh mục chính, sản phẩm chủ lực) nên được liên kết từ trang chủ.
- **Chữ trên liên kết (anchor text) là gợi ý về nội dung trang đích.** Viết "xem bảng phí sàn Shopee 2026" tốt hơn nhiều so với "bấm vào đây".

Với khách hàng, cấu trúc tốt nghĩa là ba câu hỏi luôn có câu trả lời: "Mình đang ở đâu?", "Còn gì liên quan?", "Muốn mua thì bấm đâu?". Một website trả lời được ba câu đó thường cũng là website Google hiểu dễ nhất.

## Bốn tầng của một website: trang chủ, danh mục, trang trụ cột, bài con

Đội mình hay chia website doanh nghiệp thành bốn tầng. Mỗi tầng có một việc riêng. Lẫn việc giữa các tầng là gốc của rất nhiều lỗi SEO.

| Tầng | Vai trò | Ví dụ trên website bán trà | Nên liên kết tới |
| --- | --- | --- | --- |
| Trang chủ | Cho biết doanh nghiệp là ai, dẫn tới các nhóm chính | Trang chủ thương hiệu | Danh mục sản phẩm, trang trụ cột, sản phẩm chủ lực |
| Danh mục | Gom các trang cùng loại để khách duyệt và lọc | Tất cả sản phẩm, chuyên mục bài viết | Từng sản phẩm hoặc từng bài trong nhóm |
| Trang trụ cột | Nói tổng quan một chủ đề, dẫn tới mọi bài con | Trang tổng hợp "pha trà túi lọc" | Toàn bộ bài con trong cụm, sản phẩm liên quan |
| Bài con, sản phẩm | Trả lời một câu hỏi hoặc bán một món cụ thể | Bài "cách bảo quản trà khô", trang một hộp trà | Trang trụ cột, 2–3 bài cùng cụm, sản phẩm phù hợp |

**Trang trụ cột (pillar page)** là trang tổng quan của một chủ đề lớn, liệt kê và dẫn tới tất cả bài con trong chủ đề đó. **Cụm bài (topic cluster)** là nhóm gồm một trang trụ cột và các bài con xoay quanh nó, liên kết qua lại với nhau. Hai khái niệm này không phải thuật ngữ của Google. Đây là cách làm của người làm nội dung để hiện thực hóa đúng điều Google mô tả: nhóm các trang cùng chủ đề lại, nối chúng bằng liên kết có nghĩa.

Danh mục và trang trụ cột nhiều khi là một. Trên website bán hàng, trang danh mục "Quà tặng" vừa là nơi khách lọc sản phẩm, vừa có thể là trang trụ cột cho cụm bài "chọn quà". Trên blog, trang chủ đề chính là trang trụ cột.

## Sơ đồ mẫu cho website doanh nghiệp bán hàng

Dưới đây là khung đội QHUB dùng khi dựng hoặc rà lại website bán hàng. Anh chị vẽ lại bằng giấy bút trước khi đụng tới giao diện.

```
Trang chủ
├── Sản phẩm (danh mục tổng)
│   ├── Nhóm sản phẩm A
│   │   └── Trang sản phẩm
│   └── Nhóm sản phẩm B
│       └── Trang sản phẩm
├── Kiến thức (blog)
│   ├── Chủ đề 1 = trang trụ cột
│   │   └── Bài con 1.1, 1.2, 1.3…
│   └── Chủ đề 2 = trang trụ cột
│       └── Bài con 2.1, 2.2…
├── Giới thiệu, tác giả
└── Liên hệ, chính sách
```

Ba nguyên tắc đi kèm sơ đồ:

1. **Mọi trang quan trọng nằm trong khoảng ba lần bấm tính từ trang chủ.** Đây không phải con số của Google, chỉ là thước đo đội mình dùng để tránh trang bị chôn quá sâu.
2. **Một bài chỉ thuộc một chủ đề chính.** Bài có thể liên kết sang chủ đề khác, nhưng breadcrumb và trang trụ cột chỉ nhận một "nhà".
3. **Một từ khóa chính chỉ có một trang đích.** Hai trang cùng nhắm một ý định tìm kiếm sẽ tự giành nhau. Bài [nghiên cứu từ khóa cho website doanh nghiệp](/kien-thuc/nghien-cuu-tu-khoa-cho-website-doanh-nghiep/) có cách gom từ khóa thành cụm trước khi viết.

Website nhỏ, dưới 50 trang, có thể bỏ tầng nhóm sản phẩm, đi thẳng từ "Sản phẩm" xuống từng trang. Nhưng phần Kiến thức thì nên chia chủ đề ngay từ bài đầu tiên. Thêm chủ đề sau khi đã có 200 bài là việc rất mệt.

## Cấu trúc URL chuẩn SEO đặt thế nào?

Tài liệu "URL structure best practices" của Google Search Central gói gọn trong vài ý: URL nên đơn giản, dùng từ dễ đọc thay vì chuỗi số ID dài, nối các từ bằng dấu gạch ngang (-) thay vì gạch dưới (_), và dùng mã hóa UTF-8 khi có ký tự ngoài bảng chữ Latin cơ bản. Với website tiếng Việt, cách phổ biến nhất là bỏ dấu và viết thường, ví dụ `cau-truc-website-chuan-seo`.

Câu hỏi đội mình hay nhận nhất là: có nên lồng danh mục vào URL không? Có hai kiểu, kiểu nào cũng dùng được.

| Kiểu URL | Ví dụ | Ưu điểm | Nhược điểm |
| --- | --- | --- | --- |
| Phẳng | /kien-thuc/ten-bai/ | Đổi chủ đề không phải đổi URL, URL ngắn | Nhìn URL không biết bài thuộc nhóm nào |
| Lồng danh mục | /san-pham/ten-san-pham/ | Người đọc biết ngay đang ở nhóm nào | Đổi danh mục phải đổi URL và đặt chuyển hướng |

Nguyên tắc quan trọng hơn kiểu nào là **giữ ổn định**. Mỗi lần đổi URL, anh chị phải đặt chuyển hướng 301 (chuyển hướng vĩnh viễn) từ địa chỉ cũ sang mới, sửa liên kết nội bộ, cập nhật sitemap. Làm sai một bước là mất trang đã có thứ hạng.

Thêm vài lưu ý nhỏ: không dùng ngày tháng trong URL bài kiến thức nếu định cập nhật bài hằng năm, không để tham số lọc, sắp xếp (?sort=, ?color=) tạo ra hàng trăm URL trùng nội dung, và mỗi trang chỉ có một địa chỉ chính thức (canonical).

## Breadcrumb và liên kết nội bộ nối các tầng với nhau ra sao?

**Breadcrumb** là dòng đường dẫn nhỏ phía trên trang, kiểu "Trang chủ › Kiến thức › Website chuẩn SEO › Tên bài". Nó cho khách biết mình đang ở đâu và quay lại danh mục bằng một cú bấm. Google hỗ trợ đánh dấu breadcrumb bằng dữ liệu có cấu trúc kiểu BreadcrumbList. Trong tài liệu về breadcrumb, Google khuyên breadcrumb nên thể hiện đường đi thường gặp của người dùng tới trang, chứ không nhất thiết phải chép y nguyên cấu trúc URL.

Một thay đổi cần biết: tháng 1/2025, Google thông báo trên blog Search Central rằng kết quả tìm kiếm trên điện thoại chỉ còn hiện tên miền, không hiện breadcrumb nữa; trên máy tính vẫn hiện. Điều đó không làm breadcrumb mất giá trị. Breadcrumb trên trang vẫn là một dạng liên kết nội bộ giúp Google hiểu thứ bậc, và vẫn giúp khách đi lại.

Ngoài breadcrumb, các tầng được nối bằng ba loại liên kết:

- **Liên kết dọc:** bài con trỏ lên trang trụ cột, trang trụ cột trỏ xuống mọi bài con. Đây là xương sống của cụm.
- **Liên kết ngang:** bài con trỏ sang 2–3 bài cùng cụm, đặt đúng chỗ người đọc cần ("muốn tính phí trên từng đơn, xem bài…").
- **Liên kết sang trang bán hàng:** bài kiến thức trỏ tới sản phẩm hoặc dịch vụ liên quan, trang sản phẩm trỏ ngược về bài hướng dẫn trước khi mua.

Tài liệu "Link best practices" của Google còn một yêu cầu kỹ thuật dễ bị bỏ qua: liên kết phải là thẻ `<a href="…">` thật. Nút bấm chỉ chạy bằng JavaScript mà không có href thì Google không chắc đi theo được. Bài [website bán hàng chuẩn SEO từ A đến Z](/kien-thuc/website-ban-hang-chuan-seo-nam-2026-huong-dan-tu-a-den-z/) có checklist kỹ thuật đầy đủ cho phần này.

## Ví dụ thật: cấu trúc của qhub.com.vn và qhubherbal.com

Mình lấy chính hai website đội QHUB đang vận hành để minh họa. Phần dưới chỉ mô tả cấu trúc, không nói về lượt truy cập.

### Mục Kiến thức của qhub.com.vn: URL phẳng, chủ đề là trang trụ cột

- Trang `/kien-thuc/` là danh mục tổng, liệt kê 15 chủ đề và các bài mới.
- Mỗi chủ đề có một trang riêng dạng `/kien-thuc/chu-de/<chủ đề>/`, ví dụ trang chủ đề [Website chuẩn SEO](/kien-thuc/chu-de/website-seo/). Đây là trang trụ cột của cụm.
- Mỗi bài có URL phẳng `/kien-thuc/<tên-bài>/`, không lồng tên chủ đề. Chủ đề được thể hiện qua breadcrumb "Trang chủ › Kiến thức › Tên chủ đề › Tên bài", có đánh dấu BreadcrumbList.
- Mỗi bài liên kết về trang chủ đề, sang vài bài cùng cụm và tới trang dịch vụ liên quan.

Lý do chọn URL phẳng: khi số bài tăng, đội mình có thể tách một chủ đề lớn thành hai mà không phải đổi URL của bài nào. Chỉ cần sửa breadcrumb và trang chủ đề.

### Web bán hàng qhubherbal.com: hai cửa vào cho cùng một kho bài

Website của thương hiệu trà QHUB HERBAL (https://qhubherbal.com/) có cấu trúc khác vì mục tiêu chính là bán hàng:

- Trang chủ dẫn tới danh mục `/san-pham/`, mỗi sản phẩm có URL lồng dạng `/san-pham/<tên>/`, breadcrumb "Trang chủ › Sản phẩm › Tên sản phẩm".
- Mục Kiến thức có hàng trăm bài, được gom theo hai cách. Theo chuyên mục (cẩm nang, thảo mộc, sản phẩm, câu chuyện, top) ở `/kien-thuc/chu-de/<chuyên mục>/`. Và theo từng sản phẩm ở `/kien-thuc/tra/<tên sản phẩm>/`.
- Bài viết có khung mua hàng chèn vào giữa bài, trang sản phẩm dẫn ngược về các bài liên quan.

Trên qhub.com.vn, trang tổng [QHUB HERBAL](/qhub-herbal.html) đóng vai danh mục cho 7 trang sản phẩm, breadcrumb "QHUB Commerce › QHUB HERBAL › Tên sản phẩm". Như vậy cùng một thương hiệu nhưng hai website có hai cách đặt URL khác nhau, và cả hai đều ổn vì mỗi bên giữ một quy tắc nhất quán.

Một quyết định đáng chú ý khi dựng cấu trúc cho web trà: đội mình không tạo danh mục hay cụm bài nhắm vào từ khóa công dụng chữa bệnh, vì trà là thực phẩm thông thường. Cấu trúc website phải đi cùng quy định quảng cáo của ngành, không chỉ đi theo lượng tìm kiếm.

## Lỗi hay gặp khi dựng cấu trúc website

- **Trang mồ côi.** Bài đăng xong không nằm trong chủ đề nào, không bài nào trỏ tới. Google có thể vẫn tìm thấy qua sitemap, nhưng không hiểu nó quan trọng ra sao.
- **Hai trang cùng nhắm một từ khóa.** Thường gặp khi viết bài mới mà không kiểm tra bài cũ. Cách sửa: gộp nội dung vào trang tốt hơn, chuyển hướng 301 trang còn lại.
- **Chủ đề quá nhiều, mỗi chủ đề vài bài.** Hai mươi chủ đề, mỗi cái hai bài thì chẳng cụm nào đủ sâu. Nên bắt đầu với 3–5 chủ đề, đủ 8–10 bài mới mở chủ đề mới.
- **Menu chỉ chạy bằng JavaScript.** Nhìn đẹp nhưng không có thẻ `<a href>` thật, Google có thể không đi theo được.
- **Đổi URL hàng loạt khi đổi giao diện.** Không đặt chuyển hướng là mất thứ hạng đã tích lũy. Trước khi đổi nền tảng, xuất danh sách URL cũ ra bảng tính và ghép từng URL với địa chỉ mới.
- **Tham số lọc sinh URL trùng.** Trang danh mục có bộ lọc màu, giá, sắp xếp có thể tạo ra hàng nghìn URL gần giống nhau. Cần canonical về trang gốc hoặc hạn chế cho Google thu thập các URL lọc không cần thiết.

## Kinh nghiệm thực tế từ đội vận hành

**Vẽ sơ đồ trước khi viết bài thứ nhất.** Khi dựng mục Kiến thức cho qhub.com.vn, đội mình lên danh sách chủ đề và slug cho cả kế hoạch trong một bảng tính, mỗi dòng ghi chủ đề, từ khóa chính và slug. Nhờ vậy mỗi bài mới đều có sẵn "nhà" và không trùng từ khóa với bài khác.

**Trang trụ cột phải được chăm như một bài viết.** Nhiều website để trang chủ đề chỉ là danh sách tiêu đề. Trang trụ cột tốt nên có đoạn mô tả chủ đề, nhóm bài theo thứ tự đọc hợp lý và dẫn tới trang dịch vụ hoặc sản phẩm.

**Mỗi tuần rà lại liên kết của bài mới.** Bài mới đăng cần liên kết đi (tới trang trụ cột, bài cùng cụm) và liên kết về (sửa 1–2 bài cũ để trỏ tới bài mới). Việc thứ hai hay bị quên nhất.

**Cấu trúc tốt giúp cả AI.** Các trợ lý như ChatGPT, Gemini và Chế độ AI của Google đọc website như một người đọc kỹ: trang có thứ bậc rõ, câu định nghĩa rõ và nguồn rõ thì dễ được trích dẫn hơn. Bài [GEO là gì](/kien-thuc/geo-la-gi-toi-uu-de-chatgpt-gemini-nhac-toi-thuong-hieu/) nói kỹ hơn về phần này.

## Việc cần làm ngay tuần này

1. In danh sách toàn bộ trang của website (lấy từ sitemap hoặc Google Search Console), xếp từng trang vào một trong bốn tầng.
2. Chọn 3–5 chủ đề chính cho phần nội dung, mỗi chủ đề chỉ định một trang trụ cột.
3. Tìm các trang mồ côi và các cặp trang trùng từ khóa, quyết định gộp hay tách.
4. Kiểm tra breadcrumb và dữ liệu BreadcrumbList trên một trang bài, một trang sản phẩm bằng công cụ Rich Results Test của Google.
5. Với mỗi bài mới trong tuần, thêm ít nhất một liên kết từ bài cũ trỏ tới nó.

Xem thêm các bài khác trong chủ đề [Website chuẩn SEO](/kien-thuc/chu-de/website-seo/). QHUB Commerce vận hành gian hàng đa sàn và website cho doanh nghiệp, có đội media, đội vận hành sàn, đội KOC và đội host livestream.
