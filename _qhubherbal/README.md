# Website QHUB HERBAL – qhubherbal.com

Website bán hàng của thương hiệu **QHUB HERBAL** (thuộc CÔNG TY TNHH QHUB COMMERCE). Đây là web tĩnh, build từ dữ liệu sản phẩm, chạy trên Cloudflare Pages (gói miễn phí).

## Địa chỉ & tài khoản
- **Web đang chạy:** https://qhubherbal.com (cả www), dự phòng https://qhubherbal.pages.dev. Nameserver Mắt Bão đã trỏ về Cloudflare.
- **Project ảnh sản phẩm:** `qhubherbal-img` (https://qhubherbal-img.pages.dev) chứa ảnh hộp, ảnh nguyên liệu, ảnh OG, hero… Khi build, ảnh được chuyển sang `imgsite/img`, sau đó upload zip `imgsite/`. `SITE['media_img']` trỏ tới project này.
- **Project ảnh phụ:** `qhubherbal-media` (https://qhubherbal-media.pages.dev) chứa `gallery/` (ảnh TMĐT từng sản phẩm) và `herbs/` (ảnh từng vị thảo mộc). Upload thư mục `media/` dạng zip vào project này khi đổi ảnh. `SITE['media']` trỏ tới đây để zip web chính luôn < 3,8 MB.
- **Cloudflare:** tài khoản quangnv.ads@gmail.com. Project Pages tên `qhubherbal`. Zone `qhubherbal.com` gói Free.
  - Nameserver cần đặt tại Mắt Bão: `jocelyn.ns.cloudflare.com`, `scott.ns.cloudflare.com`.
- **Đơn hàng:** Form và Sheet nằm trong tài khoản Google **quangnv.ads@gmail.com**. Form trên web gửi vào Google Form "Đơn hàng website QHUB HERBAL", câu trả lời tự đổ vào Google Sheet "Đơn hàng website QHUB HERBAL (Câu trả lời)". Thông báo email khi có đơn mới đã bật.
  - Form (sửa): https://docs.google.com/forms/d/1tGA7Ok0l77rVoa9KCngNWpy9IX3h9nIvwKHtLjaUUvg/edit
  - Sheet: https://docs.google.com/spreadsheets/d/1jcy5gCytXa80Y938WqIVChEDOe6O8wR5z1bN57E7a4k/edit
  - Endpoint & mã trường nằm trong `form_config.json`. Không đổi tên/thứ tự câu hỏi trong Google Form, nếu không mã `entry.*` sẽ sai.
- **Hotline/Zalo:** 0941 255 055 · Email hiển thị: qhubherbal@qhub.com.vn
- **Giá:** niêm yết 140.000đ, giá ưu đãi 105.000đ/hộp. Sửa ở `data.py` → `SITE`.

## Mã nguồn lưu ở đâu
- **Bản mới nhất v2** (11/11/2026, có 400 bài viết): thư mục Drive "QHUB HERBAL – Mã nguồn website (11-11-2026)" của tài khoản quangnv.cozy@gmail.com, folder ID `1aNX3CtrFq40UooPO5O1lmOnregrfuGPk`.
  - Gồm 3 file `qhubherbal-source-2026-11-11-v2-phan-1/2/3-of-3.zip`, file ID lần lượt `1yDPACLTznqqIpumhAzJR-6vbmC2OgeYL`, `1uD-G3bzffpRMF9X8A6UO51zIl0fQxol7`, `1MV3-be-dbv9JvWUuBIw_k6CT7oT5Q68R`.
  - Giải nén cả 3 vào cùng chỗ là đủ bộ. Cùng thư mục còn bản v1 (58 bài), giữ lại để tham khảo.
  - Phải chia nhỏ vì mỗi lần gửi qua connector tối đa ~3 MB.
- Bản cũ nhất (trước đợt thiết kế lại): `qhubherbal-source.zip`, file ID `1RWj_G_-Ni2yvBR6cfabA14P3Gnr7RPaf`.
- Cần: Python 3 + jinja2 + Pillow (+ pymupdf nếu dựng lại ảnh từ PDF).

## Cấu trúc
```
data.py            # TOÀN BỘ nội dung: SITE, PRODUCTS (mỗi sản phẩm 1 mục), FAQ, DAY, GIFTS, TRUST
build.py           # render templates/ + site/ -> dist/
templates/         # base.html, index.html, list.html, product.html, page.html, blog.html, post.html, _order.html (form, card, post_card)
content/posts/*.md # 400 bài Kiến thức:
                   #   10-14 = 28 bài thảo mộc, 20-25 = 30 bài sản phẩm (đợt 1)
                   #   30-35 = khoảng 50 bài cho mỗi sản phẩm (dhc, nv, xht, ndv, loi, dta)
                   #   40-top = 49 bài Top & so sánh
                   # Chuyên mục: cam-nang, thao-moc, san-pham, cau-chuyen, top
GUIDELINE-SEO-GEO.md # nguyên tắc viết bài SEO/GEO (cũng lưu ở project doc)
css/fonts.css + css/main.css  # build gộp thành assets/css/site.css (giao diện organic)
media/             # deploy riêng thành project qhubherbal-media
site/assets/css/site.css, site/assets/js/site.js
site/assets/img/products/<slug>.webp     # ảnh hộp mặt trước (bắt buộc)
site/assets/img/products/<slug>-3d.webp  # ảnh hộp góc nghiêng (bắt buộc)
site/assets/img/gallery/<slug>/*.webp    # ảnh thêm cho trang sản phẩm (tùy chọn, tự hiện)
site/assets/img/ing/<key>.webp           # ảnh nguyên liệu tròn (bắt buộc cho mỗi vị khai báo)
site/assets/img/hero.webp, lineup.webp   # ảnh ghép 6 hộp (group.py) – xếp lưới đều, KHÔNG chồng hộp
site/assets/img/og/<slug>.jpg            # ảnh chia sẻ Facebook/Zalo (og.py)
prep.py, group.py, og.py                 # script dựng ảnh từ PDF trong Project (catalogue, "Thân gửi quý khách")
```

## Thêm sản phẩm mới (dự kiến lên ~15 sản phẩm)
1. Thêm 1 mục vào `PRODUCTS` trong `data.py`, theo mẫu sản phẩm có sẵn. Các trường cần có: slug, cat (nhóm nhu cầu, dùng cho bộ lọc), name, short, color, tagline, intro, keys, when_see, for_who, time, flavor, if_list, dongy, formula, ings, habits, pair, note, ingredients_text, tcb, gtin, usage_tip.
2. Thêm ảnh `products/<slug>.webp` và `<slug>-3d.webp`, cùng ảnh nguyên liệu mới vào `ing/`.
3. Chạy `python3 og.py && python3 build.py`. build.py tự kiểm tra thiếu ảnh. Nếu muốn ảnh ghép hero hiển thị bộ mới thì sửa `group.py`.
4. Zip thư mục `dist/` rồi tải lên Cloudflare: Workers & Pages → qhubherbal → Create deployment → Production → chọn file .zip (≤ 3,8 MB) → Save and deploy.
5. Trang chủ, trang Sản phẩm, form đặt hàng, sitemap, footer và bộ lọc tự cập nhật theo danh sách.

## Trang & SEO
- Blog chia trang, mỗi trang 24 bài.
  - Trang chủ đề: `/kien-thuc/chu-de/<cat>/`.
  - Trang theo sản phẩm: `/kien-thuc/tra/<slug>/`.
- Trang thương hiệu `/gioi-thieu/` và file `/llms.txt` dành cho AI.
- Form đặt hàng trên trang bài viết được tải từ `/assets/order.html`, nhờ vậy mỗi bài nhẹ hơn và zip vẫn dưới 3,8 MB.
- Google Search Console: domain property `qhubherbal.com` (quangnv.ads@gmail.com), xác minh bằng TXT trong Cloudflare. Đã gửi sitemap.
  - Không xóa bản ghi TXT `google-site-verification`.
- Bing Webmaster: đã import từ GSC và gửi sitemap.

## Viết bài Kiến thức
- Mỗi file .md có thể chứa nhiều bài. Mỗi bài mở đầu bằng khối giữa hai dòng `+++` gồm: slug, title, seo_title, desc, cat (`thao-moc` hoặc `san-pham`), herb (key nguyên liệu, nếu là bài thảo mộc), cover (đường dẫn trong media), products (các slug, cách nhau bằng dấu phẩy), date, order. FAQ viết dạng `- Câu hỏi :: Trả lời`.
- Trong thân bài chèn `[[buy:slug]]` để hiện khung mua hàng. Mỗi `## H2` tự vào mục lục.
- Bài nào có `herb:` thì tên vị thuốc trên trang sản phẩm tự link tới bài đó.
- Thêm sản phẩm mới: viết 1 bài cho mỗi vị thảo mộc mới và 5 bài sản phẩm, gồm review, nỗi đau, góc Đông y, cách dùng, quà tặng/so sánh.

## Nguyên tắc nội dung (bắt buộc)
- Nội dung công dụng lấy theo tài liệu "THÂN GỬI QUÝ KHÁCH" (bản an toàn). Không dùng các cụm của Catalog 8.11 như "viêm gan", "tráng dương", "sỏi".
- Không viết "chữa/trị/thần dược/cam kết 100%". Mỗi trang phải có dòng "Sản phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh."
- Logo dùng đúng file gốc. Màu: Forest #173F35, Cream #F4F0E6, Sage, Copper ≤10%. Font: Be Vietnam Pro (tự host).

## Lịch sử
- 11/11/2026: dựng và triển khai bản đầu (6 sản phẩm), form → Google Sheet đã chạy thử thành công (có 1 dòng "KIỂM THỬ WEBSITE" trong Sheet, xóa được). Đã thêm zone qhubherbal.com vào Cloudflare, chờ đổi nameserver tại Mắt Bão.

- 11/11/2026 (chiều): thiết kế lại theo hướng organic (lá, giọt sương, ảnh TMĐT), viết lại copy, thêm mục Kiến thức với 58 bài SEO. Đã triển khai lên qhubherbal.com, tên miền chạy cả bản có và không có www.
- 11/11/2026: bỏ ảnh "Công dụng theo Đông y" của Nam Vương (có chữ "ích tinh"). Ảnh gốc giữ trong `media_orig/`. Sửa ảnh thảo mộc nhục thung dung ("Ích tinh huyết" → "Dưỡng huyết"), ba kích và nấm ngọc cẩu (bỏ ", ích tinh"). Không dùng cụm "ích tinh" trên web.
- 11/11/2026: thêm 342 bài, tổng 400 bài. Có thêm phân trang, trang chủ đề, /gioi-thieu/, llms.txt và tách ảnh sang project qhubherbal-img. Đã đăng ký Google Search Console và Bing.


## Cập nhật 11/11/2026 (chiều) – audit giao diện v3/v4
- **Màu sắc:** dùng xanh lá ổi (hộp Lá Ổi Mix Lá Sen): nút nền #d4e799→#b6d268, chữ #1d4224. Nền kem-xanh có họa tiết lá vẽ nét (`site/assets/img/leaf-line.svg`); họa tiết trang trí `deco-oi.svg`, `deco-sen.svg`, `deco-cuc.svg`.
- **Cách gọi:** không dùng chữ "Đông y" trên toàn site, thay bằng "quan niệm/thảo mộc phương Đông", "người xưa".
- **Mua 2 tặng 1:**
  - đợt theo tuần, đồng hồ đếm ngược thật đến 23:59:59 Chủ nhật (giờ VN), code ở cuối `site.js`;
  - nút treo `.fpromo` chỉ hiện khi đã cuộn quá 500px và ẩn khi đang ở form đặt hàng;
  - form tự tính số hộp tặng; dòng sản phẩm trong Sheet ghi "| TẶNG (mua 2 tặng 1): …".
- **Ảnh:**
  - `products/<slug>-scene.webp` (hộp kèm nguyên liệu và giọt sương) dùng cho thẻ sản phẩm; nằm ở qhubherbal-img;
  - `gallery/<slug>-thong-tin-hop.webp` ghép từ file khai triển final, giữ hotline/QR/mã vạch; nằm ở qhubherbal-media.
- **Video vùng nguyên liệu:** điền link YouTube vào `SITE["video_youtube"]` trong data.py rồi build. Khung video tự hiện và tự phát không tiếng khi khách cuộn tới; để trống thì khung ẩn hoàn toàn.
- **Slider Kiến thức:** trên trang chủ, tự lướt mỗi 5 giây, lấy bài đều từ 6 sản phẩm, Top và Thảo mộc.
- **Bài dài:** đặt ở `content/long/<slug>.md`. Chạy `python3 checklong.py` để soát từ cấm và độ dài trước khi build.
- **Giới hạn deploy:** mỗi zip tối đa 3,8 MB. Bản này zip web chính đã 3,7 MB; khi thêm nhiều bài dài sẽ vượt, cần chuyển sang deploy qua GitHub hoặc tách dự án.

## Kiến trúc deploy (từ 11/11/2026, chiều) – BẮT BUỘC đọc trước khi deploy
- **Dự án qhubherbal (web chính):** đổi từ `dist/` (`dist.zip`). Chứa trang chủ, sản phẩm, trang danh sách kiến thức, `/assets` và `_worker.js` cùng `_routes.json`.
- **Bài viết:** nằm ở 2 dự án phụ `qhubherbal-kt1` (`ktsite1.zip`) và `qhubherbal-kt2` (`ktsite2.zip`).
  - Bài thuộc dự án nào tính theo: tổng mã ký tự của slug chia lấy dư cho 2.
  - Mỗi lần chạy `build.py` sẽ tự chuyển bài sang `ktsite1/` và `ktsite2/`.
- `_worker.js` chỉ chạy trên `/kien-thuc/*`: nếu web chính không có trang thì chuyển tiếp nội bộ sang dự án phụ. Địa chỉ khách thấy vẫn là qhubherbal.com.
- **Thứ tự deploy:** qhubherbal-img (nếu ảnh đổi) → qhubherbal → qhubherbal-kt1 → qhubherbal-kt2. Phải deploy đủ cả 3 dự án web vì mọi trang đều tham chiếu `site.css?v=VERSION` mới.
- **Ảnh sản phẩm:**
  - URL ảnh có `?v=3`. Khi thay ảnh trùng tên, tăng số này trong `relocate()` ở build.py.
  - Ảnh scene tạo bằng `python3 scene.py`.
  - Ảnh hộp gốc (còn lớp bóng xám) lưu ở `media_orig/products/`.
- **Kiểm tra điện thoại:** chạy `python3 mobaudit.py 360 shots` (server xem trước ở cổng 8766, gộp dist và 2 thư mục ktsite).
