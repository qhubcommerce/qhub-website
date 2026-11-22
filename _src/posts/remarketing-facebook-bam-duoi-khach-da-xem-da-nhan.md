---
title: "Remarketing Facebook: bám đuổi khách đã xem, đã nhắn"
slug: remarketing-facebook-bam-duoi-khach-da-xem-da-nhan
topic: ban-hang-facebook
keyword: "remarketing facebook"
keywords: ["quảng cáo bám đuổi facebook", "retargeting facebook", "đối tượng tùy chỉnh facebook", "tiếp thị lại khách đã nhắn tin"]
description: "Remarketing Facebook là chạy quảng cáo lại cho người đã xem video, vào trang, nhắn tin hoặc vào website. Cách dựng tệp, chia tầng, chọn nội dung và tần suất."
date: 2026-11-23
updated: 2026-11-23
summary:
  - "Remarketing Facebook (quảng cáo bám đuổi) là chạy quảng cáo cho người đã từng tương tác với thương hiệu: xem video, tương tác Trang, Instagram, nhắn tin, vào website, hoặc có trong danh sách khách hàng."
  - "Theo tài liệu Meta for Developers, đối tượng tùy chỉnh từ website lưu tối đa 180 ngày, đối tượng tương tác lưu tối đa 365 ngày; nên chia tầng theo mức độ nóng và thời gian."
  - "Mỗi tầng cần nội dung khác nhau: người mới xem video cần lý do tin, người đã nhắn tin cần lời giải đáp và ưu đãi, khách cũ cần sản phẩm bổ sung."
  - "Tệp bám đuổi nhỏ nên dễ bị lặp quảng cáo; theo dõi tần suất và thay nội dung đều đặn để không làm phiền khách."
faq:
  - q: "Remarketing Facebook là gì?"
    a: "Là cách chạy quảng cáo nhắm lại những người đã từng tương tác với doanh nghiệp, như xem video, nhắn tin cho Trang, tương tác với Instagram, vào website hoặc có trong danh sách khách hàng. Những người này đã biết thương hiệu nên thường có chi phí mỗi đơn thấp hơn khách lạ."
  - q: "Tệp remarketing cần tối thiểu bao nhiêu người?"
    a: "Meta có thể yêu cầu đối tượng đủ lớn để phân phối và để bảo vệ quyền riêng tư; tệp quá nhỏ sẽ khó chạy hoặc chi phí cao. Theo kinh nghiệm vận hành, tệp từ vài nghìn người trở lên chạy ổn hơn. Nếu tệp nhỏ, nới khoảng thời gian hoặc gộp nhiều nguồn tương tác lại."
  - q: "Có bám đuổi được người đã nhắn tin cho Trang không?"
    a: "Được. Trong mục Đối tượng của Ads Manager, chọn tạo đối tượng tùy chỉnh từ nguồn Trang Facebook, rồi chọn điều kiện người đã gửi tin nhắn cho Trang trong một khoảng thời gian. Ngoài quảng cáo, Meta còn có tin nhắn tiếp thị trên Messenger cho người đã đồng ý nhận."
  - q: "Không có website có làm remarketing được không?"
    a: "Được. Anh chị dùng đối tượng tương tác từ video, Trang Facebook, tài khoản Instagram, biểu mẫu khách hàng tiềm năng và danh sách khách hàng tải lên. Website và Pixel chỉ thêm được tầng người đã xem sản phẩm, thêm giỏ hàng."
  - q: "Nên chạy remarketing với tần suất bao nhiêu?"
    a: "Không có con số chuẩn. Đội QHUB theo dõi tần suất 7 ngày; khi tần suất tăng cao mà CTR giảm và bình luận tiêu cực xuất hiện, đó là dấu hiệu khách đã thấy quá nhiều, cần thay nội dung hoặc giảm ngân sách tầng đó."
sources:
  - title: "Website Custom Audiences – Meta for Developers"
    url: "https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences"
  - title: "Engagement Custom Audiences – Meta for Developers"
    url: "https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/engagement-custom-audiences"
  - title: "Audiences Overview – Meta for Developers"
    url: "https://developers.facebook.com/docs/marketing-api/audiences/overview"
  - title: "Re-engage customers with marketing messages on Messenger – Meta for Developers (07/2025)"
    url: "https://developers.facebook.com/blog/post/2025/07/02/re-engage-customers-with-marketing-messages-on-messenger/"
  - title: "Meta Extends Purchase Audience Retention to 730 Days – Common Thread Collective"
    url: "https://commonthreadco.com/blogs/coachs-corner/meta-purchase-audience-730-days-ecommerce"
  - title: "Meta ra mắt Facebook Marketing Messages – Brands Vietnam"
    url: "https://www.brandsvietnam.com/congdong/topic/hot-meta-chinh-thuc-ra-mat-facebook-marketing-messages-hinh-thuc-remaketing-moi-tuong-tu-zns-sms-email-mkt"
---

**Remarketing Facebook (còn gọi là quảng cáo bám đuổi, retargeting) là chạy quảng cáo nhắm lại những người đã từng tương tác với doanh nghiệp: đã xem video, đã tương tác Trang hoặc Instagram, đã nhắn tin, đã vào website hoặc đã từng mua.** Những người này biết anh chị là ai, nên thường dễ chốt đơn hơn khách lạ. Làm đúng, remarketing là phần ngân sách có chi phí mỗi đơn thấp nhất trong tài khoản. Làm sai, nó biến thành thứ quảng cáo "đi theo" khách khắp nơi đến mức họ khó chịu.

Bài này đội QHUB chia sẻ cách dựng tệp bám đuổi, chia tầng theo độ nóng, chọn nội dung cho từng tầng, đặt ngân sách và tần suất, cùng những lỗi hay gặp khi nhận lại tài khoản quảng cáo từ khách.

## Vì sao cần remarketing trên Facebook?

Rất ít người mua ngay lần đầu thấy sản phẩm. Họ xem một video, lướt qua, vài hôm sau thấy lại, vào Trang đọc bình luận, nhắn tin hỏi giá, rồi im lặng. Nếu anh chị chỉ chạy quảng cáo cho người lạ, toàn bộ công sức kéo những người "đã gần mua" này sẽ trôi mất.

Remarketing giúp:

- **Nhắc người đã quan tâm quay lại** đúng lúc họ sẵn sàng.
- **Trả lời băn khoăn còn sót lại:** giá, vận chuyển, đổi trả, đánh giá của người dùng thật.
- **Bán thêm cho khách cũ:** sản phẩm bổ sung, mua lại khi dùng hết.
- **Làm cho ngân sách tìm khách mới hiệu quả hơn:** người lạ xem video hôm nay có thể thành đơn tuần sau qua tầng bám đuổi.

## Các nguồn dựng tệp remarketing trên Facebook

Trong Ads Manager, vào mục **Đối tượng → Tạo đối tượng → Đối tượng tùy chỉnh**. **Đối tượng tùy chỉnh (Custom Audience)** là tệp người do anh chị định nghĩa từ dữ liệu của chính mình. Các nguồn chính:

| Nguồn | Ví dụ điều kiện | Thời gian lưu tối đa | Cần chuẩn bị |
| --- | --- | --- | --- |
| Website | Đã xem trang sản phẩm, đã thêm giỏ, đã mua | 180 ngày | Pixel Meta, nên có thêm Conversions API |
| Video | Đã xem 50%, 75%, 95% video | 365 ngày | Video đăng trên Trang hoặc Instagram |
| Trang Facebook | Đã tương tác, đã gửi tin nhắn, đã lưu bài | 365 ngày | Trang đã liên kết tài khoản quảng cáo |
| Tài khoản Instagram | Đã tương tác, đã nhắn tin, đã truy cập hồ sơ | 365 ngày | Tài khoản Instagram chuyên nghiệp đã liên kết |
| Biểu mẫu khách hàng tiềm năng | Đã mở, đã gửi biểu mẫu | 90 ngày | Đã chạy quảng cáo biểu mẫu |
| Danh sách khách hàng | Số điện thoại, email của khách đã mua | Không giới hạn theo ngày, cập nhật thủ công | File danh sách, có sự đồng ý theo quy định dữ liệu cá nhân |

Mốc 180 ngày cho website và 365 ngày cho đối tượng tương tác lấy theo tài liệu Meta for Developers tại thời điểm tháng 11/2026; riêng mốc 90 ngày cho biểu mẫu là theo giao diện đội mình thường gặp, có thể khác theo tài khoản. Common Thread Collective có đưa tin Meta mở rộng thời gian lưu với đối tượng người đã mua lên 730 ngày ở một số trường hợp. Các mốc này có thể thay đổi, anh chị xem lại ngay trên màn hình tạo đối tượng.

Với danh sách khách hàng, lưu ý Luật Bảo vệ dữ liệu cá nhân năm 2025 và các văn bản hướng dẫn: chỉ dùng dữ liệu khách đã đồng ý cho mục đích tiếp thị. Cách cài Pixel và Conversions API cho tầng website, xem bài [Pixel Meta và Conversions API cho website bán hàng](/kien-thuc/pixel-meta-va-conversions-api-cho-website-ban-hang/).

## Chia tầng remarketing theo độ nóng

Gộp tất cả người đã tương tác vào một tệp rồi chạy một quảng cáo chung là cách làm phí tiền nhất. Người vừa xem 3 giây video và người đã thêm giỏ hàng hôm qua cần những thông điệp rất khác. Đội QHUB chia ba tầng:

| Tầng | Ai ở trong | Họ đang nghĩ gì | Nội dung nên chạy | Khoảng thời gian gợi ý |
| --- | --- | --- | --- | --- |
| Ấm | Xem 50% video trở lên, tương tác Trang, Instagram | "Hay đấy, nhưng có đáng tin không?" | Đánh giá thật, video dùng sản phẩm, câu chuyện thương hiệu | 30–90 ngày |
| Nóng | Đã nhắn tin, đã xem trang sản phẩm, đã thêm giỏ | "Giá này có hời không, giao có nhanh không?" | Giải đáp thắc mắc, chính sách đổi trả, ưu đãi có hạn | 3–14 ngày |
| Khách cũ | Đã mua | "Dùng hết rồi mua lại ở đâu, có gì mới?" | Sản phẩm bổ sung, mua lại, quà tri ân | 30–180 ngày tùy chu kỳ dùng |

Hai nguyên tắc khi dựng:

1. **Loại trừ tầng nóng hơn khỏi tầng lạnh hơn.** Người đã thêm giỏ không cần thấy video giới thiệu nữa. Người đã mua loại khỏi tầng nóng để không bị mời mua lại sản phẩm vừa mua.
2. **Chọn khoảng thời gian theo chu kỳ mua.** Sản phẩm dùng hết trong 30 ngày (thực phẩm, trà, mỹ phẩm) thì tầng khách cũ nên bám từ ngày 20–40 sau khi mua.

## Bám đuổi người đã nhắn tin: tầng bị bỏ quên nhiều nhất

Với shop bán qua Facebook, người đã nhắn tin cho Trang là tài sản quý nhất. Họ đã chủ động hỏi. Vậy mà rất nhiều shop chỉ trả lời một lần rồi để đó.

Có hai cách chăm lại nhóm này:

**Quảng cáo bám đuổi.** Tạo đối tượng tùy chỉnh từ Trang, điều kiện "người đã gửi tin nhắn cho Trang" trong 7–30 ngày. Chạy quảng cáo với điểm đến là tin nhắn, nội dung trả lời đúng những câu hỏi khách hay hỏi mà chưa chốt: phí ship, thời gian giao, cách đổi trả, ưu đãi tuần này. Loại trừ người đã mua (từ danh sách khách hàng hoặc sự kiện mua trên website).

**Nhắn tin trực tiếp.** Trong cửa sổ 24 giờ kể từ tin nhắn cuối của khách, Trang được nhắn lại bình thường. Ngoài cửa sổ này, việc gửi tin nhắn mang tính quảng cáo bị giới hạn. Theo bài đăng trên blog Meta for Developers (07/2025) và Brands Vietnam, Meta đã ra mắt tin nhắn tiếp thị (marketing messages) trên Messenger cho phép doanh nghiệp gửi tin quảng bá tới người đã đồng ý nhận. Điều kiện, chi phí và việc áp dụng ở Việt Nam anh chị kiểm tra trong Meta Business Suite.

Kịch bản trả lời và chốt đơn qua inbox có trong bài [quảng cáo tin nhắn Facebook: chạy và chốt đơn qua inbox](/kien-thuc/quang-cao-tin-nhan-facebook-chay-va-chot-don-qua-inbox/), còn cách chăm khách sau khi mua có trong bài [chăm sóc khách cũ trên Facebook và Messenger](/kien-thuc/cham-soc-khach-cu-tren-facebook-va-messenger/).

## Ngân sách và tần suất cho remarketing

Tệp bám đuổi nhỏ hơn rất nhiều so với tệp khách mới. Đổ quá nhiều tiền vào tệp nhỏ thì mỗi người thấy quảng cáo hàng chục lần.

Cách phân bổ đội QHUB hay dùng với shop mới bắt đầu:

| Phần ngân sách | Tỷ lệ gợi ý | Ghi chú |
| --- | --- | --- |
| Tìm khách mới | 70–80% | Nuôi tệp cho các tầng sau |
| Remarketing tầng ấm và nóng | 15–25% | Tăng dần khi tệp lớn lên |
| Khách cũ | 5–10% | Tùy chu kỳ mua lại của sản phẩm |

Đây là khung khởi đầu, không phải công thức. Với shop đã có nhiều khách cũ và sản phẩm mua lại thường xuyên, phần khách cũ có thể lớn hơn.

**Theo dõi tần suất.** Tần suất là số lần trung bình một người thấy quảng cáo. Trong báo cáo, xem tần suất 7 ngày của từng tầng. Khi tần suất tăng mà CTR giảm, chi phí mỗi kết quả tăng, và bắt đầu có bình luận kiểu "thấy quảng cáo này hoài", đó là lúc thay nội dung hoặc giảm ngân sách tầng đó.

**Có nên dùng chiến dịch tự động?** Chiến dịch Advantage+ của Meta tự tìm cả khách mới lẫn khách cũ, và cho đặt giới hạn phần ngân sách dành cho khách hiện tại. Cách dùng có trong bài [Advantage+ Shopping: quảng cáo tự động của Meta](/kien-thuc/advantage-shopping-quang-cao-tu-dong-cua-meta/). Với shop nhỏ, đội mình vẫn giữ một chiến dịch bám đuổi thủ công cho tầng nóng, vì muốn kiểm soát nội dung trả lời đúng băn khoăn của khách.

## Ví dụ: remarketing cho một sản phẩm thực phẩm dùng hằng ngày

Giả sử anh chị bán trà túi lọc, mỗi hộp dùng khoảng một tháng. Một kịch bản bám đuổi hợp lý:

- **Tầng ấm (xem 50% video trong 30 ngày):** video cận cảnh pha trà, video mở hộp cho thấy thành phần, ảnh chụp màn hình đánh giá thật của khách (có sự đồng ý). Không nói công dụng sức khỏe, vì trà là thực phẩm thông thường.
- **Tầng nóng (nhắn tin hoặc xem trang sản phẩm trong 7 ngày):** một quảng cáo trả lời ba câu khách hay hỏi: vị thế nào, pha ra sao, giao mất mấy ngày; kèm ưu đãi đang chạy của kênh đó.
- **Khách cũ (mua 20–40 ngày trước):** giới thiệu vị khác để đổi, combo quà cho dịp lễ sắp tới.

## Lỗi hay gặp khi chạy remarketing Facebook

- **Một tệp chung cho mọi người đã tương tác.** Người vừa lướt qua và người sắp mua nhận cùng một quảng cáo.
- **Không loại trừ người đã mua.** Khách vừa mua xong lại thấy quảng cáo giảm giá sâu hơn, cảm thấy bị thiệt.
- **Dùng nguyên video giới thiệu cho tầng nóng.** Người đã hỏi giá không cần xem lại giới thiệu, họ cần câu trả lời.
- **Để một quảng cáo chạy hàng tháng.** Tệp nhỏ nên quảng cáo nhanh "mòn".
- **Khoảng thời gian quá dài cho tầng nóng.** Người thêm giỏ 150 ngày trước không còn "nóng".
- **Pixel lỗi mà không biết.** Tệp website rỗng hoặc sai. Kiểm tra trình quản lý sự kiện mỗi tháng.

Nếu anh chị chạy đồng thời Facebook, Instagram, TikTok và sàn, việc dựng tầng, làm nội dung riêng cho từng tầng và đọc tần suất mỗi tuần khá tốn người. Thông tin về cách đội QHUB vận hành quảng cáo đa kênh có ở trang [dịch vụ quảng cáo](/dich-vu/quang-cao-tiktok-shopee/).

## Việc cần làm ngay tuần này

1. Kiểm tra Pixel, Conversions API và liên kết Trang, Instagram với tài khoản quảng cáo.
2. Tạo các đối tượng tùy chỉnh: xem 50% video 30 ngày, nhắn tin Trang 14 ngày, xem sản phẩm 7 ngày, đã mua 180 ngày.
3. Dựng ba tầng ấm, nóng, khách cũ, có loại trừ giữa các tầng.
4. Làm 2–3 nội dung riêng cho từng tầng.
5. Đặt lịch xem tần suất và CTR mỗi tuần, thay nội dung khi có dấu hiệu mòn.

Các bài khác về bán hàng trên Facebook có trong chủ đề [Bán hàng Facebook](/kien-thuc/chu-de/ban-hang-facebook/).
