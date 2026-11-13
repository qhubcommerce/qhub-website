"""Chụp toàn trang các trang chính sách (bản local = bản sẽ deploy) -> PDF A4 có dải ghi URL thật."""
# Cần preview ở http://localhost:8765 (xem mục Xem thử). Kết quả: /home/claude/work/bct/*.pdf để nộp hồ sơ online.gov.vn.
import asyncio, io, os
from playwright.async_api import async_playwright
from PIL import Image, ImageDraw, ImageFont

OUT = '/home/claude/work/bct'
os.makedirs(OUT, exist_ok=True)
FONT = '/home/claude/qhub-website/_qhubherbal/tools/ttf/bvp-600.ttf'
import datetime
DATE = datetime.date.today().strftime('%d/%m/%Y')
DOCS = [
    ('01-chinh-sach-bao-mat', ['/chinh-sach-bao-mat/']),
    ('02-giai-quyet-khieu-nai', ['/giai-quyet-khieu-nai/']),
    ('03-chinh-sach-gia', ['/chinh-sach-gia/']),
    ('04-chinh-sach-thanh-toan', ['/chinh-sach-thanh-toan/']),
    ('05-dieu-kien-han-che-dieu-khoan', ['/dieu-khoan/']),
    ('06-giao-hang-doi-tra-hoan-tien', ['/chinh-sach-van-chuyen/', '/chinh-sach-doi-tra/']),
    ('07-ho-tro-truc-tuyen', ['/']),
]
W = 1280


def band(url):
    f = ImageFont.truetype(FONT, 22)
    im = Image.new('RGB', (W, 56), (31, 77, 58))
    d = ImageDraw.Draw(im)
    d.text((24, 15), f'Bản chụp giao diện: https://qhubherbal.com{url}', font=f, fill='white')
    d.text((W - 260, 15), f'Ngày chụp: {DATE}', font=f, fill=(230, 214, 170))
    return im


def paginate(img, url):
    """cắt ảnh dài thành các trang tỉ lệ A4, mỗi trang có dải URL"""
    page_h = int(W * 1.414) - 56
    pages = []
    for y in range(0, img.height, page_h):
        part = img.crop((0, y, W, min(y + page_h, img.height)))
        pg = Image.new('RGB', (W, 56 + page_h), 'white')
        pg.paste(band(url), (0, 0)); pg.paste(part, (0, 56))
        pages.append(pg)
    return pages


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        for name, urls in DOCS:
            allpages = []
            for u in urls:
                pg = await b.new_page(viewport={'width': W, 'height': 900})
                await pg.goto('http://localhost:8765' + u, wait_until='networkidle')
                for yy in range(0, 20000, 700):
                    await pg.evaluate(f'window.scrollTo(0,{yy})'); await pg.wait_for_timeout(30)
                await pg.evaluate('window.scrollTo(0,0)'); await pg.wait_for_timeout(300)
                # ẩn các nút nổi để bản chụp gọn (trừ trang hỗ trợ trực tuyến)
                if u != '/':
                    await pg.add_style_tag(content='.fab,.fpromo,.mbar{display:none!important}')
                    png = await pg.screenshot(full_page=True)
                    img = Image.open(io.BytesIO(png)).convert('RGB')
                    allpages += paginate(img, u)
                else:
                    # trang chủ màn hình đầu (có nút Zalo/Gọi nổi) + chân trang (kênh liên hệ)
                    top = Image.open(io.BytesIO(await pg.screenshot())).convert('RGB')
                    h = await pg.evaluate('document.body.scrollHeight')
                    await pg.evaluate(f'window.scrollTo(0,{h})'); await pg.wait_for_timeout(400)
                    bot = Image.open(io.BytesIO(await pg.screenshot())).convert('RGB')
                    comb = Image.new('RGB', (W, top.height + bot.height + 20), 'white')
                    comb.paste(top, (0, 0)); comb.paste(bot, (0, top.height + 20))
                    allpages += paginate(comb, u)
                await pg.close()
            path = f'{OUT}/{name}.pdf'
            allpages[0].save(path, save_all=True, append_images=allpages[1:], resolution=150, quality=72)
            print(name, len(allpages), 'pages', os.path.getsize(path) // 1024, 'KB')
        await b.close()

asyncio.run(main())
