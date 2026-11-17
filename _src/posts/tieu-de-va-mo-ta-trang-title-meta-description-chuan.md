---
title: "Tiêu đề và mô tả trang (title, meta description) viết sao cho chuẩn"
slug: tieu-de-va-mo-ta-trang-title-meta-description-chuan
topic: website-seo
keyword: "title meta description"
keywords: ["thẻ title là gì", "meta description là gì", "độ dài title chuẩn seo", "google viết lại tiêu đề", "cách viết meta description"]
description: "Cách viết title meta description chuẩn: Google hiển thị và viết lại thế nào, độ dài theo pixel, công thức cho từng loại trang, lỗi hay gặp và cách đo CTR."
date: 2026-11-18
updated: 2026-11-18
summary:
  - "Title là tên trang hiện thành dòng chữ xanh bấm được trên Google, meta description là đoạn tóm tắt gợi ý cho phần mô tả bên dưới; cả hai quyết định người tìm có bấm vào trang hay không."
  - "Google tự chọn tiêu đề từ nhiều nguồn (thẻ title, H1, og:title, chữ trong liên kết…) và chủ yếu dùng nội dung trang để làm đoạn mô tả; khảo sát của Zyppy đầu năm 2022 cho thấy khoảng 61% thẻ title bị Google thay đổi."
  - "Google không đặt giới hạn ký tự cho title và meta description; con số khoảng 600px cho title trên máy tính là ước lượng của các công cụ SEO, tương đương chừng 50–60 ký tự."
  - "Cách đo đúng là xem tỷ lệ nhấp (CTR) trong báo cáo Hiệu suất của Google Search Console, so 28 ngày trước và sau khi sửa, ưu tiên trang nhiều lượt hiển thị mà ít người bấm."
faq:
  - q: "Title và meta description có giúp lên top Google không?"
    a: "Title là tín hiệu quan trọng giúp Google hiểu trang nói về gì, nên viết đúng chủ đề có ích cho thứ hạng. Meta description thì Google nói không dùng để xếp hạng, nhưng nó ảnh hưởng tới việc người tìm có bấm vào hay không. Vì vậy cả hai đều đáng viết kỹ, nhất là với trang chủ, danh mục và sản phẩm bán chạy."
  - q: "Title nên dài bao nhiêu ký tự?"
    a: "Google không quy định số ký tự, chỉ cắt bớt khi tiêu đề dài hơn bề ngang màn hình. Các công cụ SEO ước lượng khoảng 600px trên máy tính, tức chừng 50–60 ký tự Latinh. Đội QHUB thường viết 45–65 ký tự và đặt thông tin quan trọng nhất ở đầu, để có bị cắt thì vẫn đủ ý."
  - q: "Vì sao Google không hiện meta description mình đã viết?"
    a: "Theo tài liệu Google Search Central, đoạn mô tả chủ yếu lấy từ nội dung trang và thay đổi theo từng truy vấn. Google chỉ dùng meta description khi nó mô tả trang chính xác hơn phần nội dung tự trích. Mô tả chung chung, trùng lặp hoặc lệch nội dung trang dễ bị thay."
  - q: "Có cần viết meta description cho mọi trang không?"
    a: "Nên có cho các trang quan trọng: trang chủ, danh mục, sản phẩm, bài viết chính. Website hàng nghìn trang có thể tạo mô tả tự động từ dữ liệu sản phẩm, miễn mỗi trang khác nhau và đúng nội dung. Để trống còn hơn copy cùng một câu cho mọi trang."
  - q: "Sửa title xong bao lâu thì thấy kết quả?"
    a: "Google cần thu thập lại trang rồi mới hiện tiêu đề mới, thường vài ngày đến vài tuần; anh chị có thể dùng Kiểm tra URL trong Search Console để yêu cầu lập chỉ mục lại. Nên đợi đủ khoảng 4 tuần dữ liệu rồi mới so CTR, và tránh kết luận khi đang có đợt cập nhật lõi của Google."
sources:
  - title: "Influencing your title links in search results – Google Search Central"
    url: "https://developers.google.com/search/docs/appearance/title-link"
  - title: "Control your snippets in search results – Google Search Central"
    url: "https://developers.google.com/search/docs/appearance/snippet"
  - title: "Performance report (Search results) – Search Console Help"
    url: "https://support.google.com/webmasters/answer/7576553"
  - title: "Google Search may now use OG title for title links – Search Engine Land"
    url: "https://searchengineland.com/google-search-may-now-use-og-title-for-title-links-446023"
  - title: "Google Rewrites 61% of Page Title Tags [SEO Study] – Zyppy"
    url: "https://zyppy.com/seo/google-title-rewrites/"
  - title: "Google shares 4 examples of how to improve a meta description – Search Engine Land"
    url: "https://searchengineland.com/google-how-to-improve-meta-descriptions-387691"
  - title: "SEO Starter Guide – Google Search Central"
    url: "https://developers.google.com/search/docs/fundamentals/seo-starter-guide"
---

**Title meta description chuẩn là cặp "tên trang" và "lời giới thiệu ngắn" mô tả đúng nội dung trang, đặt thông tin quan trọng nhất lên đầu, mỗi trang một cặp riêng, đủ hấp dẫn để người tìm trên Google muốn bấm vào.** Title là thứ Google dùng nhiều nhất để tạo dòng chữ xanh bấm được trong kết quả tìm kiếm. Meta description là đoạn gợi ý cho phần mô tả bên dưới. Google có thể viết lại cả hai, nhưng trang có title và mô tả tốt thì ít bị viết lại hơn và được bấm nhiều hơn.

Bài này có công thức cho từng loại trang, ví dụ trước và sau, lỗi hay gặp và cách đo bằng Google Search Console. Nếu chưa nắm bức tranh tổng thể, anh chị có thể đọc trước bài [website bán hàng chuẩn SEO năm 2026](/kien-thuc/website-ban-hang-chuan-seo-nam-2026-huong-dan-tu-a-den-z/).

## Thẻ title và meta description là gì?

**Thẻ title là đoạn mã HTML khai báo tên của một trang web.** Nó hiện trên tab trình duyệt, là nguồn chính để Google tạo tiêu đề trong kết quả tìm kiếm (Google gọi là "title link", tức liên kết tiêu đề), và thường được dùng làm tiêu đề khi chia sẻ link.

**Meta description là đoạn mã HTML tóm tắt nội dung trang trong một hai câu.** Người đọc không thấy nó trên trang. Google có thể dùng nó làm phần mô tả (snippet, tức đoạn trích) dưới tiêu đề trong kết quả tìm kiếm.

Trong mã nguồn, hai thẻ nằm ở phần `<head>`:

```html
<title>Trà Dưỡng Nhan – trà thảo mộc túi lọc 9 vị | QHUB HERBAL</title>
<meta name="description" content="Trà túi lọc 9 vị hoa và thảo mộc, không thêm đường, không caffeine. Hộp 30 gói, hợp pha một ấm buổi chiều hoặc làm quà.">
```

Nhiều người hay nhầm title với vài thứ có tên gần giống. Bảng dưới phân biệt nhanh:

| Thành phần | Người đọc thấy ở đâu | Dùng để làm gì |
| --- | --- | --- |
| Thẻ title | Tab trình duyệt, kết quả Google | Đặt tên trang cho công cụ tìm kiếm và người tìm |
| Thẻ H1 | Tiêu đề lớn trên chính trang | Cho người đã vào trang biết mình đang đọc gì |
| Meta description | Có thể hiện dưới tiêu đề trên Google | Gợi ý đoạn mô tả, thuyết phục người tìm bấm vào |
| og:title, og:description | Khung xem trước khi chia sẻ lên Facebook, Zalo | Tiêu đề và mô tả cho mạng xã hội (Open Graph) |

Title và H1 có thể giống nhau hoặc khác nhau một chút. Title thường thêm tên thương hiệu ở cuối, H1 thì không cần.

## Google hiển thị và viết lại title, meta description thế nào?

Đây là phần nhiều người bỏ qua: **Google không cam kết hiển thị nguyên văn title và meta description anh chị viết.** Cả hai chỉ là gợi ý mạnh.

### Tiêu đề: Google chọn từ nhiều nguồn

Theo tài liệu "Influencing your title links in search results" trên Google Search Central, Google tạo title link tự động và có thể dựa vào nhiều nguồn: thẻ title, tiêu đề chính hiển thị trên trang, các thẻ heading như H1, chữ nổi bật trên trang, chữ trong các liên kết trỏ về trang, dữ liệu có cấu trúc. Từ khoảng tháng 8/2024, theo Search Engine Land, Google bổ sung thêm thẻ `og:title` vào danh sách nguồn này.

Google viết lại tiêu đề khi thẻ title có vấn đề. Những trường hợp tài liệu của Google nêu gồm:

- **Title nửa vời**, ví dụ chỉ có tên thương hiệu, không nói trang về gì.
- **Title lỗi thời**, ví dụ ghi năm cũ trong khi nội dung đã cập nhật.
- **Title không đúng nội dung** trang.
- **Title lặp khuôn mẫu**, nhiều trang dùng cùng một câu, chỉ khác vài chữ.
- **Thiếu title** hoặc title nhồi từ khóa.

Theo khảo sát của Zyppy công bố đầu năm 2022, Google thay đổi khoảng 61% thẻ title trong mẫu khảo sát. Đây là số của một khảo sát độc lập, không phải số Google công bố, và có thể đã khác hiện nay.

### Mô tả: Google chủ yếu trích từ nội dung trang

Theo tài liệu "Control your snippets in search results", đoạn mô tả chủ yếu được tạo từ nội dung trên trang và **có thể khác nhau theo từng truy vấn**. Google dùng meta description khi nó mô tả trang chính xác hơn phần Google tự trích. Tài liệu cũng nói không có giới hạn độ dài cho meta description; đoạn mô tả sẽ bị cắt khi cần cho vừa màn hình.

Hệ quả thực tế:

1. Meta description vẫn đáng viết, vì với truy vấn chung như tên sản phẩm, Google hay dùng nó.
2. **Đoạn đầu trang quan trọng không kém**, vì với truy vấn chi tiết Google sẽ trích từ đó. Cách viết đoạn mở đầu có trong bài [viết bài chuẩn SEO mà người đọc vẫn thích](/kien-thuc/viet-bai-chuan-seo-ma-nguoi-doc-van-thich/).
3. Title, H1, og:title nên **thống nhất cùng một ý**, để Google không phải tự chọn.

## Title và meta description dài bao nhiêu là vừa?

Câu trả lời ngắn: Google không có quy định số ký tự. Google cắt theo **bề ngang hiển thị**, đo bằng pixel (điểm ảnh), chứ không đếm chữ. Chữ "m" rộng hơn chữ "i", chữ in hoa rộng hơn chữ thường, nên hai tiêu đề cùng 60 ký tự có thể một cái hiện đủ, một cái bị cắt.

Các công cụ xem trước kết quả tìm kiếm (SERP preview) thường ước lượng như sau. Anh chị coi đây là **ước lượng của các công cụ SEO, không phải con số Google công bố**, và giao diện Google có thể đổi bất cứ lúc nào.

| Thành phần | Google nói gì | Ước lượng của công cụ SEO (tính đến 11/2026) | Đội QHUB thường viết |
| --- | --- | --- | --- |
| Title trên máy tính | Không giới hạn, cắt cho vừa màn hình | Khoảng 600px, chừng 50–60 ký tự Latinh | 45–65 ký tự, ý chính trong 50 ký tự đầu |
| Title trên điện thoại | Như trên | Có thể xuống hai dòng, dài hơn một chút | Như trên |
| Meta description | Không giới hạn, cắt khi cần | Khoảng 920px trên máy tính, chừng 150–160 ký tự | 120–160 ký tự, câu đầu đủ nghĩa |

Quy tắc quan trọng hơn con số: **đặt từ khóa và thông tin chính ở đầu**, tên thương hiệu ở cuối. Có bị cắt thì phần mất đi là phần ít quan trọng.

## Công thức viết title meta description cho từng loại trang

Mỗi loại trang phục vụ một kiểu người tìm khác nhau, nên công thức cũng khác. Từ khóa cho từng trang lấy từ bước nghiên cứu, anh chị xem cách làm trong bài [nghiên cứu từ khóa cho website doanh nghiệp](/kien-thuc/nghien-cuu-tu-khoa-cho-website-doanh-nghiep/).

| Loại trang | Công thức title | Công thức meta description |
| --- | --- | --- |
| Trang chủ | Thương hiệu – Làm gì / bán gì cho ai | Doanh nghiệp là ai, khác ở đâu, khách nhận được gì |
| Trang danh mục | Tên danh mục + đặc điểm khách hay lọc \| Thương hiệu | Danh mục gồm những gì, số lựa chọn, cách chọn, chính sách giao hàng |
| Trang sản phẩm | Tên sản phẩm + loại + đặc điểm chính \| Thương hiệu | Thành phần hoặc chất liệu, quy cách, điểm khác, ưu đãi đúng kênh |
| Bài viết | Câu hỏi hoặc chủ đề chính + lời hứa nội dung | Trả lời ngắn câu hỏi, rồi nói bài có gì: bảng, bước, ví dụ |

Vài lưu ý theo từng loại:

- **Trang chủ** thường được tìm bằng tên thương hiệu, nên thương hiệu đứng đầu là hợp lý. Ví dụ thật: title trang chủ qhub.com.vn là "QHUB Commerce – Vận hành TikTok Shop, Shopee, Website".
- **Trang danh mục** hay bị bỏ quên, title chỉ là "Sản phẩm" hay "Trà". Hãy viết như người mua gõ: "Trà thảo mộc túi lọc – 7 vị, hộp 30 gói | Tên thương hiệu". Cách chia danh mục có trong bài [cấu trúc website chuẩn SEO](/kien-thuc/cau-truc-website-chuan-seo-danh-muc-trang-tru-cot-cum-bai/).
- **Trang sản phẩm** cần tên đầy đủ để khách phân biệt với hàng tương tự. Nếu nhắc ưu đãi, **ưu đãi phải khớp kênh bán của chính trang đó** và sửa ngay khi hết hạn.
- **Bài viết** nên dùng câu hỏi người ta gõ, cộng một lời hứa mà bài thật sự có ("kèm bảng", "7 bước").

Website hàng trăm sản phẩm có thể dựng khuôn tự động từ dữ liệu, miễn câu tạo ra **khác nhau thật sự** giữa các trang. Ví dụ thật: bộ dựng trang mục Kiến thức của qhub.com.vn chỉ gắn thêm "| QHUB Commerce" khi tiêu đề bài ngắn hơn 57 ký tự, để tiêu đề dài không bị đẩy phần nội dung ra sau.

## Ví dụ trước và sau khi sửa title, meta description

Các ví dụ dưới đây là **ví dụ giả định** do đội mình dựng để minh họa, trừ những chỗ ghi rõ là trang thật.

| Loại trang | Trước khi sửa | Sau khi sửa | Vì sao tốt hơn |
| --- | --- | --- | --- |
| Danh mục | Sản phẩm – Shop ABC | Trà thảo mộc túi lọc, hộp 30 gói \| Shop ABC | Có từ khóa người mua gõ, có quy cách |
| Sản phẩm | Trà hoa hồng, trà hoa hồng ngon, trà hoa hồng giá rẻ | Trà hoa hồng sấy khô 100 g, túi zip \| Shop ABC | Bỏ nhồi từ khóa, thêm thông tin phân biệt |
| Bài viết | Kiến thức về trà | Cách pha trà túi lọc ngon: nhiệt độ nước và thời gian ngâm | Nói đúng câu hỏi, có lời hứa cụ thể |
| Mô tả sản phẩm | Shop ABC chuyên cung cấp các loại trà chất lượng cao uy tín hàng đầu | Trà hoa hồng sấy khô, túi 100 g có khóa zip. Pha 3–5 bông với nước nóng, giao toàn quốc, đổi trả trong 7 ngày | Thông tin cụ thể thay cho lời tự khen |

### Ví dụ thật: trang Trà Dưỡng Nhan của QHUB HERBAL

QHUB HERBAL là thương hiệu trà túi lọc do chính đội QHUB xây. [Trà Dưỡng Nhan](/tra-duong-nhan.html) mới ra mắt ngày 13/11/2026, nên đội vừa viết title và mô tả cho sản phẩm này. Mình kể cách nghĩ, không nói số liệu truy cập.

Trà là thực phẩm thông thường, nên **title và mô tả không có chữ nào gán tác dụng lên cơ thể**. Tên có chữ "Dưỡng Nhan" càng dễ khiến người viết, hoặc AI viết hộ, thêm câu về làn da, nên đội mình chỉ cho phép nói thành phần, quy cách, hương vị, cách dùng và dịp làm quà.

- **Title:** "Trà Dưỡng Nhan – trà thảo mộc túi lọc 9 vị | QHUB HERBAL". Tên sản phẩm đứng đầu, loại sản phẩm ngay sau, thương hiệu ở cuối.
- **Mô tả:** "Trà túi lọc 9 vị lá sen, tía tô, hoa hồng, hoa nhài, táo đỏ, kỷ tử… Không thêm đường, không caffeine, hộp 30 gói × 3 g. Hương hoa dịu, hợp làm quà."

Phần ưu đãi được xử lý theo kênh. Giá niêm yết 140.000đ, giá bán 105.000đ ở mọi kênh. Trên web bán hàng qhubherbal.com là mua 2 tặng 1 (trả 210.000đ nhận 3 hộp). Trên TikTok Shop và Shopee là mua 3 tặng 1 (trả 315.000đ nhận 4 hộp). Vì vậy mô tả viết cho website không được copy nguyên sang gian hàng trên sàn, nếu không khách sẽ thấy một ưu đãi mà kênh đó không áp dụng.

## Lỗi hay gặp khi viết title và meta description

Từ những website đội mình nhận lại để rà soát, đây là các lỗi lặp lại nhiều nhất:

- **Trùng lặp hàng loạt.** Mọi trang sản phẩm cùng title "Shop ABC – Uy tín chất lượng". Google không phân biệt được các trang và sẽ tự viết lại.
- **Nhồi từ khóa.** Lặp một cụm ba bốn lần, đúng trường hợp Google nêu là lý do thay tiêu đề.
- **Để trống.** Nền tảng tự điền "Untitled", "Trang chủ", "Sản phẩm".
- **Tên thương hiệu dài đứng đầu mọi trang,** phần quan trọng bị cắt trên điện thoại.
- **Ghi năm cũ** như "Bảng giá 2024" trong khi trang đã cập nhật.
- **Mô tả tự khen, không có thông tin** như "uy tín hàng đầu", vừa vô nghĩa vừa dễ vướng quy định quảng cáo.
- **Gán công dụng cho thực phẩm, mỹ phẩm,** rủi ro pháp lý.
- **Ưu đãi hết hạn hoặc sai kênh** vẫn nằm trong mô tả.
- **Title, H1 và og:title nói ba kiểu khác nhau.**

## Cách kiểm tra hàng loạt và đo CTR bằng Google Search Console

### Kiểm tra hàng loạt

Từ vài chục trang trở lên, nên dùng công cụ quét website (crawler), tức phần mềm tự đi qua mọi đường dẫn và lấy ra title, mô tả của từng trang. Screaming Frog SEO Spider là công cụ phổ biến, bản miễn phí giới hạn số URL mỗi lần quét (thường được nhắc là 500 URL, anh chị xem lại trên trang của hãng).

Quy trình đội mình hay làm:

1. Quét toàn bộ website, xuất ra bảng tính gồm cột URL, title, độ dài title, meta description, độ dài mô tả, H1.
2. Lọc bốn nhóm: title trống, title trùng, mô tả trống, mô tả trùng.
3. Đánh dấu title quá ngắn (dưới khoảng 30 ký tự) và quá dài (trên khoảng 65 ký tự).
4. Sửa theo thứ tự ưu tiên: trang chủ, danh mục, sản phẩm bán chạy, bài viết nhiều lượt hiển thị.

### Đo bằng Google Search Console

**CTR (Click-Through Rate) là tỷ lệ nhấp, bằng số lượt nhấp chia cho số lượt hiển thị trên Google.** Đây là con số phản ánh rõ nhất title và mô tả có thuyết phục hay không. Báo cáo Hiệu suất (Performance) của Google Search Console cho xem lượt nhấp, lượt hiển thị, CTR và vị trí trung bình theo từng trang, từng truy vấn.

| Bước | Làm gì trong Search Console | Mục đích |
| --- | --- | --- |
| 1 | Mở Hiệu suất, chọn 3 tháng gần nhất, bật cả bốn chỉ số | Có bức tranh đủ dài |
| 2 | Vào tab Trang, sắp xếp theo lượt hiển thị | Tìm trang nhiều người thấy |
| 3 | Lọc trang có vị trí trung bình khoảng 1–10 nhưng CTR thấp hơn các trang cùng nhóm | Đây là trang "được thấy mà không được bấm" |
| 4 | Bấm vào từng trang, xem tab Truy vấn | Biết người ta gõ gì để viết lại title cho trúng |
| 5 | Sửa title, mô tả; ghi lại ngày sửa; dùng Kiểm tra URL để yêu cầu lập chỉ mục lại | Có mốc để so |
| 6 | Sau khoảng 4 tuần, dùng chức năng so sánh khoảng thời gian: 28 ngày sau so với 28 ngày trước | Đo CTR có tăng thật không |

CTR phụ thuộc nhiều vào vị trí, nên chỉ so khi vị trí trung bình không đổi quá nhiều, và tách riêng truy vấn tên thương hiệu. Nếu đang có đợt cập nhật lõi của Google, như đợt bắt đầu giữa tháng 11/2026, nên đợi chạy xong mới kết luận.

### Kinh nghiệm thực tế từ đội vận hành

Ở nhiều website đội mình từng rà soát, phần cải thiện CTR rõ nhất thường không đến từ câu chữ hay hơn, mà đến từ việc **sửa title cho đúng thứ người ta gõ**. Tab Truy vấn trong Search Console hay cho thấy một trang đang hiện cho một cụm từ mà title không hề có. Thêm đúng cụm đó vào đầu title, giữ phần còn lại, thường hiệu quả hơn viết lại cả câu.

Đội mình cũng không sửa cùng lúc hàng trăm trang. Mỗi đợt 10–20 trang, đo xong mới sửa đợt tiếp, để biết thay đổi nào có tác dụng. Title và đoạn mở đầu rõ ràng còn giúp trợ lý AI nhắc đúng tên thương hiệu, phần này có trong bài [GEO là gì](/kien-thuc/geo-la-gi-toi-uu-de-chatgpt-gemini-nhac-toi-thuong-hieu/).

## Việc cần làm ngay tuần này

1. Mở mã nguồn trang chủ, một trang danh mục và một trang sản phẩm bán chạy, kiểm tra title và meta description đã có và khác nhau chưa.
2. Quét toàn website bằng một công cụ crawler, lọc title và mô tả trống hoặc trùng.
3. Trong Search Console, lấy 10 trang nhiều lượt hiển thị nhưng CTR thấp, đọc tab Truy vấn của từng trang.
4. Viết lại title theo công thức của từng loại trang, đặt từ khóa chính và thông tin phân biệt lên đầu, thương hiệu xuống cuối.
5. Rà mọi mô tả có nhắc ưu đãi: đúng kênh chưa, còn hạn không. Rà luôn các câu gán công dụng cho thực phẩm, mỹ phẩm.
6. Ghi ngày sửa vào bảng tính, hẹn 4 tuần sau so CTR trước và sau.

QHUB Commerce (qhub.com.vn) là đội vận hành gian hàng đa sàn, có đội media, đội vận hành sàn, đội KOC và đội host livestream. Đội mình viết tên, mô tả sản phẩm sao cho website và gian hàng trên sàn cùng nói đúng một thông tin, đúng ưu đãi của từng kênh.
