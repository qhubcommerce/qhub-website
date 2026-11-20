---
title: "Google Analytics 4 cho website bán hàng"
slug: google-analytics-4-cho-website-ban-hang
topic: website-seo
keyword: "google analytics 4"
keywords: ["cài đặt ga4", "sự kiện thương mại điện tử ga4", "key events ga4", "utm cho facebook tiktok zalo", "consent mode"]
description: "Google Analytics 4 cho website bán hàng: tạo thuộc tính, gắn thẻ, cài sự kiện mua hàng, đánh dấu key events, gắn UTM và các báo cáo nên xem mỗi tuần."
date: 2026-11-21
updated: 2026-11-21
summary:
  - "Google Analytics 4 (GA4) đo mọi hành động trên website dưới dạng sự kiện; website bán hàng cần tối thiểu bốn sự kiện view_item, add_to_cart, begin_checkout và purchase kèm giá trị đơn."
  - "Từ tháng 3/2024, Google đổi tên \"conversions\" trong GA4 thành \"key events\" (sự kiện chính); chữ \"conversions\" nay dùng cho chuyển đổi trong Google Ads."
  - "Thời gian lưu dữ liệu chi tiết mặc định chỉ 2 tháng; nên chỉnh lên 14 tháng ngay khi tạo thuộc tính để còn so sánh cùng kỳ năm trước."
  - "Mọi link đặt trên TikTok, Facebook, Zalo nên gắn UTM, và website cần có thông báo đồng ý cookie phù hợp Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15, hiệu lực từ 01/01/2026."
faq:
  - q: "Google Analytics 4 có mất phí không?"
    a: "Bản tiêu chuẩn của Google Analytics 4 miễn phí và đủ dùng cho hầu hết website bán hàng vừa và nhỏ. Bản trả phí Analytics 360 dành cho doanh nghiệp rất lớn, cần giới hạn dữ liệu cao hơn và thời gian lưu dữ liệu dài hơn."
  - q: "Nên gắn GA4 bằng gtag hay Google Tag Manager?"
    a: "Website chỉ cần đo cơ bản và có nền tảng hỗ trợ sẵn thì dán thẻ Google (gtag.js) hoặc dùng mục kết nối có sẵn là đủ. Nếu website còn gắn Pixel Meta, TikTok Pixel và nhiều sự kiện riêng, Google Tag Manager giúp quản lý tập trung, ít phải sửa mã nguồn. Điều quan trọng là chỉ chọn một cách, không gắn cả hai cùng lúc."
  - q: "Key events khác conversions thế nào?"
    a: "Key events là tên mới Google dùng trong GA4 từ tháng 3/2024 cho những sự kiện quan trọng với doanh nghiệp, ví dụ purchase hay gửi form. Conversions nay là chuyển đổi được dùng trong Google Ads để đo và tối ưu quảng cáo. Muốn Google Ads dùng một key event, anh chị nhập sự kiện đó từ GA4 vào Google Ads."
  - q: "Vì sao số đơn trong GA4 ít hơn số đơn thật?"
    a: "GA4 chạy trên trình duyệt nên có thể hụt dữ liệu khi khách chặn cookie, dùng trình chặn quảng cáo, từ chối đồng ý theo dõi hoặc tắt trang trước khi mã kịp chạy. Ngoài ra đơn chốt qua điện thoại, Zalo không đi qua trang cảm ơn thì GA4 không ghi được. Lệch vài phần trăm đến vài chục phần trăm là bình thường; lệch lớn hơn thì nên kiểm tra lại cách cài sự kiện purchase."
  - q: "Có bắt buộc phải có thông báo cookie khi dùng GA4 ở Việt Nam không?"
    a: "GA4 thu thập mã định danh trình duyệt và dữ liệu hành vi, nên việc này thuộc phạm vi xử lý dữ liệu cá nhân. Từ 01/01/2026, Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 có hiệu lực, yêu cầu thông báo và có sự đồng ý phù hợp. Cách an toàn là có chính sách quyền riêng tư, banner cookie cho khách chọn và hỏi luật sư cho mô hình cụ thể của mình."
sources:
  - title: "Evolving Google Analytics for more insightful measurement – Google Blog (03/2024)"
    url: "https://blog.google/products/marketingplatform/analytics/evolving-google-analytics-for-more-insightful-measurement/"
  - title: "Google Analytics 4 addresses Google Ads report discrepancies with conversion update – Search Engine Land"
    url: "https://searchengineland.com/google-analytics-4-ads-report-conversion-key-events-438613"
  - title: "[GA4] Recommended events – Analytics Help"
    url: "https://support.google.com/analytics/answer/9267735"
  - title: "Measure ecommerce – Google Analytics for Developers"
    url: "https://developers.google.com/analytics/devguides/collection/ga4/ecommerce"
  - title: "Enhanced measurement events – Analytics Help"
    url: "https://support.google.com/analytics/answer/9216061"
  - title: "Data retention – Analytics Help"
    url: "https://support.google.com/analytics/answer/7667196"
  - title: "URL builders: Collect campaign data with custom URLs – Analytics Help"
    url: "https://support.google.com/analytics/answer/10917952"
  - title: "Luật Bảo vệ dữ liệu cá nhân 2025 số 91/2025/QH15 – Thư viện Pháp luật"
    url: "https://thuvienphapluat.vn/van-ban/Bo-may-hanh-chinh/Luat-Bao-ve-du-lieu-ca-nhan-2025-so-91-2025-QH15-625628.aspx"
  - title: "Đã có Luật Bảo vệ dữ liệu cá nhân 2025, số 91/2025/QH15 – LuatVietnam"
    url: "https://luatvietnam.vn/tin-van-ban-moi/da-co-luat-bao-ve-du-lieu-ca-nhan-2025-so-91-2025-qh15-186-102925-article.html"
---

**Google Analytics 4 (GA4) là công cụ đo lường miễn phí của Google, cho anh chị biết khách đến website từ đâu, xem sản phẩm nào, bỏ giỏ ở bước nào và mua bao nhiêu tiền.** Với website bán hàng, cài cho có thì chưa đủ: phải cài đúng bốn sự kiện thương mại điện tử, đánh dấu sự kiện mua hàng là sự kiện chính, gắn UTM cho mọi link và có cơ chế đồng ý cookie. Làm đủ, anh chị biết tiền quảng cáo và công làm nội dung đang mang về đơn ở kênh nào.

Bài này đội QHUB đi từng bước, từ tạo tài khoản tới lịch xem báo cáo mỗi tuần. Thông tin được đối chiếu với trang trợ giúp của Google Analytics ngày 21/11/2026; tên nút trong giao diện có thể đổi theo thời gian.

## Google Analytics 4 là gì, khác bản cũ ở đâu?

GA4 là thế hệ Google Analytics hiện hành, thay cho Universal Analytics đã ngừng xử lý dữ liệu từ năm 2023. Điểm khác lớn nhất là **mô hình sự kiện** (event-based): mọi thứ trên website đều là một sự kiện, ví dụ xem trang là `page_view`, thêm vào giỏ là `add_to_cart`, đơn thành công là `purchase`.

Mỗi sự kiện mang theo **tham số** (parameter), tức thông tin đi kèm. Ví dụ `purchase` mang mã đơn, giá trị đơn, đơn vị tiền và danh sách sản phẩm. Nhờ vậy GA4 tính được doanh thu và sản phẩm bán chạy.

Cấu trúc gồm ba tầng: **tài khoản** (account, thường đặt theo tên doanh nghiệp), **thuộc tính** (property, nơi chứa dữ liệu và báo cáo của một website) và **luồng dữ liệu** (data stream, nguồn đổ dữ liệu vào thuộc tính). Một chỉ số mới cần biết là **tỷ lệ tương tác** (engagement rate): phần trăm phiên kéo dài hơn 10 giây, hoặc có sự kiện chính, hoặc xem từ 2 trang trở lên. Chỉ số này thay cho "tỷ lệ thoát" ở bản cũ.

Search Console cho biết chuyện xảy ra trên trang kết quả Google, còn GA4 đo chuyện xảy ra sau khi khách vào website. Nếu chưa cài Search Console, anh chị xem bài [Google Search Console: cài đặt và đọc báo cáo](/kien-thuc/google-search-console-cai-dat-va-doc-bao-cao/) trước, lát nữa mình sẽ nối hai công cụ.

## Cài đặt GA4 từng bước như thế nào?

### Tạo tài khoản, thuộc tính và luồng dữ liệu web

Phần này mất khoảng 15 phút. Dùng email Google của doanh nghiệp, không dùng email cá nhân của nhân viên hay của bên làm web.

1. Vào analytics.google.com, chọn **Bắt đầu đo lường**.
2. **Tạo tài khoản:** đặt tên doanh nghiệp, giữ các tùy chọn chia sẻ dữ liệu theo nhu cầu.
3. **Tạo thuộc tính:** đặt tên thương hiệu, chọn **múi giờ Việt Nam (GMT+7)** và **đơn vị tiền tệ Đồng Việt Nam (VND)**. Hai thông số này chọn sai thì báo cáo doanh thu và báo cáo theo ngày đều lệch.
4. Điền thông tin doanh nghiệp, chọn mục tiêu bán hàng trực tuyến.
5. **Tạo luồng dữ liệu Web:** nhập tên miền. GA4 cấp **mã đo lường** (Measurement ID) dạng `G-XXXXXXXXXX` để gắn lên website.
6. Trong phần cài đặt luồng, kiểm tra **Đo lường nâng cao** (Enhanced measurement) đang bật.

Ngay sau đó, làm thêm ba việc nhiều người bỏ quên:

- **Chỉnh thời gian lưu dữ liệu lên 14 tháng.** Vào Quản trị, mục Thu thập và sửa đổi dữ liệu, chọn Lưu giữ dữ liệu. Theo trang trợ giúp của Google, thuộc tính tiêu chuẩn chỉ có hai lựa chọn là 2 tháng hoặc 14 tháng, và mặc định là 2 tháng. Mốc này ảnh hưởng tới báo cáo Khám phá (Explorations), không ảnh hưởng báo cáo tổng hợp tiêu chuẩn, nhưng để 2 tháng thì năm sau không còn dữ liệu chi tiết để so cùng kỳ.
- **Khai báo nguồn giới thiệu không mong muốn.** Khách thanh toán qua VNPAY, MoMo, ngân hàng rồi quay về trang cảm ơn thì GA4 có thể ghi nguồn đơn là cổng thanh toán. Thêm tên miền các cổng này vào danh sách nguồn giới thiệu không mong muốn trong cấu hình thẻ của luồng dữ liệu.
- **Lọc lưu lượng nội bộ** bằng địa chỉ IP văn phòng.

### Gắn thẻ: dùng gtag hay Google Tag Manager?

Có ba cách đưa mã GA4 lên website.

| Cách gắn | Làm thế nào | Hợp với | Lưu ý |
| --- | --- | --- | --- |
| Tích hợp sẵn của nền tảng | Dán Measurement ID vào mục cài đặt của nền tảng làm web | Shop nhỏ, web dựng trên nền tảng phổ biến | Kiểm tra nền tảng có gửi sẵn sự kiện thương mại điện tử không |
| Thẻ Google (gtag.js) | Dán đoạn mã GA4 cấp vào phần `<head>` của mọi trang | Web tự viết, ít công cụ đo | Sự kiện mua hàng phải nhờ lập trình viên viết thêm |
| Google Tag Manager (GTM) | Cài một container GTM, quản lý mọi thẻ trong giao diện GTM | Web gắn nhiều công cụ: GA4, Pixel Meta, TikTok Pixel | Cần người hiểu cách đẩy dữ liệu qua dataLayer |

**Google Tag Manager** là công cụ miễn phí của Google để quản lý các mã đo lường ở một chỗ. Lập trình viên gắn GTM một lần và đẩy dữ liệu đơn hàng vào **dataLayer** (lớp dữ liệu); sau đó người làm marketing tự thêm, sửa thẻ mà không đụng mã nguồn. Website chạy quảng cáo Meta, TikTok, Google cùng lúc nên chọn GTM từ đầu và dùng chung một dataLayer với Pixel, như bài [Pixel Meta và Conversions API cho website bán hàng](/kien-thuc/pixel-meta-va-conversions-api-cho-website-ban-hang/) hướng dẫn.

Điều cấm kỵ nhất là **gắn hai lần**, ví dụ vừa dán gtag tay vừa bật tích hợp của nền tảng. Mọi số liệu bị đếm đôi.

### Đo lường nâng cao đã đo sẵn những gì?

**Đo lường nâng cao** (Enhanced measurement) là nhóm sự kiện GA4 tự ghi nhận khi được bật, không cần viết mã. Theo trang trợ giúp của Google Analytics, nhóm này gồm:

- Lượt xem trang (`page_view`).
- Cuộn trang tới khoảng 90% chiều dài (`scroll`).
- Lượt nhấp ra ngoài website (`click`), ví dụ bấm sang Shopee, TikTok Shop.
- Tìm kiếm trên website (`view_search_results`).
- Tương tác với video YouTube nhúng.
- Tải tệp (`file_download`), ví dụ tải catalogue PDF.
- Tương tác với biểu mẫu (`form_start`, `form_submit`).

Với doanh nghiệp vừa bán trên sàn vừa có website, sự kiện nhấp ra ngoài cho biết bao nhiêu người đọc web rồi bấm sang gian hàng, tức trả lời câu hỏi "website có đỡ cho sàn không" trong bài [doanh nghiệp bán trên sàn có cần website riêng không](/kien-thuc/doanh-nghiep-ban-tren-san-co-can-website-rieng-khong/). Nhưng đo lường nâng cao **không đo** xem sản phẩm, thêm giỏ hay mua hàng; những sự kiện đó phải cài riêng.

## Cài sự kiện bán hàng, key events và liên kết công cụ Google

### Website bán hàng phải có những sự kiện nào?

Google có danh sách **sự kiện đề xuất** (recommended events) cho thương mại điện tử. Đặt đúng tên thì GA4 tự đổ dữ liệu vào báo cáo bán hàng; đặt tên tự chế như `them_gio` thì báo cáo trống trơn.

| Sự kiện | Khi nào gửi | Tham số cần có | Mức độ |
| --- | --- | --- | --- |
| `view_item_list` | Xem trang danh mục, danh sách sản phẩm | `item_list_name`, `items` | Nên có |
| `view_item` | Mở trang chi tiết sản phẩm | `currency`, `value`, `items` | Bắt buộc |
| `add_to_cart` | Bấm thêm vào giỏ | `currency`, `value`, `items` | Bắt buộc |
| `begin_checkout` | Bắt đầu bước thanh toán | `currency`, `value`, `items` | Bắt buộc |
| `add_shipping_info` | Điền xong thông tin giao hàng | `shipping_tier`, `items` | Nên có |
| `purchase` | Đơn tạo thành công, ở trang cảm ơn | `transaction_id`, `currency`, `value`, `items` | Bắt buộc |
| `generate_lead` | Gửi form tư vấn, đăng ký nhận tin | `currency`, `value` (nếu có) | Nên có nếu có form |

`items` là danh sách sản phẩm, mỗi sản phẩm có `item_id`, `item_name`, `price`, `quantity`. `currency` luôn là `VND`, `value` ghi số nguyên, không có dấu chấm ngăn cách.

Lấy ví dụ một website bán hàng riêng của thương hiệu như [qhubherbal.com](https://qhubherbal.com/), web của thương hiệu trà [QHUB HERBAL](/qhub-herbal.html) do chính QHUB xây. Khi khách mua theo ưu đãi mua 2 tặng 1 trên website, trả 210.000 đồng nhận 3 hộp, sự kiện `purchase` nên ghi `value` là 210000, `currency` là VND, mã đơn là `transaction_id`, và trong `items` ghi rõ hộp tặng có giá 0. Đây là cách nghĩ để minh họa, không phải mô tả cấu hình thực tế của website đó.

Ba lưu ý với sự kiện `purchase`:

- **Luôn gửi `transaction_id`.** GA4 dùng mã này để loại bớt đơn trùng khi khách tải lại trang cảm ơn.
- **Gửi giá trị thật** sau giảm giá, không gửi giá niêm yết, không gửi một con số cố định cho mọi đơn.
- **Đơn chốt ngoài website** (điện thoại, Zalo) không có trong GA4, nên số đơn GA4 thường thấp hơn hệ thống bán hàng.

### Key events là gì?

**Key event (sự kiện chính)** là sự kiện anh chị đánh dấu là quan trọng nhất với doanh nghiệp. Từ tháng 3/2024, Google đổi tên "conversions" trong GA4 thành "key events". Theo Google Blog, chữ "conversions" từ đó dùng cho chuyển đổi trong Google Ads, để số liệu hai nơi bớt vênh. Tài liệu cũ ghi "đánh dấu là chuyển đổi" chính là bước này.

Cách làm: vào Quản trị, mục Hiển thị dữ liệu, chọn Sự kiện, bật dấu sao "Đánh dấu là sự kiện chính" cho `purchase`. Nếu website có form tư vấn thì đánh dấu thêm `generate_lead`. Không nên đánh dấu quá nhiều, kiểu cả `scroll` hay `page_view`, vì báo cáo sẽ mất ý nghĩa.

### Liên kết Search Console

Vào Quản trị, mục Liên kết sản phẩm, chọn Liên kết Search Console, chọn tài sản và luồng web. Sau đó vào Thư viện báo cáo để xuất bản nhóm báo cáo Search Console, anh chị sẽ thấy truy vấn tìm kiếm cạnh dữ liệu doanh thu. Việc này đi đôi với nền móng trong bài [website bán hàng chuẩn SEO năm 2026](/kien-thuc/website-ban-hang-chuan-seo-nam-2026-huong-dan-tu-a-den-z/).

### Liên kết Google Ads

Cũng trong Liên kết sản phẩm, chọn Liên kết Google Ads. Sau khi liên kết, nhập key event `purchase` từ GA4 vào Google Ads để làm chuyển đổi tối ưu. Lưu ý: nếu Google Ads đã có thẻ chuyển đổi riêng cho cùng hành động mua hàng, chỉ để một nguồn làm chuyển đổi chính, tránh đếm hai lần.

## Gắn UTM cho link từ TikTok, Facebook, Zalo thế nào?

**UTM** là các tham số gắn thêm vào cuối đường link để GA4 biết khách đến từ đâu, qua kênh nào, thuộc chiến dịch nào. Không gắn UTM, rất nhiều lượt truy cập từ ứng dụng như Zalo, TikTok bị GA4 xếp vào nhóm "Direct" (truy cập trực tiếp), vì ứng dụng không gửi kèm thông tin nguồn.

Theo trang trợ giúp của Google Analytics, ba tham số nên có là `utm_source` (nguồn), `utm_medium` (phương tiện) và `utm_campaign` (chiến dịch); thêm `utm_content` nếu muốn phân biệt từng video.

| Vị trí đặt link | utm_source | utm_medium | Ví dụ utm_campaign |
| --- | --- | --- | --- |
| Link bio TikTok | tiktok | social | bio |
| Bài đăng Fanpage Facebook | facebook | social | sale-12-12 |
| Quảng cáo Meta trỏ về web | facebook | paid_social | sale-12-12 |
| Tin nhắn Zalo OA gửi khách cũ | zalo | message | khach-cu-thang-12 |

Quy tắc đội mình luôn giữ:

- **Viết thường toàn bộ**, không dấu, dùng gạch ngang. GA4 phân biệt chữ hoa chữ thường, `Facebook` và `facebook` thành hai nguồn khác nhau.
- **Thống nhất bảng quy ước** trong một file chung.
- **Không gắn UTM cho link nội bộ** giữa các trang trên chính website. Làm vậy GA4 cắt phiên và ghi đè nguồn gốc thật.

## Các báo cáo nên xem mỗi tuần

Chủ shop chỉ cần nhìn vài báo cáo cố định, mỗi tuần khoảng 20 phút, luôn so với tuần trước.

| Báo cáo (trong mục Báo cáo) | Câu hỏi cần trả lời | Hành động gợi ý |
| --- | --- | --- |
| Thu nạp người dùng → Thu nạp lưu lượng truy cập | Kênh nào mang khách, kênh nào mang đơn? | Dồn công vào kênh có doanh thu, không chỉ kênh nhiều lượt xem |
| Tương tác → Trang và màn hình | Trang sản phẩm nào được xem nhiều mà ít người thêm giỏ? | Sửa ảnh, giá, mô tả của trang đó |
| Tương tác → Sự kiện | Số `add_to_cart`, `begin_checkout`, `purchase` tăng hay giảm? | Một bước giảm đột ngột thường là lỗi kỹ thuật |
| Kiếm tiền → Mua hàng thương mại điện tử | Sản phẩm nào bán chạy, doanh thu bao nhiêu? | Ưu tiên sản phẩm đó trên trang chủ và quảng cáo |
| Hành trình mua hàng / thanh toán | Khách rơi rụng ở bước nào? | Rơi nhiều ở thanh toán thì kiểm tra phí ship, phương thức thanh toán |
| Search Console → Truy vấn | Khách gõ từ gì để vào web? | Viết thêm bài, sửa tiêu đề trang cho truy vấn đang lên |

GA4 dùng để đọc xu hướng, không phải sổ kế toán. Sổ đơn thật nằm trong hệ thống bán hàng.

## Đồng ý cookie, Consent Mode và luật dữ liệu cá nhân

GA4 dùng cookie và mã định danh trình duyệt để nhận ra người dùng quay lại, tức là xử lý dữ liệu cá nhân. Trước đây khung pháp lý chính là Nghị định 13/2023/NĐ-CP. Từ **01/01/2026, Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 có hiệu lực**, kèm Nghị định 356/2025/NĐ-CP hướng dẫn chi tiết, yêu cầu người dùng được thông báo và đồng ý phù hợp.

**Consent Mode** (chế độ đồng ý) là cơ chế giúp thẻ Google điều chỉnh theo lựa chọn của khách trên banner cookie. Bản v2 có bốn tín hiệu: `analytics_storage`, `ad_storage`, `ad_user_data`, `ad_personalization`, với hai cách triển khai:

- **Cơ bản (basic):** thẻ Google chỉ chạy sau khi khách bấm đồng ý.
- **Nâng cao (advanced):** khách từ chối thì thẻ chỉ gửi tín hiệu không kèm cookie để Google ước tính phần dữ liệu thiếu.

Việc tối thiểu nên làm:

- Có trang chính sách quyền riêng tư, ghi rõ dùng Google Analytics, Pixel quảng cáo để làm gì.
- Có banner cookie cho khách chọn đồng ý hoặc từ chối, nối với Consent Mode qua công cụ quản lý đồng ý hoặc qua GTM.
- Không gửi email, số điện thoại, tên khách vào GA4; chính sách của Google Analytics cũng cấm việc này.

Phần pháp lý mình chỉ nêu tổng quát, doanh nghiệp nên hỏi luật sư cho mô hình cụ thể.

## Lỗi hay gặp khi cài Google Analytics 4

Những lỗi đội mình gặp lại nhiều nhất khi nhận website để vận hành:

- **Tài khoản GA4 nằm trong email của bên làm web.** Hết hợp đồng là doanh nghiệp mất dữ liệu.
- **Gắn mã hai lần**, doanh thu và lượt xem nhân đôi.
- **Thuộc tính để tiền tệ USD hoặc sự kiện thiếu `currency`**, doanh thu bị quy đổi lệch hoặc bỏ trống.
- **Sự kiện `purchase` gửi ở bước bấm nút "Đặt hàng"** chứ không phải khi đơn đã tạo thành công, nên đơn lỗi, đơn hủy cũng bị tính.
- **Không gắn UTM**, lượt truy cập từ Zalo, TikTok lẫn vào "Direct".
- **Cài xong rồi để đó**, lỗi đo lường tồn tại hàng tháng không ai hay.

## Việc nên làm ngay tuần này

1. Kiểm tra tài khoản GA4 thuộc email doanh nghiệp, múi giờ GMT+7, tiền tệ VND.
2. Chỉnh lưu dữ liệu lên 14 tháng.
3. Đặt một đơn thử, mở báo cáo Thời gian thực xem đủ `view_item`, `add_to_cart`, `begin_checkout`, `purchase` chưa, giá trị đơn có đúng không.
4. Đánh dấu `purchase` là key event, liên kết Search Console và Google Ads.
5. Lập bảng quy ước UTM, gắn lại link bio TikTok, Fanpage, Zalo OA.
6. Rà banner cookie và chính sách quyền riêng tư theo Luật 91/2025/QH15.

QHUB Commerce là đội vận hành gian hàng đa sàn, có đội media, đội vận hành sàn, đội KOC và đội host livestream, nên tụi mình đọc số liệu website song song với số liệu sàn mỗi tuần. Các bài khác về website và SEO nằm trong chủ đề [website và SEO](/kien-thuc/chu-de/website-seo/).
