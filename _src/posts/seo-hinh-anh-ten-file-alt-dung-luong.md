---
title: "SEO hình ảnh: đặt tên file, viết alt, giảm dung lượng đúng cách"
slug: seo-hinh-anh-ten-file-alt-dung-luong
topic: website-seo
keyword: "seo hình ảnh"
keywords: ["thẻ alt hình ảnh", "đặt tên file ảnh chuẩn seo", "dung lượng ảnh website bao nhiêu", "ảnh webp avif", "sitemap hình ảnh"]
description: "SEO hình ảnh theo hướng dẫn Google: đặt tên file không dấu, viết alt đúng, nén WebP/AVIF, srcset, lazy load, giữ LCP dưới 2,5 giây. Kèm checklist và ví dụ thật."
date: 2026-11-24
updated: 2026-11-24
summary:
  - "SEO hình ảnh là làm cho Google hiểu ảnh có gì, đặt ở trang nào, và tải ảnh đủ nhanh: dùng thẻ img, tên file mô tả, chữ thay thế (alt), ảnh đặt cạnh nội dung liên quan và dung lượng vừa phải."
  - "Google Tìm kiếm hỗ trợ các định dạng BMP, GIF, JPEG, PNG, WebP, SVG và AVIF (AVIF được thêm từ tháng 8/2024); ảnh làm hình nền bằng CSS không được lập chỉ mục."
  - "Ảnh chính đầu trang thường quyết định LCP, chỉ số nên đạt từ 2,5 giây trở xuống; không lazy load ảnh này, khai sẵn chiều rộng, chiều cao và có thể đặt fetchpriority cao."
  - "Kinh nghiệm của đội QHUB: ảnh sản phẩm vuông 1080 px nên giữ khoảng 80–150 KB, tên file chữ thường không dấu nối bằng gạch ngang, alt mô tả đúng thứ trong ảnh trong khoảng một câu."
faq:
  - q: "Thẻ alt hình ảnh nên viết bao nhiêu chữ?"
    a: "Google không đặt giới hạn số chữ, nhưng alt nên ngắn gọn và mô tả đúng thứ có trong ảnh, thường một câu khoảng 5–15 chữ là đủ. Viết như đang tả ảnh cho người không nhìn thấy. Không liệt kê từ khóa và không bắt đầu bằng “hình ảnh của…”."
  - q: "Tên file ảnh có nên viết tiếng Việt có dấu không?"
    a: "Google chấp nhận tên file có ký tự UTF-8, nhưng khi lên đường dẫn, chữ có dấu sẽ bị mã hóa thành chuỗi khó đọc như %C3%A0. Đội QHUB khuyên đặt tên chữ thường, không dấu, nối các từ bằng gạch ngang, ví dụ tra-duong-nhan-hop-30-goi-mat-truoc.webp. Cách này dễ quản lý và không lỗi khi đổi máy chủ."
  - q: "Ảnh trên website nên nặng bao nhiêu KB?"
    a: "Google không đưa con số KB cố định, chỉ khuyên ảnh đúng kích thước hiển thị và nén tốt để trang tải nhanh. Kinh nghiệm thực tế của đội QHUB là ảnh sản phẩm 1080 × 1080 px giữ khoảng 80–150 KB, banner ngang khoảng 150–250 KB, ảnh nhỏ trong danh sách dưới 50 KB. Quan trọng hơn con số là ảnh chính không làm LCP vượt 2,5 giây."
  - q: "Có cần làm sitemap hình ảnh không?"
    a: "Không bắt buộc. Nếu ảnh nằm trong thẻ img trên trang mà Google thu thập được thì Google vẫn tìm thấy. Sitemap hình ảnh hữu ích khi ảnh được nạp bằng JavaScript hoặc website có rất nhiều ảnh. Từ năm 2022 Google chỉ còn đọc thẻ image:loc trong sitemap hình ảnh."
  - q: "Lazy load ảnh có hại cho SEO không?"
    a: "Lazy load (tải chậm, chỉ tải ảnh khi người xem cuộn tới) có lợi với ảnh nằm dưới màn hình đầu tiên. Nhưng nếu lazy load cả ảnh chính đầu trang, LCP sẽ chậm hơn. Cách làm đúng là để ảnh đầu trang tải ngay, các ảnh bên dưới mới dùng loading=“lazy”."
sources:
  - title: "Google image SEO best practices – Google Search Central"
    url: "https://developers.google.com/search/docs/appearance/google-images"
  - title: "Happy AVIFriday: Google Search now supports AVIF – Google Search Central Blog (08/2024)"
    url: "https://developers.google.com/search/blog/2024/08/happy-avifriday?hl=es"
  - title: "Image sitemaps – Google Search Central"
    url: "https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps?hl=ko"
  - title: "Spring cleaning: sitemap extensions – Google Search Central Blog (05/2022)"
    url: "https://developers.google.cn/search/blog/2022/05/spring-cleaning-sitemap-extensions"
  - title: "Largest Contentful Paint (LCP) – web.dev"
    url: "https://web.dev/articles/lcp"
  - title: "How the Core Web Vitals metrics thresholds were defined – web.dev"
    url: "https://web.dev/articles/defining-core-web-vitals-thresholds"
  - title: "The performance effects of too much lazy loading – web.dev"
    url: "https://web.dev/lcp-lazy-loading"
  - title: "Optimize image priority – Chrome for Developers"
    url: "https://developer.chrome.com/docs/modern-web-guidance/guides/performance/optimize-image-priority"
---

**SEO hình ảnh là làm cho Google hiểu đúng bức ảnh có gì, gắn với nội dung nào trên trang, đồng thời để ảnh tải đủ nhanh mà không kéo chậm cả trang.** Ba việc cụ thể nhất là đặt tên file mô tả, viết chữ thay thế (alt) đúng, và giảm dung lượng bằng định dạng nhẹ, kích thước vừa đủ. Làm tốt thì ảnh có cơ hội hiện trên Google Hình ảnh, trang sản phẩm tải nhanh hơn, và người dùng trình đọc màn hình cũng hiểu được trang.

Bài này đội QHUB tóm lại hướng dẫn chính thức của Google Search Central về ảnh, ngưỡng Core Web Vitals liên quan tới ảnh, quy ước đặt tên file tiếng Việt, cách viết alt có ví dụ đúng sai, và một ví dụ thật trên trang sản phẩm trà của chính đội mình. Các hướng dẫn được kiểm tra lại qua tìm kiếm ngày 24/11/2026.

## SEO hình ảnh là gì và Google đọc ảnh bằng cách nào?

Google không "nhìn" ảnh giống người. Để hiểu một bức ảnh, Google gom nhiều tín hiệu:

- **Thẻ HTML chứa ảnh.** Theo Google, ảnh phải nằm trong thẻ `<img>` (hoặc `<picture>` có thẻ `<img>` dự phòng). Ảnh làm hình nền bằng CSS không được lập chỉ mục.
- **Chữ thay thế (alt).** Đoạn chữ mô tả gắn vào ảnh. Google nói đây là thuộc tính quan trọng nhất khi cung cấp thông tin về ảnh, cùng với công nghệ thị giác máy tính và nội dung trang.
- **Tên file và đường dẫn.** Google gọi đây là "gợi ý nhẹ" về chủ đề ảnh.
- **Ngữ cảnh trang.** Tiêu đề trang, chú thích dưới ảnh, đoạn chữ xung quanh. Ảnh đặt ngay cạnh đoạn nói về nó dễ được hiểu đúng hơn ảnh nằm lạc ở cuối trang.
- **Dữ liệu có cấu trúc.** Ví dụ thuộc tính image trong schema Product giúp Google biết đâu là ảnh sản phẩm.

Một nguyên tắc Google nhắc nhiều lần: chữ quan trọng không nên chỉ nằm trong ảnh. Tên sản phẩm, giá, thành phần nên có bằng chữ trên trang, ảnh chỉ minh họa thêm.

## Đặt tên file ảnh chuẩn SEO cho website tiếng Việt

Google ví dụ: tên file "my-new-black-kitten.jpg" tốt hơn "IMG00023.JPG". Với website tiếng Việt, Google cho phép tên file có ký tự UTF-8 và khuyên dịch cả tên file khi làm trang nhiều ngôn ngữ. Nhưng trong thực tế, chữ có dấu khi lên đường dẫn sẽ thành chuỗi mã hóa khó đọc, dễ lỗi khi chuyển máy chủ hay đổi nền tảng.

Quy ước đội QHUB dùng cho mọi website mình làm:

1. **Chữ thường, không dấu.** "Trà Dưỡng Nhan" thành "tra-duong-nhan".
2. **Nối các từ bằng gạch ngang (-),** không dùng gạch dưới hay khoảng trắng. Google cũng khuyên dùng gạch ngang trong đường dẫn.
3. **Theo thứ tự: sản phẩm, thương hiệu nếu cần, chi tiết của ảnh.** Ví dụ: tra-duong-nhan-hop-30-goi-mat-truoc.webp.
4. **Ngắn, 3–7 từ.** Không nhồi từ khóa, không thêm "gia-re", "tot-nhat".
5. **Không trùng tên giữa các ảnh khác nhau.** Ảnh mặt trước và mặt sau phải khác tên.

| Tên file | Đánh giá | Lý do |
| --- | --- | --- |
| IMG_20261113_0931.jpg | Chưa tốt | Tên máy ảnh, không nói gì về nội dung |
| Trà Dưỡng Nhan mặt trước.jpg | Chưa tốt | Có dấu và khoảng trắng, đường dẫn bị mã hóa |
| tra_duong_nhan_1.jpg | Tạm được | Có tên sản phẩm nhưng dùng gạch dưới, thiếu chi tiết |
| tra-duong-nhan-hop-30-goi-mat-truoc.webp | Tốt | Mô tả rõ, không dấu, gạch ngang |
| tra-thao-moc-gia-re-tot-nhat-ha-noi.jpg | Không nên | Nhồi từ khóa, không mô tả ảnh |

Một lưu ý quan trọng: ảnh đã lên Google rồi thì đừng vội đổi tên hàng loạt. Đổi tên là đổi đường dẫn, Google phải thu thập và xử lý lại từ đầu. Quy ước này nên áp dụng cho ảnh mới, còn ảnh cũ chỉ đổi khi đằng nào cũng phải làm lại trang.

## Viết thẻ alt hình ảnh thế nào cho đúng?

Alt text (văn bản thay thế) là đoạn chữ đặt trong thuộc tính alt của thẻ ảnh. Nó dùng cho người khiếm thị nghe trình đọc màn hình, hiện ra khi ảnh không tải được, và giúp Google hiểu ảnh.

Cách viết dễ nhất: **tưởng tượng mình đang tả bức ảnh qua điện thoại cho một người không nhìn thấy.** Tả thứ có trong ảnh, đủ cụ thể, trong khoảng một câu.

Google đưa ví dụ về một chú chó: để trống là kém, "chó con" là tạm, "chó đốm con đang chơi nhặt bóng" là tốt, còn một chuỗi từ khóa dài là xấu. Áp vào ảnh sản phẩm:

| Alt | Đánh giá | Ghi chú |
| --- | --- | --- |
| (để trống) với ảnh sản phẩm chính | Kém | Google và trình đọc màn hình không biết ảnh có gì |
| "trà" | Chưa đủ | Quá chung |
| "Hộp Trà Dưỡng Nhan QHUB HERBAL 30 gói túi lọc, mặt trước" | Tốt | Đúng sản phẩm, đúng góc chụp |
| "trà dưỡng nhan, trà thảo mộc, trà túi lọc, trà ngon, mua trà" | Xấu | Nhồi từ khóa, có thể bị xem là spam |
| "Hình ảnh của sản phẩm trà" | Thừa | Trình đọc màn hình đã báo đây là ảnh |

Ba trường hợp đặc biệt:

- **Ảnh trang trí** (đường kẻ, họa tiết nền, icon lặp lại chữ bên cạnh) nên để `alt=""`. Trình đọc màn hình sẽ bỏ qua, người nghe không bị làm phiền.
- **Ảnh có chữ** (infographic, bảng thành phần) thì alt tóm ý chính của chữ trong ảnh, và phần chữ đầy đủ nên có trên trang.
- **Ngành thực phẩm, mỹ phẩm:** alt chỉ mô tả thứ nhìn thấy. Đừng viết công dụng vào alt kiểu "trà giúp ngủ ngon". Alt vẫn là nội dung trên trang, vẫn chịu quy định quảng cáo như mọi đoạn chữ khác.

## Giảm dung lượng ảnh: định dạng, kích thước, srcset

Ảnh nặng là thủ phạm hay gặp nhất làm trang chậm. Ba việc cần làm:

**1. Chọn định dạng phù hợp.** Google Tìm kiếm hỗ trợ BMP, GIF, JPEG, PNG, WebP, SVG và AVIF. AVIF được Google thêm vào danh sách từ tháng 8/2024. Thực tế dùng:

| Định dạng | Dùng cho | Ghi chú |
| --- | --- | --- |
| WebP | Ảnh sản phẩm, banner, ảnh bài viết | Nhẹ hơn JPEG đáng kể ở cùng chất lượng, trình duyệt phổ biến đều hỗ trợ |
| AVIF | Ảnh lớn cần nhẹ tối đa | Thường nén tốt hơn WebP, nhưng xuất file chậm hơn, nên có ảnh dự phòng |
| JPEG | Ảnh chụp khi nền tảng chưa hỗ trợ WebP | Nén chất lượng khoảng 75–85 là vừa |
| PNG | Ảnh cần nền trong suốt, ảnh chụp màn hình | Thường nặng với ảnh chụp thật |
| SVG | Logo, icon | Nhẹ, nét ở mọi kích thước |

**2. Xuất đúng kích thước hiển thị.** Khung ảnh chỉ rộng 800 px thì không cần tải ảnh rộng 4.000 px. Google khuyên dùng ảnh đáp ứng (responsive): thuộc tính `srcset` liệt kê vài bản ảnh khác cỡ, trình duyệt tự chọn bản vừa với màn hình. Ví dụ:

`<img src="tra-duong-nhan-hop-1080.webp" srcset="tra-duong-nhan-hop-540.webp 540w, tra-duong-nhan-hop-1080.webp 1080w" sizes="(max-width: 600px) 100vw, 540px" width="1080" height="1080" alt="Hộp Trà Dưỡng Nhan QHUB HERBAL 30 gói túi lọc, mặt trước">`

**3. Đặt mục tiêu dung lượng.** Google không công bố con số KB. Dưới đây là mức đội QHUB đặt cho các website mình làm, chỉ là kinh nghiệm để anh chị có mốc:

| Loại ảnh | Kích thước thường dùng | Dung lượng nên giữ |
| --- | --- | --- |
| Ảnh sản phẩm chính | 1080 × 1080 px | Khoảng 80–150 KB |
| Banner trang chủ | Rộng 1600–1920 px | Khoảng 150–250 KB |
| Ảnh trong bài viết | Rộng 800–1200 px | Khoảng 60–150 KB |
| Ảnh nhỏ trong danh sách | Rộng 300–400 px | Dưới 50 KB |
| Logo, icon | SVG | Vài KB |

## Ảnh và Core Web Vitals: giữ LCP dưới 2,5 giây

Core Web Vitals là bộ chỉ số trải nghiệm trang của Google. Chỉ số gắn chặt nhất với ảnh là LCP (Largest Contentful Paint, thời điểm khối nội dung lớn nhất trong màn hình đầu tiên hiện xong). Theo web.dev, LCP tốt là từ **2,5 giây trở xuống**, đo ở mức 75% lượt truy cập. Trên trang sản phẩm, khối lớn nhất gần như luôn là ảnh sản phẩm chính.

Bốn nguyên tắc cho ảnh đầu trang:

1. **Không lazy load ảnh đầu trang.** Lazy load giúp ảnh bên dưới không tải sớm, nhưng web.dev đã chỉ ra lazy load quá tay làm LCP chậm đi. Chỉ dùng `loading="lazy"` cho ảnh nằm dưới màn hình đầu tiên.
2. **Ưu tiên tải ảnh chính** bằng `fetchpriority="high"`, theo hướng dẫn tối ưu ưu tiên ảnh của Chrome.
3. **Khai chiều rộng, chiều cao** (`width`, `height`) để trình duyệt giữ chỗ trước, bố cục không bị xô, giúp chỉ số CLS (độ ổn định bố cục) đạt từ 0,1 trở xuống.
4. **Banner một ảnh tĩnh** thường tốt hơn slider năm ảnh tự chạy.

Cách đo và sửa từng chỉ số, anh chị xem bài [tốc độ website và Core Web Vitals](/kien-thuc/toc-do-website-va-core-web-vitals/).

## Sitemap hình ảnh có cần không?

Sitemap hình ảnh là phần khai báo thêm đường dẫn ảnh trong file sitemap. Không bắt buộc. Nếu ảnh nằm trong thẻ `<img>` trên trang mà Google thu thập được, Google vẫn tìm thấy ảnh.

Nên làm khi ảnh được nạp bằng JavaScript, nằm trên máy chủ ảnh riêng (CDN), hoặc website có hàng nghìn ảnh. Lưu ý từ tháng 5/2022 Google đã bỏ các thẻ phụ như chú thích (caption), tiêu đề (title), vị trí địa lý và giấy phép trong sitemap hình ảnh, chỉ còn đọc thẻ `image:loc`. Muốn mô tả ảnh thì dùng alt và chữ trên trang. Cách khai báo sitemap nói chung có trong bài [sitemap, robots.txt và llms.txt](/kien-thuc/sitemap-robots-txt-va-llms-txt-khai-bao-cho-google-va-ai/).

Một lỗi hay gặp liên quan: robots.txt chặn thư mục ảnh. Khi đó ảnh không bao giờ lên Google Hình ảnh, dù tên file và alt có chuẩn tới đâu.

## Ví dụ thật: ảnh hộp Trà Dưỡng Nhan trên qhub.com.vn

QHUB HERBAL là thương hiệu trà túi lọc do chính đội QHUB xây. Trang [Trà Dưỡng Nhan](/tra-duong-nhan.html), sản phẩm ra mắt ngày 13/11/2026, là ví dụ để anh chị xem cách đội mình đang làm, kể cả chỗ chưa tối ưu. Phần dưới chỉ nói về ảnh, không nói về công dụng sản phẩm.

**Đang làm được.** Trang có 5 ảnh sản phẩm định dạng JPEG, cùng kích thước 1080 × 1080 px, mỗi ảnh khoảng 130–140 KB. Ảnh chính khai sẵn chiều rộng, chiều cao và có `fetchpriority="high"` để tải trước. Các ảnh bên dưới và ảnh thu nhỏ dùng `loading="lazy"`. Ảnh thu nhỏ trùng với ảnh lớn nên để `alt=""`, tránh trình đọc màn hình đọc lại hai lần. Ảnh bảng thành phần có alt "Thành phần Trà Dưỡng Nhan". Cả 5 ảnh được khai trong thuộc tính image của schema Product.

**Chưa tối ưu.** Tên file đang rất ngắn kiểu g-dn-1.jpg, chỉ có nghĩa với nội bộ đội mình. Nếu đặt theo quy ước ở trên, ảnh hộp mặt trước sẽ là tra-duong-nhan-hop-30-goi-mat-truoc.webp, với alt "Hộp Trà Dưỡng Nhan QHUB HERBAL 30 gói túi lọc, mặt trước". Alt chỉ tả cái hộp: tên sản phẩm, thương hiệu, quy cách, góc chụp. Không có chữ nào về công dụng, vì trà là thực phẩm thông thường. Định dạng cũng có thể chuyển sang WebP để nhẹ hơn nữa. Theo đúng lưu ý ở mục đặt tên file, những thay đổi này hợp nhất để làm vào lần cập nhật trang tới, thay vì đổi tên ngay ảnh đã được Google thu thập.

Cách dựng phần còn lại của trang sản phẩm (tên, mô tả, giá, schema), anh chị đọc bài [trang sản phẩm chuẩn SEO trên website](/kien-thuc/trang-san-pham-chuan-seo-tren-website/).

## Lỗi hay gặp khi làm SEO hình ảnh

- **Tải nguyên file gốc 3–5 MB từ máy ảnh hoặc file in bao bì lên web.** Ảnh đẹp nhưng trang chậm hẳn trên điện thoại.
- **Plugin tăng tốc bật lazy load cho mọi ảnh,** kể cả ảnh chính, khiến LCP tệ hơn.
- **Alt nhồi từ khóa** hoặc dùng chung một alt cho cả chục ảnh.
- **Đưa giá, tên sản phẩm, khuyến mãi chỉ vào ảnh banner,** trên trang không có chữ.
- **Ảnh không khai kích thước,** tải xong đẩy chữ xuống, khách bấm nhầm nút.
- **Dùng ảnh lấy từ trang khác.** Vừa có rủi ro bản quyền, vừa không giúp gì vì Google đã thấy ảnh đó ở nơi khác.

## Checklist SEO hình ảnh và việc cần làm ngay tuần này

| Hạng mục | Đạt khi |
| --- | --- |
| Thẻ ảnh | Ảnh quan trọng nằm trong `<img>`, không làm hình nền CSS |
| Tên file | Chữ thường, không dấu, gạch ngang, mô tả đúng ảnh |
| Alt | Một câu tả đúng ảnh; ảnh trang trí để trống |
| Ngữ cảnh | Ảnh đặt cạnh đoạn chữ liên quan, chữ quan trọng có trên trang |
| Định dạng | WebP hoặc AVIF cho ảnh chụp, SVG cho logo |
| Kích thước | Đúng khung hiển thị, có srcset cho điện thoại |
| Ảnh đầu trang | Không lazy load, có fetchpriority cao, khai width và height |
| Ảnh bên dưới | Có loading="lazy" |
| Tốc độ | LCP từ 2,5 giây trở xuống trong PageSpeed Insights |
| Khai báo | robots.txt không chặn thư mục ảnh; sitemap hình ảnh nếu ảnh nạp bằng JavaScript |

Tuần này, anh chị làm bốn việc:

1. Mở trang sản phẩm bán chạy nhất trong PageSpeed Insights, xem phần tử LCP là ảnh nào và nặng bao nhiêu.
2. Xuất lại ảnh chính của 5 sản phẩm chủ lực sang WebP, đúng 1080 px, giữ khoảng 80–150 KB.
3. Viết lại alt cho các ảnh đó theo mẫu "tên sản phẩm + thương hiệu + quy cách + góc chụp".
4. Gửi quy ước đặt tên file cho người chụp ảnh và người đăng web, áp dụng từ ảnh mới tiếp theo.

Các bài khác về website và tìm kiếm có trong chủ đề [website và SEO](/kien-thuc/chu-de/website-seo/). QHUB Commerce là đội vận hành gian hàng đa sàn, có đội media chụp và xử lý ảnh sản phẩm cho cả sàn lẫn website, cùng đội vận hành sàn, đội KOC và đội host livestream.
