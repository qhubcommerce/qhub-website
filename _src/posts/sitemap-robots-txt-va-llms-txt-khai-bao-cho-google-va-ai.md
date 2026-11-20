---
title: "Sitemap, robots.txt và llms.txt: khai báo cho Google và AI"
slug: sitemap-robots-txt-va-llms-txt-khai-bao-cho-google-va-ai
topic: website-seo
keyword: "robots txt llms txt"
keywords: ["sitemap.xml là gì", "cách viết robots.txt", "llms.txt là gì", "chặn GPTBot ClaudeBot", "IndexNow Bing"]
description: "Sitemap, robots.txt và llms.txt là ba file khai báo cho Google và bot AI. Cách viết đúng, bot AI nào nên cho phép, lỗi hay gặp và file mẫu từ qhub.com.vn."
date: 2026-11-21
updated: 2026-11-21
summary:
  - "sitemap.xml là danh sách URL muốn được lập chỉ mục; mỗi file tối đa 50.000 URL hoặc 50MB chưa nén, Google dùng lastmod khi ngày đó chính xác và bỏ qua priority, changefreq."
  - "robots.txt chỉ điều khiển việc thu thập (crawl), không điều khiển việc lập chỉ mục; muốn trang không hiện trên Google thì dùng noindex và đừng chặn trang đó trong robots.txt."
  - "Mỗi hãng AI có nhiều bot với vai trò khác nhau (huấn luyện, tìm kiếm, đọc theo yêu cầu người dùng); chặn nhầm OAI-SearchBot hay Claude-SearchBot có thể làm website vắng mặt trong câu trả lời của AI."
  - "llms.txt là đề xuất của Jeremy Howard từ 03/09/2024, đến 11/2026 vẫn chưa phải chuẩn chính thức và Google nói không dùng; nên làm vì tốn ít công, nhưng không coi là yếu tố quyết định."
faq:
  - q: "Website nhỏ có cần sitemap.xml không?"
    a: "Google nói website nhỏ, liên kết nội bộ tốt thì có thể không cần sitemap. Nhưng sitemap gần như không tốn công khi website hoặc CMS tự tạo, lại giúp anh chị theo dõi số trang được lập chỉ mục trong Search Console. Vì vậy đội QHUB vẫn khuyên mọi website bán hàng nên có."
  - q: "Chặn một trang trong robots.txt thì trang đó có biến mất khỏi Google không?"
    a: "Không chắc. Disallow chỉ cấm bot đọc trang, nếu có nơi khác trỏ link tới thì URL vẫn có thể hiện trên Google, chỉ là không có đoạn mô tả. Muốn trang biến mất, hãy để Google đọc được trang và gắn thẻ meta robots noindex."
  - q: "Chặn GPTBot có làm website mất khỏi ChatGPT search không?"
    a: "Theo tài liệu của OpenAI, GPTBot dùng cho việc huấn luyện mô hình, còn OAI-SearchBot mới là bot đưa trang vào kết quả tìm kiếm của ChatGPT. Hai bot được điều khiển riêng, nên chặn GPTBot mà vẫn cho phép OAI-SearchBot thì website vẫn có thể được ChatGPT search trích dẫn."
  - q: "llms.txt có giúp website lên top Google hay được AI nhắc tới không?"
    a: "Hiện chưa có bằng chứng. Google nhiều lần nói không dùng llms.txt cho Tìm kiếm và tính năng AI của Google. File này tốn ít công nên làm được, nhưng nội dung tốt, robots.txt mở đúng bot và sitemap chuẩn vẫn quan trọng hơn nhiều."
  - q: "IndexNow là gì, Google có dùng không?"
    a: "IndexNow là giao thức để website chủ động báo cho công cụ tìm kiếm biết URL vừa thêm, sửa hoặc xóa. Bing, Yandex và một số công cụ khác hỗ trợ. Google không tham gia IndexNow, nên với Google anh chị vẫn dựa vào sitemap và Search Console."
sources:
  - title: "Build and submit a sitemap – Google Search Central"
    url: "https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap?authuser=4"
  - title: "Introduction to robots.txt – Google Search Central"
    url: "https://developers.google.com/search/docs/advanced/robots"
  - title: "Overview of OpenAI Crawlers – OpenAI"
    url: "https://developers.openai.com/api/docs/bots"
  - title: "Does Anthropic crawl data from the web, and how can site owners block the crawler? – Claude Help Center"
    url: "https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler"
  - title: "The /llms.txt file – llmstxt.org"
    url: "https://llmstxt.org/"
---

**Sitemap, robots.txt và llms.txt là ba file văn bản đặt ở thư mục gốc website để khai báo với Google và các bot AI: trang nào cần đọc, bot nào được vào, và nội dung chính của website là gì.** sitemap.xml liệt kê các URL muốn được lập chỉ mục. robots.txt quy định bot nào được thu thập phần nào. llms.txt là bản tóm tắt dạng markdown cho mô hình ngôn ngữ, hiện vẫn chỉ là đề xuất. Hai file đầu là việc bắt buộc của mọi website bán hàng, file thứ ba là việc nên làm thêm.

Bài này đội QHUB viết từ chính các file đang chạy trên qhub.com.vn: viết thế nào, khai báo ở đâu, bot AI nào nên mở, và những lỗi nhỏ làm mất trang khỏi Google. Thông tin về các bot mình đối chiếu với tài liệu của từng hãng, tính đến tháng 11/2026.

## sitemap.xml là gì và cần viết thế nào?

Sitemap (sơ đồ trang web) là file XML liệt kê các URL anh chị muốn công cụ tìm kiếm biết tới, kèm ngày sửa lần cuối. Sitemap không ép Google phải lập chỉ mục. Nó chỉ giúp Google tìm ra trang nhanh hơn, nhất là trang mới, trang nằm sâu ít liên kết nội bộ.

Những quy tắc chính theo Google Search Central:

- **Giới hạn mỗi file:** tối đa 50.000 URL hoặc 50MB khi chưa nén. Vượt mức thì chia thành nhiều file và gom lại bằng một sitemap index (file chỉ mục sitemap).
- **URL tuyệt đối và đúng bản chính:** ghi đủ `https://` và tên miền. Chỉ đưa URL bản chính (canonical), không đưa trang lọc, trang có tham số, trang đã chuyển hướng hay trang trả về lỗi 404.
- **lastmod:** ngày sửa nội dung lần cuối. Google cho biết sẽ dùng giá trị này nếu nó chính xác một cách nhất quán. Website ghi lastmod bằng ngày hôm nay cho mọi trang, dù không sửa gì, thì dần bị Google bỏ qua trường này.
- **priority và changefreq:** Google đã nói rõ là bỏ qua hai trường này. Có thể giữ cho các công cụ khác, nhưng đừng mất công chỉnh.

Đây là vài dòng đầu trong sitemap thật của qhub.com.vn (file hiện có 236 URL, do bộ build tự sinh mỗi lần đăng bài):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://qhub.com.vn/</loc><lastmod>2026-11-21</lastmod><priority>1.0</priority></url>
  <url><loc>https://qhub.com.vn/kien-thuc/</loc><lastmod>2026-11-21</lastmod><priority>0.9</priority></url>
  <url><loc>https://qhub.com.vn/kien-thuc/toc-do-website-va-core-web-vitals/</loc><lastmod>2026-11-19</lastmod><priority>0.6</priority></url>
</urlset>
```

Bài viết ghi lastmod đúng ngày cập nhật bài, còn trang chủ và trang mục Kiến thức đổi ngày vì nội dung thật sự thay đổi khi có bài mới. Cột priority vẫn còn, nhưng Google không dùng nó.

### Khai báo sitemap ở đâu?

Có hai chỗ, nên làm cả hai:

1. **Trong Google Search Console:** vào mục Sơ đồ trang web (Sitemaps), dán đường dẫn sitemap và gửi. Sau đó Search Console báo số URL đã đọc được, lỗi nếu có. Cách cài Search Console từng bước có trong bài [Google Search Console: cài đặt và đọc báo cáo](/kien-thuc/google-search-console-cai-dat-va-doc-bao-cao/).
2. **Trong robots.txt:** thêm một dòng `Sitemap:` kèm URL đầy đủ. Mọi bot đọc robots.txt đều thấy sitemap, kể cả Bing và các bot AI.

Lưu ý: Google đã bỏ cách "ping" sitemap qua đường dẫn `google.com/ping?sitemap=...` (thông báo từ tháng 6/2023). Giờ chỉ cần gửi trong Search Console và giữ lastmod chính xác.

## robots.txt là gì, cú pháp viết ra sao?

robots.txt là file văn bản thuần đặt ở gốc tên miền (ví dụ `https://qhub.com.vn/robots.txt`), dùng để nói với bot nào được thu thập phần nào của website. Nó chỉ có hiệu lực cho đúng tên miền, đúng giao thức đó. Tên miền phụ như `shop.tenmien.vn` phải có file riêng.

Cú pháp gồm các nhóm. Mỗi nhóm bắt đầu bằng một hoặc nhiều dòng `User-agent` (tên bot), theo sau là các quy tắc:

| Lệnh | Ý nghĩa | Ví dụ |
| --- | --- | --- |
| `User-agent:` | Tên bot mà nhóm quy tắc áp dụng; `*` là mọi bot | `User-agent: GPTBot` |
| `Disallow:` | Đường dẫn không được thu thập | `Disallow: /gio-hang/` |
| `Allow:` | Đường dẫn được thu thập, dùng để mở lại một phần trong thư mục đã chặn | `Allow: /gio-hang/huong-dan.html` |
| `Sitemap:` | URL đầy đủ của sitemap, đặt ở đâu trong file cũng được | `Sitemap: https://tenmien.vn/sitemap.xml` |
| `#` | Ghi chú, bot bỏ qua | `# chặn trang tìm kiếm nội bộ` |

Một file robots.txt hợp lý cho website bán hàng thường trông như sau:

```txt
User-agent: *
Disallow: /gio-hang/
Disallow: /thanh-toan/
Disallow: /tai-khoan/
Disallow: /tim-kiem?
Allow: /

Sitemap: https://tenmien.vn/sitemap.xml
```

Nên chặn thu thập giỏ hàng, thanh toán, tài khoản khách, trang tìm kiếm nội bộ, các URL lọc sinh ra vô hạn tổ hợp: chúng không có giá trị tìm kiếm mà lại ngốn lượt thu thập của bot. Trang sản phẩm, danh mục, bài viết, file CSS và JavaScript thì phải để mở, vì Google cần đọc CSS, JavaScript để hiểu trang hiển thị ra sao.

### Disallow không phải noindex

Đây là hiểu lầm phổ biến nhất. Google ghi rõ trong tài liệu: robots.txt dùng để quản lý việc thu thập, không phải cơ chế để giữ trang khỏi Google.

Nếu một trang bị chặn trong robots.txt nhưng có nơi khác trỏ link tới, Google vẫn có thể đưa URL đó lên kết quả, chỉ là không có đoạn mô tả. Muốn trang không xuất hiện, anh chị làm ngược lại: **để mở** trang trong robots.txt và gắn thẻ `<meta name="robots" content="noindex">`. Google phải đọc được trang thì mới thấy thẻ noindex. Chặn cả hai cùng lúc là tự khóa cửa không cho Google đọc lời nhắn "đừng lập chỉ mục".

Google cũng không còn hỗ trợ lệnh `noindex` viết trong robots.txt từ ngày 01/09/2019, và không dùng lệnh `Crawl-delay`. Các lệnh này nếu có trong file thì Google bỏ qua.

## Bot AI là những bot nào, nên cho phép hay chặn?

Điểm quan trọng nhất: **mỗi hãng AI có nhiều bot với vai trò khác nhau**. Có bot thu thập để huấn luyện mô hình, có bot lập chỉ mục cho tính năng tìm kiếm, có bot chỉ đọc trang khi người dùng yêu cầu. Chặn sai bot là tự làm website biến mất khỏi câu trả lời của AI.

Bảng dưới mình tổng hợp từ tài liệu của OpenAI, Anthropic, Google, Apple và Perplexity, tính đến tháng 11/2026. Các hãng sửa tài liệu khá thường xuyên, anh chị nên kiểm tra lại trước khi sửa file.

| Tên trong robots.txt | Hãng | Vai trò chính | Gợi ý cho website bán hàng |
| --- | --- | --- | --- |
| Googlebot | Google | Thu thập cho Google Tìm kiếm, gồm cả AI Overviews | Luôn cho phép |
| Google-Extended | Google | Không phải bot riêng, là mã điều khiển việc dùng nội dung cho Gemini; Google nói không ảnh hưởng thứ hạng Tìm kiếm | Cho phép nếu muốn có mặt trong Gemini |
| GPTBot | OpenAI | Thu thập nội dung có thể dùng huấn luyện mô hình | Tùy chọn |
| OAI-SearchBot | OpenAI | Đưa trang vào kết quả tìm kiếm của ChatGPT | Nên cho phép |
| ChatGPT-User | OpenAI | Đọc trang khi người dùng ChatGPT yêu cầu | OpenAI cho biết robots.txt có thể không áp dụng |
| ClaudeBot | Anthropic | Thu thập nội dung có thể dùng huấn luyện mô hình | Tùy chọn |
| Claude-SearchBot | Anthropic | Lập chỉ mục để cải thiện kết quả tìm kiếm của Claude | Nên cho phép |
| Claude-User | Anthropic | Đọc trang khi người dùng Claude yêu cầu | Nên cho phép |
| PerplexityBot | Perplexity | Đưa trang vào kết quả tìm kiếm của Perplexity | Nên cho phép |
| Applebot-Extended | Apple | Không tự thu thập, là mã cho phép hay không việc dùng dữ liệu Applebot đã thu thập để huấn luyện mô hình của Apple | Tùy chọn |

Với Perplexity còn có Perplexity-User, bot đọc trang theo yêu cầu người dùng; theo tài liệu của Perplexity, bot này thường không áp dụng robots.txt.

Vậy nên chặn hay mở? Với doanh nghiệp bán hàng, đội QHUB khuyên **mở các bot tìm kiếm** (Googlebot, OAI-SearchBot, Claude-SearchBot, PerplexityBot), vì đó là cửa để khách hỏi AI rồi tìm ra mình. **Bot huấn luyện** (GPTBot, ClaudeBot, Google-Extended, Applebot-Extended) là lựa chọn riêng: báo chí, nội dung trả phí có lý do để chặn, còn doanh nghiệp bán sản phẩm thường muốn AI hiểu rõ thương hiệu nên mở.

Nếu anh chị muốn chặn huấn luyện mà vẫn có mặt trong tìm kiếm của AI, có thể viết:

```txt
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /
```

Còn qhub.com.vn chọn mở toàn bộ. Đây là robots.txt thật đang chạy (rút gọn phần giống nhau):

```txt
User-agent: *
Allow: /
Disallow: /_src/
Disallow: /_tools/

User-agent: Googlebot
Allow: /

User-agent: OAI-SearchBot
Allow: /

Sitemap: https://qhub.com.vn/sitemap.xml
```

File thật còn các nhóm `Allow: /` tương tự cho Bingbot, Google-Extended, GPTBot, ChatGPT-User, PerplexityBot, ClaudeBot, Claude-SearchBot và Applebot-Extended. Lý do: QHUB muốn khi ai đó hỏi AI về đơn vị vận hành TikTok Shop, AI có đủ thông tin đúng để trả lời. Cách tối ưu cho việc được AI nhắc tới có trong bài [GEO là gì: tối ưu để ChatGPT, Gemini nhắc tới thương hiệu](/kien-thuc/geo-la-gi-toi-uu-de-chatgpt-gemini-nhac-toi-thuong-hieu/).

## llms.txt là gì, có nên làm không?

llms.txt là file markdown đặt ở gốc website, tóm tắt website là gì và liệt kê các trang quan trọng kèm mô tả ngắn, để mô hình ngôn ngữ lớn (LLM, như ChatGPT, Claude) đọc nhanh mà không phải lội qua HTML, menu, quảng cáo.

Nguồn gốc: Jeremy Howard (đồng sáng lập Answer.AI) đưa ra đề xuất này ngày 03/09/2024, trang chính thức là llmstxt.org. Cần nói thật rõ hai điều:

- **llms.txt chưa phải tiêu chuẩn chính thức.** Đến tháng 11/2026 nó vẫn là một đề xuất cộng đồng, không có tổ chức tiêu chuẩn nào phê duyệt, khác với sitemap hay robots.txt.
- **Google nói không dùng llms.txt.** Đại diện Google như Gary Illyes và John Mueller nhiều lần phát biểu rằng Google không dùng file này cho Tìm kiếm hay tính năng AI của Google, và làm SEO bình thường là đủ. Một số bài báo ngành ghi nhận có bot đã tải file llms.txt, nhưng việc tải về không đồng nghĩa với việc dùng nó để xếp hạng hay trích dẫn.

Cấu trúc theo đề xuất gồm: một tiêu đề `#` là tên website, một đoạn trích dẫn `>` tóm tắt ngắn, vài đoạn thông tin thêm, rồi các mục `##` chứa danh sách liên kết dạng `[tên trang](url): mô tả`. File llms.txt của qhub.com.vn khoảng 280 dòng, mở đầu như sau:

```markdown
# QHUB Commerce

> QHUB Commerce (gọi ngắn là QHUB; website chính thức https://qhub.com.vn)
> là Phòng Tăng Trưởng Thuê Ngoài cho doanh nghiệp bán hàng đa sàn...

## Trang chính
- [Trang chủ QHUB Commerce](https://qhub.com.vn/): dịch vụ, cách làm, đội ngũ
- [Giới thiệu QHUB Commerce](https://qhub.com.vn/gioi-thieu/): thông tin doanh nghiệp
```

Vậy có nên làm? Đội QHUB vẫn làm vì tốn ít công (bộ build tự sinh lại mỗi lần đăng bài), không gây hại, và buộc mình rà lại thông tin doanh nghiệp cho thống nhất. Nhưng mình không hứa với khách là "có llms.txt thì AI sẽ nhắc tới anh chị", vì chưa có cơ sở.

## IndexNow: báo Bing ngay khi có trang mới

IndexNow là giao thức mở do Microsoft Bing và Yandex khởi xướng năm 2021, cho phép website chủ động báo cho công cụ tìm kiếm biết URL vừa thêm, sửa hoặc xóa, thay vì chờ bot tự quay lại. Google không tham gia IndexNow, nên giao thức này chủ yếu có ích với Bing, vốn cũng là nguồn tìm kiếm mà một số trợ lý AI dùng.

Cách hoạt động gồm hai bước:

1. Tạo một khóa (key) là chuỗi ký tự ngẫu nhiên, lưu thành file `<khóa>.txt` ở gốc website, nội dung file chính là khóa đó. File này chứng minh anh chị sở hữu tên miền.
2. Mỗi khi có trang mới, gửi danh sách URL tới địa chỉ IndexNow của Bing.

```bash
curl -X POST "https://www.bing.com/indexnow" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{"host":"tenmien.vn","key":"KHOA_CUA_BAN",
       "keyLocation":"https://tenmien.vn/KHOA_CUA_BAN.txt",
       "urlList":["https://tenmien.vn/kien-thuc/bai-moi/"]}'
```

Ở qhub.com.vn, việc này chạy tự động: sau khi đăng bài, hệ thống chờ trang lên sóng, kiểm tra trang trả về mã 200 (mở được bình thường), kiểm tra file khóa, rồi mới gửi. Bing trả về mã 200 hoặc 202 là đã nhận. WordPress cũng có plugin làm sẵn việc này.

## Lỗi hay gặp khi khai báo cho Google và AI

Đây là những lỗi đội QHUB gặp nhiều nhất khi rà website. Phần lớn sửa trong vài phút, nhưng để lâu thì mất trang.

- **Quên gỡ `Disallow: /` khi website lên chính thức.** Bản thử nghiệm thường chặn mọi bot, quên sửa thì Google không đọc được trang nào.
- **Nghĩ rằng các nhóm quy tắc cộng dồn với nhau.** Theo Google, mỗi bot chỉ làm theo nhóm `User-agent` cụ thể nhất khớp với tên nó. Nếu có nhóm riêng cho Googlebot thì Googlebot bỏ qua hoàn toàn nhóm `*`. Ví dụ: file có dòng chặn `/admin/` trong nhóm `*`, đồng thời có nhóm riêng `User-agent: Googlebot` với `Allow: /`, thì Googlebot vẫn vào được `/admin/`. Cách viết đúng là chép các dòng Disallow vào từng nhóm, hoặc gom nhiều `User-agent` vào chung một nhóm.
- **Chặn CSS, JavaScript hoặc thư mục ảnh.** Google không hiển thị được trang như người dùng thấy, ảnh sản phẩm không lên Google Hình ảnh. Xem thêm bài [tốc độ website và Core Web Vitals](/kien-thuc/toc-do-website-va-core-web-vitals/).
- **Sitemap chứa URL lỗi.** Trang 404, trang đã chuyển hướng, trang gắn noindex, trang có tham số lọc. Search Console sẽ báo lỗi và Google giảm tin tưởng vào sitemap.
- **lastmod giả.** Cho mọi trang lấy ngày hôm nay để "trông mới". Google nhận ra và bỏ qua lastmod của cả website.
- **Chặn nhầm bot tìm kiếm của AI.** Muốn chặn huấn luyện nhưng lại chặn luôn OAI-SearchBot hay Claude-SearchBot. Kết quả là website vắng mặt trong câu trả lời của ChatGPT, Claude.
- **Dùng robots.txt để giấu trang nhạy cảm.** Ai cũng đọc được robots.txt, nên `Disallow: /bang-gia-dai-ly/` là đang chỉ đường cho người tò mò. Trang nội bộ phải đặt mật khẩu.

Website đang xây lại thì nên tính luôn cấu trúc danh mục và URL cho gọn, như trong bài [cấu trúc website chuẩn SEO](/kien-thuc/cau-truc-website-chuan-seo-danh-muc-trang-tru-cot-cum-bai/).

## Rà robots.txt, llms.txt và sitemap ngay tuần này

Dành khoảng một buổi để rà ba file này. Thứ tự đội QHUB hay làm:

1. Mở `tenmien.vn/robots.txt`. Kiểm tra không có `Disallow: /` cho Googlebot hay nhóm `*`. Đảm bảo có dòng `Sitemap:`.
2. Quyết định chính sách cho bot AI: mở bot tìm kiếm, chọn mở hoặc chặn bot huấn luyện. Nếu có nhóm riêng cho từng bot, chép đủ các dòng Disallow vào từng nhóm.
3. Mở sitemap, xem có đúng URL bản chính, lastmod có phản ánh ngày sửa thật không. Gửi sitemap trong Search Console và xem báo cáo trang đã lập chỉ mục.
4. Nếu website đăng bài thường xuyên, cài IndexNow để báo Bing.
5. Nếu còn thời gian, viết một file llms.txt ngắn: tên doanh nghiệp, một đoạn tóm tắt, các trang chính. Đừng kỳ vọng nó tạo ra thay đổi lớn.

Xem thêm các bài khác trong chủ đề [Website chuẩn SEO](/kien-thuc/chu-de/website-seo/). QHUB Commerce (qhub.com.vn) có dịch vụ vận hành gian hàng đa sàn, với đội media, đội vận hành sàn, đội KOC và đội host livestream.
