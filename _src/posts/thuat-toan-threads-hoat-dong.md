---
title: "Thuật toán Threads hoạt động thế nào"
slug: thuat-toan-threads-hoat-dong
topic: threads
keyword: "thuật toán threads"
keywords: ["threads xếp hạng bài viết", "bảng tin dành cho bạn threads", "dear algo threads", "tăng tiếp cận threads"]
description: "Thuật toán Threads xếp bài thế nào: 3 bước Meta công bố, bảng tín hiệu xếp hạng, các thay đổi 2024–2026 và việc thương hiệu nên làm để được đề xuất."
date: 2026-11-15
updated: 2026-11-15
summary:
  - "Theo Meta, bảng tin Dành cho bạn của Threads do một hệ thống AI gồm nhiều mô hình học máy xếp hạng; bảng tin Đang theo dõi thì xếp theo thời gian đăng."
  - "Hệ thống dự đoán khả năng người xem thích bài, mở xem trả lời, bấm vào trang cá nhân, theo dõi tác giả hay lướt qua, rồi bài nào được dự đoán có giá trị hơn sẽ đứng cao hơn."
  - "Meta không công bố trọng số của từng tín hiệu. Mọi con số kiểu “trả lời tăng x% tiếp cận” trên mạng đều là quan sát của bên thứ ba, không phải số liệu chính thức."
  - "Từ 2024 đến 2026, Threads ưu tiên lại bài của tài khoản đang theo dõi, xếp hạng link đúng hơn, thêm thẻ chủ đề, cộng đồng và cho người dùng tự chỉnh bảng tin bằng Dear Algo, Your Algo."
faq:
  - q: "Thuật toán Threads ưu tiên điều gì nhất?"
    a: "Meta không xếp thứ tự ưu tiên công khai. Theo trang giải thích xếp hạng của Meta, hệ thống dự đoán bài nào có giá trị nhất với từng người, dựa trên khả năng họ thích, mở xem trả lời, bấm vào trang cá nhân, theo dõi tác giả hoặc lướt qua. Trên thực tế, bài khơi được trò chuyện thật thường đi xa hơn."
  - q: "Bài Threads có link có bị giảm tiếp cận không?"
    a: "Meta chưa từng nói có “phạt” link. Tháng 6/2025, Adam Mosseri (người đứng đầu Instagram) cho biết đội Threads đã làm việc để link được xếp hạng đúng và link hoạt động tốt hơn từ hơn một tháng trước đó. Dù vậy, người dùng Threads ít bấm link, nên bài có link vẫn cần nội dung đủ hay ngay trong bài."
  - q: "Dear Algo và Your Algo là gì, đã dùng được ở Việt Nam chưa?"
    a: "Dear Algo (ra mắt 11/02/2026) cho người dùng đăng công khai một bài bắt đầu bằng “Dear Algo” để yêu cầu xem nhiều hoặc ít một chủ đề trong 3 ngày. Your Algo (16/06/2026) làm việc tương tự nhưng riêng tư, chọn 1, 3 hoặc 7 ngày. Khi công bố, cả hai chỉ có ở một số nước như Mỹ, Anh, Úc, New Zealand (Your Algo thêm Canada), chưa có Việt Nam; anh chị kiểm tra lại trong ứng dụng."
  - q: "Thẻ chủ đề có giúp bài Threads được đề xuất nhiều hơn không?"
    a: "Meta cho biết dữ liệu nội bộ của họ cho thấy bài có gắn chủ đề nhận được nhiều lượt xem hơn, nhưng không công bố mức chênh lệch. Mỗi bài chỉ gắn được một thẻ chủ đề, nên hãy chọn thẻ sát với nội dung và với nhóm khách mình muốn tiếp cận."
  - q: "Đăng nhiều bài mỗi ngày có làm tài khoản Threads bị giảm tiếp cận không?"
    a: "Meta không công bố giới hạn số bài hay hình phạt cho việc đăng nhiều. Kinh nghiệm của đội QHUB là 1–2 bài chất lượng mỗi ngày kèm thời gian trả lời bình luận hiệu quả hơn đăng dày mà bỏ mặc phần trò chuyện."
sources:
  - title: "Instagram Threads Feed AI system – Meta Transparency Center"
    url: "https://transparency.meta.com/features/explaining-ranking/ig-threads-feed/"
  - title: "Control Your Threads Feed With New Dear Algo Feature – Meta Newsroom (11/02/2026)"
    url: "https://about.fb.com/news/2026/02/threads-dear-algo/"
  - title: "New Threads Features for a More Personalized Experience That You Control – Meta Newsroom (2025, cập nhật 30/10/2025)"
    url: "https://about.fb.com/news/2025/03/new-threads-features-more-personalized-experience-you-control/"
  - title: "Threads adjusts its algorithm to show you more content from accounts you follow – TechCrunch (21/11/2024)"
    url: "https://techcrunch.com/2024/11/21/threads-adjusts-its-algorithm-to-show-you-more-content-from-accounts-you-follow"
  - title: "Threads adds new personalization and community features as it reaches 500M monthly users – TechCrunch (16/06/2026)"
    url: "https://techcrunch.com/2026/06/16/threads-adds-new-personalization-and-community-features-as-it-reaches-500m-monthly-users/"
  - title: "Meta says link posts are being ranked properly on Threads – Social Media Today (06/2025)"
    url: "https://www.socialmediatoday.com/news/meta-says-link-posts-ranked-properly-threads-reach/750126/"
  - title: "Threads reaches 150 million daily users – Social Media Today (29/10/2025)"
    url: "https://www.socialmediatoday.com/news/threads-reaches-150-million-daily-users-more-ad-options/804213/"
---

**Thuật toán Threads là một hệ thống AI của Meta, gồm nhiều mô hình học máy chạy cùng nhau, dự đoán mỗi bài viết có giá trị với từng người xem đến đâu rồi xếp bài đó lên cao hay xuống thấp trong bảng tin Dành cho bạn.** Hệ thống dựa vào những việc người xem có khả năng làm với bài: thích, mở xem trả lời, bấm vào trang cá nhân, theo dõi tác giả, hay lướt qua luôn. Meta có công bố cách hệ thống vận hành, nhưng không công bố trọng số của từng tín hiệu.

Trên mạng có rất nhiều "công thức thuật toán Threads" kèm con số phần trăm, phần lớn là quan sát của bên thứ ba chứ không phải số liệu từ Meta. Bài này đội QHUB tách rõ hai phần: **điều Meta chính thức nói** (có nguồn, có mốc thời gian) và **điều là kinh nghiệm vận hành**. Thông tin được tổng hợp đến ngày 15/11/2026.

Nếu anh chị mới bắt đầu, nên đọc trước bài [Threads là gì và doanh nghiệp có nên dùng năm 2026](/kien-thuc/threads-la-gi-va-doanh-nghiep-co-nen-dung-nam-2026/) để nắm nền tảng.

## Thuật toán Threads là gì? Hai bảng tin, hai cách xếp

Khi mở Threads, người dùng có hai bảng tin chính, và mỗi bảng xếp bài theo một cách khác nhau:

- **Dành cho bạn (For You):** bảng tin mặc định, do hệ thống AI của Meta chọn và xếp hạng. Ở đây có cả bài của tài khoản mình đang theo dõi lẫn bài được đề xuất từ tài khoản lạ. Khi người ta nói "thuật toán Threads", gần như là đang nói về bảng tin này.
- **Đang theo dõi (Following):** chỉ hiện bài của những tài khoản mình theo dõi, xếp theo thời gian đăng, bài mới nhất ở trên.

Ngoài ra, Threads có bảng tin tùy chỉnh (custom feed) theo chủ đề hoặc nhóm tài khoản. Từ năm 2025, người dùng có thể chọn bảng tin nào hiện ra mặc định khi mở ứng dụng.

Ý nghĩa với thương hiệu: người đã theo dõi anh chị vẫn có thể thấy bài qua bảng Đang theo dõi, nhưng phần lớn **tiếp cận mới** (người chưa biết thương hiệu) đến từ bảng Dành cho bạn. Muốn được đề xuất tới người lạ thì phải hiểu cách bảng tin này chọn bài.

## Thuật toán Threads xếp bài qua những bước nào?

Meta có một trang riêng giải thích hệ thống AI xếp hạng bảng tin Threads trên Trung tâm minh bạch (Transparency Center). Tóm lại bằng lời của mình, quy trình có ba bước.

### Bước 1: gom "kho" bài có thể hiển thị

Hệ thống nhìn vào toàn bộ bài có thể đưa vào bảng tin của một người: bài từ tài khoản họ theo dõi và bài từ tài khoản họ chưa theo dõi. Chỉ những bài chữ, ảnh, video đáp ứng quy định về chất lượng và tính toàn vẹn của Meta mới được đưa vào xếp hạng. Bài vi phạm tiêu chuẩn cộng đồng hoặc không đủ điều kiện đề xuất sẽ bị loại hoặc bị hạn chế ngay từ bước này.

Lưu ý: đăng bài không có nghĩa toàn bộ người theo dõi sẽ thấy ngay.

### Bước 2: dự đoán hành động của người xem

Với từng bài, hệ thống dự đoán xác suất người xem sẽ:

- thích bài;
- bấm mở để xem các trả lời;
- bấm vào trang cá nhân của tác giả;
- theo dõi tác giả;
- lướt qua bài (tín hiệu không tích cực).

Để dự đoán, hệ thống dùng nhiều tín hiệu đầu vào, ví dụ lịch sử tương tác của người xem với tác giả và với các chủ đề tương tự, việc họ gần đây có bấm vào trang cá nhân của tác giả không, có xem trang Instagram của tác giả không.

### Bước 3: xếp hạng theo giá trị dự đoán

Các dự đoán được gộp lại thành một điểm. Theo cách Meta diễn đạt, bài mà hệ thống dự đoán mang lại nhiều giá trị hơn cho người xem sẽ đứng cao hơn trong bảng tin. Meta không công bố công thức gộp, cũng không nói hành động nào nặng ký hơn hành động nào.

Người xem cũng tác động trực tiếp lên kết quả: bỏ theo dõi, tắt tiếng, ẩn bài, báo cáo bài, dùng bộ lọc từ ẩn (Hidden Words). Mỗi thao tác này là một tín hiệu cho hệ thống biết họ không muốn xem gì.

## Bảng tín hiệu xếp hạng và việc thương hiệu nên làm

Bảng dưới gom các tín hiệu đã được Meta hoặc lãnh đạo Threads nói công khai, kèm việc nên làm tương ứng. Cột "việc nên làm" là kinh nghiệm của đội QHUB, không phải hướng dẫn chính thức.

| Tín hiệu | Meta nói gì (nguồn, mốc) | Việc thương hiệu nên làm |
| --- | --- | --- |
| Khả năng thích bài | Một trong các dự đoán chính (Transparency Center) | Mỗi bài một ý rõ, câu đầu chạm đúng nỗi lo của khách |
| Khả năng mở xem trả lời | Một trong các dự đoán chính (Transparency Center) | Kết bài bằng câu hỏi dễ trả lời; trả lời bình luận nhanh để chuỗi trò chuyện dài ra |
| Khả năng bấm vào trang cá nhân, theo dõi tác giả | Một trong các dự đoán chính (Transparency Center) | Ảnh đại diện, tiểu sử, bài ghim cho biết ngay thương hiệu làm gì, vì sao nên theo dõi |
| Lướt qua bài | Tín hiệu không tích cực (Transparency Center) | Bỏ phần chào hỏi dài dòng, không mở bài bằng giá và hotline |
| Bài từ tài khoản đang theo dõi | Mosseri cân bằng lại xếp hạng để ưu tiên bài từ người mình theo dõi (21/11/2024) | Xây tệp người theo dõi thật, đúng khách hàng mục tiêu |
| Thẻ chủ đề | Dữ liệu nội bộ Meta cho thấy bài có chủ đề được xem nhiều hơn, không công bố mức chênh (2025) | Chọn 2–3 chủ đề cố định; mỗi bài gắn một thẻ sát nội dung |
| Link trong bài | Mosseri: đã làm để link được xếp hạng đúng, link chạy tốt hơn (06/2025) | Gắn link khi thật sự hữu ích; bài vẫn phải tự đứng được khi không ai bấm |
| Hoạt động trên Instagram | Lãnh đạo Threads cho biết hoạt động Instagram nay đóng vai trò nhỏ hơn trong đề xuất (10/2025) | Không trông chờ tệp Instagram; xây tương tác ngay trên Threads |
| Lựa chọn chủ động của người xem | Ẩn, tắt tiếng, báo cáo, Dear Algo, Your Algo | Tránh nội dung gây khó chịu; nói đúng chủ đề người theo dõi chờ đợi |

Hai điều cần nhớ khi đọc bảng. Thứ nhất, Meta liệt kê **loại** tín hiệu chứ không cho biết **mức độ**. Thứ hai, thuật toán Threads được điều chỉnh liên tục, nên bảng này đúng với các công bố đến 15/11/2026.

## Thuật toán Threads đã thay đổi thế nào từ 2023 đến 2026?

Các mốc dưới đây cho thấy Threads đang đi từ một bảng tin đầy bài lạ sang ưu tiên trò chuyện, chủ đề, cộng đồng và cho người dùng quyền chỉnh bảng tin.

| Thời điểm | Thay đổi | Ý nghĩa với thương hiệu |
| --- | --- | --- |
| 12/2023 | Ra mắt thẻ chủ đề (tag), mỗi bài chỉ một thẻ. Mosseri nói muốn thẻ xoay quanh cộng đồng hơn là "hack" tương tác | Không nhồi thẻ; chọn đúng một chủ đề |
| 21/11/2024 | Cân bằng lại xếp hạng, ưu tiên bài từ tài khoản đang theo dõi. Mosseri cảnh báo tiếp cận tới người lạ có thể giảm, tiếp cận tới người theo dõi tăng | Người theo dõi thật quan trọng hơn lượt xem nhất thời |
| 2025 | Gắn tối đa 10 chủ đề lên hồ sơ; thẻ chủ đề hiện rõ hơn trên bảng Dành cho bạn; chọn bảng tin tùy chỉnh làm mặc định | Hồ sơ nên khai rõ các chủ đề thương hiệu theo đuổi |
| 15/05/2025 | Gắn tối đa 5 link ở tiểu sử; thống kê lượt bấm link; báo cáo tổng kết tuần | Đo được Threads kéo bao nhiêu người về website, gian hàng |
| 06/2025 | Mosseri cho biết link được xếp hạng đúng hơn | Có thể dùng link vừa phải, không cần né hoàn toàn |
| 22/07/2025 | Thống kê nơi bài được khám phá; bài đủ điều kiện có thể được đề xuất cho người dùng Instagram và Facebook | Một bài Threads tốt có thể đi ra ngoài Threads |
| 30/10/2025 | Duyệt trả lời trước khi hiện công khai, lọc trả lời | Kiểm soát được bình luận xấu, spam dưới bài |
| 10/2025 | Meta báo khoảng 150 triệu người dùng hằng ngày; hoạt động Instagram giảm vai trò trong đề xuất | Tương tác ngay trên Threads quyết định nhiều hơn |
| 11/02/2026 | Dear Algo: đăng công khai để yêu cầu xem nhiều hoặc ít một chủ đề trong 3 ngày (Mỹ, Anh, Úc, New Zealand) | Người xem chủ động chọn chủ đề; nội dung lạc đề càng khó được đề xuất |
| 16/06/2026 | 500 triệu người dùng hằng tháng; Your Algo chỉnh bảng tin riêng tư 1, 3 hoặc 7 ngày; Cộng đồng ra khỏi giai đoạn thử nghiệm | Tham gia đúng cộng đồng ngành là một đường tiếp cận mới |

Khi công bố, Dear Algo và Your Algo chưa có ở Việt Nam; anh chị kiểm tra lại trong ứng dụng.

## Những điều Meta chưa bao giờ nói về thuật toán Threads

Nhiều lời khuyên trên mạng nghe hợp lý nhưng không có nguồn chính thức:

- **"Trả lời bình luận tăng x% tiếp cận."** Meta không công bố con số nào như vậy. Điều Meta nói là hệ thống dự đoán khả năng người xem mở xem trả lời. Nghĩa là bài có trò chuyện sống động thì có lợi, nhưng mức lợi bao nhiêu thì không ai ngoài Meta biết.
- **"Có giờ vàng 30 phút đầu."** Không có công bố chính thức về khung thời gian cố định. Việc bài mới thường được thử với một nhóm người trước là quan sát phổ biến, chưa phải tài liệu của Meta.
- **"Link bị phạt."** Như đã nói, Mosseri cho biết đội Threads làm để link được xếp hạng đúng. Bài có link ít tương tác thường vì người đọc ngại rời ứng dụng, không hẳn vì bị phạt.
- **"Đăng quá 3 bài một ngày sẽ bị bóp."** Không có giới hạn công khai nào như vậy.

Gặp mẹo "thuật toán" nào, hãy hỏi: ai nói, nói lúc nào, có nguồn của Meta không. Không có thì xem đó là giả thuyết để thử.

## Kinh nghiệm thực tế từ đội vận hành

Phần này là quan sát của đội QHUB khi làm nội dung Threads cho thương hiệu, không phải công bố của Meta. Anh chị nên thử trên tài khoản của mình và đo lại.

**Câu đầu quyết định có bị lướt qua hay không.** Vì "lướt qua" là tín hiệu không tích cực, bài mở đầu bằng lời chào, giới thiệu công ty hay giá khuyến mãi thường chết rất sớm. Bài mở bằng một quan sát cụ thể, một câu hỏi chạm nỗi lo hoặc một con số từ chính công việc thường giữ người đọc tốt hơn. Cách viết chi tiết có trong bài [cách viết bài Threads được nhiều tương tác](/kien-thuc/cach-viet-bai-threads-duoc-nhieu-tuong-tac/).

**Trò chuyện thật giữ bài sống lâu hơn.** Bài có nhiều người trả lời qua lại, và tác giả tham gia trả lời, thường còn được đẩy sau nhiều giờ. Đội mình hay dành 15–20 phút sau khi đăng để trả lời từng bình luận bằng câu có nội dung, không trả lời rập khuôn.

**Hồ sơ là nơi chuyển lượt xem thành người theo dõi.** Hệ thống dự đoán cả khả năng bấm vào trang cá nhân và theo dõi. Khi người lạ bấm vào, họ cần thấy ngay: tài khoản này nói về gì, đăng đều không, có đáng theo dõi không.

**Đều chủ đề quan trọng hơn bắt trend.** Tài khoản nói chuyện xoay quanh 2–3 chủ đề rõ ràng thường được đề xuất đúng người hơn tài khoản hôm nay bàn bóng đá, mai bàn tài chính, mốt quay sang bán hàng. Điều này càng đúng khi người xem có thể chủ động chọn chủ đề bằng Dear Algo, Your Algo.

**Tài khoản người thật thường được quan tâm hơn tài khoản thương hiệu.** Chủ doanh nghiệp hay người làm nghề chia sẻ chân thật thường nhận nhiều trả lời hơn một trang thương hiệu nói giọng thông cáo.

**Instagram vẫn có ích, nhưng không còn là "đòn bẩy" như trước.** Lãnh đạo Threads đã nói hoạt động Instagram giảm vai trò trong đề xuất. Thương hiệu có Instagram mạnh vẫn có lợi thế ban đầu về người theo dõi, nhưng tương tác trên Threads mới là thứ giữ tiếp cận. Anh chị xem thêm bài [phát triển Instagram cho thương hiệu năm 2026](/kien-thuc/phat-trien-instagram-cho-thuong-hieu-nam-2026/) để hai kênh hỗ trợ nhau.

## Lỗi hay gặp khi cố "chiều" thuật toán Threads

- **Câu mồi tương tác.** "bình luận một chữ để nhận quà", "thả tim nếu đồng ý" có thể kéo lượt bấm trong ngắn hạn, nhưng tạo ra trò chuyện rỗng và dễ khiến người xem ẩn bài. Meta nhiều lần nói muốn thẻ chủ đề và bảng tin phục vụ cộng đồng chứ không phục vụ "hack" tương tác.
- **Gắn thẻ chủ đề đang nóng nhưng không liên quan.** Bài đến tay người không quan tâm, họ lướt qua, và đó chính là tín hiệu không tích cực.
- **Mua người theo dõi, mua tương tác ảo, dùng nhóm "đổi tương tác".** Vi phạm quy định của Meta, làm tệp người theo dõi lệch khỏi khách hàng thật, về lâu dài còn kéo tiếp cận xuống.
- **Chỉ nhìn lượt xem.** Bài nhiều lượt xem từ người lạ nhưng không ai theo dõi, không ai bấm link thì chưa giúp gì cho kinh doanh.

## Đọc số liệu để biết thuật toán có đang đẩy bài của mình không

Từ giữa năm 2025, phần thống kê (Insights) của Threads đã chi tiết hơn: báo cáo tuần so sánh số bài, lượt xem, người theo dõi mới và lượt trả lời; xem được lượt bấm link; xem bài được khám phá ở đâu, kể cả trên ứng dụng khác của Meta. Đội mình đọc theo bảng nhỏ này mỗi tuần:

| Dấu hiệu trong Insights | Có thể đang xảy ra | Nên chỉnh gì |
| --- | --- | --- |
| Lượt xem cao, trả lời thấp | Câu mở hút nhưng bài không mời được trò chuyện | Kết bài bằng câu hỏi cụ thể, dễ trả lời |
| Trả lời nhiều, lượt xem thấp | Bài hay nhưng chưa được đề xuất rộng | Gắn thẻ chủ đề sát hơn, đăng vào giờ người theo dõi hoạt động |
| Lượt xem cao, ít người theo dõi mới | Người lạ thấy bài nhưng hồ sơ chưa thuyết phục | Sửa tiểu sử, ghim bài giới thiệu rõ giá trị |
| Lượt bấm link gần như bằng 0 | Link chưa liên quan hoặc bài chưa tạo lý do để bấm | Chỉ gắn link vào bài hướng dẫn, nói rõ bấm vào sẽ được gì |

Sau 4–6 tuần, anh chị sẽ thấy dạng bài nào hợp với tệp của mình. Đó mới là "thuật toán" đáng tin nhất: số liệu của chính tài khoản.

## Việc cần làm ngay tuần này

1. Kiểm tra hồ sơ Threads: tiểu sử nói rõ thương hiệu làm gì, có link, có bài ghim, gắn các chủ đề thương hiệu theo đuổi.
2. Chọn 2–3 chủ đề cố định và dùng đúng một thẻ chủ đề sát nội dung cho mỗi bài.
3. Viết lại câu đầu của 5 bài sắp đăng để không ai phải lướt qua phần chào hỏi.
4. Đặt lịch 15–20 phút sau mỗi bài để trả lời bình luận, và 10 phút mỗi ngày trả lời bài của người khác trong ngành.
5. Cuối tuần mở Insights, ghi lại lượt xem, trả lời, người theo dõi mới, lượt bấm link, đối chiếu với bảng ở trên.

Các bài khác trong chủ đề [phát triển Threads](/kien-thuc/chu-de/threads/) sẽ đi sâu vào lịch đăng, thẻ chủ đề và bán hàng mềm. QHUB Commerce (qhub.com.vn) là đơn vị vận hành gian hàng đa sàn, có đội media, đội vận hành sàn, đội KOC và đội host livestream, nên đội mình xem Threads như một mắt xích để lắng nghe khách và thử ý tưởng trước khi đưa lên video, livestream.
