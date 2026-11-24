---
title: "Kéo khách từ Facebook về website và sàn"
slug: keo-khach-tu-facebook-ve-website-va-san
topic: ban-hang-facebook
keyword: "kéo khách facebook về shop"
keywords: ["chạy quảng cáo facebook về shopee", "gắn utm cho link facebook", "facebook về website hay về sàn", "cpas shopee", "link theo dõi shopee"]
description: "Kéo khách Facebook về shop: khi nào về website, khi nào về Shopee hay TikTok Shop, gắn UTM, đo bằng GA4, Pixel, Conversions API, CPAS và lỗi hay gặp."
date: 2026-11-25
updated: 2026-11-25
summary:
  - "Kéo khách từ Facebook về shop nghĩa là chọn một điểm đến cho từng nhóm khách: website riêng khi cần đo kỹ và giữ dữ liệu khách, sàn khi khách cần sự yên tâm của sàn và ưu đãi sàn."
  - "Link về website gắn UTM để GA4 đọc nguồn, kèm Meta Pixel và Conversions API có chung event_id để Meta không đếm trùng đơn; link về Shopee dùng link theo dõi của công cụ Traffic Ngoại sàn hoặc chạy Quảng cáo Cộng tác (CPAS)."
  - "Mỗi kênh có thể có ưu đãi riêng, như QHUB HERBAL: website qhubherbal.com mua 2 tặng 1, TikTok Shop và Shopee mua 3 tặng 1; bài đăng và tin nhắn phải nói rõ ưu đãi nào ở kênh nào."
  - "Chiều ngược lại, kéo khách đang mua trên sàn ra ngoài qua chat hay phiếu trong hộp hàng, là việc các sàn hạn chế và có thể bị phạt."
faq:
  - q: "Nên kéo khách Facebook về website hay về Shopee?"
    a: "Tùy mục tiêu. Về website khi anh chị cần đo từng bước, giữ số điện thoại khách và không mất phí sàn trên đơn. Về Shopee hay TikTok Shop khi khách mới còn ngại mua ở web lạ, cần đánh giá, voucher và chính sách trả hàng của sàn. Nhiều thương hiệu chạy cả hai, mỗi nhóm khách một điểm đến."
  - q: "Gắn UTM cho link Facebook thế nào để GA4 nhận đúng?"
    a: "Tối thiểu có utm_source, utm_medium và utm_campaign. Với quảng cáo, đội QHUB dùng utm_source=facebook và utm_medium=paid_social để GA4 xếp vào nhóm Paid Social; với bài đăng thường dùng utm_medium=social. Viết thường toàn bộ và giữ một quy ước cho cả đội."
  - q: "Gắn UTM vào link Shopee có đo được không?"
    a: "GA4 không đọc được vì anh chị không gắn được mã GA4 lên Shopee. Muốn đo đơn từ Facebook về Shopee, dùng link chứa mã theo dõi của công cụ Traffic Ngoại sàn trong Kênh Người Bán, hoặc chạy Quảng cáo Cộng tác Facebook (CPAS) để Shopee trả dữ liệu đơn về trình quản lý quảng cáo."
  - q: "Có cần cả Meta Pixel và Conversions API không?"
    a: "Nên có cả hai cho website bán hàng. Pixel đo trên trình duyệt, dễ bị chặn; Conversions API gửi sự kiện từ máy chủ nên bù được phần thiếu. Hai nguồn phải gửi cùng event_id và tên sự kiện để Meta loại bản trùng, theo tài liệu dành cho nhà phát triển của Meta."
  - q: "Có được gửi link website cho khách đang chat trên Shopee không?"
    a: "Không nên. Các sàn đều hạn chế việc điều hướng khách ra ngoài sàn qua tin nhắn, mô tả sản phẩm hay phiếu gửi kèm hàng, và có thể phạt điểm hoặc khóa gian hàng. Kéo khách về website nên làm từ kênh của chính anh chị như fanpage, nhóm, Messenger."
sources:
  - title: "Công cụ Traffic Ngoại sàn là gì? – Shopee Uni"
    url: "https://banhang.shopee.vn/edu/article/14809"
  - title: "Link chứa mã theo dõi là gì? – Shopee Uni"
    url: "https://banhang.shopee.vn/edu/article/14811"
  - title: "2 hình thức đăng ký Quảng Cáo Cộng Tác Facebook (CPAS) với Shopee – Shopee Uni"
    url: "https://banhang.shopee.vn/edu/article/16464"
  - title: "Handling Duplicate Pixel and Conversions API Events – Meta for Developers"
    url: "https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events"
  - title: "Best Practices – Conversions API – Meta for Developers"
    url: "https://developers.facebook.com/docs/marketing-api/conversions-api/best-practices"
  - title: "[GA4] Traffic-source dimensions và nhóm kênh mặc định – Trợ giúp Google Analytics"
    url: "https://support.google.com/analytics/answer/9756891"
  - title: "[GA4] How traffic source dimensions are updated – Trợ giúp Google Analytics"
    url: "https://support.google.com/analytics/answer/15593651"
  - title: "Điều khoản và điều kiện Chương trình Tiếp thị liên kết (cập nhật 01/12/2025) – Shopee"
    url: "https://shopee.vn/affiliate/kol-dieu-khoan-tham-gia-update-01-12-2025/"
  - title: "Shopee hợp tác với Meta ra mắt trải nghiệm mua sắm mới – Tuổi Trẻ (10/2025)"
    url: "https://tuoitre.vn/shopee-hop-tac-voi-meta-ra-mat-trai-nghiem-mua-sam-moi-20251023145841982.htm"
  - title: "Chính sách TikTok Shop cho người bán – GHN"
    url: "https://ghn.vn/blogs/tip-ban-hang/chinh-sach-tiktok-shop"
  - title: "Nhà bán hàng tìm cách kéo khách khỏi Shopee, TikTok Shop – 24hMoney"
    url: "https://24hmoney.vn/news/nha-ban-hang-tim-cach-keo-khach-khoi-shopee-tiktok-shop-c2a2840719.html"
---

**Kéo khách Facebook về shop hiệu quả là chọn đúng điểm đến cho từng nhóm khách: khách đã quen thương hiệu, cần tư vấn kỹ hoặc mua lặp lại thì đưa về website riêng; khách mới còn ngại, quen săn voucher thì đưa về Shopee hay TikTok Shop.** Điểm đến nào cũng phải đo được. Link về website gắn UTM, có Meta Pixel và Conversions API. Link về Shopee dùng link theo dõi của sàn hoặc Quảng cáo Cộng tác. Không đo được thì anh chị không biết tiền quảng cáo và công làm nội dung đang ra đơn ở đâu.

Bài này đội QHUB viết cho chủ shop đã có fanpage, có thể đang chạy quảng cáo Meta, và đang bán cùng lúc trên website lẫn sàn. Thông tin công cụ tổng hợp từ Shopee Uni, tài liệu của Meta và Google đến ngày 25/11/2026. Giao diện, điều kiện chương trình có thể đã đổi, anh chị kiểm tra lại trong Kênh Người Bán và Seller Center.

## Kéo khách Facebook về shop: về website hay về sàn?

Đây là câu hỏi đầu tiên, và không có đáp án chung. Mình tách theo việc anh chị cần gì nhất từ đơn hàng.

| Tiêu chí | Website riêng | Shopee | TikTok Shop |
| --- | --- | --- | --- |
| Phí trên mỗi đơn | Không có phí sàn, chỉ phí cổng thanh toán, vận chuyển | Phí cố định theo ngành, phí xử lý giao dịch, phí dịch vụ nếu tham gia | Hoa hồng nền tảng theo ngành, phí giao dịch, phí xử lý đơn |
| Dữ liệu khách | Có số điện thoại, địa chỉ, lịch sử mua | Sàn giữ, người bán thấy hạn chế | Sàn giữ, người bán thấy hạn chế |
| Đo từ Facebook | Đầy đủ: UTM, GA4, Pixel, Conversions API | Link theo dõi Traffic Ngoại sàn, CPAS | Đội QHUB chưa thấy chương trình đo chính thức với Meta |
| Niềm tin của khách mới | Thấp hơn nếu thương hiệu còn lạ | Cao: đánh giá, chính sách trả hàng, ví, voucher sàn | Cao với người quen mua trên TikTok |
| Tỷ lệ chuyển đổi | Phụ thuộc trang đích, tốc độ, cách thanh toán | Thường tốt nếu trang sản phẩm có đánh giá thật | Mở link ngoài TikTok có thể phải qua ứng dụng, rơi rụng |
| Hợp nhất với | Khách cũ, khách cần tư vấn, đơn sỉ, combo riêng | Khách mới, ngày sale đôi, sản phẩm người ta so giá | Shop đã mạnh trên TikTok, khách trẻ quen mua trong app |

Cách đội mình hay dùng là chia theo vòng đời khách:

- **Khách lạ lần đầu thấy quảng cáo:** về sàn, vì họ tin đánh giá và chính sách trả hàng của sàn hơn một website mới.
- **Người đã tương tác, đã nhắn tin, đã mua một lần:** về website, vì đó là nơi anh chị giữ được thông tin để chăm sóc lâu dài và không mất phí sàn ở đơn sau.
- **Ngày sale đôi:** về sàn, vì voucher sàn và lượng người săn sale tập trung ở đó.

Nếu anh chị còn phân vân có nên làm website hay không, bài [doanh nghiệp bán trên sàn có cần website riêng không](/kien-thuc/doanh-nghiep-ban-tren-san-co-can-website-rieng-khong/) đi kỹ phần chi phí và lợi ích.

### Một lưu ý về chiều ngược lại

Kéo khách từ Facebook sang sàn hay sang website là việc bình thường. Chiều ngược lại thì khác. Gửi link website hay số Zalo cho khách đang chat trên Shopee, ghi trong mô tả sản phẩm, hay bỏ phiếu "mua lần sau trên web giảm thêm" vào hộp hàng giao từ sàn là những việc các sàn đều hạn chế. Báo 24hMoney từng viết về chuyện nhà bán tìm cách kéo khách khỏi sàn, còn các bài tổng hợp chính sách của GHN nhắc đây là nhóm lỗi có thể bị phạt điểm hoặc khóa. Đội QHUB không làm và khuyên anh chị tránh hẳn. Muốn khách biết website, hãy để họ gặp website từ kênh của chính anh chị: fanpage, nhóm, Messenger.

## Đưa khách về Shopee và TikTok Shop: dùng công cụ nào?

### Về Shopee: link theo dõi và Quảng cáo Cộng tác

Shopee không cho gắn mã đo của anh chị lên gian hàng, nên không gắn được Pixel hay GA4. Thay vào đó, theo Shopee Uni, sàn có sẵn:

- **Công cụ Traffic Ngoại sàn:** tạo link dẫn vào shop hoặc từng sản phẩm, rồi xem lượt truy cập và đơn đến từ link đó.
- **Link chứa mã theo dõi:** mỗi link mang một mã riêng để biết khách đến từ chiến dịch nào. Mỗi bài đăng, mỗi nhóm quảng cáo nên một link.
- **Quảng cáo Cộng tác Facebook (CPAS):** CPAS (Collaborative Performance Advertising Solution) là giải pháp của Meta cho phép nhà bán lẻ như Shopee chia sẻ danh mục sản phẩm, để thương hiệu chạy quảng cáo trên Facebook, Instagram dẫn thẳng vào trang sản phẩm trên Shopee và nhận lại dữ liệu đơn hàng. Shopee Uni có bài hướng dẫn hai hình thức đăng ký.

Đến 25/11/2026 bài CPAS vẫn còn trên Shopee Uni, nhưng đội QHUB chưa xác nhận được điều kiện tham gia hiện tại như ngân sách tối thiểu hay loại shop được mời. Anh chị xem mục Kênh Marketing trong Kênh Người Bán của shop mình. Phần chi tiết hơn về cách tính hòa vốn khi chạy quảng cáo về Shopee, đội mình đã viết ở bài [quảng cáo ngoài sàn kéo về Shopee](/kien-thuc/quang-cao-ngoai-san-keo-ve-shopee-facebook-tiktok-google/).

Ngoài ra, Tuổi Trẻ đưa tin tháng 10/2025 Shopee hợp tác với Meta để người dùng Việt Nam liên kết tài khoản Facebook với Shopee Affiliate và gắn sản phẩm Shopee vào nội dung. Với shop, đây là cách để người khác kéo khách Facebook về gian hàng của mình, trả tiền theo đơn. Điều khoản chương trình tiếp thị liên kết, bản cập nhật ngày 01/12/2025 trên trang Shopee, quy định cách ghi nhận đơn và hoa hồng; anh chị đọc trước khi đặt mức hoa hồng.

### Về TikTok Shop: cẩn thận hơn

Từ Facebook, anh chị vẫn có thể chia sẻ link sản phẩm TikTok Shop. Có ba điểm cần biết:

1. Link thường mở ứng dụng TikTok. Người không cài ứng dụng hoặc chưa đăng nhập dễ bỏ giữa chừng.
2. Đội QHUB chưa tìm thấy chương trình đo lường chính thức kiểu CPAS giữa Meta và TikTok Shop ở Việt Nam. Anh chị chỉ đối chiếu được bằng mã giảm giá riêng hoặc so doanh thu theo ngày.
3. Trong chính TikTok, video và phiên live gắn giỏ hàng chỉ dẫn tới sản phẩm trong TikTok Shop. Kêu gọi người xem mua ngoài nền tảng trong nội dung có giỏ hàng là điều nên tránh; anh chị kiểm tra quy định nội dung trong Học viện người bán TikTok Shop trước khi làm.

Vì vậy, đội mình chỉ đưa khách Facebook về TikTok Shop khi gian hàng TikTok đã có nhiều đánh giá thật và tệp khách trẻ quen mua trong ứng dụng. Còn lại, về Shopee hoặc website thường gọn hơn.

## Gắn UTM và theo dõi bằng GA4, Meta Pixel, Conversions API thế nào?

Phần này chỉ áp dụng cho link về website, vì đó là nơi anh chị gắn được mã đo.

**UTM** là các tham số gắn thêm vào cuối đường link để GA4 biết khách đến từ đâu. Theo trang trợ giúp Google Analytics về nhóm kênh mặc định, GA4 dựa vào nguồn và phương tiện để xếp lượt truy cập vào nhóm như Paid Social (mạng xã hội trả tiền) hay Organic Social (mạng xã hội tự nhiên). Phương tiện có chữ như "paid" hay "cpc" đi cùng nguồn là mạng xã hội thì được xếp vào Paid Social. Ghi sai quy ước, lượt truy cập rơi vào nhóm "Unassigned" (chưa xếp nhóm).

Bảng quy ước đội QHUB dùng:

| Vị trí link | utm_source | utm_medium | utm_campaign | utm_content |
| --- | --- | --- | --- | --- |
| Quảng cáo Meta | facebook | paid_social | tet2027-combo | video01 |
| Bài đăng fanpage | facebook | social | bai-huong-dan-pha | 2611 |
| Nhóm Facebook | facebook | social | nhom-khach-quen | bai-ghim |
| Tin nhắn Messenger | facebook | messenger | cham-soc-khach-cu | mau-tin-03 |
| Quảng cáo Instagram | instagram | paid_social | tet2027-combo | reels02 |

Ba nguyên tắc: viết thường hết, không dấu, không khoảng trắng; một người giữ file quy ước; không gắn UTM cho link nội bộ giữa các trang trên website vì GA4 sẽ ghi đè nguồn thật. Cài đặt GA4 và sự kiện mua hàng, đội mình đã viết trong bài [Google Analytics 4 cho website bán hàng](/kien-thuc/google-analytics-4-cho-website-ban-hang/).

**Meta Pixel** là đoạn mã đặt trên website để gửi về Meta các sự kiện như xem sản phẩm, thêm vào giỏ, mua hàng. **Conversions API** là cách gửi các sự kiện đó từ máy chủ của website, không phụ thuộc trình duyệt. Pixel dễ bị chặn bởi trình chặn quảng cáo hay cài đặt riêng tư, nên Meta khuyên chạy cả hai. Điều kiện bắt buộc: hai nguồn gửi cùng một sự kiện phải có chung `event_id` và tên sự kiện, để Meta nhận ra đó là một đơn và loại bản trùng. Thiếu bước này, báo cáo Meta có thể đếm đơn gấp đôi, nhìn quảng cáo rất lãi trong khi thực tế không phải. Cách cài từng bước có ở bài [Pixel Meta và Conversions API](/kien-thuc/pixel-meta-va-conversions-api-cho-website-ban-hang/).

Một điều cần chấp nhận: số đơn trong Meta, trong GA4 và trong hệ thống đơn hàng của website sẽ không bằng nhau. Mỗi bên ghi nhận theo cách riêng. Đội mình lấy đơn thật trong hệ thống website làm gốc, dùng Meta và GA4 để so xu hướng giữa các chiến dịch.

## Bài đăng, nhóm, Messenger, quảng cáo: mỗi điểm chạm dẫn về đâu?

Không phải nội dung nào cũng nên có link. Đội QHUB chia như sau:

- **Bài đăng fanpage:** bài hướng dẫn, câu chuyện sản phẩm, ảnh đóng gói. Link đặt cuối bài hoặc ở bình luận ghim, về trang sản phẩm cụ thể chứ không về trang chủ. Bài nói về ngày sale thì link về sàn, bài nói về combo riêng của website thì link về website.
- **Nhóm Facebook:** nơi giữ khách quen. Khách trong nhóm đã tin thương hiệu, nên đây là chỗ hợp để giới thiệu website và ưu đãi riêng của website. Link trong nhóm nên đặt ở bài ghim và bài tổng hợp hằng tuần, không rải vào mọi bài.
- **Messenger:** khách hỏi xong muốn mua thì hỏi lại họ thích mua ở đâu. Người quen mua trên Shopee thì gửi link theo dõi Shopee. Người muốn đặt nhanh, cần xuất hóa đơn hay mua số lượng lớn thì gửi link website có UTM, hoặc chốt đơn ngay trong tin nhắn.
- **Quảng cáo Meta:** tách chiến dịch theo điểm đến. Một chiến dịch về website tối ưu theo sự kiện mua hàng của Pixel. Một chiến dịch về Shopee qua CPAS nếu shop dùng được. Không trộn hai điểm đến trong một nhóm quảng cáo vì không tối ưu được.

Mẫu câu Messenger đội mình hay dùng: "Dạ anh chị quen mua trên Shopee thì em gửi link gian hàng ạ, còn nếu đặt trên website thì ưu đãi khác một chút, em gửi cả hai để anh chị chọn nhé."

## Ví dụ QHUB HERBAL: hai ưu đãi cho hai kênh, nói sao cho rõ?

[QHUB HERBAL](/qhub-herbal.html) là thương hiệu trà túi lọc do chính đội QHUB xây, bán trên website qhubherbal.com, TikTok Shop và Shopee. Mỗi hộp giá niêm yết 140.000 đồng, giá bán 105.000 đồng ở mọi kênh. Ưu đãi combo thì khác theo kênh:

| Kênh | Ưu đãi | Khách trả | Khách nhận | Giá mỗi hộp sau ưu đãi |
| --- | --- | --- | --- | --- |
| Website qhubherbal.com | Mua 2 tặng 1 | 210.000 đồng | 3 hộp | 70.000 đồng |
| TikTok Shop | Mua 3 tặng 1 | 315.000 đồng | 4 hộp | 78.750 đồng |
| Shopee | Mua 3 tặng 1 | 315.000 đồng | 4 hộp | 78.750 đồng |

Ở mọi kênh, khách được chọn hộp tặng khác vị. Trên website, mua 2 tặng 1 đã là mức ưu đãi 50% so với giá niêm yết, nên website không chồng thêm mã giảm giá. Trên sàn, khách còn có thể có voucher của sàn tùy chương trình.

Khi kéo khách từ Facebook, đội mình giữ ba nguyên tắc:

1. **Bài đăng nào nói ưu đãi thì ghi rõ kênh.** "Mua 2 tặng 1 trên website qhubherbal.com" hoặc "Mua 3 tặng 1 trên Shopee, TikTok Shop", không bao giờ ghi chung chung "đang mua 2 tặng 1" rồi gắn link sàn.
2. **Link đi đúng với ưu đãi.** Bài nói ưu đãi website thì link website có UTM. Bài ngày sale thì link theo dõi Shopee.
3. **Admin nhóm và người trực Messenger có chung một bảng ưu đãi theo kênh**, cập nhật mỗi khi đổi chương trình.

Nội dung quảng cáo cho trà chỉ nói hương vị, cách pha, dịp dùng, món quà. Không gán công dụng sức khỏe, vì trà là thực phẩm thông thường và chính sách quảng cáo của Meta với ngành thực phẩm khá chặt.

## Lỗi hay gặp khi kéo khách Facebook về shop

- **Một link cho mọi nơi.** Cuối tháng không biết bài nào, quảng cáo nào ra đơn.
- **Dẫn về trang chủ.** Khách phải tự tìm sản phẩm, rơi rụng nhiều. Hãy dẫn về đúng trang sản phẩm đang nói tới.
- **Ghi ưu đãi của kênh này, gắn link kênh kia.** Khách vào thấy giá khác, nhắn hỏi hoặc bỏ đi, có khi còn khiếu nại về thông tin khuyến mại.
- **UTM viết lung tung**: lúc "Facebook", lúc "fb", lúc "facebook.com". GA4 tách thành ba nguồn khác nhau.
- **Gắn UTM vào link Shopee rồi chờ GA4 báo.** GA4 không đo được trên Shopee. Phải dùng link theo dõi của sàn.
- **Có Pixel và Conversions API nhưng không chống trùng.** Đơn bị đếm hai lần, quảng cáo trông lãi giả.
- **Kéo khách đang mua trên sàn ra website** qua chat hay phiếu trong hộp hàng. Dễ bị sàn phạt.
- **Tin tuyệt đối số đơn trong trình quản lý quảng cáo.** Luôn đối chiếu với đơn thật trong hệ thống website và báo cáo của sàn.

Kinh nghiệm thực tế từ đội vận hành: đội QHUB giữ một bảng theo tuần với các cột ngày, điểm chạm, điểm đến, chi phí, lượt nhấp, đơn ghi nhận theo link và doanh thu thật của từng kênh. Chỉ cần nhìn bảng này mỗi sáng thứ Hai là biết nên dồn tiền về website hay về sàn tuần tới.

## Việc cần làm ngay tuần này

1. Chốt bảng ưu đãi theo kênh (website, Shopee, TikTok Shop) và gửi cho người đăng bài, người trực Messenger, admin nhóm.
2. Lập file quy ước UTM, gắn lại toàn bộ link website trên fanpage, nhóm, mẫu tin nhắn.
3. Tạo link theo dõi Shopee riêng cho từng bài đăng và chiến dịch; kiểm tra shop đã dùng được Quảng cáo Cộng tác chưa.
4. Kiểm tra Pixel và Conversions API trên website đã gửi chung `event_id` cho sự kiện mua hàng.
5. Tách chiến dịch quảng cáo Meta theo điểm đến trước mùa sale 12.12 và Tết.

QHUB Commerce có đội vận hành sàn, đội media và đội quảng cáo cùng làm một bảng đo cho cả website lẫn sàn. Nếu anh chị cần người dựng hệ đo và chạy quảng cáo, có thể xem [dịch vụ quảng cáo TikTok và Shopee](/dich-vu/quang-cao-tiktok-shopee/).
