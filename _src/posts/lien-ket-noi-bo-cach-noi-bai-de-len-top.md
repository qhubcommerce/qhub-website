---
title: "Liên kết nội bộ: cách nối bài để lên top"
slug: lien-ket-noi-bo-cach-noi-bai-de-len-top
topic: website-seo
keyword: "liên kết nội bộ"
keywords: ["internal link là gì", "anchor text", "trang mồ côi", "liên kết nội bộ seo", "trang trụ cột cụm bài"]
description: "Liên kết nội bộ là gì, vì sao Google và AI cần, cách nối trang trụ cột với cụm bài, đặt anchor text, xử lý trang mồ côi, link chết và quy trình rà soát mỗi tháng."
date: 2026-11-22
updated: 2026-11-22
summary:
  - "Liên kết nội bộ là đường link từ trang này sang trang khác trên cùng website; Google dùng nó để tìm trang mới và hiểu trang nào quan trọng, nói về chủ đề gì."
  - "Theo hướng dẫn Link best practices của Google Search Central, link phải là thẻ a có href, chữ gắn link nên mô tả rõ trang đích, ngắn gọn và không nhồi từ khóa."
  - "Mô hình trang trụ cột – cụm bài nối mọi bài con lên trang chủ đề, nối các bài cùng cụm với nhau và nối sang trang sản phẩm hoặc dịch vụ liên quan."
  - "Mỗi tháng nên rà một lần: thêm link từ bài cũ sang bài mới, tìm trang mồ côi, sửa link chết, dùng báo cáo Liên kết trong Google Search Console và một công cụ quét như Screaming Frog."
faq:
  - q: "Liên kết nội bộ là gì?"
    a: "Liên kết nội bộ (internal link) là đường link trỏ từ một trang sang một trang khác trên cùng tên miền, ví dụ từ bài viết sang trang sản phẩm. Nó giúp người đọc đi tiếp, giúp Google tìm và hiểu cấu trúc website. Khác với backlink là link từ website khác trỏ về."
  - q: "Mỗi bài viết nên có bao nhiêu liên kết nội bộ?"
    a: "Google không đưa ra con số cố định. Kinh nghiệm của đội QHUB là 3–6 link trong thân bài cho một bài 2.000–3.000 chữ, mỗi link đặt đúng chỗ người đọc cần. Quan trọng hơn số lượng là link phải liên quan và chữ gắn link phải mô tả rõ trang đích."
  - q: "Trang mồ côi là gì và có hại gì?"
    a: "Trang mồ côi là trang không có liên kết nội bộ nào trỏ tới. Google khó tìm ra nó nếu chỉ dựa vào việc đi theo link, và kể cả khi tìm thấy qua sitemap, trang cũng bị xem là ít quan trọng. Người đọc gần như không bao giờ tới được trang này nếu không tìm kiếm."
  - q: "Anchor text nên viết thế nào?"
    a: "Anchor text là chữ hiển thị được gắn link. Nên viết ngắn, mô tả đúng nội dung trang đích, ví dụ “cách đọc báo cáo Search Console” thay vì “bấm vào đây”. Không nên lặp đúng một cụm từ khóa ở mọi link vì trông gượng và không giúp người đọc."
  - q: "Kiểm tra liên kết nội bộ bằng công cụ nào?"
    a: "Google Search Console có báo cáo Liên kết, cho biết trang nào được liên kết nội bộ nhiều nhất. Screaming Frog SEO Spider quét toàn website để tìm link chết, chuyển hướng và trang có ít link trỏ tới. Website nhỏ có thể bắt đầu bằng hai công cụ này là đủ."
sources:
  - title: "Link best practices for Google – Google Search Central"
    url: "https://developers.google.com/search/docs/crawling-indexing/links-crawlable"
  - title: "Links report – Search Console Help"
    url: "https://support.google.com/webmasters/answer/9049606?hl=en"
  - title: "Breadcrumb (BreadcrumbList) structured data – Google Search Central"
    url: "https://developers.google.com/search/docs/data-types/breadcrumbs"
  - title: "Get started with Search – Google Search Central"
    url: "https://developers.google.com/search/docs/beginner/get-started"
  - title: "Screaming Frog SEO Spider"
    url: "https://www.screamingfrog.co.uk/seo-spider/"
---

**Liên kết nội bộ là đường link nối từ trang này sang trang khác trên cùng một website, và đó là cách rẻ nhất để giúp bài viết lên top.** Google đi theo các đường link này để tìm trang mới, hiểu trang nói về chủ đề gì và trang nào quan trọng hơn. Người đọc cũng đi theo chúng để đọc tiếp, xem sản phẩm, để lại thông tin. Một bài hay mà không ai trỏ link tới thì giống một căn phòng đẹp nhưng không có cửa.

Bài này đội QHUB chia sẻ cách mình nối bài trên chính mục Kiến thức của qhub.com.vn: định nghĩa, vì sao Google và AI cần, mô hình trang trụ cột – cụm bài, cách viết chữ gắn link, nên đặt bao nhiêu link, xử lý trang mồ côi và link chết, công cụ kiểm tra và một quy trình rà soát mỗi tháng. Các hướng dẫn của Google được đối chiếu với Google Search Central ngày 22/11/2026.

## Liên kết nội bộ là gì, khác backlink thế nào?

**Liên kết nội bộ** (internal link) là link trỏ tới một trang khác trên cùng tên miền. Ví dụ, trong bài này mình trỏ tới bài [cấu trúc website chuẩn SEO](/kien-thuc/cau-truc-website-chuan-seo-danh-muc-trang-tru-cot-cum-bai/), đó là một liên kết nội bộ.

**Backlink** (liên kết ngoài trỏ về) là link từ website khác trỏ về website của mình. Backlink khó kiếm, phụ thuộc người khác. Liên kết nội bộ thì hoàn toàn nằm trong tay mình, sửa lúc nào cũng được, không tốn đồng nào.

Trên một website có ba loại liên kết nội bộ chính:

| Loại link | Nằm ở đâu | Vai trò |
| --- | --- | --- |
| Menu, chân trang | Mọi trang | Dẫn tới trang chính: danh mục, dịch vụ, giới thiệu |
| Breadcrumb | Đầu trang | Cho biết trang nằm ở tầng nào, quay lại danh mục |
| Link trong thân bài | Giữa nội dung | Nối các bài liên quan, có giá trị ngữ cảnh cao nhất |

Link trong thân bài là loại đáng đầu tư nhất. Nó có chữ xung quanh giải thích vì sao nên đọc trang kia, nên cả Google lẫn người đọc đều hiểu rõ mối liên hệ.

## Vì sao Google và AI cần liên kết nội bộ?

Tài liệu "Get started with Search" của Google Search Central nói khá rõ: Google tìm trang mới chủ yếu bằng cách đi theo link từ những trang nó đã biết. Sitemap giúp khai báo thêm, nhưng link vẫn là con đường chính. Từ đó, liên kết nội bộ làm được ba việc:

1. **Giúp Google tìm trang mới nhanh hơn.** Bài mới được trỏ link từ trang chủ đề và vài bài cũ đã có chỗ đứng thường được thu thập sớm hơn bài nằm một mình.
2. **Báo cho Google biết trang nào quan trọng.** Trang được nhiều trang khác trong website trỏ tới thường được hiểu là trang trọng tâm.
3. **Giải thích chủ đề của trang.** Chữ gắn link mô tả trang đích. Hai mươi bài cùng trỏ tới một trang với chữ xoay quanh "phí sàn TikTok Shop" là một tín hiệu rất rõ.

Với các trợ lý AI như ChatGPT, Gemini hay AI Overviews của Google, nguyên lý cũng tương tự. Các hệ thống này cần hiểu website có chiều sâu về chủ đề nào. Một cụm bài nối với nhau chặt chẽ cho thấy website không chỉ có một bài lẻ, mà có cả một kho kiến thức đầy đủ quanh chủ đề đó.

## Mô hình trang trụ cột – cụm bài nối thế nào?

**Trang trụ cột** (pillar page) là trang tổng quan của một chủ đề lớn. **Cụm bài** (cluster) là các bài con đi sâu từng khía cạnh nhỏ của chủ đề đó. Liên kết nội bộ là sợi dây buộc chúng lại.

Có ba hướng nối cần làm đủ:

- **Nối dọc:** mỗi bài con trỏ lên trang trụ cột, trang trụ cột trỏ xuống mọi bài con.
- **Nối ngang:** mỗi bài con trỏ sang 2–3 bài cùng cụm, đặt đúng chỗ người đọc cần biết thêm.
- **Nối sang trang bán hàng:** bài kiến thức trỏ tới sản phẩm hoặc dịch vụ liên quan, trang sản phẩm trỏ ngược về bài hướng dẫn.

### Ví dụ quy trình trên qhub.com.vn

Mục Kiến thức của qhub.com.vn chia bài theo chủ đề. Mỗi chủ đề có một trang riêng dạng `/kien-thuc/chu-de/<chủ đề>/`, ví dụ trang chủ đề Website chuẩn SEO mà bài này thuộc về. Trang này đóng vai trang trụ cột, liệt kê mọi bài trong cụm. Mỗi bài con có breadcrumb trỏ ngược lên trang chủ đề.

Khi viết một bài mới, đội mình có mấy quy tắc cố định:

- Mỗi bài có từ 3 đến 6 link trong thân bài, chỉ trỏ tới bài đã đăng, trang chủ đề hoặc trang dịch vụ liên quan.
- Bài nói về thuê ngoài, chi phí dịch vụ, quảng cáo, KOC, livestream thì có một link tới trang dịch vụ tương ứng.
- Bộ công cụ dựng trang tự gỡ những link trỏ tới bài chưa đăng, để không bao giờ xuất bản một link dẫn vào trang lỗi.

### Ví dụ với trang sản phẩm QHUB HERBAL

QHUB HERBAL là thương hiệu trà do chính đội QHUB xây. Trên qhub.com.vn, trang tổng [QHUB HERBAL](/qhub-herbal.html) đóng vai trang trụ cột cho bảy trang sản phẩm. Mỗi trang sản phẩm trỏ về trang tổng. Các bài kiến thức có nhắc tới một sản phẩm thì gắn link tới đúng trang sản phẩm đó, ví dụ bài viết về cách viết trang sản phẩm có nhắc [Trà Dưỡng Nhan](/tra-duong-nhan.html) thì trỏ thẳng tới trang của trà này. Ngược lại, trang sản phẩm dẫn về các bài hướng dẫn liên quan. Người đọc đi từ kiến thức sang sản phẩm, rồi từ sản phẩm quay lại đọc tiếp, đều có đường.

## Anchor text nên viết thế nào cho đúng?

**Anchor text** là chữ hiển thị được gắn link, tức phần chữ người đọc bấm vào. Tài liệu "Link best practices for Google" của Google Search Central đưa ra mấy nguyên tắc chính, mình tóm lại bằng lời dễ hiểu:

- **Mô tả rõ trang đích.** Đọc chữ gắn link là đoán được trang kia nói về gì.
- **Ngắn gọn.** Vài chữ đến một cụm ngắn, không gắn link cho cả câu dài.
- **Liên quan tới trang hiện tại và trang đích.** Đặt link ở đoạn đang nói đúng chủ đề đó.
- **Không nhồi từ khóa.** Lặp đi lặp lại một cụm từ khóa ở mọi link chỉ làm câu văn gượng.
- **Link phải là thẻ `<a href="…">` thật.** Nút bấm chỉ chạy bằng JavaScript mà không có href thì Google không chắc đi theo được.

| Cách viết | Ví dụ | Đánh giá |
| --- | --- | --- |
| Chung chung | "xem tại đây", "bấm vào đây" | Không nói gì về trang đích, nên tránh |
| Nhồi từ khóa | "liên kết nội bộ seo liên kết nội bộ tốt nhất" | Gượng, khó đọc |
| Quá dài | Gắn link cho cả một câu hai dòng | Khó biết trang đích nói gì |
| Mô tả rõ, tự nhiên | "cách đọc báo cáo Search Console" | Nên dùng |

Một mẹo nhỏ: thay đổi cách diễn đạt giữa các bài. Mười bài cùng trỏ tới trang phí sàn có thể dùng "bảng phí sàn TikTok Shop", "cách tính phí trên từng đơn", "các loại phí năm 2026". Vẫn cùng chủ đề, nhưng tự nhiên như người viết thật.

## Mỗi bài nên có bao nhiêu link, đặt ở đâu?

Google không đưa ra con số tối đa cố định. Kinh nghiệm của đội QHUB với bài dài 2.000–3.000 chữ là 3–6 link trong thân bài. Ít hơn thì bài bị cô lập. Nhiều hơn thì người đọc bị kéo đi khắp nơi, link nào cũng mất giá trị.

Chỗ đặt link quan trọng không kém số lượng:

- **Một link sớm, trong 2–3 đoạn đầu**, trỏ tới bài nền tảng cho người mới.
- **Link ở đúng câu nhắc tới khái niệm**, ví dụ nhắc "Search Console" thì trỏ tới bài hướng dẫn Search Console.
- **Một link ở phần kết**, dẫn tới trang chủ đề hoặc trang dịch vụ để người đọc đi tiếp.
- **Không trỏ hai link khác nhau bằng cùng một chữ** trong một bài, người đọc sẽ rối.

### Link từ bài cũ sang bài mới

Đây là việc hay bị quên nhất. Bài mới đăng chỉ có link đi ra, chưa có link nào trỏ vào. Sau khi đăng, hãy tìm 2–3 bài cũ cùng chủ đề, nhất là bài đang có lượt hiển thị tốt trên Google, rồi chèn thêm một câu kèm link sang bài mới. Cách tìm nhanh: gõ `site:tênmiền.vn từ khóa` trên Google để xem những bài nào đang nói về chủ đề đó.

Bài [viết bài chuẩn SEO mà người đọc vẫn thích](/kien-thuc/viet-bai-chuan-seo-ma-nguoi-doc-van-thich/) có quy trình viết đầy đủ. Bước nối link nên được thêm vào cuối quy trình đó, như một việc bắt buộc trước khi xem là xong bài.

## Trang mồ côi, link chết và breadcrumb

**Trang mồ côi** (orphan page) là trang không có liên kết nội bộ nào trỏ tới. Trang này có thể vẫn nằm trong sitemap, nhưng Google xem nó ít quan trọng, còn người đọc thì gần như không tìm thấy. Trang mồ côi hay sinh ra khi gỡ bài khỏi menu, đổi danh mục hoặc đăng landing page chạy quảng cáo rồi quên.

**Link chết** (broken link) là link trỏ tới trang không còn tồn tại, trả lỗi 404. Link chết làm người đọc bực, làm Google tốn công thu thập vô ích. Nó hay xuất hiện khi đổi đường dẫn bài mà không đặt chuyển hướng, hoặc xóa sản phẩm hết hàng.

Cách xử lý:

- Đổi đường dẫn thì đặt chuyển hướng 301 từ cũ sang mới, rồi sửa luôn các link nội bộ trỏ thẳng tới đường dẫn mới, không để đi vòng qua chuyển hướng.
- Xóa trang thì tìm mọi link trỏ tới trang đó và sửa hoặc gỡ.
- Trang mồ côi còn giá trị thì thêm link từ trang chủ đề và vài bài liên quan. Trang không còn giá trị thì gộp vào trang khác hoặc gỡ hẳn.

**Breadcrumb** là dòng đường dẫn nhỏ phía trên trang, kiểu "Trang chủ › Kiến thức › Website chuẩn SEO › Tên bài". Nó là một dạng liên kết nội bộ tự động, nối bài lên trang chủ đề. Google Search Central có hướng dẫn đánh dấu breadcrumb bằng dữ liệu có cấu trúc BreadcrumbList. Từ tháng 1/2025, kết quả tìm kiếm trên điện thoại chỉ hiện tên miền thay cho breadcrumb, nhưng breadcrumb trên trang vẫn giúp Google hiểu thứ bậc và giúp khách đi lại.

## Công cụ kiểm tra liên kết nội bộ

| Công cụ | Xem được gì | Lưu ý |
| --- | --- | --- |
| Google Search Console, mục Liên kết | Trang được liên kết nội bộ nhiều nhất, trang được website khác trỏ tới | Miễn phí, dữ liệu từ chính Google |
| Screaming Frog SEO Spider | Link chết, chuyển hướng, số link trỏ vào mỗi trang, chữ gắn link | Có bản miễn phí giới hạn số URL quét mỗi lần, bản trả phí mở thêm tính năng |
| Sitemap so với kết quả quét | Trang có trong sitemap nhưng không ai trỏ link tới | Cách thủ công tìm trang mồ côi |

Trong **Google Search Console**, báo cáo Liên kết nằm ở menu bên trái. Phần liên kết nội bộ cho biết những trang nào được trỏ tới nhiều nhất. Nếu trang trụ cột hay trang sản phẩm chủ lực nằm tít dưới danh sách, đó là dấu hiệu cần thêm link. Cách cài và đọc các báo cáo khác có trong bài [Google Search Console: cài đặt và đọc báo cáo](/kien-thuc/google-search-console-cai-dat-va-doc-bao-cao/).

**Screaming Frog SEO Spider** là phần mềm cài trên máy tính, quét website giống cách Google thu thập. Theo trang giới thiệu của Screaming Frog, bản miễn phí có giới hạn số URL mỗi lần quét, đủ cho phần lớn website nhỏ. Anh chị kiểm tra con số giới hạn hiện hành trên trang của họ trước khi dùng. Sau khi quét, xem cột số link trỏ vào của từng trang và danh sách trang trả lỗi 4xx.

## Lỗi hay gặp khi làm liên kết nội bộ

Từ việc rà soát nhiều website doanh nghiệp, đội mình hay gặp các lỗi sau:

- **Chỉ nối link một chiều.** Bài mới trỏ ra bài cũ, nhưng không bài cũ nào trỏ lại.
- **Dồn hết link về trang chủ.** Trang chủ vốn đã có link từ mọi trang qua menu, link trong thân bài nên dành cho trang trụ cột và bài liên quan.
- **Dùng "xem thêm tại đây" khắp nơi.** Mất cơ hội giải thích trang đích cho Google.
- **Link tới trang đang chuyển hướng.** Đổi đường dẫn nhiều lần, link đi vòng qua hai ba bước mới tới trang thật.
- **Trang danh mục, trang chủ đề trống rỗng.** Chỉ có danh sách tiêu đề, không có đoạn giới thiệu, nên trang trụ cột không đủ sức làm trụ.
- **Gắn link vào nút chỉ chạy bằng JavaScript.** Người bấm được, nhưng Google không chắc đi theo được.

## Quy trình rà liên kết nội bộ mỗi tháng

Đội QHUB chạy quy trình này mỗi tháng cho mục Kiến thức. Website vài chục trang làm mất chừng một buổi.

1. **Lập danh sách bài mới trong tháng.** Với mỗi bài, chọn 2–3 bài cũ cùng chủ đề để chèn link trỏ sang.
2. **Mở báo cáo Liên kết trong Search Console.** Xem trang trụ cột và trang sản phẩm chủ lực có nằm trong nhóm được trỏ link nhiều không.
3. **Quét website bằng Screaming Frog.** Lọc link chết, chuyển hướng, trang có ít link trỏ vào.
4. **So sitemap với kết quả quét** để tìm trang mồ côi.
5. **Sửa theo thứ tự ưu tiên:** link chết trước, trang mồ côi còn giá trị sau, rồi tới bổ sung link cho bài mới.
6. **Ghi lại thay đổi** vào một bảng tính nhỏ để tháng sau đối chiếu.

## Việc cần làm ngay tuần này

- Mở Google Search Console, vào mục Liên kết, xem năm trang được liên kết nội bộ nhiều nhất có phải trang anh chị muốn lên top không.
- Chọn ba bài mới nhất, mỗi bài tìm hai bài cũ cùng chủ đề và chèn link sang.
- Rà lại chữ gắn link trong mười bài gần nhất, đổi hết "xem tại đây" thành chữ mô tả rõ trang đích.
- Quét website một lần bằng Screaming Frog và sửa mọi link chết.

Liên kết nội bộ không làm thứ hạng tăng vọt sau một đêm, nhưng làm đều mỗi tháng thì cả website khỏe lên. Các bài khác về SEO nằm trong chủ đề [Website chuẩn SEO](/kien-thuc/chu-de/website-seo/). Nếu anh chị cần một đội vận hành cả website lẫn gian hàng đa sàn, QHUB Commerce (qhub.com.vn) có đội media, đội vận hành sàn, đội KOC và đội host livestream để cùng làm.
