"""Hero "The Living Botanical Garden": ghép 7 ảnh hộp GỐC lên nền studio thảo mộc (AI).

Nền (không có chữ, không có sản phẩm) do Gemini tạo: tools/hero/plate_land.png (ngang) và
tools/hero/plate_port.png (dọc). Hộp lấy nguyên ảnh chính thức products/<slug>-3d.webp —
chỉ co giãn đều theo tỉ lệ gốc, không đổi màu, không vẽ lại chữ/logo.

Chạy: python3 tools/hero_garden.py   (từ thư mục _qhubherbal)
Ra:   site/assets/img/hero-garden-{2000,1600,1200}.webp (desktop)
      site/assets/img/hero-garden-m-{1080,720}.webp      (mobile 4:5)
"""
import sys
from PIL import Image, ImageFilter, ImageDraw, ImageEnhance

P = 'site/assets/img/products/'
H = 'tools/hero/'
OUT = 'site/assets/img/'


def box(slug, h):
    im = Image.open(P + slug + '-3d.webp').convert('RGBA')
    a = im.getchannel('A').point(lambda v: 255 if v > 200 else 0)
    im = im.crop(a.getbbox())
    return im.resize((round(im.width * h / im.height), h), Image.LANCZOS)


def put(cv, slug, cx, bottom, h, cast=1.0):
    """đặt hộp: đáy hộp tại (cx, bottom); bóng đổ về phía dưới-phải (nắng từ trên-trái 45°)"""
    W, Hh = cv.size
    im = box(slug, h)
    x, y = round(cx - im.width / 2), bottom - im.height
    a = im.getchannel('A')
    # 1) bóng đổ: bóng hộp nghiêng sang phải, ép dẹt, mờ dần
    sh_h = max(8, int(h * 0.20))
    sh = a.resize((im.width, sh_h))
    sh = sh.transform((im.width + int(h * 0.45), sh_h), Image.AFFINE,
                      (1, -h * 0.45 / sh_h, 0, 0, 1, 0), resample=Image.BICUBIC)
    sh = sh.filter(ImageFilter.GaussianBlur(h * 0.035)).point(lambda v: int(v * 0.30 * cast))
    layer = Image.new('RGBA', sh.size, (70, 58, 40, 0)); layer.putalpha(sh)
    cv.alpha_composite(layer, (x + int(h * 0.02), bottom - int(sh_h * 0.55)))
    # 2) bóng tiếp xúc: dải tối mảnh ngay chân hộp
    ct = Image.new('L', (W, Hh), 0)
    ImageDraw.Draw(ct).ellipse((x - h * .01, bottom - h * .018, x + im.width + h * .03, bottom + h * .022), fill=150)
    ct = ct.filter(ImageFilter.GaussianBlur(h * 0.012))
    layer = Image.new('RGBA', (W, Hh), (55, 44, 30, 0)); layer.putalpha(ct)
    cv.alpha_composite(layer)
    # 3) hộp gốc + bóng môi trường rất nhẹ ở chân hộp (≤9%, chỉ là ánh sáng, không đổi màu in)
    ao = Image.linear_gradient('L').resize((im.width, im.height)).point(lambda v: max(0, v - 215) * 23 // 40)
    ao = Image.composite(ao, Image.new('L', im.size, 0), a)
    shade = Image.new('RGBA', im.size, (40, 32, 20, 0)); shade.putalpha(ao)
    cv.alpha_composite(im, (x, y))
    cv.alpha_composite(shade, (x, y))
    return (x, y, x + im.width, bottom)


def soft_blur_plate(path, scale=1.0):
    pl = Image.open(path).convert('RGB')
    if scale != 1.0:
        pl = pl.resize((round(pl.width * scale), round(pl.height * scale)), Image.LANCZOS)
    # nền ảnh AI độ phân giải thấp: làm mềm nhẹ cho giống ảnh chụp xóa phông, rồi tăng tương phản rất nhẹ
    pl = pl.filter(ImageFilter.GaussianBlur(0.8))
    return pl.convert('RGBA')


BACK = ['la-oi-mix-la-sen', 'nam-vuong', 'xau-ho-tim-tam-sen', 'duong-tam-an']   # trái → phải trên 4 cột
FRONT = [('ca-gai-diep-ha-chau', 'L'), ('ngay-dau-ve', 'R'), ('duong-nhan', 'C')]  # giữa vẽ sau cùng


def desktop():
    cv = soft_blur_plate(H + 'plate_land.png')          # 2048 x 1144
    cols = [(1018, 543, 262), (1205, 452, 262), (1428, 365, 262), (1617, 508, 262)]
    for slug, (cx, b, h) in zip(BACK, cols):
        put(cv, slug, cx, b, h, 0.8)
    front = {'L': (975, 772, 312), 'R': (1518, 742, 312), 'C': (1210, 862, 348)}
    for slug, k in FRONT:
        cx, b, h = front[k]
        put(cv, slug, cx, b, h, 1.0)
    return cv


def mobile():
    cv = soft_blur_plate(H + 'plate_port.png')          # 1530 x 2048
    cols = [(466, 1203, 345), (697, 1078, 345), (979, 962, 345), (1216, 1147, 345)]
    for slug, (cx, b, h) in zip(BACK, cols):
        put(cv, slug, cx, b, h, 0.8)
    front = {'L': (405, 1528, 400), 'R': (1088, 1505, 400), 'C': (692, 1650, 445)}
    for slug, k in FRONT:
        cx, b, h = front[k]
        put(cv, slug, cx, b, h, 1.0)
    # 3:4 → 4:5: bớt 136px (40 trên, 96 dưới)
    return cv.crop((0, 40, 1530, 40 + 1912))


def save(cv, name, widths):
    rgb = cv.convert('RGB')
    for w in widths:
        h = round(rgb.height * w / rgb.width)
        rgb.resize((w, h), Image.LANCZOS).save(OUT + f'{name}-{w}.webp', quality=84, method=6)
        print(name, w, h)


if __name__ == '__main__':
    d = desktop(); save(d, 'hero-garden', (2000, 1600, 1200, 800))
    d.convert('RGB').resize((1024, 572)).save('/tmp/hg_d.png')
    m = mobile(); save(m, 'hero-garden-m', (1080, 720))
    m.convert('RGB').resize((612, 765)).save('/tmp/hg_m.png')
