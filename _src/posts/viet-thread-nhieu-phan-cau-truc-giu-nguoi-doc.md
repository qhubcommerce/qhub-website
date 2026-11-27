---
title: "Viết thread nhiều phần: cấu trúc giữ người đọc"
slug: viet-thread-nhieu-phan-cau-truc-giu-nguoi-doc
topic: threads
keyword: "viết thread nhiều phần"
keywords: ["chuỗi bài threads", "cách nối bài trên threads", "mẫu thread nhiều phần", "đánh số bài threads"]
description: "Viết thread nhiều phần trên Threads: giới hạn 500 ký tự mỗi phần, cách nối bài, khung mở – thân – kết, 4 mẫu chuỗi và một chuỗi 7 phần viết sẵn cho shop."
date: 2026-11-28
updated: 2026-11-28
summary:
  - "Viết thread nhiều phần là chia một nội dung thành nhiều bài nối nhau, mỗi bài tối đa 500 ký tự, bài 1 làm móc, các bài giữa mỗi bài một ý, bài cuối tóm lại và mời người đọc làm một việc."
  - "Từ khoảng tháng 8–9/2025, Threads tự hiện bộ đếm vị trí trong chuỗi, nên đánh số tay như 1/7 không còn bắt buộc; đội QHUB vẫn ghi rõ số phần ở bài 1 để người đọc biết trước."
  - "Nội dung có nhiều bước, nhiều ý thì dùng chuỗi; một ý dài cần giải thích kỹ thì dùng văn bản đính kèm tới 10.000 ký tự (có từ 09/2025)."
  - "Bốn khung dễ dùng nhất cho shop: danh sách, kể chuyện, hướng dẫn từng bước và phân tích sai lầm; độ dài hợp lý là 4–8 phần."
faq:
  - q: "Mỗi phần trong thread nhiều phần trên Threads được viết bao nhiêu ký tự?"
    a: "Mỗi bài trên Threads giới hạn 500 ký tự, mỗi phần trong chuỗi cũng vậy. Với tiếng Việt, 500 ký tự là khoảng 80–110 chữ. Đội QHUB thường viết mỗi phần 250–450 ký tự để dễ đọc trên điện thoại."
  - q: "Có cần tự đánh số 1/7, 2/7 cho chuỗi bài Threads không?"
    a: "Không bắt buộc nữa. Theo Social Media Today và Social Samosa, từ khoảng tháng 8–9/2025 Threads tự hiện tổng số bài và vị trí của từng bài trong chuỗi. Đội QHUB vẫn ghi số phần ở bài 1, ví dụ «chuỗi 7 phần», để người lướt biết trước độ dài và quyết định đọc."
  - q: "Nên viết chuỗi nhiều phần hay dùng văn bản đính kèm?"
    a: "Nội dung có nhiều bước, mỗi bước đứng riêng được và cần ảnh minh họa thì dùng chuỗi. Một ý dài như bài phân tích hay hướng dẫn chi tiết thì dùng văn bản đính kèm tới 10.000 ký tự. Theo TechCrunch, phần đính kèm không được công cụ tìm kiếm lập chỉ mục, nên câu quan trọng nhất vẫn để ở bài chính."
  - q: "Một chuỗi bài Threads nên dài bao nhiêu phần?"
    a: "Đội QHUB thấy 4–8 phần là vừa với shop bán hàng. Ngắn hơn thì gộp lại thành một bài cho gọn. Dài hơn 8 phần thì người đọc dễ bỏ giữa chừng, nên tách thành hai chuỗi và hẹn phần sau."
  - q: "Có nên gắn link sản phẩm trong chuỗi bài nhiều phần?"
    a: "Có thể, nhưng chỉ ở bài cuối hoặc trong phần trả lời bên dưới, sau khi chuỗi đã cho người đọc đủ giá trị. Gắn link ngay bài 1 làm chuỗi trông như quảng cáo và người đọc dễ lướt qua. Một chuỗi chỉ nên có một lời mời rõ ràng."
sources:
  - title: "Attach Text to Your Threads Posts and Share Longer Perspectives – Meta Newsroom (09/2025)"
    url: "https://about.fb.com/news/2025/09/attach-text-threads-posts-share-longer-perspectives/"
  - title: "Threads challenges X by offering free support for up to 10K characters plus prominent links – TechCrunch (04/09/2025)"
    url: "https://techcrunch.com/2025/09/04/threads-challenges-x-by-offering-free-support-for-up-to-10k-characters-plus-prominent-links"
  - title: "Threads Adds Post Counter for Linked Updates – Social Media Today"
    url: "https://www.socialmediatoday.com/news/threads-adds-post-counter-for-longer-threads/757755/"
  - title: "Threads rolls out auto-added threads counter for posts – Social Samosa (09/2025)"
    url: "https://www.socialsamosa.com/news-2/threads-auto-added-counter-posts-10059350"
  - title: "Meta cải thiện cách hiển thị chuỗi bài đăng trên Threads – Báo Lao Động"
    url: "https://news.laodong.vn/cong-nghe/meta-cai-thien-cach-hien-thi-chuoi-bai-dang-tren-threads-1569961.ldo"
  - title: "Meta is fixing threads on Threads – Engadget (09/2025)"
    url: "https://www.engadget.com/social-media/meta-is-fixing-threads-on-threads-190123221.html"
  - title: "Threads now supports up to 20 photos or videos per post – Social Samosa"
    url: "https://www.socialsamosa.com/news-2/threads-supports-20-photos-videos-per-post-7078403"
  - title: "Text Attachments – Threads API, Meta for Developers"
    url: "https://developers.facebook.com/documentation/threads/create-posts/text-attachments"
---

**Viết thread nhiều phần là chia một nội dung thành nhiều bài nối nhau trên Threads, mỗi bài tối đa 500 ký tự: bài 1 làm móc để người lướt dừng lại, các bài giữa mỗi bài nói đúng một ý, bài cuối tóm lại và mời người đọc làm một việc cụ thể.** Chuỗi giữ được người đọc không nhờ viết dài, mà nhờ mỗi phần đều khiến họ muốn xem phần tiếp theo. Shop bán hàng dùng chuỗi rất hợp cho hướng dẫn, danh sách kinh nghiệm và chuyện hậu trường có nhiều bước.

Bài này đội QHUB đi sâu vào riêng chuỗi bài: tính năng, cách nối bài, khung mở – thân – kết, bốn mẫu khung và một chuỗi 7 phần viết sẵn. Cách viết một bài đơn có tương tác, anh chị xem bài [cách viết bài Threads được nhiều tương tác](/kien-thuc/cach-viet-bai-threads-duoc-nhieu-tuong-tac/). Thông tin tính năng tổng hợp đến 28/11/2026.

## Thread nhiều phần là gì, khi nào nên dùng?

**Thread nhiều phần** (còn gọi là chuỗi bài, bài nối) là một nhóm bài do cùng một tài khoản đăng, nối tiếp nhau dưới bài đầu tiên. Người xem thấy bài 1 trên bảng tin, bấm vào thì đọc tiếp các phần sau theo thứ tự.

Không phải nội dung nào cũng nên tách chuỗi. Threads có ba cách đăng nội dung dài ngắn khác nhau, mỗi cách hợp một việc:

| Cách đăng | Giới hạn | Hợp với nội dung | Không hợp với |
| --- | --- | --- | --- |
| Bài đơn | 500 ký tự | Một quan điểm, một câu hỏi, một mẹo nhỏ | Hướng dẫn có nhiều bước |
| Chuỗi nhiều phần | Mỗi phần 500 ký tự | Danh sách, các bước, câu chuyện có diễn biến, mỗi phần cần một ảnh | Một ý duy nhất bị kéo dài cho đủ số phần |
| Văn bản đính kèm | Tới 10.000 ký tự, có định dạng, từ 09/2025 | Bài phân tích, câu hỏi thường gặp, bản đầy đủ của một quy trình | Nội dung muốn người đọc trả lời từng ý |

Cách đội QHUB chọn: nội dung có từ 4 ý trở lên, mỗi ý đứng riêng được, thì viết chuỗi. Một ý cần giải thích kỹ thì dùng văn bản đính kèm. Viết gọn được trong 500 ký tự thì đừng tách.

## Threads hiện cho phép gì khi viết chuỗi bài?

Bảng dưới tổng hợp từ thông báo của Meta và các trang công nghệ, tính đến 28/11/2026. Giao diện có thể khác tùy phiên bản ứng dụng, anh chị kiểm tra lại trong app.

| Mục | Thông tin | Nguồn, thời điểm |
| --- | --- | --- |
| Độ dài mỗi bài | 500 ký tự, mỗi phần trong chuỗi cũng vậy | Meta, TechCrunch |
| Văn bản đính kèm | Tới 10.000 ký tự, có định dạng chữ đậm, nghiêng, link nổi bật | Meta Newsroom, 09/2025 |
| Bộ đếm trong chuỗi | Threads tự hiện tổng số bài và vị trí của từng bài, không cần đánh số tay | Social Media Today, Social Samosa, khoảng 08–09/2025 |
| Cách hiển thị chuỗi | Meta chỉnh lại giao diện để các bài nối của cùng tác giả hiện rõ hơn | Engadget (09/2025), Lao Động |
| Ảnh, video | Tối đa 20 ảnh hoặc video trong một bài | Social Samosa |
| Thẻ chủ đề | Mỗi bài gắn một thẻ chủ đề | Xem bài về topic tag |

Bộ đếm giúp người đọc biết chuỗi dài bao nhiêu, nhưng phần lớn người xem chỉ thấy bài 1. Còn theo TechCrunch, văn bản đính kèm không được công cụ tìm kiếm lập chỉ mục, nên nội dung muốn khách tìm qua Google vẫn cần bản đầy đủ trên website.

Cách gắn thẻ chủ đề cho bài 1 để chuỗi đến đúng người, anh chị xem bài [chủ đề (topic tag) trên Threads](/kien-thuc/chu-de-topic-tag-tren-threads/).

### Cách thêm bài vào chuỗi trên ứng dụng

Thao tác cơ bản trên điện thoại như sau. Tên nút có thể khác giữa các phiên bản và ngôn ngữ giao diện.

1. Bấm biểu tượng tạo bài mới, viết bài 1.
2. Ngay bên dưới khung soạn có dòng **Thêm vào thread** (Add to thread). Bấm vào để mở khung cho phần tiếp theo.
3. Viết phần 2, chèn ảnh nếu cần. Lặp lại cho đến phần cuối.
4. Đọc lại toàn bộ chuỗi trong khung soạn, rồi bấm Đăng. Cả chuỗi lên cùng lúc.

Đăng rồi mới nhớ ra cần thêm ý, anh chị có thể tự trả lời dưới bài cuối của mình và ghi rõ "bổ sung". Cách hiển thị phần trả lời này có thể khác phần soạn sẵn, nên tốt nhất là soạn đủ cả chuỗi ở ghi chú, đếm ký tự từng phần, rồi mới dán vào app.

## Cấu trúc viết thread nhiều phần: mở – thân – kết

| Khối | Số phần | Nhiệm vụ | Câu kiểm tra |
| --- | --- | --- | --- |
| Mở (bài 1) | 1 | Làm móc: nói rõ người đọc được gì, chuỗi dài mấy phần | Người lạ đọc riêng bài này có hiểu và muốn bấm vào không? |
| Thân | 3–6 | Mỗi phần một ý, một ví dụ hoặc một ảnh | Bỏ phần này đi, chuỗi có mất gì không? |
| Kết (bài cuối) | 1 | Tóm lại, kêu gọi một hành động | Người đọc biết bước tiếp theo phải làm gì chưa? |

### Bài 1 làm móc: hứa một điều cụ thể

**Móc** (hook) là câu hoặc bài mở đầu khiến người lướt dừng tay. Với chuỗi, bài 1 phải làm được ba việc trong vài câu:

- **Nói rõ lợi ích:** người đọc sẽ biết thêm gì, tránh được lỗi gì.
- **Cho thấy mình có quyền nói:** một chi tiết từ việc thật, như "sau ba mùa đóng gói hàng dễ vỡ".
- **Báo độ dài:** "chuỗi 7 phần", "6 lỗi, mình kể lần lượt bên dưới".

Đừng mở bằng "Hôm nay shop muốn chia sẻ một số kinh nghiệm…". Mở bằng việc đã xảy ra, như phần 1 của chuỗi mẫu bên dưới.

### Phần thân: mỗi phần một ý, đứng riêng được

Nguyên tắc quan trọng nhất của phần thân là **mỗi phần một ý**: câu đầu nói thẳng ý chính, hai ba câu sau giải thích hoặc đưa ví dụ, có thể kèm một ảnh đúng ý đó.

Viết sao cho ai đó đăng lại riêng phần 4 thì người đọc vẫn hiểu. Tránh câu kiểu "như đã nói ở trên". Thỉnh thoảng có thể kết bằng nửa câu dẫn sang phần sau, nhưng phần nào cũng treo lửng thì người đọc thấy bị dắt mũi.

### Bài cuối: tóm lại và một lời mời duy nhất

**CTA** (call to action, lời kêu gọi hành động) là câu mời người đọc làm một việc cụ thể. Bài cuối của chuỗi nên có hai thứ: tóm lại 2–3 ý chính trong một hai câu, và một CTA duy nhất.

CTA hợp với Threads thường là mời trò chuyện, không phải mời mua: "Anh chị đóng hàng dễ vỡ thế nào, kể mình nghe với". Muốn dẫn về sản phẩm thì đặt một link ở bài cuối hoặc phần trả lời, nói rõ link dẫn đi đâu. Cách gắn link không phiền người đọc có trong bài [bán hàng mềm trên Threads mà không bị ghét](/kien-thuc/ban-hang-mem-tren-threads-ma-khong-bi-ghet/).

### Đánh số và chèn ảnh thế nào?

Trước đây, người viết chuỗi phải tự ghi 1/7, 2/7 ở đầu mỗi phần. Từ khoảng tháng 8–9/2025, theo Social Media Today và Social Samosa, Threads tự hiện bộ đếm vị trí trong chuỗi. Đội QHUB hiện làm thế này:

- Ghi độ dài ở bài 1 bằng lời ("chuỗi 7 phần") để người lướt biết trước.
- Các phần sau không bắt buộc đánh số. Nếu app của anh chị chưa hiện bộ đếm, hoặc chuỗi là danh sách cần nhớ thứ tự, cứ ghi 2/7, 3/7 cho chắc.
- Không đánh số khi chưa chốt chuỗi. Thêm một phần giữa chừng là phải sửa lại mọi con số.

Về ảnh: không cần phần nào cũng có. Đội mình đặt ảnh ở bài 1 và ở 1–2 phần cần nhìn mới hiểu, như ảnh trước và sau. Ảnh thật chụp bằng điện thoại thường hợp với Threads hơn ảnh thiết kế bóng bẩy.

## Bốn mẫu khung viết thread nhiều phần cho shop

Bốn khung dưới đây là bốn cách sắp xếp mở – thân – kết, dùng lại được mãi.

| Khung | Bài 1 (móc) | Phần thân | Bài cuối | Hợp với shop khi |
| --- | --- | --- | --- | --- |
| Danh sách | "5 điều…", "7 câu khách hỏi nhiều nhất…" | Mỗi phần một điều, có ví dụ | Điều nào anh chị thấy đúng nhất? | Muốn được lưu lại, chia sẻ |
| Kể chuyện | Một khoảnh khắc giữa sự việc | Diễn biến theo thời gian, mỗi phần một mốc | Bài học, hỏi kinh nghiệm người đọc | Muốn người đọc tin và nhớ shop |
| Hướng dẫn từng bước | Kết quả người đọc sẽ làm được | Mỗi phần một bước, có ảnh | Tóm các bước, mời hỏi chỗ chưa rõ | Sản phẩm cần dùng đúng cách |
| Phân tích sai lầm | "Mình từng sai ở…", "Lỗi khiến đơn bị hoàn" | Mỗi phần một lỗi, nguyên nhân, cách sửa | Lỗi nào anh chị từng gặp? | Muốn thể hiện hiểu nghề |

Vài lưu ý: khung danh sách nên đặt ý mạnh ở phần 2, vì người đọc hay bỏ ở đó. Khung hướng dẫn nên mở mỗi phần bằng động từ ("Lót", "Gói", "Dán"). Khung phân tích sai lầm chỉ nói lỗi của chính mình, không chỉ trích shop khác hay khách. Khung kể chuyện chỉ kể chuyện có thật, mỗi phần một chi tiết cụ thể; bài [kể chuyện nghề trên Threads](/kien-thuc/ke-chuyen-nghe-tren-threads-chan-that-thang-hoanh-trang/) có khung bốn phần cho từng bài kể.

### Ví dụ khung kể chuyện: chiếc hộp của QHUB HERBAL

Đây là khung 5 phần đội QHUB có thể kể về việc làm hộp cho [QHUB HERBAL](/qhub-herbal.html), thương hiệu trà túi lọc do chính đội xây. Chỉ kể quy trình, không kể số bán, không nói công dụng sản phẩm.

| Phần | Ý chính | Chi tiết thật nên có |
| --- | --- | --- |
| 1 | Một đội vận hành sàn tự làm hộp cho trà của mình | Mỗi vị một hộp riêng, cùng bố cục, khác màu chủ đạo |
| 2 | Bản khai triển: hộp phẳng trước khi gấp | File khai triển và đường khuôn bế, phải khớp kích thước thật của hộp |
| 3 | Lớp ép nhũ tách riêng | Phần ép nhũ làm thành một file vector riêng để xưởng in làm khuôn |
| 4 | Mặt sau là phần khó nhất | Thành phần, khối lượng tịnh, số tự công bố, mã vạch phải đủ và đọc được |
| 5 | Bài học và câu hỏi | Duyệt hộp trên ảnh nhỏ như ảnh bìa sàn; hỏi người đọc khâu nào họ thấy khó |

## Ví dụ một chuỗi 7 phần viết sẵn cho shop bán hàng

Dưới đây là chuỗi mẫu theo khung danh sách, cho một **shop gốm giả định** bán cốc, đĩa làm quà. Các chi tiết là ví dụ giả định, anh chị thay bằng kinh nghiệm thật của shop mình. Mỗi phần dưới 500 ký tự.

> **Phần 1.** Đơn cốc gốm đầu tiên của shop đến tay khách thì vỡ quai. Từ đó tụi mình đổi cách đóng gói nhiều lần, và rút ra 5 điều nên biết trước khi chọn cốc gốm làm quà. Chuỗi 7 phần, mình kể lần lượt bên dưới.

> **Phần 2.** Điều 1: hỏi dung tích trước, đừng chỉ nhìn ảnh. Cốc trong ảnh chụp cận trông to hơn thật. Người uống cà phê sữa đá cần cốc lớn, người uống trà nóng lại thích cốc nhỏ cầm vừa tay. Tụi mình luôn ghi dung tích và chụp thêm một ảnh cốc đặt cạnh bàn tay.

> **Phần 3.** Điều 2: hỏi cốc có dùng được lò vi sóng và máy rửa bát không. Cốc có viền vàng, viền nhũ thường không nên cho vào lò vi sóng. Shop nào cũng nên ghi rõ điều này ở trang sản phẩm, đừng để khách phải đoán.

> **Phần 4.** Điều 3: men thủ công thì mỗi chiếc mỗi khác. Vệt men, chấm nhỏ là đặc điểm của gốm làm tay chứ không phải lỗi. Nhưng shop phải nói trước, kèm ảnh thật của nhiều chiếc, để khách nhận hàng không thấy hụt hẫng.

> **Phần 5.** Điều 4: hỏi shop đóng gói thế nào. Cách tụi mình đang dùng: lót đáy hộp, quấn từng chiếc, nhét kín lòng cốc, chèn đầy khoảng trống để lắc không kêu. Ảnh bên dưới là một hộp trước khi dán băng keo.

> **Phần 6.** Điều 5: hỏi chính sách khi hàng vỡ lúc giao. Cần quay video khi mở hộp không, báo trong bao lâu, đổi mới hay hoàn tiền. Nói rõ từ đầu thì cả shop và khách đều yên tâm.

> **Phần 7.** Tóm lại: hỏi dung tích, cách dùng, đặc điểm men, cách đóng gói và chính sách hàng vỡ. Năm câu này giúp món quà đến tay người nhận nguyên vẹn. Anh chị từng nhận món quà gốm nào bị vỡ chưa? Kể tụi mình nghe với. Ai cần bảng câu hỏi này để hỏi shop, lưu chuỗi lại nhé.

Chuỗi này giữ người đọc vì bài 1 có tình huống thật, lời hứa và độ dài; mỗi phần thân mở bằng "Điều 1, Điều 2…" để đọc lướt vẫn theo kịp; ảnh đặt đúng phần cần nhìn; bài cuối không có giá, không có link. Ai hỏi mua ở đâu, shop trả lời trong bình luận.

## Lỗi hay gặp và kinh nghiệm thực tế từ đội vận hành

Những lỗi đội QHUB gặp nhiều nhất, kể cả lỗi của chính đội mình:

- **Bài 1 không đứng riêng được.** Mở bằng "Thread về đóng gói" rồi để hết thông tin xuống dưới. Người lướt không biết vì sao phải bấm.
- **Kéo một ý thành bảy phần.** Mỗi phần chỉ một câu, đọc rất mệt. Nội dung chỉ có 2–3 ý thì viết một bài đơn.
- **Nhồi CTA khắp nơi.** Phần nào cũng "inbox shop", "link ở bio". Chuỗi biến thành tờ rơi.
- **Đánh số trước, sửa nội dung sau.** Thêm một phần mà quên sửa số, chuỗi thành 1/6 rồi 3/6. Chốt nội dung rồi mới đánh số, hoặc để Threads tự đếm.
- **Trượt sang khen công dụng.** Kể chuyện làm thực phẩm, mỹ phẩm thì chỉ kể quy trình, hương vị, cách dùng; không khẳng định sản phẩm chữa được bệnh.

Một vài kinh nghiệm đội mình giữ lại:

- **Đăng chuỗi vào ngày có người ngồi trực.** Mỗi phần là một chỗ để người đọc trả lời, nên cần 1–2 giờ đầu ngồi trò chuyện.
- **Tối đa một chuỗi mỗi tuần với đội nhỏ.** Phần còn lại là bài đơn, hỏi ý kiến, hậu trường.
- **Đo chuỗi bằng tỷ lệ, không bằng lượt xem.** Đội QHUB so lượt trả lời và người theo dõi mới trên 1.000 lượt xem của chuỗi với bài đơn cùng tuần. Cách tính có trong bài [đọc số liệu Threads](/kien-thuc/doc-so-lieu-threads/). Nếu lượt xem các phần sau tụt mạnh so với bài 1, xem lại phần 2: đó thường là chỗ người đọc bỏ đi.

## Việc cần làm ngay tuần này

- Chọn một nội dung có từ 4 ý trở lên mà khách hay hỏi shop: cách chọn, cách dùng, cách bảo quản, lỗi hay gặp.
- Chọn một trong bốn khung: danh sách, kể chuyện, hướng dẫn từng bước hoặc phân tích sai lầm.
- Soạn chuỗi 5–7 phần ở ghi chú trước. Viết bài 1 sau cùng, khi đã biết chuỗi có gì hay nhất.
- Đếm ký tự từng phần, chèn 1–2 ảnh thật, chốt nội dung rồi mới đánh số nếu cần.
- Đăng vào ngày có người trực, trả lời bình luận trong 1–2 giờ đầu, cuối tuần so tỷ lệ trả lời của chuỗi với bài đơn.

QHUB Commerce (qhub.com.vn) vận hành gian hàng đa sàn, có đội media, đội vận hành sàn, đội KOC và đội host livestream.
