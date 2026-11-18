---
title: "Tốc độ website và Core Web Vitals"
slug: toc-do-website-va-core-web-vitals
topic: website-seo
keyword: "core web vitals"
keywords: ["tốc độ website", "lcp inp cls là gì", "pagespeed insights", "tăng tốc website bán hàng"]
description: "Core Web Vitals gồm LCP, INP, CLS: ngưỡng đạt, cách đo bằng PageSpeed Insights và Search Console, nguyên nhân web bán hàng chậm và thứ tự sửa."
date: 2026-11-19
updated: 2026-11-19
summary:
  - "Core Web Vitals là ba chỉ số Google dùng để đo trải nghiệm thật của người dùng: LCP (tốc độ tải phần chính), INP (độ nhạy khi bấm) và CLS (độ ổn định bố cục)."
  - "Ngưỡng tốt theo web.dev: LCP từ 2,5 giây trở xuống, INP từ 200 mili giây trở xuống, CLS từ 0,1 trở xuống, tính ở phân vị 75 của lượt truy cập, xét riêng điện thoại và máy tính."
  - "INP thay thế FID trong bộ Core Web Vitals từ ngày 12/3/2024, nên các bài hướng dẫn cũ còn nói FID cần đọc lại."
  - "Với web bán hàng, thủ phạm hay gặp nhất là ảnh nặng, quá nhiều plugin, font tải chậm và script quảng cáo, chat, theo dõi; nên sửa theo thứ tự ảnh, script, font, bố cục, rồi mới tới máy chủ."
faq:
  - q: "Core Web Vitals là gì?"
    a: "Là bộ ba chỉ số của Google đo trải nghiệm thật khi người dùng mở trang: LCP đo phần nội dung lớn nhất hiện ra nhanh hay chậm, INP đo trang phản hồi nhanh hay chậm khi bấm, CLS đo bố cục có bị xô lệch khi đang tải không. Dữ liệu lấy từ người dùng Chrome thật qua bộ dữ liệu CrUX."
  - q: "Ngưỡng Core Web Vitals đạt chuẩn là bao nhiêu?"
    a: "Theo web.dev, mức tốt là LCP từ 2,5 giây trở xuống, INP từ 200 mili giây trở xuống và CLS từ 0,1 trở xuống. Mức kém là LCP trên 4 giây, INP trên 500 mili giây, CLS trên 0,25. Một trang được tính là đạt khi 75% lượt truy cập nằm trong mức tốt."
  - q: "Điểm PageSpeed Insights thấp thì có bị tụt hạng không?"
    a: "Điểm số 0–100 trong PageSpeed Insights là điểm phòng thí nghiệm, dùng để tìm lỗi, không phải thứ Google dùng để xếp hạng. Google Search Central nói hệ thống xếp hạng có dùng Core Web Vitals dựa trên dữ liệu người dùng thật, nhưng nội dung phù hợp vẫn quan trọng hơn. Anh chị nên nhìn phần dữ liệu thực tế ở đầu báo cáo và báo cáo Core Web Vitals trong Search Console."
  - q: "Website mới, ít người vào thì đo Core Web Vitals thế nào?"
    a: "Trang ít lượt truy cập thường chưa có dữ liệu CrUX, nên Search Console và PageSpeed Insights sẽ báo không đủ dữ liệu. Lúc này anh chị dùng phần đo phòng thí nghiệm (Lighthouse) để sửa trước các lỗi lớn như ảnh nặng, script chặn tải, ảnh không khai kích thước. Khi lượng truy cập tăng, dữ liệu thực tế sẽ xuất hiện."
  - q: "INP khác FID thế nào?"
    a: "FID chỉ đo độ trễ của lần bấm đầu tiên. INP xét gần như mọi lần bấm, chạm, gõ phím trong suốt lượt xem và lấy một lần phản hồi chậm tiêu biểu. Vì vậy INP khó đạt hơn, nhất là với trang có nhiều script. INP chính thức thay FID từ 12/3/2024."
sources:
  - title: "Web Vitals – web.dev"
    url: "https://web.dev/articles/vitals"
  - title: "Interaction to Next Paint becomes a Core Web Vital on March 12 – web.dev"
    url: "https://web.dev/blog/inp-cwv-march-12"
  - title: "Understanding Core Web Vitals and Google search results – Google Search Central"
    url: "https://developers.google.com/search/docs/appearance/core-web-vitals"
  - title: "Core Web Vitals report – Search Console Help"
    url: "https://support.google.com/webmasters/answer/9205520"
  - title: "About PageSpeed Insights – Google for Developers"
    url: "https://developers.google.com/speed/docs/insights/v5/about"
  - title: "How the Core Web Vitals metrics thresholds were defined – web.dev"
    url: "https://web.dev/articles/defining-core-web-vitals-thresholds"
---

**Core Web Vitals là bộ ba chỉ số Google dùng để đo trải nghiệm thật khi người dùng mở một trang web: LCP đo tốc độ hiện phần nội dung chính, INP đo độ nhạy khi bấm, CLS đo độ ổn định của bố cục.** Theo web.dev, một trang đạt chuẩn khi LCP từ 2,5 giây trở xuống, INP từ 200 mili giây trở xuống và CLS từ 0,1 trở xuống, tính ở phân vị 75 của lượt truy cập. Với web bán hàng, ba con số này gắn thẳng với việc khách ở lại xem hay bấm quay lại.

Bài này đội QHUB viết cho chủ doanh nghiệp có website bán hàng, không cần biết lập trình: đo ở đâu, vì sao web hay chậm, sửa theo thứ tự nào và checklist để giao cho người làm web. Nếu anh chị đang dựng web từ đầu, nên đọc trước bài [website bán hàng chuẩn SEO năm 2026](/kien-thuc/website-ban-hang-chuan-seo-nam-2026-huong-dan-tu-a-den-z/).

## Core Web Vitals là gì và vì sao chủ shop nên quan tâm?

Hãy hình dung một khách thấy bài quảng cáo, bấm vào trang sản phẩm trên điện thoại. Ba điều xảy ra trong vài giây đầu quyết định họ có mua không:

1. **Ảnh sản phẩm và tên sản phẩm có hiện ra nhanh không?** Đây là LCP.
2. **Bấm nút "Thêm vào giỏ" có phản hồi ngay không, hay đứng im một nhịp?** Đây là INP.
3. **Đang định bấm thì trang bị xô xuống vì một khung quảng cáo chèn vào, làm bấm nhầm?** Đây là CLS.

Ba chỉ số này mô tả đúng cảm giác của người mua. Trang chậm, giật, bấm không ăn thì khách vào từ quảng cáo chỉ cần một cú vuốt là quay về.

Về SEO, Google Search Central nói rõ hệ thống xếp hạng có dùng Core Web Vitals. Nhưng Google cũng nói nội dung phù hợp, hữu ích vẫn là yếu tố lớn hơn. Nói gọn: web nhanh không tự kéo anh chị lên top, nhưng web quá chậm là điểm trừ và trực tiếp làm mất đơn.

## Ba chỉ số LCP, INP, CLS đo cái gì?

### LCP: phần lớn nhất hiện ra sau bao lâu

LCP (Largest Contentful Paint, thời điểm vẽ nội dung lớn nhất) đo thời gian từ lúc bấm vào đến khi khối nội dung lớn nhất trong màn hình đầu tiên hiện xong. Trên trang sản phẩm, khối đó thường là ảnh sản phẩm chính. Trên trang chủ, thường là ảnh banner lớn.

Vì thế LCP gần như là "chỉ số của ảnh".

### INP: bấm vào thì bao lâu trang mới phản hồi

INP (Interaction to Next Paint, thời gian từ tương tác đến lần vẽ kế tiếp) đo độ trễ khi người dùng bấm, chạm hoặc gõ phím. Nó xét các lần tương tác trong suốt lượt xem và lấy một lần chậm tiêu biểu.

INP chính thức thay thế FID (First Input Delay, độ trễ lần bấm đầu tiên) trong bộ Core Web Vitals từ ngày 12/3/2024, theo thông báo trên web.dev. INP khó đạt hơn FID, vì mỗi script chạy ngầm trên trang đều có thể làm nút bấm "đơ" một nhịp. Tài liệu cũ còn nhắc FID thì cần đọc lại.

### CLS: bố cục có bị xô lệch không

CLS (Cumulative Layout Shift, tổng độ xô lệch bố cục) đo mức độ các phần tử trên trang tự dịch chuyển khi đang tải. CLS không tính bằng giây mà là một con số không có đơn vị. Càng gần 0 càng tốt.

Lỗi CLS điển hình: ảnh không khai chiều rộng, chiều cao nên khi ảnh tải xong thì đẩy chữ bên dưới xuống; thanh thông báo khuyến mãi chèn lên đầu trang sau vài giây; font chữ đổi kiểu làm dòng chữ nhảy.

## Ngưỡng Core Web Vitals hiện hành và cách sửa từng chỉ số

Bảng dưới tổng hợp ngưỡng theo web.dev và Google Search Central, kèm nguyên nhân hay gặp và cách sửa cho web bán hàng.

| Chỉ số | Đo cái gì | Tốt | Cần cải thiện | Kém | Nguyên nhân hay gặp | Sửa gì trước |
| --- | --- | --- | --- | --- | --- | --- |
| LCP | Tốc độ hiện nội dung chính | ≤ 2,5 giây | 2,5–4 giây | > 4 giây | Banner, ảnh sản phẩm nặng; máy chủ phản hồi chậm; CSS, JS chặn tải | Nén ảnh, dùng WebP/AVIF, đúng kích thước; không lazy-load ảnh đầu trang; bật bộ nhớ đệm và CDN |
| INP | Độ nhạy khi bấm, chạm | ≤ 200 ms | 200–500 ms | > 500 ms | Script quảng cáo, chat, pixel theo dõi; plugin nặng; giao diện nhiều hiệu ứng | Gỡ script thừa; trì hoãn chat, pixel; bớt plugin; tránh slider, hiệu ứng chạy liên tục |
| CLS | Độ ổn định bố cục | ≤ 0,1 | 0,1–0,25 | > 0,25 | Ảnh, video, iframe không khai kích thước; banner chèn muộn; font đổi kiểu | Khai width/height cho mọi ảnh; giữ chỗ trước cho banner; dùng font-display hợp lý |

Có ba điểm anh chị cần nhớ khi đọc bảng này:

- **Đánh giá ở phân vị 75.** Nghĩa là xếp tất cả lượt truy cập từ nhanh đến chậm, lấy mốc ở vị trí 75%. Trang chỉ "đạt" khi ít nhất 75% lượt truy cập có trải nghiệm tốt. Một lần đo nhanh trên máy văn phòng không nói lên điều gì.
- **Điện thoại và máy tính xét riêng.** Khách mua hàng online ở Việt Nam phần lớn dùng điện thoại, nên hãy ưu tiên kết quả trên điện thoại.
- **Một trang chỉ đạt khi cả ba chỉ số cùng tốt.** LCP đẹp mà CLS kém thì vẫn bị xếp vào nhóm cần cải thiện.

## Đo tốc độ website ở đâu: PageSpeed Insights, Search Console, CrUX

**CrUX (Chrome User Experience Report, báo cáo trải nghiệm người dùng Chrome)** là bộ dữ liệu Google thu thập ẩn danh từ người dùng Chrome thật, theo khung 28 ngày gần nhất. Đây là "nguồn sự thật" mà các công cụ khác đọc lại. Trang quá ít người vào sẽ chưa có dữ liệu CrUX.

**PageSpeed Insights** (pagespeed.web.dev) là nơi kiểm tra từng đường dẫn cụ thể. Báo cáo có hai phần:

- Phần trên là **dữ liệu thực tế** lấy từ CrUX. Đây mới là thứ phản ánh trải nghiệm của khách.
- Phần dưới là **dữ liệu phòng thí nghiệm** do Lighthouse chạy một lần trên máy giả lập, kèm điểm 0–100 và danh sách gợi ý sửa. Điểm này dao động giữa các lần chạy và chỉ dùng để tìm lỗi.

**Báo cáo Core Web Vitals trong Google Search Console** nhìn toàn website. Nó gom các trang giống nhau thành nhóm, chia ba mức Tốt, Cần cải thiện, Kém cho điện thoại và máy tính. Đây là chỗ anh chị nên xem mỗi tháng để biết nhóm trang nào đang có vấn đề, rồi mới mở PageSpeed Insights để soi từng trang.

Cách làm đội mình hay dùng: mở Search Console trước để biết **nhóm trang nào** kém, lấy một đường dẫn mẫu của nhóm đó dán vào PageSpeed Insights, đọc phần gợi ý để biết **vì sao** kém, sửa xong thì bấm "Xác thực bản sửa lỗi" trong Search Console. Quá trình xác thực theo dõi dữ liệu trong khoảng 28 ngày, nên đừng sốt ruột khi chưa thấy đổi màu ngay.

## Vì sao website bán hàng hay chậm?

Qua nhiều website doanh nghiệp đội QHUB từng rà soát, nguyên nhân thường không nằm ở máy chủ, mà ở những thứ được gắn thêm dần theo thời gian.

**Ảnh quá nặng.** Ảnh sản phẩm chụp bằng máy ảnh hoặc điện thoại đời mới thường vài MB mỗi tấm. Tải nguyên lên web là cách nhanh nhất làm hỏng LCP.

**Quá nhiều plugin, tiện ích.** Web làm bằng WordPress hay các nền tảng có kho tiện ích rất dễ bị "cài cho có". Mỗi plugin thêm một ít CSS, JavaScript chạy trên mọi trang, kể cả trang không dùng tới.

**Font chữ tải chậm.** Dùng 3–4 họ font, mỗi họ nhiều độ đậm, lại tải từ máy chủ bên ngoài. Trình duyệt phải chờ font về mới hiện chữ, hoặc hiện chữ tạm rồi đổi, làm bố cục nhảy.

**Script quảng cáo, chat, theo dõi.** Pixel quảng cáo của nhiều nền tảng, công cụ đo lường, khung chat, nút gọi nổi, cửa sổ bật lên thu thập số điện thoại. Mỗi thứ một ít, nhưng chúng tranh nhau chạy đúng lúc khách đang muốn bấm. Đây là thủ phạm số một của INP kém.

**Hosting và bộ nhớ đệm chưa được cấu hình.** Máy chủ ở xa, không bật nén, không bật bộ nhớ đệm, không dùng CDN (Content Delivery Network, mạng phân phối nội dung đặt máy chủ gần người xem).

## Sửa theo thứ tự nào để đỡ tốn công?

Đội mình khuyên sửa theo thứ tự "rẻ trước, đắt sau". Không cần làm hết một lúc.

### Bước 1: Xử lý ảnh

- Xuất ảnh đúng kích thước hiển thị. Ảnh chỉ hiện rộng 800 điểm ảnh thì không cần tải ảnh rộng 4.000.
- Chuyển sang định dạng WebP hoặc AVIF, nén ở mức mắt thường không thấy khác biệt.
- Dùng thuộc tính srcset để điện thoại tải ảnh nhỏ, máy tính tải ảnh lớn.
- Bật lazy-load (tải chậm, chỉ tải khi cuộn tới) cho ảnh bên dưới, nhưng **không** lazy-load ảnh chính ở đầu trang. Ảnh đầu trang nên được ưu tiên tải.
- Banner trang chủ: một ảnh tĩnh tốt hơn slider năm ảnh.

Ví dụ ngay ở nhà mình: website bán hàng [qhubherbal.com](https://qhubherbal.com/) của thương hiệu trà QHUB HERBAL có nhiều ảnh hộp trà, ảnh nguyên liệu, ảnh gói lọc. Nguyên tắc đội mình đặt ra khi chuẩn bị ảnh cho web là xuất riêng một bộ ảnh nhẹ cho web, đúng khung hiển thị, thay vì dùng lại file gốc chụp studio hay file in bao bì. Trang tổng các sản phẩm ở [QHUB HERBAL](/qhub-herbal.html) cũng theo cách đó. Mình không đưa số đo tốc độ ở đây vì nó thay đổi theo từng lần cập nhật; anh chị cứ tự dán đường dẫn web của mình vào PageSpeed Insights để xem.

### Bước 2: Dọn script bên thứ ba

- Liệt kê mọi pixel, công cụ đo lường, chat, popup đang gắn trên web. Cái nào không còn dùng thì gỡ.
- Gom các thẻ theo dõi về một chỗ quản lý, tránh gắn trùng một pixel hai lần.
- Cho khung chat, nút gọi nổi tải sau khi trang đã hiện xong, hoặc chỉ tải khi khách bấm vào biểu tượng.

### Bước 3: Rà plugin và giao diện

- Tắt thử từng plugin trên bản sao của web để xem plugin nào nặng nhất.
- Thay plugin "làm mọi thứ" bằng plugin nhỏ làm đúng một việc, hoặc bỏ hẳn nếu không cần.
- Bớt hiệu ứng chuyển động, nhất là trên điện thoại.

### Bước 4: Font chữ và bố cục

- Dùng tối đa 2 họ font, chỉ tải các độ đậm thật sự dùng.
- Ưu tiên tự lưu font trên máy chủ của web, khai font-display: swap để chữ hiện ngay.
- Khai chiều rộng, chiều cao cho mọi ảnh, video, khung nhúng.
- Thanh khuyến mãi, banner cookie phải có chỗ giữ sẵn, không chèn đẩy nội dung.

### Bước 5: Máy chủ, bộ nhớ đệm, CDN

Khi bốn bước trên đã làm mà LCP vẫn chậm, lúc đó mới xem tới hosting: bật nén, bật bộ nhớ đệm trang, dùng CDN, nâng gói máy chủ nếu thật cần.

Song song, nhớ rằng tốc độ chỉ là một phần của nền kỹ thuật. Cấu trúc trang, [dữ liệu có cấu trúc schema](/kien-thuc/du-lieu-co-cau-truc-schema-cho-website-ban-hang/) và [tiêu đề, mô tả trang](/kien-thuc/tieu-de-va-mo-ta-trang-title-meta-description-chuan/) cũng cần làm cùng lúc thì web mới có sức cạnh tranh trên kết quả tìm kiếm.

### Checklist để giao cho người làm web

Anh chị có thể chép nguyên bảng này gửi cho đơn vị làm web:

| Hạng mục | Việc cần kiểm tra | Đạt khi |
| --- | --- | --- |
| Đo lường | Có báo cáo Core Web Vitals trong Search Console, kiểm tra mỗi tháng | Biết rõ nhóm trang nào Tốt, Cần cải thiện, Kém |
| Ảnh | Ảnh đúng kích thước, WebP/AVIF, có srcset | Không còn ảnh nặng vài MB trên trang |
| Ảnh đầu trang | Ảnh chính không bị lazy-load, được ưu tiên tải | LCP trên điện thoại ≤ 2,5 giây |
| Script | Danh sách pixel, chat, popup đã rà, gỡ cái thừa | Không có thẻ trùng, chat tải sau |
| Plugin | Chỉ giữ plugin thật sự dùng | Đã thử tắt từng cái trên bản sao |
| Font | Tối đa 2 họ font, tự lưu, có font-display | Chữ hiện ngay, không nhảy dòng |
| Bố cục | Ảnh, video, khung nhúng có kích thước; banner có chỗ giữ sẵn | CLS ≤ 0,1 |
| Phản hồi | Nút mua, giỏ hàng bấm là có phản hồi | INP ≤ 200 ms |
| Máy chủ | Bật nén, bộ nhớ đệm, cân nhắc CDN | Phản hồi đầu tiên của máy chủ ổn định |
| Sau mỗi thay đổi | Đo lại trang sản phẩm chính bằng PageSpeed Insights | Không chỉ số nào tụt mức |

Nếu website của anh chị còn đang lộn xộn về cấu trúc danh mục, nên xem thêm bài [cấu trúc website chuẩn SEO](/kien-thuc/cau-truc-website-chuan-seo-danh-muc-trang-tru-cot-cum-bai/), vì trang gọn và ít tầng cũng thường dễ làm nhanh hơn. Các bài khác về chủ đề này nằm trong mục [website và SEO](/kien-thuc/chu-de/website-seo/).

## Lỗi hay gặp khi tối ưu Core Web Vitals

- **Chạy theo điểm 100 trong PageSpeed Insights.** Điểm phòng thí nghiệm chỉ là công cụ chẩn đoán. Có trang điểm 70 mà dữ liệu thực tế vẫn đạt cả ba chỉ số. Cái cần đạt là dữ liệu thực tế ở phân vị 75.
- **Chỉ kiểm tra trang chủ.** Khách từ quảng cáo và tìm kiếm thường vào thẳng trang sản phẩm, trang danh mục. Hãy kiểm tra cả các mẫu trang đó.
- **Lazy-load luôn cả ảnh đầu trang.** Plugin tăng tốc bật lazy-load cho mọi ảnh, kể cả ảnh sản phẩm chính, khiến LCP chậm hơn.
- **Gắn thêm script mới mà không kiểm tra lại.** Mỗi lần thêm pixel, chat, popup, hãy đo lại trang sản phẩm chính. Tốc độ thường hỏng dần theo từng lần "gắn thêm một chút".
- **Sửa xong không bấm xác thực trong Search Console.** Báo cáo sẽ cập nhật chậm và anh chị không biết bản sửa đã có tác dụng chưa.

## Việc anh chị nên làm ngay tuần này

1. Mở Google Search Console, vào báo cáo Core Web Vitals, chụp lại tình trạng hiện tại trên điện thoại để làm mốc so sánh.
2. Chọn ba đường dẫn quan trọng nhất: trang chủ, một trang danh mục, một trang sản phẩm bán chạy. Dán từng cái vào PageSpeed Insights, ghi lại LCP, INP, CLS ở phần dữ liệu thực tế (nếu có).
3. Liệt kê toàn bộ script quảng cáo, chat, popup đang gắn trên web. Gỡ ngay những cái không còn dùng.
4. Nhờ người làm web nén lại ảnh banner và ảnh sản phẩm chính, khai kích thước cho ảnh, bỏ lazy-load ở ảnh đầu trang.
5. Hẹn lịch kiểm tra lại sau 28 ngày, khi dữ liệu thực tế đã kịp cập nhật.

Tốc độ website không phải việc làm một lần là xong. Giữ thói quen đo lại sau mỗi thay đổi, anh chị sẽ giữ được trải nghiệm tốt cho khách mà không phải làm lại từ đầu.
