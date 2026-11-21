---
title: "TikTok Pixel và Events API: đo chuyển đổi trên website"
slug: tiktok-pixel-va-events-api-do-chuyen-doi-tren-website
topic: quang-cao-tiktok
keyword: "tiktok pixel"
keywords: ["tiktok events api", "cài tiktok pixel cho website", "sự kiện chuẩn tiktok", "tiktok pixel helper", "event_id tiktok"]
description: "TikTok Pixel và Events API là gì, khác nhau ra sao, website bán hàng cần đo sự kiện nào, cách cài, chống đếm trùng bằng event_id và kiểm tra dữ liệu."
date: 2026-11-22
updated: 2026-11-22
summary:
  - "TikTok Pixel là đoạn mã chạy trên trình duyệt để ghi nhận hành động của khách trên website; Events API gửi cùng dữ liệu đó từ máy chủ của website thẳng tới TikTok."
  - "TikTok khuyên dùng cả hai; để không đếm trùng, sự kiện gửi từ hai đường phải có cùng tên sự kiện và cùng mã event_id."
  - "Website bán hàng tối thiểu nên đo xem sản phẩm, thêm vào giỏ, bắt đầu thanh toán và hoàn tất thanh toán có kèm giá trị đơn bằng VND."
  - "Gửi email, số điện thoại đã mã hóa cho TikTok là xử lý dữ liệu cá nhân, phải tuân theo Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 có hiệu lực từ 01/01/2026."
faq:
  - q: "TikTok Pixel là gì?"
    a: "TikTok Pixel là đoạn mã gắn vào website để ghi nhận hành động của người xem đến từ quảng cáo TikTok, như xem sản phẩm, thêm vào giỏ, thanh toán. Dữ liệu này giúp TikTok đo hiệu quả quảng cáo, tối ưu theo đơn hàng và tạo tệp khách để quảng cáo lại."
  - q: "Events API của TikTok khác Pixel thế nào?"
    a: "Pixel chạy trên trình duyệt của khách nên có thể bị chặn bởi trình chặn quảng cáo, cài đặt quyền riêng tư hoặc mạng chậm. Events API gửi sự kiện từ máy chủ của website tới TikTok, không phụ thuộc trình duyệt. Dùng cả hai giúp dữ liệu đầy đủ hơn, với điều kiện phải chống đếm trùng bằng event_id."
  - q: "Làm sao kiểm tra TikTok Pixel đã chạy đúng chưa?"
    a: "Cài tiện ích TikTok Pixel Helper trên Chrome, mở website và xem Pixel có bắn đúng sự kiện ở từng trang không. Sau đó dùng mục Kiểm tra sự kiện trong TikTok Events Manager, tự đặt một đơn thử và xem sự kiện có về từ cả trình duyệt lẫn máy chủ không."
  - q: "Website nhỏ có cần Events API không?"
    a: "Nếu website có chạy quảng cáo TikTok với mục tiêu chuyển đổi thì nên có, vì phần sự kiện bị trình duyệt chặn sẽ được bù lại. Nhiều nền tảng làm web như Shopify, WooCommerce có tích hợp đối tác nên bật Events API khá nhanh. Web chưa chạy quảng cáo có thể bắt đầu với Pixel trước."
  - q: "Cửa sổ phân bổ trên TikTok Ads Manager là gì?"
    a: "Là khoảng thời gian sau khi khách bấm hoặc xem quảng cáo mà một chuyển đổi vẫn được tính cho quảng cáo đó. TikTok cho phép chọn cửa sổ sau nhấp và sau xem trong phần cài đặt phân bổ. Khi so số liệu giữa TikTok, Meta và Google Analytics, anh chị phải nhớ mỗi bên tính theo cửa sổ khác nhau."
sources:
  - title: "About event deduplication – TikTok Ads Manager Help"
    url: "https://ads.tiktok.com/help/article/event-deduplication"
  - title: "About Standard Events in TikTok Ads Manager"
    url: "https://ads.tiktok.com/help/article/supported-standard-events"
  - title: "How to Adopt TikTok’s Updated Standard Events"
    url: "https://ads.tiktok.com/help/article/how-to-adopt-tiktoks-updated-standard-events?lang=en"
  - title: "About Advanced Matching for Web – TikTok Ads Manager Help"
    url: "https://ads.tiktok.com/help/article/advanced-matching-web"
  - title: "Partner Integrations for Web Events – TikTok Ads Manager Help"
    url: "https://ads.tiktok.com/help/article/partner-integrations-for-web-tracking"
  - title: "How to set up TikTok Pixel with Google Tag Manager in TikTok Events Manager"
    url: "https://ads.tiktok.com/help/article/get-started-google-tag-manager?lang=en"
  - title: "Troubleshoot with Pixel Helper – TikTok Ads Manager Help"
    url: "https://ads.tiktok.com/help/article/pixel-downloadable-guides"
  - title: "About the attribution window on TikTok Ads Manager"
    url: "https://ads.tiktok.com/help/article/about-the-attribution-window-on-tiktok-ads-manager"
  - title: "Luật Bảo vệ dữ liệu cá nhân 2025 số 91/2025/QH15 – Thư viện Pháp luật"
    url: "https://thuvienphapluat.vn/van-ban/Bo-may-hanh-chinh/Luat-Bao-ve-du-lieu-ca-nhan-2025-so-91-2025-QH15-625628.aspx"
  - title: "Điểm mới của Nghị định 356/2025 so với Nghị định 13/2023 về bảo vệ dữ liệu cá nhân – Luật Việt An"
    url: "https://luatvietan.vn/diem-moi-cua-nghi-dinh-356-2025-so-voi-nghi-dinh-13-2023-ve-huong-dan-bao-ve-du-lieu-ca-nhan.html"
---

**TikTok Pixel là đoạn mã gắn trên website để ghi nhận hành động của khách đến từ quảng cáo TikTok, còn Events API gửi cùng dữ liệu đó từ máy chủ của website thẳng tới TikTok.** TikTok khuyên dùng cả hai. Pixel dễ cài nhưng có thể bị trình duyệt hoặc trình chặn quảng cáo cắt mất. Events API bù vào phần bị mất. Để một đơn không bị đếm thành hai, mỗi sự kiện phải mang cùng tên và cùng mã event_id ở cả hai đường.

Bài này đội QHUB viết cho chủ shop và người chạy quảng cáo muốn kéo khách từ TikTok về website riêng. Mình đi lần lượt: Pixel và Events API là gì, cần đo sự kiện nào, cài theo cách nào, kiểm tra ra sao, đọc số thế nào cho đúng, và phần dữ liệu cá nhân theo luật Việt Nam. Thông tin được đối chiếu với Trung tâm trợ giúp TikTok Ads ngày 22/11/2026. Giao diện Events Manager thay đổi khá thường xuyên, nên tên nút có thể khác đôi chút khi anh chị đọc bài.

## TikTok Pixel là gì và để làm gì?

Hãy hình dung quảng cáo TikTok là người phát tờ rơi ngoài phố. Website là cửa hàng. TikTok Pixel là người đứng trong cửa hàng ghi sổ: khách nào vào, xem món gì, bỏ gì vào giỏ, có ra quầy trả tiền không.

Dữ liệu Pixel ghi được dùng cho ba việc:

1. **Đo hiệu quả.** Biết quảng cáo nào mang về đơn hàng thật, không chỉ lượt bấm.
2. **Tối ưu quảng cáo.** Khi chọn mục tiêu chuyển đổi trên website, hệ thống TikTok cần dữ liệu sự kiện để tìm người dễ mua.
3. **Tạo tệp khách.** Ví dụ người đã thêm vào giỏ trong 7 ngày nhưng chưa mua, để quảng cáo nhắc lại.

Không có Pixel, chạy quảng cáo TikTok về website gần như chạy mù. Anh chị chỉ thấy lượt bấm, còn bao nhiêu đơn, đơn bao nhiêu tiền thì không rõ. Nếu đang phân vân nên kéo khách về website, Zalo hay form, bài [quảng cáo TikTok ngoài TikTok Shop](/kien-thuc/quang-cao-tiktok-ngoai-tiktok-shop-keo-ve-website-zalo-form/) so sánh ba hướng này khá kỹ.

## Events API là gì, vì sao nên dùng cùng Pixel?

**Events API** là cách gửi sự kiện từ máy chủ (server-side, tức phía máy chủ) của website tới TikTok. Thay vì nhờ trình duyệt của khách gửi, chính hệ thống đơn hàng gửi khi có sự kiện, ví dụ lúc đơn được tạo hoặc lúc thanh toán thành công.

Vì sao cần thêm? Vì Pixel phụ thuộc trình duyệt, mà trình duyệt ngày càng chặn nhiều.

| Tình huống | TikTok Pixel | Events API |
| --- | --- | --- |
| Khách dùng trình chặn quảng cáo | Có thể bị chặn | Vẫn gửi được |
| Trình duyệt hạn chế cookie, theo dõi | Có thể mất dữ liệu | Không phụ thuộc trình duyệt |
| Khách tắt trang trước khi mã chạy xong | Có thể mất sự kiện | Máy chủ vẫn ghi nhận đơn |
| Đơn xác nhận qua điện thoại, ngoài website | Không ghi được | Gửi được từ hệ thống |
| Độ khó cài đặt | Dễ | Trung bình đến khó |

Cách TikTok khuyến nghị là chạy song song. Pixel bắt sự kiện trên trình duyệt. Events API gửi lại từ máy chủ. Sự kiện nào cả hai cùng bắt được thì TikTok gộp làm một. Cách nghĩ này giống hệt Meta, đội mình đã giải thích trong bài [Pixel Meta và Conversions API cho website bán hàng](/kien-thuc/pixel-meta-va-conversions-api-cho-website-ban-hang/). Website đang làm cho Meta rồi thì thêm TikTok thường nhẹ hơn nhiều.

### Chống đếm trùng bằng event_id

Theo bài "About event deduplication" trên Trung tâm trợ giúp TikTok Ads, TikTok nhận ra hai bản ghi là một sự kiện khi chúng có **cùng tên sự kiện** và **cùng event_id**. Cách đơn giản nhất cho sự kiện mua hàng là lấy mã đơn hàng làm event_id. Pixel trên trang cảm ơn gửi sự kiện với event_id là mã đơn. Máy chủ gửi qua Events API với đúng mã đơn đó. TikTok nhận hai, tính một.

Với sự kiện như thêm vào giỏ, website tạo một mã ngẫu nhiên khi khách bấm nút, rồi dùng chung mã đó cho cả hai đường. Thiếu bước này, báo cáo sẽ đếm đơn gấp đôi. ROAS (doanh thu chia chi phí quảng cáo) trông đẹp gấp đôi thực tế, và anh chị dễ quyết định tăng ngân sách dựa trên số ảo. TikTok còn có giới hạn thời gian giữa hai bản ghi để được gộp, anh chị xem chi tiết trong bài trợ giúp nói trên.

## TikTok Pixel cần đo những sự kiện chuẩn nào?

TikTok có danh sách **sự kiện chuẩn** (standard events), tức các sự kiện có tên định sẵn mà hệ thống hiểu và tối ưu được. Với website bán hàng, đội mình luôn cài tối thiểu các sự kiện dưới đây.

| Sự kiện chuẩn | Khi nào bắn | Thông tin nên gửi kèm |
| --- | --- | --- |
| ViewContent | Khách xem trang sản phẩm | content_id (mã sản phẩm), tên, giá |
| AddToCart | Bấm thêm vào giỏ | content_id, số lượng, value (giá trị) |
| InitiateCheckout | Vào trang thanh toán | Giá trị giỏ, số sản phẩm |
| AddPaymentInfo | Chọn hoặc nhập phương thức thanh toán | Giá trị giỏ |
| CompletePayment | Đơn tạo thành công | Mã đơn làm event_id, value, currency = VND |

Website có form tư vấn thì thêm sự kiện gửi form. Website có nút gọi hoặc nhắn Zalo thì thêm sự kiện liên hệ.

Một điểm cần để ý: TikTok có bài hướng dẫn "How to Adopt TikTok's Updated Standard Events", nghĩa là bộ sự kiện chuẩn đã được cập nhật và một số tên có thể thay đổi. Ví dụ có tài liệu mới gọi sự kiện mua hàng là Purchase thay vì CompletePayment. Anh chị đừng chép tên sự kiện từ bài cũ trên mạng. Hãy mở Events Manager của chính tài khoản mình, chọn đúng tên đang được đề xuất ở đó.

Hai lưu ý với sự kiện mua hàng:

- **Chỉ bắn một lần cho mỗi đơn.** Lỗi hay gặp là trang cảm ơn bị tải lại, Pixel bắn thêm một lần.
- **Gửi giá trị đơn thật**, đúng đơn vị VND. Không gửi một giá trị cố định cho mọi đơn.

Lấy ví dụ website bán hàng riêng qhubherbal.com của thương hiệu trà [QHUB HERBAL](/qhub-herbal.html). Nếu gắn Pixel, các sự kiện mẫu sẽ là xem từng trang trà, thêm hộp vào giỏ, vào trang thanh toán và hoàn tất đơn. Với ưu đãi trên website là trả 210.000đ nhận 3 hộp, sự kiện mua hàng của đơn đó nên mang giá trị 210.000 và đơn vị VND, không phải giá niêm yết của 3 hộp. Đây là danh sách minh họa cách nghĩ, không phải mô tả cấu hình thực tế của website đó.

## Cài TikTok Pixel và Events API theo cách nào?

Mọi việc bắt đầu trong **TikTok Events Manager** (Trình quản lý sự kiện), nằm trong TikTok Ads Manager. Anh chị tạo một nguồn dữ liệu web, đặt tên, rồi chọn cách kết nối. Có ba hướng chính, từ dễ tới khó.

### Cách 1: tích hợp đối tác

TikTok có danh sách tích hợp đối tác cho sự kiện web, gồm các nền tảng như Shopify, WooCommerce, BigCommerce, Shopline. Với nhóm này, anh chị cài ứng dụng hoặc plugin TikTok, đăng nhập tài khoản doanh nghiệp, chọn Pixel. Nhiều tích hợp đã tự bắn sẵn sự kiện chuẩn và có lựa chọn bật Events API. Đây là cách nhanh nhất, ít lỗi nhất, hợp phần lớn shop nhỏ.

### Cách 2: Google Tag Manager

TikTok có hướng dẫn cài Pixel qua **Google Tag Manager** (GTM, công cụ miễn phí của Google để quản lý mã đo lường ở một chỗ) và có mẫu thẻ chính thức. Lập trình viên gắn GTM một lần, đẩy dữ liệu đơn hàng vào dataLayer (lớp dữ liệu). Sau đó người chạy quảng cáo tự cấu hình thẻ TikTok, Meta, Google trên cùng một dữ liệu. Website gắn nhiều công cụ nên đi theo hướng này, giống cách bài [Google Analytics 4 cho website bán hàng](/kien-thuc/google-analytics-4-cho-website-ban-hang/) gợi ý. Muốn có Events API thì dùng GTM bản máy chủ, cần người hiểu kỹ thuật và có chi phí máy chủ.

### Cách 3: tự lập trình

Dán mã Pixel thủ công vào phần đầu trang, tự viết lệnh bắn sự kiện ở từng bước. Events API được gọi trực tiếp từ hệ thống đặt hàng. Kiểm soát tốt nhất, hợp với website tự viết.

| Cách cài | Độ khó | Chi phí | Hợp với |
| --- | --- | --- | --- |
| Tích hợp đối tác | Dễ | Thường miễn phí | Web làm trên Shopify, WooCommerce và nền tảng có sẵn kết nối |
| Google Tag Manager | Trung bình | Miễn phí, thêm phí máy chủ nếu làm Events API | Web gắn nhiều công cụ đo |
| Tự lập trình | Khó | Công lập trình | Web tự viết, có hệ thống đơn riêng |

Dù chọn cách nào, chỉ chọn **một** cách cho mỗi sự kiện. Cài plugin rồi dán thêm mã tay là con đường ngắn nhất tới dữ liệu đếm đôi.

## Advanced Matching và chất lượng khớp sự kiện

**Advanced Matching** (khớp nâng cao) là việc gửi kèm thông tin nhận diện khách như email, số điện thoại, đã được mã hóa SHA-256 (biến thông tin thành một chuỗi ký tự không đọc ngược được), để TikTok nhận ra người đó là tài khoản nào. Khớp được càng nhiều, TikTok càng gắn đúng đơn với quảng cáo và tối ưu càng tốt.

Theo Trung tâm trợ giúp TikTok Ads, có hai kiểu:

- **Tự động:** bật trong phần cài đặt Pixel, Pixel tự nhận thông tin khách điền trong form trên trang.
- **Thủ công:** lập trình viên tự gửi thông tin đã mã hóa kèm sự kiện.

Với Events API, ngoài email và số điện thoại đã mã hóa, nên gửi thêm mã nhấp chuột ttclid (TikTok gắn vào đường dẫn khi khách bấm quảng cáo) và cookie _ttp của Pixel nếu có. Các mã này giúp TikTok nối sự kiện từ máy chủ với lượt bấm quảng cáo.

Trong Events Manager có phần chẩn đoán và theo dõi chất lượng sự kiện. Ở đó anh chị xem được tỷ lệ sự kiện có thông tin khớp, cảnh báo thiếu tham số, cảnh báo event_id không trùng nhau giữa Pixel và Events API. Tên và cách chấm điểm có thể thay đổi theo thời gian, nên mình không nêu con số chuẩn ở đây. Nguyên tắc chung: cảnh báo nào hiện màu đỏ thì sửa trước khi tăng ngân sách.

## Kiểm tra dữ liệu và đọc số thế nào cho đúng?

### Kiểm tra sau khi cài

Đội mình kiểm theo thứ tự:

1. **TikTok Pixel Helper.** Đây là tiện ích miễn phí trên Chrome. Mở từng trang của website, tiện ích sẽ cho biết Pixel có chạy không, bắn sự kiện gì, có lỗi tham số không.
2. **Kiểm tra sự kiện trong Events Manager.** Tự đặt một đơn thử, xem sự kiện có về từ cả trình duyệt và máy chủ không, giá trị đơn có đúng không.
3. **Trạng thái gộp sự kiện.** Xem TikTok có báo event_id không khớp không.
4. **Đối chiếu với đơn thật.** So số đơn TikTok ghi nhận trong 7 ngày với số đơn trong hệ thống. Chênh nhỏ là bình thường. TikTok ghi nhiều đơn hơn thực tế là dấu hiệu đếm trùng.

### Cửa sổ phân bổ

**Cửa sổ phân bổ** (attribution window) là khoảng thời gian sau khi khách bấm hoặc xem quảng cáo mà một đơn vẫn được tính cho quảng cáo đó. Theo Trung tâm trợ giúp TikTok Ads, anh chị có thể đặt cửa sổ sau nhấp và sau xem trong phần cài đặt phân bổ. Nhiều tài liệu nói mặc định thường là 7 ngày sau nhấp và 1 ngày sau xem, nhưng anh chị nên kiểm tra lại đúng cài đặt trong tài khoản của mình.

Điều này giải thích vì sao số đơn trên TikTok, trên Meta và trên Google Analytics không bao giờ khớp nhau. Mỗi bên dùng cửa sổ và cách quy đơn riêng. Một khách xem video TikTok, hai hôm sau bấm quảng cáo Facebook rồi mua, có thể được cả hai nền tảng cùng nhận công. Đội mình luôn lấy số đơn trong hệ thống bán hàng làm gốc, rồi dùng thêm UTM trong Google Analytics để xem kênh nào đưa khách tới.

## Dữ liệu khách hàng và luật bảo vệ dữ liệu cá nhân

Gửi email, số điện thoại của khách cho TikTok, dù đã mã hóa, vẫn là xử lý dữ liệu cá nhân. Về khung pháp lý tại Việt Nam:

- **Nghị định 13/2023/NĐ-CP** về bảo vệ dữ liệu cá nhân có hiệu lực từ 01/07/2023, là văn bản đầu tiên quy định khá đầy đủ việc này.
- **Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15** có hiệu lực từ 01/01/2026, kèm **Nghị định 356/2025/NĐ-CP** quy định chi tiết. Theo các bài so sánh của các công ty luật, Nghị định 356/2025 thay cho Nghị định 13/2023 từ thời điểm luật có hiệu lực.

Những việc tối thiểu website nên làm:

- Có trang chính sách quyền riêng tư, nói rõ thu thập dữ liệu gì, để làm gì, chia sẻ cho ai, trong đó có các nền tảng quảng cáo như TikTok, Meta, Google.
- Có thông báo và cơ chế đồng ý phù hợp khi thu thập dữ liệu, ví dụ ô đồng ý cookie.
- Mã hóa thông tin trước khi gửi, chỉ gửi thông tin cần thiết.
- Không gửi dữ liệu nhạy cảm, ví dụ thông tin sức khỏe, vào tên sự kiện hay đường dẫn.

Phần này mình chỉ nêu ở mức tổng quát. Doanh nghiệp nên hỏi luật sư hoặc bộ phận pháp chế để có chính sách phù hợp mô hình của mình.

## Lỗi hay gặp khi cài TikTok Pixel

Nhiều tài khoản đội mình nhận lại để chạy tiếp thường mắc các lỗi giống nhau:

- **Cài Pixel hai lần**, một lần qua plugin, một lần dán tay. Mọi sự kiện bị đếm đôi.
- **Sự kiện mua hàng bắn ở trang thanh toán** thay vì sau khi đơn tạo thành công.
- **Dùng cả Pixel và Events API nhưng không có event_id.**
- **Giá trị đơn sai đơn vị tiền**, hoặc gửi giá trị cố định cho mọi đơn.
- **Pixel nằm trong tài khoản của người làm web.** Họ nghỉ thì doanh nghiệp mất quyền. Pixel phải thuộc tài khoản doanh nghiệp của chính chủ shop.
- **Chạy mục tiêu chuyển đổi khi Pixel chưa ghi nhận đủ sự kiện.** Hệ thống không có gì để học. Giai đoạn đầu có thể tối ưu theo thêm vào giỏ hoặc bắt đầu thanh toán, đủ dữ liệu rồi mới chuyển sang mua hàng.
- **Sửa giao diện website mà quên kiểm lại Pixel.** Đổi nút, đổi trang thanh toán là sự kiện có thể ngừng bắn mà không ai hay.

## Việc nên làm ngay tuần này

- Mở TikTok Events Manager, kiểm tra Pixel thuộc tài khoản doanh nghiệp của mình.
- Cài TikTok Pixel Helper, đi một vòng website và đặt một đơn thử. Xem đủ các sự kiện chuẩn chưa, sự kiện mua hàng có đúng giá trị VND không.
- Nếu đã bật Events API, xem phần chẩn đoán có cảnh báo event_id không khớp không.
- Ghi lại cửa sổ phân bổ đang dùng để đọc báo cáo cho đúng.
- Rà lại trang chính sách quyền riêng tư theo Luật 91/2025/QH15.

Nếu anh chị muốn có đội cùng thiết lập đo lường và chạy quảng cáo TikTok về website, QHUB Commerce (qhub.com.vn) có [dịch vụ quảng cáo TikTok và Shopee](/dich-vu/quang-cao-tiktok-shopee/), bên cạnh đội media, đội vận hành sàn, đội KOC và đội host livestream. Các bài khác về quảng cáo nằm trong chủ đề [quảng cáo TikTok](/kien-thuc/chu-de/quang-cao-tiktok/).
