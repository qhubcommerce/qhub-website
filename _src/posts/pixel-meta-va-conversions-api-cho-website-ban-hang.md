---
title: "Pixel Meta và Conversions API cho website bán hàng: cài đúng từ đầu"
slug: pixel-meta-va-conversions-api-cho-website-ban-hang
topic: ban-hang-facebook
keyword: "pixel facebook"
keywords: ["pixel meta", "conversions api là gì", "cài pixel facebook cho website", "sự kiện purchase facebook", "event match quality"]
description: "Pixel Facebook và Conversions API là gì, khác nhau ra sao, website bán hàng cần đo sự kiện nào, cách cài, chống đếm trùng bằng event_id và kiểm tra dữ liệu."
date: 2026-11-20
updated: 2026-11-20
summary:
  - "Pixel Facebook (Meta Pixel) là đoạn mã chạy trên trình duyệt để ghi nhận hành động của khách trên website; Conversions API gửi cùng dữ liệu đó từ máy chủ của website thẳng tới Meta."
  - "Meta khuyên dùng cả hai cùng lúc; để không bị đếm trùng, mỗi sự kiện gửi từ hai đường phải có cùng tên sự kiện và cùng mã event_id."
  - "Website bán hàng tối thiểu cần đo 5 sự kiện: xem trang, xem sản phẩm, thêm vào giỏ, bắt đầu thanh toán và mua hàng có kèm giá trị đơn."
  - "Dữ liệu khách hàng gửi cho Meta phải được mã hóa và thu thập đúng Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15, có hiệu lực từ 01/01/2026."
faq:
  - q: "Pixel Facebook là gì?"
    a: "Pixel Facebook, nay gọi là Meta Pixel, là đoạn mã gắn vào website để ghi nhận hành động của người xem như xem sản phẩm, thêm vào giỏ, mua hàng. Dữ liệu này giúp Meta đo hiệu quả quảng cáo, tối ưu quảng cáo theo đơn hàng và tạo tệp khách để quảng cáo lại."
  - q: "Conversions API khác Pixel thế nào?"
    a: "Pixel chạy trên trình duyệt của khách, nên có thể bị chặn bởi trình chặn quảng cáo, cài đặt quyền riêng tư hoặc mạng chậm. Conversions API gửi dữ liệu từ máy chủ của website tới Meta, không phụ thuộc trình duyệt. Dùng cả hai giúp dữ liệu đầy đủ hơn, với điều kiện phải chống đếm trùng."
  - q: "Website nhỏ có cần Conversions API không?"
    a: "Nếu website có chạy quảng cáo Meta và muốn tối ưu theo đơn hàng thì nên có. Nhiều nền tảng làm web bán hàng đã có tích hợp sẵn, chỉ cần kết nối trong phần cài đặt. Website ít đơn, chưa chạy quảng cáo có thể bắt đầu bằng Pixel, rồi thêm Conversions API khi tăng ngân sách."
  - q: "Làm sao để không bị đếm trùng đơn khi dùng cả Pixel và Conversions API?"
    a: "Mỗi sự kiện gửi từ trình duyệt và từ máy chủ phải có cùng tên sự kiện, ví dụ Purchase, và cùng mã event_id, thường dùng mã đơn hàng. Meta dựa vào hai thông tin này để nhận ra đây là một sự kiện và chỉ tính một lần."
  - q: "Event Match Quality là gì?"
    a: "Event Match Quality là điểm từ 0 đến 10 trong Trình quản lý sự kiện, cho biết dữ liệu khách hàng gửi kèm sự kiện giúp Meta nhận ra người dùng tốt tới đâu. Gửi thêm thông tin đã mã hóa như email, số điện thoại, cùng mã nhận diện trình duyệt thường giúp điểm này tăng."
sources:
  - title: "Conversions API – Meta for Developers"
    url: "https://developers.facebook.com/documentation/ads-commerce/conversions-api"
  - title: "Handling duplicate Pixel and Conversions API events – Meta for Developers"
    url: "https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events"
  - title: "Conversion tracking – Meta Pixel – Meta for Developers"
    url: "https://developers.facebook.com/documentation/meta-pixel/implementation/conversion-tracking"
  - title: "Conversions API best practices – Meta for Developers"
    url: "https://developers.facebook.com/docs/marketing-api/conversions-api/best-practices"
  - title: "Luật Bảo vệ dữ liệu cá nhân 2025 số 91/2025/QH15 – Thư viện Pháp luật"
    url: "https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Luat-Bao-ve-du-lieu-ca-nhan-2025-91-2025-QH15-625628.aspx"
  - title: "Nghị định 356/2025/NĐ-CP quy định chi tiết Luật Bảo vệ dữ liệu cá nhân – LuatVietnam"
    url: "https://luatvietnam.vn/dan-su/nghi-dinh-356-2025-nd-cp-quy-dinh-chi-tiet-luat-bao-ve-du-lieu-ca-nhan-422896-d1.html"
  - title: "Luật Bảo vệ dữ liệu cá nhân 2025 có hiệu lực khi nào – LuatVietnam"
    url: "https://luatvietnam.vn/dan-su/luat-bao-ve-du-lieu-ca-nhan-2025-co-hieu-luc-khi-nao-568-103652-article.html"
---

**Pixel Facebook (nay gọi là Meta Pixel) là đoạn mã chạy trên trình duyệt để ghi nhận hành động của khách trên website, còn Conversions API gửi cùng dữ liệu đó từ máy chủ của website thẳng tới Meta.** Meta khuyên dùng cả hai cùng lúc. Pixel dễ cài nhưng có thể bị chặn bởi trình duyệt và trình chặn quảng cáo. Conversions API bù vào phần bị mất. Để không đếm trùng một đơn thành hai, mỗi sự kiện phải mang cùng tên và cùng mã event_id ở cả hai đường.

Bài này đội QHUB giải thích hai công cụ bằng lời dễ hiểu, những sự kiện website bán hàng cần đo, các cách cài từ dễ tới khó, cách kiểm tra dữ liệu và những lỗi đội mình hay gặp khi nhận lại tài khoản quảng cáo của khách. Thông tin kỹ thuật được kiểm tra qua tài liệu Meta for Developers ngày 20/11/2026. Giao diện Trình quản lý sự kiện có thể đổi tên nút theo thời gian.

## Pixel Facebook là gì và để làm gì?

Hãy hình dung website như một cửa hàng. Quảng cáo Facebook đưa khách tới cửa. Pixel là người đứng trong cửa hàng ghi sổ: khách nào xem kệ nào, bỏ gì vào giỏ, có ra quầy thanh toán không.

Dữ liệu Pixel ghi lại được dùng cho ba việc:

1. **Đo hiệu quả quảng cáo.** Biết quảng cáo nào mang lại đơn hàng thật, không chỉ lượt nhấp.
2. **Tối ưu quảng cáo theo mục tiêu.** Khi chọn mục tiêu "mua hàng", Meta cần dữ liệu sự kiện mua hàng để tìm người có khả năng mua.
3. **Tạo tệp khách hàng.** Ví dụ người đã thêm vào giỏ nhưng chưa mua trong 7 ngày, để quảng cáo nhắc lại.

Không có Pixel, quảng cáo website giống như phát tờ rơi rồi không biết ai đã tới cửa hàng.

## Conversions API là gì, vì sao cần thêm?

Conversions API (viết tắt CAPI) là cách gửi sự kiện từ máy chủ của website tới Meta. Thay vì nhờ trình duyệt của khách gửi, máy chủ tự gửi khi có sự kiện, ví dụ khi đơn hàng được tạo trong hệ thống.

Vì sao cần? Vì Pixel phụ thuộc trình duyệt, và trình duyệt ngày càng chặn nhiều:

| Tình huống | Pixel | Conversions API |
| --- | --- | --- |
| Khách dùng trình chặn quảng cáo | Có thể bị chặn | Vẫn gửi được |
| Trình duyệt hạn chế theo dõi | Có thể mất dữ liệu | Không phụ thuộc trình duyệt |
| Khách tắt trang trước khi mã chạy xong | Có thể mất sự kiện | Máy chủ vẫn ghi nhận đơn |
| Sự kiện xảy ra ngoài website (xác nhận đơn qua điện thoại) | Không ghi được | Gửi được từ hệ thống |
| Độ khó cài đặt | Dễ | Trung bình đến khó |

Meta khuyến nghị dùng cả hai theo kiểu "dự phòng": Pixel bắt sự kiện trên trình duyệt, CAPI gửi lại từ máy chủ. Sự kiện nào cả hai cùng bắt được thì Meta gộp làm một.

## Website bán hàng cần đo những sự kiện nào?

Meta có danh sách sự kiện chuẩn. Với website bán hàng, đội mình luôn cài tối thiểu 5 sự kiện:

| Sự kiện chuẩn | Khi nào bắn | Thông tin nên gửi kèm |
| --- | --- | --- |
| PageView | Mỗi lần tải trang | Tự động |
| ViewContent | Xem trang sản phẩm | Mã sản phẩm, tên, giá |
| AddToCart | Bấm thêm vào giỏ | Mã sản phẩm, số lượng, giá trị |
| InitiateCheckout | Bắt đầu trang thanh toán | Giá trị giỏ, số sản phẩm |
| Purchase | Đơn hàng tạo thành công | Mã đơn, giá trị đơn, đơn vị tiền VND |

Nếu website có form tư vấn, thêm sự kiện **Lead** khi gửi form thành công. Nếu có nút gọi điện hoặc nhắn tin, có thể thêm **Contact**.

Ví dụ với một web bán hàng riêng như qhubherbal.com của thương hiệu trà [QHUB HERBAL](/qhub-herbal.html), danh sách sự kiện mẫu sẽ gồm xem từng sản phẩm trà, thêm hộp vào giỏ, bắt đầu thanh toán và mua hàng với giá trị đơn (ví dụ đơn mua 2 tặng 1 trên website là 210.000 đồng nhận 3 hộp). Đây là danh sách mẫu để minh họa cách nghĩ, không phải mô tả cấu hình thực tế của website đó.

Hai lưu ý quan trọng với sự kiện Purchase:

- **Chỉ bắn một lần cho mỗi đơn.** Lỗi hay gặp là trang cảm ơn bị tải lại, Pixel bắn Purchase lần nữa.
- **Gửi giá trị đơn thật**, đúng đơn vị VND, không gửi giá cố định cho mọi đơn. Meta cần giá trị để tối ưu theo doanh thu.

## Các cách cài Pixel và Conversions API

Từ dễ tới khó:

### Cách 1: tích hợp sẵn của nền tảng làm web

Nhiều nền tảng làm web bán hàng có mục kết nối Meta trong phần cài đặt. Anh chị đăng nhập Business Manager, chọn tập dữ liệu (Pixel), bật Conversions API nếu nền tảng hỗ trợ. Cách này nhanh nhất, ít lỗi nhất, phù hợp phần lớn shop nhỏ. Trước khi cài, Business Manager cần được thiết lập đúng như hướng dẫn trong bài [Business Manager và Meta Business Suite](/kien-thuc/business-manager-meta-business-suite-thiet-lap-dung-ngay-tu-dau/).

### Cách 2: Conversions API Gateway

Meta có giải pháp Conversions API Gateway, chạy trên hạ tầng đám mây, nhận sự kiện từ Pixel rồi gửi lại từ máy chủ. Hợp với website không có tích hợp sẵn mà đội không có lập trình viên. Có chi phí hạ tầng hằng tháng tùy nhà cung cấp.

### Cách 3: Google Tag Manager phía máy chủ

Dùng Google Tag Manager bản máy chủ (server-side) để gửi sự kiện tới Meta, đồng thời tới các nền tảng khác như TikTok, Google. Linh hoạt, nhưng cần người hiểu kỹ thuật và có chi phí máy chủ.

### Cách 4: lập trình trực tiếp

Lập trình viên gọi Conversions API từ hệ thống đặt hàng. Kiểm soát tốt nhất, hợp với website tự viết, có hệ thống đơn riêng.

| Cách cài | Độ khó | Chi phí | Hợp với |
| --- | --- | --- | --- |
| Tích hợp sẵn | Dễ | Thường miễn phí | Web làm trên nền tảng phổ biến |
| Conversions API Gateway | Trung bình | Phí hạ tầng | Web không có tích hợp, không có lập trình viên |
| Tag Manager phía máy chủ | Khó | Phí máy chủ | Đội có người kỹ thuật, chạy nhiều nền tảng |
| Lập trình trực tiếp | Khó | Công lập trình | Web tự viết |

## Chống đếm trùng: event_id là gì?

Khi Pixel và CAPI cùng gửi sự kiện Purchase cho một đơn, Meta phải biết đó là một đơn, không phải hai. Theo tài liệu Meta for Developers, Meta gộp hai sự kiện khi chúng có **cùng tên sự kiện** và **cùng event_id**.

Cách làm đơn giản nhất: dùng mã đơn hàng làm event_id cho sự kiện Purchase. Pixel trên trang cảm ơn gửi Purchase với event_id = mã đơn. Máy chủ gửi Purchase qua CAPI với cùng event_id = mã đơn. Meta nhận hai, tính một.

Với các sự kiện khác như AddToCart, website tạo một mã ngẫu nhiên khi khách bấm nút, rồi dùng cùng mã đó cho cả hai đường.

Thiếu bước này, báo cáo sẽ đếm đơn gấp đôi, ROAS trông đẹp gấp đôi thực tế, và anh chị ra quyết định tăng ngân sách dựa trên số ảo.

## Kiểm tra dữ liệu sau khi cài

Sau khi cài, đội mình kiểm tra theo thứ tự:

1. **Công cụ kiểm tra sự kiện** trong Trình quản lý sự kiện: tự đặt một đơn thử, xem sự kiện có hiện từ cả trình duyệt và máy chủ không.
2. **Trạng thái gộp sự kiện**: Trình quản lý sự kiện cho biết sự kiện đã được gộp đúng chưa.
3. **Event Match Quality**: điểm từ 0 đến 10 cho biết thông tin gửi kèm giúp Meta nhận ra người dùng tốt tới đâu. Gửi thêm email, số điện thoại đã mã hóa SHA-256, cùng các mã nhận diện trình duyệt như fbp, fbc thường giúp điểm tăng.
4. **Đối chiếu với đơn thật**: so số Purchase Meta ghi nhận trong 7 ngày với số đơn trong hệ thống. Chênh lệch nhỏ là bình thường do cách quy đơn khác nhau. Chênh lớn, hoặc Meta ghi nhiều đơn hơn thực tế, là dấu hiệu đếm trùng.

## Dữ liệu khách hàng và luật bảo vệ dữ liệu cá nhân

Gửi email, số điện thoại của khách cho Meta là xử lý dữ liệu cá nhân. Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 có hiệu lực từ 01/01/2026, cùng Nghị định 356/2025/NĐ-CP quy định chi tiết. Những việc tối thiểu nên làm:

- Có chính sách quyền riêng tư trên website, nói rõ thu thập dữ liệu gì, để làm gì, chia sẻ cho ai (trong đó có nền tảng quảng cáo).
- Có thông báo và cơ chế đồng ý phù hợp khi thu thập dữ liệu.
- Mã hóa thông tin trước khi gửi. Pixel và CAPI đều hỗ trợ mã hóa SHA-256.
- Chỉ gửi dữ liệu cần thiết.

Phần này mình chỉ nêu ở mức tổng quát. Doanh nghiệp nên hỏi luật sư hoặc bộ phận pháp chế để có chính sách phù hợp với mô hình của mình.

## Lỗi hay gặp khi cài Pixel và Conversions API

- **Cài Pixel hai lần**, một lần qua plugin, một lần dán mã tay. Mọi sự kiện bị đếm đôi.
- **Purchase bắn ở trang thanh toán** thay vì sau khi đơn tạo thành công.
- **Không có event_id** khi dùng cả Pixel và CAPI.
- **Giá trị đơn sai đơn vị tiền** hoặc gửi giá trị cố định.
- **Pixel nằm trong tài khoản cá nhân của người làm web**, khi họ nghỉ thì doanh nghiệp mất quyền. Pixel phải thuộc Business Manager của doanh nghiệp.
- **Tối ưu theo Purchase khi mỗi tuần chỉ có vài đơn.** Quá ít dữ liệu, Meta khó tối ưu. Giai đoạn đầu có thể tối ưu theo AddToCart hoặc InitiateCheckout, như mình chia sẻ trong bài [quảng cáo Facebook Meta Ads cho người mới](/kien-thuc/quang-cao-facebook-meta-ads-cho-nguoi-moi/).

## Việc nên làm ngay tuần này

- Mở Trình quản lý sự kiện, kiểm tra Pixel thuộc Business Manager của doanh nghiệp.
- Đặt một đơn thử, xem đủ 5 sự kiện chuẩn chưa, Purchase có giá trị đúng không.
- Nếu đã có CAPI, kiểm tra trạng thái gộp sự kiện và điểm Event Match Quality.
- Rà lại chính sách quyền riêng tư trên website.

Nếu anh chị muốn có đội cùng thiết lập đo lường và chạy quảng cáo cho website, có thể tham khảo [dịch vụ quảng cáo](/dich-vu/quang-cao-tiktok-shopee/) của đội QHUB. Các bài khác về bán hàng qua Facebook nằm trong chủ đề [bán hàng Facebook](/kien-thuc/chu-de/ban-hang-facebook/).
