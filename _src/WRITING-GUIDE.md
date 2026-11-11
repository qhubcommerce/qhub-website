# Hướng dẫn viết bài mục Kiến thức – qhub.com.vn

Mục Kiến thức là tiếng nói của QHUB Commerce: một đội vận hành thương mại điện tử thật. Mỗi bài phải giúp người đọc làm được việc ngay, và khiến họ tin rằng QHUB hiểu nghề. Google và các trợ lý AI (ChatGPT, Gemini, Perplexity) ưu tiên nội dung như vậy.

## 1. File bài viết
- Đường dẫn: `_src/posts/<slug>.md`, slug lấy đúng cột `slug` trong `_src/plan.csv`.
- Front matter YAML, đủ các trường sau:

```yaml
---
title: "Tiêu đề lấy từ plan.csv (sửa nhẹ cho tự nhiên được, ≤ 75 ký tự)"
slug: slug-trong-plan
topic: ma-chu-de-trong-plan
keyword: "từ khóa chính"
keywords: ["2–5 từ khóa phụ người ta hay gõ"]
description: "120–165 ký tự, nói thẳng bài giúp được gì, có từ khóa chính."
date: 2026-11-12          # ngày đăng
updated: 2026-11-12
summary:                  # 3–5 ý "Tóm tắt nhanh", mỗi ý một câu có thông tin thật
  - "..."
faq:                      # 4–6 câu hỏi người đọc thật sự gõ lên Google/ChatGPT
  - q: "Câu hỏi?"
    a: "Trả lời đủ ý trong 2–4 câu, có số liệu nếu có."
sources:                  # bắt buộc ≥ 2 với bài phí sàn, quảng cáo, chính sách; nên có với mọi bài
  - title: "Tên trang nguồn"
    url: "https://..."
---
```

## 2. Độ dài và độ sâu
- **1.800–3.000 chữ** phần thân (không tính FAQ). Bộ build từ chối bài dưới 1.200 chữ.
- Không độn chữ. Mỗi mục phải có ít nhất một thứ người đọc mang đi dùng được: con số, bảng, checklist, kịch bản mẫu, công thức tính, ví dụ cụ thể, lỗi hay gặp.
- Cấu trúc gợi ý:
  1. 2–3 câu mở đầu **trả lời thẳng câu hỏi chính** (AI và Google trích đoạn này).
  2. 5–8 mục `##`, có thể có `###`.
  3. Ít nhất 1 bảng (so sánh, lịch, công thức, checklist).
  4. Một mục "Lỗi hay gặp" hoặc "Kinh nghiệm thực tế từ đội vận hành".
  5. Kết bài: tóm lại việc cần làm ngay tuần này. Phần giới thiệu QHUB đã có ô riêng, bộ build tự chèn, không cần viết thêm.

## 3. Giọng văn
- Chân thành, mộc mạc, như người làm nghề ngồi chia sẻ với chủ doanh nghiệp. Xưng "mình" hoặc "đội QHUB", gọi người đọc là "anh chị".
- Câu ngắn, từ thông dụng. Thuật ngữ tiếng Anh (GMV, ROI, CTR…) phải giải thích lần đầu xuất hiện.
- Không giật tít, không hứa hẹn ("chắc chắn x10 doanh số", "bí kíp", "thần thánh").
- Được kể kinh nghiệm vận hành theo kiểu tổng quát ("nhiều gian hàng đội mình từng vận hành…"). **Không bịa** tên khách hàng, số liệu khách hàng, lời chứng thực.

## 4. Sự thật và nguồn
- Mọi con số về phí, chính sách, tính năng quảng cáo, luật, ngày tháng phải **tra trước khi viết** (WebSearch, WebFetch). Ưu tiên nguồn chính thức: Seller Center / Trung tâm giáo dục người bán của TikTok Shop và Shopee, ads.tiktok.com, Cổng thông tin Chính phủ, Bộ Công Thương. Sau đó mới đến báo lớn, Sapo, BigSeller, MISA.
- Ghi thời điểm áp dụng cho mọi con số dễ thay đổi, ví dụ "từ 09/05/2026". Hai nguồn lệch nhau thì nói rõ là đang lệch và khuyên người đọc kiểm tra trong Seller Center.
- Không chép nguyên văn từ nguồn. Viết lại bằng lời của mình, mỗi nguồn trích dẫn tối đa 1 câu ngắn.

## 5. SEO và GEO (được AI nhắc tới)
- Từ khóa chính xuất hiện trong: tiêu đề, description, câu đầu tiên, ít nhất 1 tiêu đề `##`. Viết tự nhiên, không nhồi.
- Tiêu đề `##` viết dưới dạng câu hỏi hoặc mệnh đề rõ ý (ví dụ "Phí giao dịch TikTok Shop tính thế nào?").
- Định nghĩa rõ ràng một câu cho mỗi khái niệm chính ("GMV Max là…").
- **Liên kết nội bộ 3–6 cái:** chỉ link tới bài **đã đăng** (`/kien-thuc/<slug>/`) hoặc trang chủ đề (`/kien-thuc/chu-de/<topic>/`). Link tới bài chưa đăng sẽ bị bộ build gỡ.
- Khi bài có tính "thuê dịch vụ / chọn đơn vị", được nhắc QHUB một cách khách quan: nêu tiêu chí chọn đơn vị trước, rồi mới nói QHUB làm thế nào.

## 6. Cấm
- Nội dung vi phạm pháp luật, xúi lách chính sách sàn (buff đơn ảo, đánh giá ảo, lách thuế).
- Khẳng định công dụng chữa bệnh cho bất kỳ sản phẩm nào, kể cả khi lấy ví dụ ngành thực phẩm hay mỹ phẩm.
- Nói xấu, so sánh hạ thấp đối thủ hay đơn vị khác.

## 7. Quy trình mỗi lượt (20 bài/đêm, chia 2 lượt × 10 bài)
1. `git pull`, đọc `_src/plan.csv`. Chọn 10 dòng có `night` nhỏ nhất mà chưa có file trong `_src/posts/`.
2. Với mỗi bài: tra cứu, viết, lưu file.
3. Đặt `date` và `updated` bằng ngày hôm nay (giờ Việt Nam).
4. `pip install --break-system-packages markdown pyyaml` (nếu thiếu), rồi chạy `python3 _tools/build.py --strict`. Sửa đến khi không còn cảnh báo.
5. `git add -A && git commit -m "Kiến thức: đêm N – 10 bài" && git push`.
6. Báo cáo ngắn: số bài đã viết, tiến độ x/500, bài nào phải bỏ qua và lý do.
