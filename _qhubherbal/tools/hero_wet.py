"""Hero phương án "Sương sớm" (bản xem trước): 7 hộp GỐC đứng trên cùng một mặt bàn trắng ướt nước,
mỗi hộp một vị trí gần–xa khác nhau. Nền Gemini (không chữ, không sản phẩm): tools/hero/wet_land.png, wet_port.png.
Hộp = ảnh chính thức products/<slug>-3d.webp, chỉ co giãn đều; không đổi màu, không vẽ lại chữ.
Chạy: python3 tools/hero_wet.py [--publish]
"""
import sys
from PIL import Image, ImageFilter, ImageDraw

P = 'site/assets/img/products/'
H = 'tools/hero/'
OUT = 'site/assets/img/'


def box(slug, h):
    im = Image.open(P + slug + '-3d.webp').convert('RGBA')
    a = im.getchannel('A').point(lambda v: 255 if v > 200 else 0)
    im = im.crop(a.getbbox())
    return im.resize((round(im.width * h / im.height), h), Image.LANCZOS)


def put(cv, slug, cx, base, h):
    W, Hh = cv.size
    im = box(slug, h)
    x, y = round(cx - im.width / 2), base - im.height
    # bóng mềm đổ ra sau-phải (nắng trên-trái), cảnh sáng nên nhạt
    sh = Image.new('L', (W, Hh), 0)
    ImageDraw.Draw(sh).polygon([(x + im.width * .2, base), (x + im.width, base),
                                (x + im.width * 1.45, base - h * .16), (x + im.width * .75, base - h * .16)], fill=60)
    sh = sh.filter(ImageFilter.GaussianBlur(h * .06))
    lay = Image.new('RGBA', (W, Hh), (80, 100, 95, 0)); lay.putalpha(sh); cv.alpha_composite(lay)
    # phản chiếu trên mặt ướt
    rh = int(h * .55)
    rf = im.transpose(Image.FLIP_TOP_BOTTOM).crop((0, 0, im.width, rh)).filter(ImageFilter.GaussianBlur(h * .012))
    g = Image.linear_gradient('L').resize((im.width, rh)).point(lambda v: int(max(0, 215 - v) * .30))
    rf.putalpha(Image.composite(g, Image.new('L', g.size, 0), rf.getchannel('A')))
    cv.alpha_composite(rf, (x, base))
    # bóng tiếp xúc
    ct = Image.new('L', (W, Hh), 0)
    ImageDraw.Draw(ct).ellipse((x + h * .02, base - h * .012, x + im.width - h * .01, base + h * .014), fill=130)
    ct = ct.filter(ImageFilter.GaussianBlur(h * .009))
    lay = Image.new('RGBA', (W, Hh), (55, 65, 60, 0)); lay.putalpha(ct); cv.alpha_composite(lay)
    cv.alpha_composite(im, (x, y))


def front_leaves(pl, region):
    """mặt nạ lá/hoa tiền cảnh (xanh lá hoặc trắng-hồng bão hoà) trong vùng region, để đặt lại lên trên hộp"""
    import colorsys
    x0, y0, x1, y1 = region
    m = Image.new('L', pl.size, 0); px = pl.load(); mp = m.load()
    for y in range(y0, y1):
        for x in range(x0, x1):
            r, g, b = px[x, y][:3]
            h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
            if (0.16 < h < 0.45 and s > 0.28) or (s > 0.25 and (h > 0.85 or h < 0.05)):
                mp[x, y] = 255
    return m.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(1.5))


def render(plate, spots, crop=None, fg=None):
    pl = Image.open(H + plate).convert('RGB').filter(ImageFilter.GaussianBlur(0.5)).convert('RGBA')
    cv = pl.copy()
    for slug, cx, base, h in sorted(spots, key=lambda s: s[2]):     # xa (đáy cao) vẽ trước
        put(cv, slug, cx, base, h)
    if fg:
        cv = Image.composite(pl, cv, front_leaves(pl, fg))
    return cv.crop(crop) if crop else cv


DESK = [  # slug, tâm x, đáy y, cao   (khung 2048x1144) – cụm tự nhiên nhiều tầng gần–xa, hộp không che tên nhau
    ('nam-vuong', 1150, 690, 188), ('xau-ho-tim-tam-sen', 1330, 705, 192),
    ('la-oi-mix-la-sen', 990, 800, 215), ('duong-tam-an', 1500, 815, 218),
    ('ca-gai-diep-ha-chau', 1085, 960, 250), ('ngay-dau-ve', 1440, 950, 248),
    ('duong-nhan', 1262, 1040, 285),
]


MOB = [  # khung 1530x2048, sau đó cắt 4:5 (1456x1820) bỏ dấu ✦ của Gemini ở góc dưới
    ('nam-vuong', 500, 1100, 262), ('xau-ho-tim-tam-sen', 790, 1105, 266),
    ('la-oi-mix-la-sen', 245, 1210, 290), ('duong-tam-an', 1075, 1215, 290),
    ('ca-gai-diep-ha-chau', 390, 1450, 345), ('ngay-dau-ve', 935, 1460, 340),
    ('duong-nhan', 650, 1660, 390),
]


def save(cv, name, widths):
    rgb = cv.convert('RGB')
    for w in widths:
        rgb.resize((w, round(rgb.height * w / rgb.width)), Image.LANCZOS).save(OUT + f'{name}-{w}.webp', quality=84, method=6)


if __name__ == '__main__':
    d = render('lush_land.png', DESK, fg=(1490, 790, 2048, 1144))
    m = render('lush_port.png', MOB, crop=(37, 0, 37 + 1456, 1820), fg=(760, 1290, 1530, 2048))
    d.convert('RGB').save('/tmp/wet_d.jpg', quality=92)
    m.convert('RGB').save('/tmp/wet_m.jpg', quality=92)
    if '--publish' in sys.argv:
        save(d, 'hero-dew', (2000, 1600, 1200, 800))
        save(m, 'hero-dew-m', (1080, 720))
