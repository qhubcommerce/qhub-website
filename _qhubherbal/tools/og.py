# Ảnh chia sẻ (OG 1200x630) – giao diện "Nắng sớm". Chạy từ thư mục _qhubherbal: python3 tools/og.py
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, sys
sys.path.insert(0,'.'); import data
T=os.path.join(os.path.dirname(os.path.abspath(__file__)),'ttf')
O='site/assets/img/'; os.makedirs(O+'og',exist_ok=True)
F=lambda w,s: ImageFont.truetype(f'{T}/bvp-{w}.ttf',s)
vnd=lambda n: f"{n:,}".replace(',', '.')+'đ'
LIST=vnd(data.SITE['price_list']); SALE_T=vnd(data.SITE['price_sale'])
FOREST=(31,77,58); LEAF=(60,122,86); GOLD=(135,86,26); SALE=(177,79,42); MUTED=(91,106,98)
logo=Image.open(O+'logo-forest.png').convert('RGBA')
leaf=Image.open(O+'leaf-blur-c.webp').convert('RGBA')
def base():
    W,H=1200,630; im=Image.new('RGBA',(W,H)); d=ImageDraw.Draw(im)
    for y in range(H): t=y/H; d.line([(0,y),(W,y)],fill=(int(249-5*t),int(252-4*t),int(247-4*t),255))
    for box,col,al in [([-300,-320,560,300],(255,250,236),230),([700,250,1400,900],(220,238,226),200),([820,-260,1400,240],(232,244,236),150)]:
        mk=Image.new('L',(W,H),0); ImageDraw.Draw(mk).ellipse(box,fill=al); mk=mk.filter(ImageFilter.GaussianBlur(90))
        im.paste(Image.new('RGBA',(W,H),col+(255,)),(0,0),mk)
    lf=leaf.copy(); lf.thumbnail((420,420)); a=lf.getchannel('A').point(lambda v:int(v*.45)); lf.putalpha(a); im.alpha_composite(lf,(W-lf.width+120,-110))
    l=logo.copy(); l.thumbnail((110,110)); im.alpha_composite(l,(64,44)); return im,ImageDraw.Draw(im)
def tag(d,x,y):
    t='MUA 2 TẶNG 1 · chỉ có khi đặt tại website'; f=F(700,22); w=d.textlength(t,font=f)
    d.rounded_rectangle([x,y,x+w+36,y+44],radius=22,fill=(251,243,226),outline=(234,211,166),width=2); d.text((x+18,y+9),t,font=f,fill=GOLD)
def pricebox(d,x,y):
    d.text((x,y),SALE_T,font=F(700,52),fill=SALE); w=d.textlength(SALE_T,font=F(700,52))
    d.text((x+w+18,y+20),LIST,font=F(400,28),fill=(120,128,124)); w2=d.textlength(LIST,font=F(400,28)); d.line((x+w+18,y+38,x+w+18+w2,y+38),fill=(120,128,124),width=2)
def shadow(im,x,y,w,h):
    s=Image.new('RGBA',im.size,(0,0,0,0)); ImageDraw.Draw(s).ellipse([x+20,y+h-16,x+w-20,y+h+20],fill=(31,77,58,70)); im.alpha_composite(s.filter(ImageFilter.GaussianBlur(16)))
im,d=base()
hero=Image.open(O+'hero.webp').convert('RGBA'); hero.thumbnail((470,470)); hx,hy=1200-hero.width-60,(630-hero.height)//2+10
shadow(im,hx,hy,hero.width,hero.height); im.alpha_composite(hero,(hx,hy)); d=ImageDraw.Draw(im)
d.text((64,186),'Chăm sóc từ bên trong,',font=F(700,48),fill=FOREST)
d.text((64,244),'bằng tinh túy thảo mộc.',font=F(700,48),fill=LEAF)
d.text((64,318),'6 công thức trà thảo mộc túi lọc',font=F(400,26),fill=MUTED)
pricebox(d,64,372); tag(d,64,456)
d.text((64,540),'qhubherbal.com · Zalo 0941 255 055',font=F(600,24),fill=FOREST)
im.convert('RGB').save(O+'og.jpg',quality=86)
for p in data.PRODUCTS:
    im,d=base()
    b=Image.open(O+f"products/{p['slug']}.webp").convert('RGBA'); b.thumbnail((360,500)); bx,by=1200-b.width-130,(630-b.height)//2+10
    shadow(im,bx,by,b.width,b.height); im.alpha_composite(b,(bx,by)); d=ImageDraw.Draw(im)
    name=p['name']; size=52
    while d.textlength(name,font=F(700,size))>640: size-=2
    d.text((64,186),name,font=F(700,size),fill=FOREST)
    d.text((64,256),p['tagline'],font=F(600,30),fill=LEAF)
    d.text((64,310),'Trà thảo mộc túi lọc · 30 túi × 3 g',font=F(400,26),fill=MUTED)
    pricebox(d,64,372); tag(d,64,456)
    d.text((64,540),'qhubherbal.com · Zalo 0941 255 055',font=F(600,24),fill=FOREST)
    im.convert('RGB').save(O+f"og/{p['slug']}.jpg",quality=86)
print('ok')
