---
title: "Website trên điện thoại: chuẩn mobile-first"
slug: website-tren-dien-thoai-chuan-mobile-first
topic: website-seo
keyword: "website mobile"
keywords: ["mobile-first indexing", "thiết kế web responsive", "website bán hàng trên điện thoại", "kiểm tra website trên điện thoại"]
description: "Website mobile chuẩn mobile-first: Google lập chỉ mục bản điện thoại, cách làm viewport, cỡ chữ, vùng chạm, nút mua cố định, form, checkout và cách tự kiểm tra."
date: 2026-11-19
updated: 2026-11-19
summary:
  - "Google lập chỉ mục và xếp hạng website chủ yếu dựa trên phiên bản điện thoại; từ 05/7/2024 Googlebot cho điện thoại thu thập gần như toàn bộ web, trang không truy cập được trên điện thoại sẽ không được lập chỉ mục."
  - "Website mobile chuẩn cần đủ năm thứ: thẻ viewport đúng, chữ nội dung khoảng 16px, vùng chạm đủ lớn (web.dev khuyên khoảng 48×48 pixel), nội dung bản điện thoại giống bản máy tính và trang tải nhanh."
  - "Với web bán hàng, chỗ mất đơn nhiều nhất trên điện thoại là nút mua khó bấm, form dài, ô nhập bị bàn phím che và cửa sổ bật lên che nội dung."
  - "Công cụ Kiểm tra thân thiện với thiết bị di động và báo cáo Khả năng sử dụng trên thiết bị di động đã ngừng từ 12/2023; nay kiểm tra bằng điện thoại thật, Lighthouse, PageSpeed Insights và Search Console."
faq:
  - q: "Mobile-first indexing là gì?"
    a: "Là cách Google dùng phiên bản điện thoại của trang để thu thập, lập chỉ mục và xếp hạng. Google đã chuyển gần như toàn bộ web sang cách này; theo Google Search Central, từ ngày 05/7/2024 trang không truy cập được trên điện thoại sẽ không còn được lập chỉ mục. Nội dung chỉ có ở bản máy tính mà thiếu ở bản điện thoại có thể bị Google bỏ qua."
  - q: "Website responsive đã đủ chuẩn mobile-first chưa?"
    a: "Responsive là nền tốt nhất vì một địa chỉ, một mã nguồn, nội dung giống nhau trên mọi thiết bị. Nhưng responsive chưa đủ nếu chữ quá nhỏ, nút quá sát nhau, ảnh nặng làm trang chậm, hoặc phần nội dung bị ẩn đi trên điện thoại. Cần kiểm tra thêm tốc độ, vùng chạm và luồng đặt hàng."
  - q: "Kiểm tra website có thân thiện với điện thoại ở đâu khi Google đã bỏ công cụ cũ?"
    a: "Google ngừng công cụ Kiểm tra thân thiện với thiết bị di động và báo cáo Khả năng sử dụng trên thiết bị di động từ tháng 12/2023. Anh chị dùng Lighthouse trong Chrome, PageSpeed Insights chọn tab Điện thoại, báo cáo Core Web Vitals trong Search Console và quan trọng nhất là tự đặt một đơn thử trên điện thoại thật."
  - q: "Nút Zalo, nút gọi cố định ở góc màn hình có ảnh hưởng SEO không?"
    a: "Nút nhỏ cố định thường không sao nếu không che nội dung chính và không che nút mua. Điều Google khuyên tránh là các cửa sổ bật lên che phần lớn nội dung khi người dùng vừa vào trang. Nên gom nút liên hệ thành một thanh gọn ở đáy màn hình thay vì ba bốn bong bóng nổi chồng nhau."
  - q: "Cỡ chữ bao nhiêu là hợp trên điện thoại?"
    a: "Chữ nội dung nên khoảng 16px, dòng giãn khoảng 1,5 lần cỡ chữ. Ô nhập trong form cũng nên từ 16px trở lên, vì trên iPhone, ô nhập chữ nhỏ hơn 16px khiến trình duyệt tự phóng to màn hình khi khách bấm vào, làm lệch bố cục."
sources:
  - title: "Mobile site and mobile-first indexing best practices – Google Search Central"
    url: "https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing"
  - title: "Mobile indexing vLast final final (2).doc – Google Search Central Blog (06/2024)"
    url: "https://developers.google.com/search/blog/2024/06/mobile-indexing-vlast-final-final.doc"
  - title: "Mobile-first indexing has landed – Google Search Central Blog (10/2023)"
    url: "https://developers.google.com/search/blog/2023/10/mobile-first-is-here?hl=en"
  - title: "Google officially drops Mobile Usability report, Mobile-Friendly Test tool and API – Search Engine Land"
    url: "https://searchengineland.com/google-officially-drops-mobile-usability-report-mobile-friendly-test-tool-and-mobile-friendly-test-api-435377"
  - title: "Responsive web design basics – web.dev"
    url: "https://web.dev/articles/responsive-web-design-basics"
  - title: "Accessible tap targets – web.dev"
    url: "https://web.dev/articles/accessible-tap-targets"
  - title: "What's New in WCAG 2.2 – W3C"
    url: "https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/"
  - title: "Web Vitals – web.dev"
    url: "https://web.dev/articles/vitals"
  - title: "Avoid intrusive interstitials and dialogs – Google Search Central"
    url: "https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials"
  - title: "Cấp huyện kết thúc hoạt động từ 1/7 – Cổng thông tin điện tử tỉnh Hà Tĩnh"
    url: "https://hatinh.gov.vn/vi/bai-viet/cap-huyen-ket-thuc-hoat-dong-tu-17"
---

**Website mobile chuẩn mobile-first là website được thiết kế cho màn hình điện thoại trước, rồi mới mở rộng ra máy tính, vì Google lập chỉ mục và xếp hạng chủ yếu dựa trên phiên bản điện thoại của trang.** Theo Google Search Central, từ ngày 05/7/2024 Googlebot cho điện thoại thu thập gần như toàn bộ web, và trang không truy cập được trên điện thoại sẽ không còn được lập chỉ mục. Với web bán hàng, chuyện này còn gắn thẳng với đơn hàng: phần lớn khách bấm vào từ quảng cáo, Zalo, Facebook trên chính chiếc điện thoại của họ.

Bài này đội QHUB viết cho chủ doanh nghiệp, không cần biết lập trình: Google đang xử lý bản điện thoại thế nào, năm thứ tối thiểu để web dùng tốt trên điện thoại, cách làm nút mua, form và trang thanh toán, rồi cách tự kiểm tra trong 30 phút. Phần tốc độ chi tiết đội mình đã viết riêng ở bài [tốc độ website và Core Web Vitals](/kien-thuc/toc-do-website-va-core-web-vitals/), bài này chỉ nhắc phần liên quan tới điện thoại.

## Mobile-first indexing là gì và tình trạng hiện nay ra sao?

**Mobile-first indexing** (lập chỉ mục ưu tiên thiết bị di động) là cách Google dùng phiên bản điện thoại của trang để thu thập, hiểu và xếp hạng nội dung. Trước đây Google đọc bản máy tính là chính. Giờ thì ngược lại.

Mốc thời gian đáng nhớ, theo blog Google Search Central:

| Thời điểm | Chuyện gì xảy ra | Ý nghĩa với chủ web |
| --- | --- | --- |
| 10/2023 | Google thông báo mobile-first indexing đã hoàn tất cho phần lớn web | Gần như mọi trang được đọc bằng bản điện thoại |
| 06/2024 | Google thông báo bước cuối: từ 05/7/2024 chuyển nốt các trang còn lại | Trang không mở được trên điện thoại sẽ không được lập chỉ mục |
| Hiện tại (11/2026) | Googlebot cho điện thoại là bộ thu thập chính; theo Google, bộ thu thập cho máy tính vẫn có thể thỉnh thoảng được dùng | Bản điện thoại là "bản chính" của website |

Hệ quả thực tế mà nhiều web bán hàng gặp:

- **Nội dung bị ẩn trên điện thoại.** Có web giấu bớt mô tả sản phẩm, bảng thành phần, phần hỏi đáp trên điện thoại cho gọn. Google đọc bản điện thoại, nên phần bị bỏ đi coi như không tồn tại.
- **Thiếu dữ liệu có cấu trúc và thẻ meta ở bản điện thoại.** Trang hướng dẫn mobile-first của Google khuyên bản điện thoại phải có cùng tiêu đề, mô tả, dữ liệu có cấu trúc, thẻ robots và văn bản thay thế cho ảnh như bản máy tính.
- **Nội dung chỉ hiện khi người dùng thao tác.** Google khuyên không tải chậm (lazy-load) phần nội dung chính theo kiểu phải vuốt hay bấm mới hiện, vì Googlebot không vuốt hay bấm như người.

Gói gọn: **bản điện thoại phải đủ nội dung như bản máy tính.** Thu gọn giao diện thì được, cắt nội dung thì không.

## Ba kiểu làm web cho điện thoại: chọn kiểu nào?

| Kiểu | Cách hoạt động | Ưu | Nhược | Đội QHUB khuyên |
| --- | --- | --- | --- | --- |
| Responsive (thiết kế đáp ứng) | Một địa chỉ, một mã nguồn, bố cục tự co giãn theo màn hình | Dễ quản lý, nội dung luôn giống nhau, Google khuyên dùng | Phải thiết kế cẩn thận để không nặng trên điện thoại | Chọn kiểu này cho gần như mọi web doanh nghiệp |
| Dynamic serving (phân phối động) | Một địa chỉ, máy chủ trả mã khác nhau theo thiết bị | Tối ưu riêng từng thiết bị | Dễ sai, bản điện thoại hay bị thiếu nội dung | Chỉ dùng khi có đội kỹ thuật riêng |
| Trang m. riêng | Hai địa chỉ, ví dụ m.tenmien.vn | Làm nhanh cho web cũ | Hai bộ nội dung, dễ lệch, phải cấu hình liên kết hai chiều | Không nên làm mới, web cũ nên dần chuyển sang responsive |

Các nền tảng làm web phổ biến hiện nay thường đã có giao diện responsive, nhưng responsive vẫn có thể dùng rất khó trên điện thoại, nên cần kiểm tra từng chi tiết dưới đây.

## Năm thứ tối thiểu để website mobile dùng tốt

### 1. Thẻ viewport đúng

**Thẻ viewport** là một dòng mã trong phần đầu trang, báo cho trình duyệt điện thoại biết phải hiển thị trang theo đúng chiều rộng màn hình. Thiếu nó, trình duyệt hiển thị trang như màn hình máy tính thu nhỏ, chữ li ti. Theo web.dev, dòng chuẩn là:

`<meta name="viewport" content="width=device-width, initial-scale=1">`

Đừng thêm `user-scalable=no` hay `maximum-scale=1` để chặn phóng to. Người lớn tuổi, người mắt kém cần phóng to để đọc thành phần, giá, chính sách đổi trả.

### 2. Cỡ chữ và khoảng cách dòng

- Chữ nội dung khoảng **16px**, dòng giãn khoảng 1,5 lần cỡ chữ.
- Đoạn văn ngắn, 2–4 câu.
- Giá bán, nút mua, chính sách giao hàng phải đọc được mà không cần phóng to.
- Màu chữ đủ tương phản với nền. Chữ xám nhạt trên nền trắng nhìn sang trọng trên máy tính nhưng đọc rất mệt dưới nắng.

### 3. Vùng chạm đủ lớn

**Vùng chạm** (tap target) là phần diện tích có thể bấm của nút, đường link, ô chọn. Ngón tay to hơn con trỏ chuột rất nhiều.

- web.dev khuyên vùng chạm khoảng **48×48 pixel** và cách nhau khoảng 8 pixel.
- Tiêu chuẩn tiếp cận WCAG 2.2 của W3C có tiêu chí 2.5.8 đặt mức tối thiểu **24×24 pixel** CSS, hoặc đủ khoảng trống xung quanh.
- Hay sai nhất: nút tăng giảm số lượng, ô chọn vị, đường link chính sách nằm sát nhau, bấm một cái trúng cái bên cạnh.

### 4. Ảnh nhẹ và đúng tỷ lệ

- Ảnh sản phẩm xuất ở định dạng WebP hoặc AVIF, cỡ vừa với màn hình điện thoại, không đưa ảnh 4000 pixel gốc lên.
- Luôn khai báo chiều rộng và chiều cao cho ảnh để trang không bị xô khi ảnh tải xong.
- Ảnh đầu trang (ảnh lớn nhất) không tải chậm; các ảnh phía dưới mới tải chậm.
- Banner chữ nhiều nên làm riêng bản dọc cho điện thoại, thay vì thu nhỏ banner ngang đến mức chữ không đọc được.

### 5. Tốc độ và độ nhạy trên điện thoại

Ba chỉ số **Core Web Vitals** đo trải nghiệm thật của người dùng. Theo web.dev, mức tốt là **LCP** (thời gian hiện phần nội dung lớn nhất) từ 2,5 giây trở xuống, **INP** (độ trễ phản hồi khi bấm, thay FID từ 12/3/2024) từ 200 mili giây trở xuống, và **CLS** (độ xô lệch bố cục) từ 0,1 trở xuống, tính ở 75% lượt truy cập và xét riêng điện thoại với máy tính. Điện thoại tầm trung với mạng 4G yếu là nơi các chỉ số này hay trượt nhất, nhất là INP khi trang gắn quá nhiều mã chat, mã theo dõi, mã quảng cáo.

## Nút mua, Zalo, gọi điện cố định: làm sao cho đúng?

Trên điện thoại, khách cuộn rất dài. Nút mua nằm tít trên đầu thì cuộn xuống đọc xong lại phải cuộn ngược lên. Vì vậy web bán hàng gần như luôn cần **thanh hành động cố định** ở đáy màn hình.

| Nên | Không nên |
| --- | --- |
| Một thanh gọn ở đáy, cao vừa phải, gồm nút chính "Mua ngay" và một hai nút phụ (Zalo, Gọi) | Ba bốn bong bóng nổi (Zalo, Messenger, gọi, chat) chồng lên nhau ở góc |
| Nút chính một màu nổi bật, chữ rõ hành động: "Mua ngay", "Thêm vào giỏ" | Chữ mơ hồ như "Xem thêm", "Liên hệ" cho nút mua |
| Thanh cố định chừa khoảng trống ở cuối trang để không che chữ, che chân trang | Nút cố định che mất nút thanh toán hoặc ô nhập mã giảm giá |
| Nút Gọi dùng liên kết `tel:` để bấm là gọi ngay | Số điện thoại chỉ là chữ thường, khách phải ghi nhớ rồi gõ lại |
| Cửa sổ bật lên, nếu có, nhỏ và dễ đóng, xuất hiện sau khi khách đã đọc một lúc | Cửa sổ bật lên che kín màn hình ngay khi vừa vào trang |

Về cửa sổ bật lên, trang hướng dẫn của Google Search Central khuyên tránh các hộp thoại xâm phạm, kiểu che phần lớn nội dung khiến người dùng khó tiếp cận trang. Thông báo cookie hay xác nhận độ tuổi theo quy định pháp luật thì không bị tính là xâm phạm nếu làm gọn gàng.

## Form và checkout trên điện thoại: chỗ mất đơn nhiều nhất

Với web bán hàng nhỏ ở Việt Nam, đội QHUB thường thấy nhiều đơn rơi ở bước điền thông tin chứ không chỉ ở bước xem sản phẩm. Checklist dưới đây đội mình dùng khi rà form đặt hàng:

- [ ] **Ít ô nhất có thể.** Đơn hàng giao tận nhà thường chỉ cần: họ tên, số điện thoại, địa chỉ, ghi chú. Email để tùy chọn.
- [ ] **Không bắt tạo tài khoản** trước khi mua. Cho đặt hàng nhanh, mời tạo tài khoản sau.
- [ ] **Bàn phím đúng loại.** Ô số điện thoại dùng kiểu `tel` để hiện bàn phím số; ô email dùng kiểu `email`.
- [ ] **Bật tự điền** (autocomplete) cho tên, số điện thoại, địa chỉ để điện thoại gợi ý sẵn.
- [ ] **Ô nhập cỡ chữ từ 16px trở lên.** Trên iPhone, ô nhập chữ nhỏ hơn 16px làm trình duyệt tự phóng to khi khách bấm vào.
- [ ] **Chọn tỉnh, phường dễ dùng.** Từ 01/7/2025 Việt Nam vận hành chính quyền địa phương hai cấp, cấp huyện kết thúc hoạt động và cả nước còn 34 tỉnh, thành; danh sách địa chỉ trên web cần cập nhật theo, ô chọn nên có tìm kiếm.
- [ ] **Báo lỗi ngay tại ô sai**, bằng chữ rõ ràng, không xóa sạch những gì khách đã nhập.
- [ ] **Bàn phím không che nút đặt hàng.** Thử trên điện thoại thật: điền đến ô cuối, nút "Đặt hàng" có còn nhìn thấy không.
- [ ] **Tổng tiền hiện rõ trước khi bấm đặt**, gồm phí giao hàng và ưu đãi, không để khách bất ngờ ở bước cuối.
- [ ] **Trang cảm ơn** nói rõ bước tiếp theo: khi nào gọi xác nhận, qua kênh nào, giao trong bao lâu.

Nếu có chuyển khoản, ngoài mã QR nên có nút sao chép số tài khoản và nội dung chuyển khoản, vì khách không thể dùng chính chiếc điện thoại đang xem để quét mã trên màn hình của nó.

## Cách tự kiểm tra website mobile trong 30 phút

Google đã **ngừng công cụ Kiểm tra thân thiện với thiết bị di động và báo cáo Khả năng sử dụng trên thiết bị di động trong Search Console từ tháng 12/2023**, theo Search Engine Land. Bộ kiểm tra đội QHUB dùng hiện nay:

| Bước | Công cụ | Xem gì | Thời gian |
| --- | --- | --- | --- |
| 1 | Điện thoại thật, một máy Android tầm trung và một iPhone, tắt Wi-Fi dùng 4G | Đặt một đơn thử từ trang chủ đến trang cảm ơn | 10 phút |
| 2 | PageSpeed Insights, tab Điện thoại | Dữ liệu người dùng thật (nếu có) và gợi ý sửa ảnh, mã | 5 phút |
| 3 | Search Console, báo cáo Core Web Vitals, mục Điện thoại | Nhóm trang có LCP, INP, CLS kém | 5 phút |
| 4 | Chrome trên máy tính, công cụ nhà phát triển, chế độ thiết bị | Bố cục ở vài cỡ màn hình, chữ có tràn, nút có chồng nhau | 5 phút |
| 5 | Search Console, công cụ Kiểm tra URL | Ảnh chụp trang Googlebot thấy, có đủ nội dung như người xem không | 5 phút |

Khi đặt đơn thử ở bước 1, anh chị ghi lại mọi chỗ phải phóng to, bấm nhầm, chờ lâu hay khó hiểu. Danh sách đó thường giá trị hơn mọi điểm số.

## Ví dụ thật: đội QHUB rà website QHUB HERBAL trên điện thoại thế nào?

QHUB HERBAL là thương hiệu trà do chính đội QHUB xây, có web bán hàng riêng tại [qhubherbal.com](https://qhubherbal.com/) bên cạnh gian hàng TikTok Shop và Shopee (giới thiệu chung ở trang [QHUB HERBAL](/qhub-herbal.html)). Mình không nói điểm số hay số đơn, chỉ kể những câu hỏi đội tự đặt khi rà web trên điện thoại:

- **Giá có đọc được trong một cái nhìn không?** Mỗi hộp giá niêm yết 140.000 đồng, giá bán 105.000 đồng. Trên website, ưu đãi là mua 2 tặng 1: khách trả 210.000 đồng, nhận 3 hộp, được chọn hộp tặng khác vị. Trên TikTok Shop và Shopee là mua 3 tặng 1 (trả 315.000 đồng, nhận 4 hộp). Vì ưu đãi theo kênh khác nhau, trang trên web phải ghi rõ đây là ưu đãi của website để khách không nhầm.
- **Chọn hộp tặng khác vị có dễ bấm không?** Khách chọn trong bảy vị trà, nên mỗi lựa chọn phải đủ lớn để chạm bằng ngón cái, có ảnh hộp và không nằm sát nhau.
- **Thông tin sản phẩm có đầy đủ như trên máy tính không?** Thành phần, quy cách 30 gói × 3 g, số tự công bố, hướng dẫn pha đều phải có trên bản điện thoại, không giấu sau nút "xem thêm" mà Googlebot không mở.
- **Lời lẽ có đúng mực không?** Trà là thực phẩm thông thường, nên trên mọi màn hình chỉ mô tả hương vị, thành phần, cách pha, cách dùng làm quà; không có câu nào về công dụng lên cơ thể.

Nếu anh chị đang cân nhắc có nên làm web riêng bên cạnh sàn, đội mình đã phân tích trong bài [doanh nghiệp bán trên sàn có cần website riêng không](/kien-thuc/doanh-nghiep-ban-tren-san-co-can-website-rieng-khong/).

## Lỗi hay gặp khi làm website mobile

- **Duyệt thiết kế trên máy tính.** Người làm web gửi ảnh chụp màn hình máy tính, chủ shop duyệt, đến khi lên điện thoại mới thấy chữ nhỏ, nút sát.
- **Ẩn nội dung trên điện thoại cho gọn**, quên rằng Google đọc bản điện thoại.
- **Gắn quá nhiều mã bên ngoài**: chat, Zalo, Messenger, ba bốn mã theo dõi quảng cáo. Mỗi mã một ít, cộng lại làm INP và tốc độ tụt rõ.
- **Đưa bảng giá, bảng thành phần lên dưới dạng ảnh chụp**: trên điện thoại khó đọc, Google cũng không hiểu như văn bản.
- **Cửa sổ bật lên giảm giá ngay giây đầu** che hết trang sản phẩm khách vừa bấm vào từ quảng cáo.
- **Chỉ thử trên iPhone đời mới với Wi-Fi văn phòng.** Khách thật dùng đủ loại máy, mạng chập chờn.

### Kinh nghiệm thực tế từ đội vận hành

Thói quen đơn giản nhất mà hiệu quả nhất đội QHUB áp dụng: **mỗi tháng một lần, một người không làm web cầm điện thoại đặt một đơn thật**, vừa làm vừa nói ra thành tiếng chỗ nào khó. Người làm web ngồi cạnh ghi chép, không được nhắc. Những chỗ "ai cũng biết bấm" thường lại là chỗ khách lạ lúng túng nhất. Ngoài ra, trước khi bật quảng cáo mới dẫn về web, đội luôn mở đúng trang đích đó trên điện thoại để thử.

## Việc cần làm ngay tuần này

1. Tự đặt một đơn thử trên điện thoại thật, dùng 4G, ghi lại mọi chỗ phải phóng to, bấm nhầm hoặc chờ lâu.
2. Kiểm tra mã nguồn trang có thẻ viewport chuẩn và không chặn phóng to.
3. So một trang sản phẩm trên điện thoại và máy tính: mô tả, thành phần, hỏi đáp có đầy đủ như nhau không.
4. Gom các bong bóng liên hệ thành một thanh hành động gọn ở đáy màn hình, thử xem có che nút thanh toán không.
5. Rút form đặt hàng về số ô tối thiểu, đặt đúng kiểu bàn phím và cỡ chữ ô nhập từ 16px.
6. Mở báo cáo Core Web Vitals trong Search Console, mục Điện thoại, ghi lại nhóm trang kém để giao người làm web.

Muốn rà toàn bộ website từ kỹ thuật đến nội dung, anh chị xem thêm bài [website bán hàng chuẩn SEO năm 2026](/kien-thuc/website-ban-hang-chuan-seo-nam-2026-huong-dan-tu-a-den-z/) và các bài trong chủ đề [Website và SEO](/kien-thuc/chu-de/website-seo/). QHUB Commerce (qhub.com.vn) vận hành gian hàng đa sàn với đội media, đội vận hành sàn, đội KOC và đội host livestream; nếu anh chị muốn website và gian hàng trên sàn cùng nói một giọng, đội mình sẵn lòng trao đổi.
