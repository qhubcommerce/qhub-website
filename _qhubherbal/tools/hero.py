"""Dựng ảnh đầu trang chủ (hero-organic*.webp) từ ảnh hộp các sản phẩm.

Bố cục kim tự tháp 2 hàng: hàng sau 4 hộp (tông lạnh), hàng trước 3 hộp (tông ấm),
sản phẩm mới (is_new) đứng giữa hàng trước, lớn nhất; thảo mộc ở hai góc dưới.
Chạy: python3 tools/hero.py  (từ thư mục _qhubherbal)
"""
import os, sys
from PIL import Image, ImageFilter, ImageDraw
sys.path.insert(0, os.getcwd())
import data

P = 'site/assets/img/products/'
D = 'tools/decor/'
OUT = 'site/assets/img/'
W, H = 1500, 1160

BACK = ['la-oi-mix-la-sen', 'ca-gai-diep-ha-chau', 'nam-vuong', 'xau-ho-tim-tam-sen']
new = [p['slug'] for p in data.PRODUCTS if p.get('is_new')]
center = new[0] if new else 'duong-tam-an'
FRONT = ['ngay-dau-ve', center, 'duong-tam-an'] if center != 'duong-tam-an' else ['ngay-dau-ve', center, 'la-oi-mix-la-sen']


def box(slug, h):
    im = Image.open(P + slug + '.webp').convert('RGBA')
    im = im.crop(im.getbbox())
    # cắt bỏ phần mờ (bóng) dưới đáy nếu có: giữ vùng alpha đậm
    a = im.getchannel('A').point(lambda v: 255 if v > 200 else 0)
    im = im.crop(a.getbbox())
    return im.resize((round(im.width * h / im.height), h), Image.LANCZOS)


def shadow(canvas, cx, bottom, w, strength=110):
    sh = Image.new('L', (W, H), 0)
    d = ImageDraw.Draw(sh)
    d.ellipse((cx - w * 0.62, bottom - 26, cx + w * 0.62, bottom + 30), fill=strength)
    sh = sh.filter(ImageFilter.GaussianBlur(22))
    layer = Image.new('RGBA', (W, H), (24, 60, 42, 0))
    layer.putalpha(sh)
    canvas.alpha_composite(layer)


def side_shadow(canvas, im, x, y, strength=70):
    """bóng mềm in lên hộp phía sau (tạo chiều sâu)"""
    a = im.getchannel('A').filter(ImageFilter.GaussianBlur(18)).point(lambda v: v * strength // 255)
    layer = Image.new('RGBA', im.size, (20, 50, 35, 0)); layer.putalpha(a)
    canvas.alpha_composite(layer, (x + 14, y + 10))


def decor(name, h, flip=False, rot=0):
    im = Image.open(D + name + '.webp').convert('RGBA')
    if flip: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    if rot: im = im.rotate(rot, expand=True, resample=Image.BICUBIC)
    im = im.crop(im.getbbox())
    return im.resize((round(im.width * h / im.height), h), Image.LANCZOS)


def main():
    cv = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    # hàng sau: 4 hộp, chừa trọn tên hộp
    hb = 440; top_b = 70
    xs_b = [258, 586, 914, 1242]
    for slug, cx in zip(BACK, xs_b):
        im = box(slug, hb)
        shadow(cv, cx, top_b + hb, im.width, 80)
        x = cx - im.width // 2
        cv.alpha_composite(im, (x, top_b))
    # hàng trước: 2 hộp bên rồi hộp giữa (sản phẩm mới) vẽ sau cùng để nổi lên trên
    order = [(FRONT[0], 416), (FRONT[2], 1084), (FRONT[1], 750)]
    for slug, cx in order:
        hf = 560 if slug == center else 500
        bottom = 930 if slug == center else 905
        im = box(slug, hf)
        shadow(cv, cx, bottom, im.width, 140)
        x = cx - im.width // 2; y = bottom - hf
        side_shadow(cv, im, x, y, 60 if slug != center else 90)
        cv.alpha_composite(im, (x, y))
    # thảo mộc hai góc dưới (vẽ sau cùng, đè chân hộp)
    L1 = decor('mimosa', 270); cv.alpha_composite(L1, (10, H - L1.height - 60))
    L2 = decor('lotus', 230, flip=True); cv.alpha_composite(L2, (140, H - L2.height - 4))
    R1 = decor('guava', 270, flip=True); cv.alpha_composite(R1, (W - R1.width - 4, H - R1.height - 120))
    R2 = decor('cuc', 240); cv.alpha_composite(R2, (W - R2.width - 30, H - R2.height - 10))
    R3 = decor('gung', 150); cv.alpha_composite(R3, (W - R2.width - R3.width + 40, H - R3.height - 12))
    bb = cv.getbbox(); print('bbox', bb)
    cv.save(OUT + 'hero-organic.webp', quality=88, method=6)
    for w in (1200, 800, 480):
        cv.resize((w, round(H * w / W)), Image.LANCZOS).save(OUT + f'hero-organic-{w}.webp', quality=86, method=6)
    prev = Image.new('RGB', (W, H), (244, 248, 242)); prev.paste(cv, (0, 0), cv)
    prev.thumbnail((900, 900)); prev.save('/tmp/hero_new.png')


main()
