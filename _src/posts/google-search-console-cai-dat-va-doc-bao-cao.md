---
title: "Google Search Console: cài đặt và đọc báo cáo cho website bán hàng"
slug: google-search-console-cai-dat-va-doc-bao-cao
topic: website-seo
keyword: "google search console"
keywords: ["cài đặt google search console", "cách dùng search console", "báo cáo hiệu suất search console", "xác minh website với google", "gửi sitemap lên google"]
description: "Hướng dẫn cài Google Search Console từ đầu: xác minh website, gửi sitemap, đọc báo cáo hiệu suất, lập chỉ mục và báo cáo AI mới cho doanh nghiệp nhỏ."
date: 2026-11-21
updated: 2026-11-21
summary:
  - "Google Search Console là công cụ miễn phí của Google cho biết website hiện ra ở đâu trên Google, được bấm bao nhiêu lần và trang nào đang bị lỗi lập chỉ mục."
  - "Cài đặt gồm ba bước: thêm tài sản (nên chọn loại Miền), xác minh bằng bản ghi DNS, rồi gửi sitemap.xml."
  - "Bốn chỉ số cần đọc trong báo cáo Hiệu suất là lượt nhấp, lượt hiển thị, CTR và vị trí trung bình; luôn so cùng kỳ và lọc theo trang, truy vấn."
  - "Từ 2025–2026 Search Console có thêm chế độ xem theo tuần, theo tháng, chú thích trên biểu đồ, báo cáo Insights mới và báo cáo hiệu suất AI tạo sinh."
faq:
  - q: "Google Search Console có mất phí không?"
    a: "Không. Search Console là công cụ miễn phí của Google. Anh chị chỉ cần một tài khoản Google và quyền chỉnh tên miền hoặc website để xác minh quyền sở hữu."
  - q: "Nên chọn tài sản loại Miền hay Tiền tố URL?"
    a: "Nên chọn loại Miền nếu anh chị quản lý được DNS của tên miền. Loại này gom cả http, https, có www và không www, cùng mọi tên miền phụ vào một chỗ. Tiền tố URL chỉ hợp khi không vào được DNS, ví dụ website thuê trên nền tảng có sẵn."
  - q: "Gửi sitemap xong bao lâu thì Google lập chỉ mục?"
    a: "Không có mốc cố định. Trang mới có thể được lập chỉ mục sau vài ngày đến vài tuần, tùy chất lượng trang, liên kết nội bộ và mức độ website được Google tin. Gửi sitemap chỉ giúp Google biết có trang mới, không bảo đảm trang được đưa vào kết quả."
  - q: "Vì sao số lượt nhấp trong Search Console khác Google Analytics?"
    a: "Hai công cụ đo khác nhau. Search Console đếm lượt nhấp từ trang kết quả Google, còn Google Analytics đếm phiên truy cập trên website và phụ thuộc vào việc mã đo có chạy, người dùng có đồng ý cookie hay không. Lệch vài chục phần trăm là bình thường."
  - q: "Trang bị báo 'Đã thu thập dữ liệu – hiện chưa được lập chỉ mục' thì làm gì?"
    a: "Đây thường là dấu hiệu Google thấy trang chưa đủ giá trị hoặc trùng lặp với trang khác. Anh chị nên làm nội dung sâu hơn, thêm liên kết nội bộ từ các trang mạnh, gộp các trang na ná nhau, rồi mới yêu cầu lập chỉ mục lại."
sources:
  - title: "Ra mắt chế độ xem theo tuần và theo tháng trong Search Console – Google Search Central (12/2025)"
    url: "https://developers.google.com/search/blog/2025/12/weekly-monthly-views-search-console?hl=vi"
  - title: "Bổ sung thông tin bối cảnh cho dữ liệu Search Console bằng chú thích tuỳ chỉnh – Google Search Central (11/2025)"
    url: "https://developers.google.com/search/blog/2025/11/custom-chart-annotations?hl=vi"
  - title: "Báo cáo Search Console Insights mới đã ra mắt – Google Search Central (06/2025)"
    url: "https://developers.google.com/search/blog/2025/06/search-console-insights?hl=vi"
  - title: "Đơn giản hoá số liệu phân tích Search Console bằng tính năng Cấu hình dựa trên AI – Google Search Central (12/2025)"
    url: "https://developers.google.com/search/blog/2025/12/ai-powered-configuration?hl=vi"
  - title: "Introducing Search Generative AI performance reports in Search Console – Google Search Central (06/2026)"
    url: "https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports"
  - title: "Google Search Console AI performance reports rolling out globally – Search Engine Land"
    url: "https://searchengineland.com/google-search-console-ai-performance-reports-and-search-generative-ai-control-rolling-out-globally-486269"
---

**Google Search Console là công cụ miễn phí của Google cho anh chị biết website đang hiện ra ở đâu trên Google, được bấm bao nhiêu lần, khách gõ từ gì để tìm thấy mình và trang nào đang gặp lỗi.** Cài đặt chỉ mất khoảng 15 phút: thêm website, xác minh quyền sở hữu, gửi sitemap. Phần khó hơn là đọc báo cáo đúng cách để biết tuần này nên sửa trang nào, viết thêm bài gì.

Bài này đội QHUB viết theo đúng cách tụi mình đang dùng Search Console cho chính qhub.com.vn và các website bán hàng của doanh nghiệp: cài đặt từng bước, bốn chỉ số cần nhìn, những báo cáo mới Google bổ sung trong năm 2025–2026, và một lịch kiểm tra 15 phút mỗi tuần.

## Google Search Console là gì và khác Google Analytics thế nào?

Search Console (trước đây gọi là Google Webmaster Tools) là "bảng điều khiển" giữa website và Google Tìm kiếm. Nó trả lời những câu hỏi mà chỉ Google mới biết: trang của mình có được lập chỉ mục không, xuất hiện cho những truy vấn nào, đứng vị trí bao nhiêu, được hiển thị bao nhiêu lần.

Google Analytics thì đo chuyện xảy ra **sau khi** khách đã vào website: họ xem trang nào, ở lại bao lâu, có mua hàng không. Hai công cụ bổ sung cho nhau chứ không thay thế nhau.

| Câu hỏi | Search Console | Google Analytics |
| --- | --- | --- |
| Khách gõ từ gì trên Google để thấy mình? | Có | Gần như không |
| Trang có được Google lập chỉ mục không? | Có | Không |
| Vị trí trung bình trên Google | Có | Không |
| Khách làm gì sau khi vào website | Không | Có |
| Nguồn truy cập ngoài Google (Facebook, Zalo, sàn) | Không | Có |
| Đơn hàng, doanh thu | Không | Có (nếu cài sự kiện) |

Với doanh nghiệp đang bán chủ yếu trên TikTok Shop và Shopee, website thường là nơi để khách tìm hiểu thương hiệu và để Google, ChatGPT, Gemini biết đến mình. Vì thế Search Console gần như là công cụ duy nhất cho thấy website có đang "làm việc" hay không. Nếu anh chị còn phân vân có nên làm website riêng, bài [doanh nghiệp bán trên sàn có cần website riêng không](/kien-thuc/doanh-nghiep-ban-tren-san-co-can-website-rieng-khong/) có phân tích chi tiết.

## Cài đặt Google Search Console từng bước

### Bước 1: Thêm tài sản

Vào search.google.com/search-console, đăng nhập bằng tài khoản Google của doanh nghiệp (nên dùng email công ty, không dùng email cá nhân của nhân viên). Bấm "Thêm tài sản" và chọn một trong hai loại:

- **Miền (Domain):** nhập tên miền trần, ví dụ `qhub.com.vn`. Loại này gom hết http, https, có www, không www và mọi tên miền phụ. Đây là lựa chọn nên dùng.
- **Tiền tố URL (URL prefix):** nhập đầy đủ, ví dụ `https://qhub.com.vn/`. Chỉ theo dõi đúng phần địa chỉ bắt đầu bằng tiền tố đó.

### Bước 2: Xác minh quyền sở hữu

Với loại Miền, Google đưa một bản ghi TXT dạng `google-site-verification=...`. Anh chị vào trang quản lý tên miền (nơi mua tên miền hoặc Cloudflare), thêm bản ghi TXT này vào DNS rồi quay lại bấm "Xác minh". Bản ghi có thể cần vài phút đến vài giờ mới có hiệu lực.

Với loại Tiền tố URL, có thêm các cách: tải file HTML lên thư mục gốc, chèn thẻ meta vào trang chủ, dùng Google Analytics hoặc Google Tag Manager đã cài sẵn. Cách tải file HTML rất tiện cho website tĩnh.

**Lưu ý:** đừng xóa bản ghi hoặc file xác minh sau khi xong. Google kiểm tra lại định kỳ, mất bản ghi là mất quyền truy cập.

### Bước 3: Gửi sitemap

Sitemap là file liệt kê các trang anh chị muốn Google biết, thường nằm ở `/sitemap.xml`. WordPress, Haravan, Sapo đều tự tạo sitemap. Vào mục **Sơ đồ trang web**, nhập `sitemap.xml` và gửi. Trạng thái "Thành công" kèm số URL đã phát hiện là ổn.

### Bước 4: Thêm người dùng và kết nối công cụ khác

Vào **Cài đặt → Người dùng và quyền** để cấp quyền cho người phụ trách SEO hoặc đơn vị bên ngoài. Nên cấp quyền "Toàn bộ" hoặc "Hạn chế", giữ quyền "Chủ sở hữu" cho doanh nghiệp. Khi chấm dứt hợp tác với ai, nhớ thu hồi quyền.

Nếu đã có Google Analytics 4, anh chị liên kết hai công cụ để xem dữ liệu tìm kiếm ngay trong Analytics.

## Báo cáo Hiệu suất: bốn chỉ số phải hiểu

Báo cáo **Hiệu suất → Kết quả tìm kiếm** là nơi anh chị sẽ dành 80% thời gian. Nó có bốn chỉ số:

| Chỉ số | Nghĩa | Đọc thế nào |
| --- | --- | --- |
| Lượt nhấp (Clicks) | Số lần người dùng bấm vào website từ kết quả Google | Chỉ số gần doanh thu nhất |
| Lượt hiển thị (Impressions) | Số lần website xuất hiện trong kết quả người dùng nhìn thấy | Tăng nghĩa là Google đang thử website cho nhiều truy vấn hơn |
| CTR | Tỷ lệ nhấp = Lượt nhấp ÷ Lượt hiển thị | Thấp bất thường thì xem lại tiêu đề, mô tả |
| Vị trí trung bình | Thứ hạng trung bình của website cho truy vấn đó | Số càng nhỏ càng tốt; vị trí 1–3 nhận phần lớn lượt nhấp |

CTR (click-through rate) là tỷ lệ phần trăm người thấy kết quả rồi bấm vào. Vị trí trung bình là một con số bình quân, nên một trang có thể đứng hạng 3 cho từ khóa này và hạng 40 cho từ khóa khác, trung bình ra hạng 20.

### Cách đọc báo cáo cho ra việc

Đừng nhìn tổng số rồi vui hay buồn. Hãy dùng các bộ lọc và tab bên dưới biểu đồ:

1. **Tab Truy vấn:** xem khách thật sự gõ gì. Rất nhiều lần đội mình phát hiện từ khóa đem khách về khác hẳn từ khóa mình định nhắm.
2. **Tab Trang:** xem trang nào kéo khách nhiều nhất, trang nào có hiển thị cao nhưng nhấp thấp.
3. **So sánh thời gian:** bấm vào ngày, chọn "So sánh", đặt 28 ngày gần nhất với 28 ngày trước đó hoặc cùng kỳ năm trước. Ngành có mùa vụ như quà Tết thì phải so cùng kỳ.
4. **Lọc theo thiết bị và quốc gia:** website bán hàng ở Việt Nam thường có phần lớn lượt tìm từ điện thoại, nên trang di động phải chuẩn.

### Ba "mỏ vàng" nên tìm mỗi tháng

- **Truy vấn vị trí 5–15, hiển thị cao:** trang đã gần top. Bổ sung nội dung, thêm mục hỏi đáp, gắn thêm liên kết nội bộ là có thể lên trang một.
- **Trang hiển thị cao, CTR thấp:** viết lại tiêu đề và mô tả cho rõ lợi ích, đúng ý người tìm. Bài [tiêu đề và mô tả trang chuẩn](/kien-thuc/tieu-de-va-mo-ta-trang-title-meta-description-chuan/) có công thức cụ thể.
- **Truy vấn chưa có bài riêng:** khách đang hỏi điều mình chưa trả lời. Đây là danh sách chủ đề viết bài tiếp theo, đáng tin hơn mọi công cụ đoán từ khóa.

## Lập chỉ mục: trang của mình có lên Google không?

Báo cáo **Lập chỉ mục → Trang** chia trang thành hai nhóm: đã lập chỉ mục và chưa lập chỉ mục, kèm lý do. Lập chỉ mục là việc Google lưu trang vào kho dữ liệu để có thể hiển thị khi có người tìm.

Những lý do hay gặp và cách xử lý:

| Trạng thái | Ý nghĩa | Nên làm |
| --- | --- | --- |
| Trang có lệnh chuyển hướng | Trang cũ đã chuyển sang địa chỉ khác | Bình thường nếu chủ động chuyển |
| Đã loại trừ bởi thẻ noindex | Trang tự chặn Google | Kiểm tra có chặn nhầm trang quan trọng không |
| Không tìm thấy (404) | Địa chỉ không còn tồn tại | Chuyển hướng 301 về trang thay thế nếu trang từng có khách |
| Trang trùng lặp, Google chọn trang chính tắc khác | Google thấy hai trang na ná nhau | Gộp nội dung hoặc đặt thẻ canonical rõ ràng |
| Đã thu thập dữ liệu – hiện chưa được lập chỉ mục | Google đã đọc nhưng chưa thấy đáng đưa vào | Làm nội dung sâu hơn, thêm liên kết nội bộ |
| Đã phát hiện – hiện chưa được lập chỉ mục | Google biết trang nhưng chưa ghé đọc | Kiểm tra tốc độ máy chủ, thêm liên kết từ trang mạnh |

Không cần trang nào cũng được lập chỉ mục. Trang giỏ hàng, trang tìm kiếm nội bộ, trang lọc sản phẩm nên để ngoài. Điều quan trọng là **trang sản phẩm, trang danh mục và bài viết chính** phải nằm trong nhóm đã lập chỉ mục.

### Công cụ Kiểm tra URL

Dán một địa chỉ vào ô tìm kiếm trên cùng để xem Google thấy trang đó thế nào: đã lập chỉ mục chưa, lần thu thập gần nhất, trang có thân thiện di động không. Khi vừa sửa xong một trang quan trọng, bấm "Yêu cầu lập chỉ mục". Đừng bấm hàng loạt cho cả trăm trang, Google giới hạn số lần và việc này không thay được nội dung tốt.

## Những báo cáo mới Google thêm trong năm 2025–2026

Search Console thay đổi khá nhiều trong hai năm qua. Theo blog chính thức của Google Search Central:

- **Search Console Insights mới (6/2025):** báo cáo tóm tắt dễ đọc hơn, nằm ngay trong Search Console, cho thấy trang và truy vấn đang tăng, trang mới đang thu hút khách.
- **Chú thích tùy chỉnh trên biểu đồ (11/2025):** anh chị ghi chú ngày đổi giao diện, ngày đăng loạt bài, ngày chạy chiến dịch ngay trên biểu đồ để sau này đọc số không bị nhầm nguyên nhân.
- **Chế độ xem theo tuần và theo tháng (12/2025):** gom dữ liệu theo tuần, tháng giúp thấy xu hướng rõ hơn, không bị nhiễu bởi chênh lệch ngày thường với cuối tuần.
- **Cấu hình dựa trên AI (12/2025):** gõ yêu cầu bằng ngôn ngữ tự nhiên để Search Console tự đặt bộ lọc, so sánh trong báo cáo Hiệu suất. Tính năng triển khai dần, có thể chưa có trong mọi tài khoản và ngôn ngữ.
- **Kênh mạng xã hội trong Search Console (12/2025):** Google bắt đầu cho xem hiệu suất của các kênh mạng xã hội gắn với website trong Search Console.
- **Báo cáo hiệu suất AI tạo sinh (6/2026):** Google giới thiệu báo cáo riêng cho sự xuất hiện của website trong các trải nghiệm AI của Google Tìm kiếm như AI Overviews và AI Mode, sau đó mở rộng ra nhiều quốc gia. Theo các bài tin công nghệ, báo cáo hiện thiên về số lượt hiển thị, dữ liệu lượt nhấp còn hạn chế.

Tên gọi và vị trí từng mục có thể khác nhau giữa các tài khoản vì Google triển khai dần. Nếu chưa thấy, anh chị cứ dùng báo cáo Hiệu suất truyền thống trước. Muốn hiểu rộng hơn về việc được AI nhắc tới, xem bài [GEO là gì](/kien-thuc/geo-la-gi-toi-uu-de-chatgpt-gemini-nhac-toi-thuong-hieu/).

## Trải nghiệm trang, dữ liệu có cấu trúc và bảo mật

Ngoài Hiệu suất và Lập chỉ mục, có ba nhóm báo cáo anh chị nên mở ít nhất mỗi tháng một lần:

- **Chỉ số Core Web Vitals:** đánh giá tốc độ tải và độ ổn định của trang theo dữ liệu người dùng thật, chia theo điện thoại và máy tính. Trang bị xếp "Kém" nên được sửa trước. Bài [tốc độ website và Core Web Vitals](/kien-thuc/toc-do-website-va-core-web-vitals/) giải thích từng chỉ số.
- **Nâng cao (dữ liệu có cấu trúc):** nếu website có schema Sản phẩm, Câu hỏi thường gặp, Đường dẫn (breadcrumb), Search Console báo trang nào hợp lệ, trang nào lỗi. Lỗi ở đây làm mất cơ hội hiển thị giá, đánh giá trên kết quả tìm kiếm.
- **Bảo mật và thao tác thủ công:** nếu website bị hack hoặc bị Google phạt thủ công, thông báo sẽ nằm ở đây. Mục này trống là tốt.

Search Console cũng gửi email khi có lỗi mới. Hãy để email về hộp thư có người đọc thật, đừng để về một địa chỉ không ai mở.

## Lỗi hay gặp khi dùng Search Console

Từ kinh nghiệm hỗ trợ website cho doanh nghiệp, đội QHUB hay gặp những lỗi sau:

- **Xác minh bằng tài khoản của nhân viên hoặc đơn vị làm web.** Khi người đó nghỉ, doanh nghiệp mất quyền truy cập và mất cả lịch sử dữ liệu. Chủ sở hữu luôn phải là tài khoản doanh nghiệp.
- **Chỉ thêm loại Tiền tố URL bản có www** trong khi website chạy bản không www. Báo cáo trống trơn và tưởng website không có khách.
- **Chỉ nhìn vị trí trung bình.** Vị trí trung bình tụt có khi là tin tốt: website bắt đầu xuất hiện cho nhiều truy vấn mới ở vị trí thấp, kéo số trung bình xuống nhưng tổng lượt nhấp lại tăng.
- **Hoảng khi thấy nhiều trang "chưa lập chỉ mục".** Phần lớn là trang lọc, trang phân trang, trang chuyển hướng. Chỉ lo khi trang sản phẩm, bài viết chính nằm trong nhóm này.
- **Đổi đường dẫn hàng loạt mà không chuyển hướng 301.** Lượt nhấp rơi mạnh sau vài tuần. Khi đổi cấu trúc, luôn lập bảng ánh xạ địa chỉ cũ sang mới.
- **Gửi sitemap chứa trang lỗi.** Sitemap chỉ nên có trang trả về mã 200, không chuyển hướng, không noindex.

## Lịch kiểm tra Search Console 15 phút mỗi tuần

Không cần ngồi cả buổi. Đội mình dùng khung sau cho mỗi website:

| Tần suất | Việc | Thời gian |
| --- | --- | --- |
| Hằng tuần | Xem Hiệu suất 7 ngày so với 7 ngày trước; ghi 3 truy vấn tăng, 3 truy vấn giảm | 5 phút |
| Hằng tuần | Mở Lập chỉ mục → Trang, kiểm tra có lỗi mới với trang quan trọng không | 5 phút |
| Hằng tuần | Kiểm tra URL các bài, trang sản phẩm mới đăng | 5 phút |
| Hằng tháng | Lọc truy vấn vị trí 5–15 để chọn bài cần nâng cấp; xem Core Web Vitals | 30 phút |
| Hằng quý | So cùng kỳ năm trước, rà sitemap, rà người dùng có quyền | 1 giờ |

Ghi kết quả vào một bảng tính đơn giản. Sau ba tháng, anh chị sẽ có bức tranh rất rõ: chủ đề nào Google thích, trang nào đáng đầu tư tiếp.

## Việc nên làm ngay tuần này

Nếu website chưa có Search Console, hãy cài ngay hôm nay theo bốn bước ở trên: thêm tài sản loại Miền, xác minh bằng DNS, gửi sitemap, cấp quyền cho người phụ trách. Nếu đã có, mở báo cáo Hiệu suất 3 tháng gần nhất, lọc ra 10 truy vấn có vị trí từ 5 đến 15 và chọn 3 trang để nâng cấp nội dung trong tháng này. Các bài khác trong chủ đề [website và SEO](/kien-thuc/chu-de/website-seo/) sẽ giúp anh chị đi tiếp từng bước.

Search Console không làm website lên top. Nhưng nó cho anh chị biết chính xác chỗ cần sửa, thay vì đoán.
