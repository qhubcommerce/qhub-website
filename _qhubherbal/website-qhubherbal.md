# Website QHUB HERBAL – qhubherbal.com

Website bán hàng của thương hiệu **QHUB HERBAL** (thuộc CÔNG TY TNHH QHUB COMMERCE). Đây là web tĩnh, build từ dữ liệu sản phẩm, chạy trên Cloudflare Pages (gói miễn phí).

## ⚡ TIẾP TỤC LÀM VIỆC Ở PHIÊN MỚI / MÁY KHÁC (đọc đầu tiên)

Mã nguồn **không nằm trên máy tính của anh Quang**. Nó nằm trong không gian làm việc đám mây của từng phiên chat với Claude, và có bản sao lưu trên Google Drive.

- **Cùng một cuộc trò chuyện:** mở lại trên máy nào cũng được (claude.ai, app Claude). Dữ liệu trong `/home/claude/work` vẫn còn, làm tiếp bình thường.
- **Cuộc trò chuyện mới, hoặc phiên cũ đã mất dữ liệu:** khôi phục từ Drive theo các bước sau:
  1. Tìm trên Google Drive (connector, tài khoản quangnv.cozy@gmail.com) thư mục ID `1aNX3CtrFq40UooPO5O1lmOnregrfuGPk`. Lấy các file `qhubherbal-backup-<ngày>-vN.tgz.part0…partN` có ngày và số phiên bản mới nhất.
  2. Tải tất cả các phần về một thư mục trống (ví dụ `/home/claude/restore`), rồi chạy `cat qhubherbal-backup-*.tgz.part* > all.tgz && mkdir -p /home/claude/work && tar xzf all.tgz -C /home/claude/work`.
  3. Cài thư viện: `pip install --break-system-packages jinja2 pillow markdown` (thêm `pymupdf` nếu cần dựng lại ảnh từ PDF).
  4. Chạy `cd /home/claude/work && python3 build.py`. Kết quả ra 3 thư mục `dist/`, `ktsite1/`, `ktsite2/`.
- **Bản sao lưu mới nhất:** `qhubherbal-backup-2026-11-11-v3.tgz.part0…part5` (6 phần, khoảng 13 MB). Bản này có 92 bài viết dài, trang chính sách và feed Merchant.
  - File ID: part0 `1rY5TuNTHEuMIrsoVBrxTkk0ZRSWNBZN-`, part1 `1guSa3Y5KwP-TIUJ9gYT-SVNCjpWX_Dql`, part2 `1sJHf-86qJ04amaCLRsdnO7a2a6z8TV1m`, part3 `1urj11lYE4d-X2bgKLV2Ct69p1rCTtqf3`, part4 `1OH9cQIKHN-OZjoKJXxLZHcRcm9dTu1bB`, part5 `1vB0XEYdpVj795LBzLS9WqSw8rmY_4qhD`.
  - Chia nhỏ vì mỗi lần tải lên qua connector Drive tối đa khoảng 2,5 MB.
- **Quy tắc:** sau mỗi đợt thay đổi lớn (khoảng 10 bài mới hoặc sửa code), tạo bản sao lưu mới `vN+1` lên cùng thư mục và cập nhật mục này.
- **Deploy:** dùng Claude in Chrome trên máy có Chrome đã đăng nhập Cloudflare bằng quangnv.ads@gmail.com. Máy cố định ở nhà là máy chính để deploy, Chrome luôn mở và có extension Claude. Nếu có nhiều trình duyệt kết nối, chọn đúng máy đó.

## Địa chỉ & tài khoản
- **Web đang chạy:** https://qhubherbal.com (cả www), dự phòng https://qhubherbal.pages.dev. Nameserver Mắt Bão đã trỏ về Cloudflare.
- **Project ảnh sản phẩm:** `qhubherbal-img` (https://qhubherbal-img.pages.dev) chứa ảnh hộp, ảnh nguyên liệu, OG, hero… Khi build, ảnh được chuyển sang `imgsite/img`, sau đó upload zip `imgsite/`. `SITE['media_img']` trỏ tới đây.
- **Project ảnh phụ:** `qhubherbal-media` (https://qhubherbal-media.pages.dev) chứa `gallery/` và `herbs/`. Upload thư mục `media/` dạng zip khi đổi ảnh. `SITE['media']` trỏ tới đây.
- **Cloudflare:** tài khoản quangnv.ads@gmail.com, account ID `39ff8bdab570cb3dd789dc1d109e5e3c`. Các project Pages: `qhubherbal`, `qhubherbal-kt1`, `qhubherbal-kt2`, `qhubherbal-img`, `qhubherbal-media`.
  - Trang deploy: `https://dash.cloudflare.com/39ff8bdab570cb3dd789dc1d109e5e3c/pages/view/<project>/deployments/new`.
  - Thao tác: tìm input file ẩn → upload zip → cuộn xuống → bấm "Save and deploy"/"Lưu và triển khai" ở góc phải dưới.
- **Đơn hàng:** Form và Sheet trong tài khoản Google **quangnv.ads@gmail.com**. Form trên web gửi vào Google Form "Đơn hàng website QHUB HERBAL", câu trả lời đổ vào Sheet "Đơn hàng website QHUB HERBAL (Câu trả lời)". Đã bật email báo đơn mới.
  - Form (sửa): https://docs.google.com/forms/d/1tGA7Ok0l77rVoa9KCngNWpy9IX3h9nIvwKHtLjaUUvg/edit
  - Sheet: https://docs.google.com/spreadsheets/d/1jcy5gCytXa80Y938WqIVChEDOe6O8wR5z1bN57E7a4k/edit
  - Endpoint & mã trường trong `form_config.json`. Không đổi tên/thứ tự câu hỏi trong Google Form.
- **Hotline/Zalo:** 0941 255 055 · Email hiển thị: qhubherbal@qhub.com.vn
- **Giá:** niêm yết 140.000đ (đổi từ 160.000đ ngày 11/11/2026 để mua 2 tặng 1 = đúng 50%, trần khuyến mại theo NĐ 81/2018 sửa bởi NĐ 128/2024), ưu đãi 105.000đ/hộp. Sửa ở `data.py` → `SITE`. KHÔNG để tổng ưu đãi vượt 50%.
- **Vận chuyển / đổi trả (đã chốt 11/11/2026):** miễn phí giao hàng toàn quốc, 2–5 ngày (xử lý 0–1 ngày + vận chuyển 1–4 ngày). Đổi trả 7 ngày kể cả không lỗi: hàng lỗi QHUB chịu phí; đổi ý thì hộp phải còn nguyên tem, khách chịu phí gửi trả. Khai báo trong `data.py` (`ship_*`, `return_days`).
- **Kênh:** YouTube https://www.youtube.com/@QHUBHERBAL đã gắn ở footer và `sameAs`.
  - Fanpage, TikTok: điền vào `SITE['social']` (hiện ở footer).
  - Shopee, TikTok Shop: điền vào `SITE['marketplaces']`, chỉ khai báo `sameAs`, không hiện link để khách không bỏ sang sàn.

## Thông báo website TMĐT với Bộ Công Thương (NĐ 248/2026)
- Website thuộc diện "nền tảng TMĐT kinh doanh trực tiếp có chức năng đặt hàng trực tuyến": phải được UBND tỉnh Phú Thọ (Sở Công Thương) xác nhận thông báo. Nộp trên Cổng DVC quốc gia, kết nối online.gov.vn.
- Hồ sơ soạn sẵn ở Claude Docs: https://claude.ai/artifact/HJQdpfX31GqzfjGaw7ySUS
- Trạng thái 11/11/2026: CHƯA NỘP. Chờ anh Quang gửi ngày cấp, nơi cấp ĐKDN, người đại diện pháp luật, người vận hành, email nhận kết quả; anh tự đăng nhập VNeID tổ chức và tự nhập số CCCD.
- Đã thêm trang `/chinh-sach-thanh-toan/` (COD) và `/giai-quyet-khieu-nai/`; viết lại Chính sách bảo mật và Điều khoản (quyền, nghĩa vụ, giới hạn); form có ô đồng ý bắt buộc (`dongy`).
- `data.py`: `dkdn_date`, `dkdn_place`, `legal_rep` – điền vào là footer và các trang chính sách tự hiển thị.
- Sau khi được xác nhận, gắn biểu tượng xác nhận điện tử vào footer. Không gắn logo trước khi được xác nhận.

## Google Business Profile & Merchant Center (trạng thái 11/11/2026)
- **Business Profile "QHUB HERBAL":** đã tạo trong quangnv.ads@gmail.com.
  - Loại: Bán lẻ trực tuyến + Doanh nghiệp dịch vụ (ẩn địa chỉ, khu vực Phú Thọ và Hà Nội), ngành "Cửa hàng trà". Đã có hotline, website, mô tả, 6 ảnh sản phẩm. Chưa có giờ làm việc.
  - **Chưa xác minh:** chỉ có cách quay video, anh Quang tự làm trên app Google Maps.
- **Merchant Center:** chưa có tài khoản. Anh Quang tự tạo và đồng ý điều khoản (Claude không được tạo tài khoản). Sau đó Claude cài tiếp:
  - xác minh website qua Search Console cùng tài khoản;
  - shipping: VN, 0đ, 2–5 ngày;
  - return policy 7 ngày;
  - nguồn dữ liệu: file `https://qhubherbal.com/google-merchant-feed.xml` (6 sản phẩm, gtin, `price` 160000 VND, `sale_price` 105000 VND, `google_product_category` 2073).
- **Trang chính sách:** `/chinh-sach-van-chuyen/`, `/chinh-sach-doi-tra/`, `/dieu-khoan/`, `/chinh-sach-bao-mat/`. Mỗi trang sản phẩm có schema `shippingDetails` + `hasMerchantReturnPolicy`.

## Cấu trúc
```
data.py            # TOÀN BỘ nội dung: SITE, PRODUCTS, FAQ, DAY, GIFTS, TRUST
build.py           # render templates/ + site/ -> dist/ (+ ktsite1/ ktsite2/), sitemap, llms.txt, feed Merchant
refs.py            # tự thêm mục "Nguồn tham khảo" (nguồn uy tín đã kiểm chứng) cho bài dài theo từ khóa
checklong.py       # soát từ cấm + độ dài bài dài
templates/         # base.html, index.html, list.html, product.html, page.html, blog.html, post.html, _order.html
content/posts/*.md # 401 bài gốc (ngắn) – bài ngắn bị noindex
content/long/<slug>.md # bài viết dài viết lại (ghi đè bài ngắn cùng slug) – vào sitemap, hiện trước
css/fonts.css + css/main.css  # build gộp thành assets/css/site.css
media/             # project qhubherbal-media
imgsite/           # project qhubherbal-img
site/              # tài sản tĩnh (favicon, logo, js…)
media_orig/        # ảnh gốc
```

## Viết bài dài (đang làm: 92/401 xong)
- **Cấu trúc file:** `content/long/<slug>.md`. Mở đầu bằng khối `+++` gồm dòng `desc:` và 5 dòng FAQ dạng `- Câu hỏi :: Trả lời`, sau đó đến thân bài.
- **Cấu trúc bài:**
  - mở bằng câu chuyện nhân vật minh họa;
  - phần khoa học có bảng, chỉ trích nghiên cứu đã kiểm chứng (tên tác giả + năm);
  - góc nhìn phương Đông;
  - "Khi nào cần đi khám";
  - đoạn sản phẩm kèm `[[buy:slug]]` và lưu ý chống chỉ định;
  - lời kết.
- **Hai dòng cuối bắt buộc:** "*… là thực phẩm, không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh.*" và "*Nhân vật trong bài là nhân vật minh họa.*"
- **Nguồn tham khảo:** khi có cụm chủ đề mới, thêm vào `refs.py` (SRC + RULES). Chỉ dùng URL đã kiểm tra mở được.
- **Còn lại (chưa viết dài):** thao-moc 87, san-pham 80, cau-chuyen 57, cam-nang 44, top 41.
  - cam-nang kế tiếp: dan-van-phong-ngoi-dieu-hoa-bung-lanh, ve-sinh-ky-kinh-dung-cach, yoga-giam-dau-bung-kinh, thuc-don-3-ngay-ky-kinh, theo-doi-chu-ky-kinh-nguyet, tu-lam-tui-chuom-ngai-cuu-muoi-rang, nghi-ngoi-ky-kinh-o-van-phong, thuc-pham-de-tieu-cho-nguoi-hay-day-bung, an-tet-khong-tang-can, che-do-an-cho-nguoi-hay-an-ngoai…
  - Lấy danh sách còn lại: so slug trong `content/posts` với tên file trong `content/long`.
- **Quy trình mỗi đợt:**
  1. Viết khoảng 6–10 bài.
  2. Chạy `python3 checklong.py` rồi `python3 build.py`.
  3. Zip: `for d in dist ktsite1 ktsite2; do (cd $d && rm -f ../$d.zip && zip -qr ../$d.zip .); done`.
  4. Deploy theo thứ tự qhubherbal → kt1 → kt2.
  5. Sao lưu Drive định kỳ.

## Nguyên tắc nội dung (bắt buộc)
- Nội dung công dụng lấy theo tài liệu "THÂN GỬI QUÝ KHÁCH" (bản an toàn). Không dùng các cụm "viêm gan", "tráng dương", "sỏi", "ích tinh", "cường dương".
- Không viết "chữa/trị/điều trị/thần dược/cam kết 100%" như công dụng sản phẩm. Mỗi trang có dòng "Sản phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh."
- Không dùng chữ "Đông y", thay bằng "thảo mộc/quan niệm phương Đông".
- Không bịa đánh giá, lời chứng thực. Nhân vật phải ghi là minh họa. Không dùng đồng hồ đếm ngược giả.
- **Trà Lá Ổi:** người đang táo bón nên tạm ngưng (tanin săn se).
- **Trà Ngày Dâu Về:** không dùng khi mang thai, cho con bú. Người ra kinh nhiều hoặc dùng thuốc chống đông phải hỏi bác sĩ.
- **Nhận diện:** logo dùng đúng file gốc. Màu Forest #173F35, Cream #F4F0E6. Font Be Vietnam Pro (tự host).

## Kiến trúc deploy – BẮT BUỘC đọc trước khi deploy
- **qhubherbal (web chính, `dist.zip`):** trang chủ, sản phẩm, danh sách kiến thức, chính sách, `/assets`, feed, `_worker.js` + `_routes.json`.
- **Bài viết `/kien-thuc/<slug>/`:** ở `qhubherbal-kt1` (`ktsite1.zip`) và `qhubherbal-kt2` (`ktsite2.zip`), chia theo `sum(ord(slug)) % 2`. Worker chuyển tiếp nội bộ, nên khách vẫn thấy qhubherbal.com.
- **Thứ tự:** qhubherbal-img (nếu ảnh đổi) → qhubherbal → kt1 → kt2. Phải deploy đủ 3 dự án web vì mọi trang tham chiếu `site.css?v=VERSION` mới.
- **Giới hạn:** mỗi zip ≤ 3,8 MB khi tải qua Chrome.
- **Ảnh:** URL ảnh có `?v=3`, tăng số khi thay ảnh trùng tên (`relocate()` trong build.py).
- **Kiểm tra trên điện thoại:** `python3 mobaudit.py 360 shots`.
- **Kiểm tra trang thật:** dùng WebFetch (shell không gọi được qhubherbal.com).

## SEO
- **Google Search Console:** domain property `qhubherbal.com` (quangnv.ads@gmail.com), xác minh bằng TXT trong Cloudflare. Không xóa bản ghi TXT `google-site-verification`. Bing đã import.
- **Schema:** Organization (`sameAs`, `contactPoint`, `hasMerchantReturnPolicy`), WebSite (trang chủ), Product + Offer (shipping, return), Article + FAQPage cho bài.
- **Title trang chủ:** "QHUB HERBAL – Tinh hoa trà thảo mộc phương Đông | 100% thiên nhiên".
- `/llms.txt` dành cho AI.

## Lịch sử
- 11/11/2026: dựng bản đầu, thiết kế lại organic, 400 bài ngắn, tách ảnh sang project phụ, tách bài sang kt1/kt2, đăng ký GSC và Bing.
- 11/11/2026 tối:
  - **Nội dung:** viết lại 92 bài dài có nguồn tham khảo; thêm câu chuyện Huy Hoàng (Trà Lá Ổi).
  - **Thương hiệu & SEO:** sửa title/description trang chủ, thêm favicon và schema WebSite, gắn YouTube.
  - **Merchant Center:** thêm 3 trang chính sách, schema ship/đổi trả, feed Merchant; tạo Google Business Profile (chờ xác minh video).
  - **Sao lưu:** bản v3 lên Drive.
