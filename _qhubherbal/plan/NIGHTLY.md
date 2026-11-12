# Quy trình viết bài tự động mỗi đêm – qhubherbal.com

Kế hoạch: `plan/plan-600.tsv` có 600 bài, 100 bài cho mỗi sản phẩm. Mỗi đêm viết **12 bài, mỗi sản phẩm 2 bài**, theo cột `night`. Chạy 50 đêm, bắt đầu đêm 12/11/2026.
- Cột `kind`:
  - `viet-lai`: bài ngắn đã có trong `content/posts`, cần viết lại thành bài dài.
  - `moi`: chủ đề mới, phải thêm khung bài (stub) trước khi viết.
- Cột `status`: `todo` → `done` (ghi kèm ngày viết).

## 0. Việc đầu tiên mỗi lần chạy (01:21, chạy hoàn toàn trên cloud – KHÔNG cần máy anh Quang)
1. Lịch chạy là **scheduled task định kỳ hằng ngày** (cron 01:21 Asia/Saigon, trig_011Z5pMHbzki5NHo8G5VmHcs) – không cần tự đặt lịch nối tiếp, KHÔNG dùng send_later. Không hỏi lại anh Quang bất cứ điều gì; tự quyết và ghi rõ trong báo cáo.
2. Lấy mã nguồn: gọi `add_repo` (owner `qhubcommerce`, repo `qhub-website`, access `push`), rồi `git clone --depth 1 https://github.com/qhubcommerce/qhub-website /home/claude/qhub-website` (timeout dài ~10 phút). Thư mục làm việc: `/home/claude/qhub-website/_qhubherbal`. Cài `pip install --break-system-packages jinja2 markdown pillow` nếu thiếu.
3. Thư mục gốc repo là web **qhub.com.vn** (công ty) – KHÔNG sửa gì ngoài `_qhubherbal/` và `.github/workflows/qhubherbal-deploy.yml`.

## 1. Chọn bài
Lấy các dòng `status=todo` có `night` nhỏ nhất, 12 dòng. Nếu đêm trước còn sót bài, viết bù trước.

## 2. Viết bài – tiêu chuẩn BẮT BUỘC (không viết qua loa)
- **Độ dài:** 2.200–3.500 chữ tiếng Việt. Bài phải thực sự sâu, không độn chữ.
- **Nghiên cứu trước khi viết:** dùng WebSearch, WebFetch cho số liệu, khuyến nghị, nghiên cứu. Chỉ nêu tên nghiên cứu (tác giả + năm, tạp chí) hoặc tổ chức (WHO, NIH, Mayo Clinic, Bộ Y tế…) khi đã kiểm chứng được. Không bịa số liệu.
- **Cấu trúc file `content/long/<slug>.md`:**
  - Khối `+++`: dòng `desc:` khoảng 150–200 ký tự, tóm tắt cụ thể; 5 dòng FAQ dạng `- Câu hỏi :: Trả lời` (câu hỏi thật người dùng hay tìm, trả lời đủ ý 1–3 câu).
  - Mở bài: câu chuyện nhân vật minh họa gần gũi, có tên, tuổi, nghề.
  - Các mục `##`: giải thích khoa học (cơ chế, số liệu, bảng so sánh); hướng dẫn thực hành cụ thể (bảng, danh sách, thực đơn, lịch); góc nhìn phương Đông; "Khi nào cần đi khám".
  - Đoạn giới thiệu sản phẩm phù hợp, có `[[buy:<slug sản phẩm>]]` và lưu ý chống chỉ định.
  - Lời kết quay lại nhân vật.
- **Hai dòng cuối bắt buộc:**
  - `*Thông tin mang tính tham khảo, không thay thế tư vấn y khoa. <Tên trà> là thực phẩm, không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh.*`
  - `*Nhân vật trong bài là nhân vật minh họa.*`
- **Tối ưu SEO và GEO** (để ChatGPT, Gemini dễ trích dẫn):
  - Câu trả lời trực tiếp cho câu hỏi chính nằm ngay 2–3 câu đầu của mục đầu tiên.
  - Định nghĩa rõ ràng, có số liệu kèm nguồn, bảng tóm tắt, mục FAQ.
  - Từ khóa chính có trong `desc`, câu mở và ít nhất một tiêu đề `##`.
  - Tiêu đề (`title` của stub) tối đa khoảng 60 ký tự, từ khóa chính đứng đầu; `desc` 140–160 ký tự.
  - Nếu tiêu đề bài dài hơn 50 ký tự, thêm dòng `seo_title: <bản ngắn ≤ 50 ký tự, từ khóa chính đứng đầu>` vào khối `+++` của `content/long/<slug>.md` (đây là thẻ title Google hiển thị; tiêu đề H1 vẫn giữ bản đầy đủ).
  - Liên kết nội bộ tự nhiên tới 2–3 bài liên quan đã có trong `content/long` (dạng `[chữ](/kien-thuc/<slug>/)`).
- **Tuân thủ nội dung:**
  - Không dùng: chữa, trị, điều trị (khi nói về sản phẩm), thần dược, cam kết 100%, tráng dương, cường dương, ích tinh, "Đông y" (thay bằng "thảo mộc/quan niệm phương Đông").
  - Không đưa ra tuyên bố bệnh lý cho sản phẩm. Không bịa đánh giá hay lời chứng thực khách hàng.
  - Bài về bệnh (gan, tiểu đường, mất ngủ…) phải khuyên đi khám, làm theo bác sĩ.
- **Bài `viet-lai`:** giữ nguyên slug. Đọc bài ngắn cũ trong `content/posts` để giữ ý chính, rồi viết lại sâu hơn nhiều.
- **Bài `moi`:**
  1. Thêm stub vào `content/posts/50-plan-moi.md` gồm `+++`, `slug: <slug>`, `title: <tiêu đề hấp dẫn, chứa từ khóa>`, `desc: <mô tả ngắn>`, `cat: <cat trong plan>`, `products: <product>`, `+++`, 1 dòng mô tả, `[[buy:<product>]]`.
  2. Viết `content/long/<slug>.md`.
- **Thông tin sản phẩm** (công thức lấy từ `data.py` → `formula`):
  - ca-gai-diep-ha-chau: cà gai leo 40%, diệp hạ châu 15%, xạ đen, an xoa, giảo cổ lam, cỏ ngọt.
  - nam-vuong: ba kích, nhục thung dung, nấm ngọc cẩu, mú từn, kim tiền thảo, dứa dại, cỏ ngọt.
  - xau-ho-tim-tam-sen: xấu hổ tím 30%, tâm sen 10%, lạc tiên, đinh lăng, hoa cúc vàng, cỏ ngọt.
  - ngay-dau-ve: ích mẫu, ngải cứu, cỏ máu, gừng, táo đỏ, mâm xôi, thiên niên kiện, cam thảo. Không dùng khi mang thai, cho con bú; người ra kinh nhiều hoặc dùng thuốc chống đông phải hỏi bác sĩ.
  - la-oi-mix-la-sen: lá ổi 50%, lá sen 20%, giảo cổ lam, gạo lứt rang, cỏ ngọt. Người đang táo bón nên tạm ngưng (tanin).
  - duong-tam-an: lạc tiên, tâm sen, đinh lăng, hoa cúc.
  - Giá: niêm yết 140.000đ, bán 105.000đ; khuyến mại mua 2 tặng 1 (ưu đãi đúng 50%); miễn phí ship toàn quốc; đổi trả 7 ngày; thanh toán khi nhận hàng (COD).
- **Nguồn tham khảo:** khi gặp cụm chủ đề mới chưa có trong `refs.py`, thêm cụm (SRC + RULES) với URL đã mở thử được.

## 3. Kiểm tra và build
1. Chạy `python3 checklong.py`: sửa hết từ cấm. Từ "điều trị" chỉ được dùng trong ngữ cảnh "đi khám, điều trị theo bác sĩ".
2. Chạy `python3 build.py`: phải ra "built N pages" không lỗi (để kiểm tra; GitHub Actions sẽ build lại khi deploy).
3. Cập nhật `status=done <ngày>` trong `plan/plan-600.tsv` (file CRLF, giữ nguyên định dạng).
4. Ảnh gốc nằm ở `site/assets/img` và `media/`. Không commit `dist/`, `ktsite*/`, `imgsite/` (đã có .gitignore).

## 4. Deploy (tự động qua GitHub Actions – không dùng Chrome)
1. Commit và đẩy lên GitHub:
   `cd /home/claude/qhub-website && git add -A _qhubherbal && git commit -m "QHUB HERBAL: đêm N – 12 bài" && git pull --rebase origin main && git push origin main`
   (push lỗi do repo đổi thì `git pull --rebase` rồi push lại; repo này còn có lịch viết bài của qhub.com.vn chạy song song.)
2. Workflow `.github/workflows/qhubherbal-deploy.yml` tự chạy: build → `wrangler pages deploy` 5 project (qhubherbal-img, qhubherbal-media, qhubherbal-kt1, qhubherbal-kt2, qhubherbal) → kiểm tra HTTP 200 → báo **IndexNow** (Bing/Copilot/ChatGPT Search, Yandex) cho các bài mới/đổi. Token Cloudflare nằm ở secret `CLOUDFLARE_API_TOKEN` của repo.
3. Chờ ~6 phút rồi WebFetch kiểm tra 1–2 bài mới trên `https://qhubherbal.com/kien-thuc/<slug>/`. Nếu chưa lên: WebFetch `https://github.com/qhubcommerce/qhub-website/actions` xem lượt chạy "QHUB HERBAL – build & deploy" có lỗi không, sửa và push lại.
4. Google: sitemap tự cập nhật (Google đọc lại định kỳ), không cần thao tác. Nếu Claude in Chrome đang kết nối và đã đăng nhập Search Console thì có thể gửi thêm tối đa 10 URL theo cách cũ; không kết nối thì BỎ QUA, không báo lỗi, không hỏi anh Quang.
5. `plan/PENDING_SUBMIT.txt` (nếu có): URL GSC trong đó chỉ gửi khi Chrome kết nối; không thì để nguyên.

## 5. Báo cáo
Cuối mỗi lần chạy, gửi SendUserMessage ngắn gồm:
- đêm thứ mấy;
- 12 tiêu đề đã viết;
- đã đẩy lên GitHub và web đã có bài chưa (kết quả WebFetch);
- tổng tiến độ (x/600).

