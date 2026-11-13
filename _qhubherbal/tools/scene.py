# Tạo ảnh thẻ sản phẩm: hộp ở giữa, nguyên liệu xung quanh, giọt sương, nền pastel sáng
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance
import math, random, sys, os
sys.path.insert(0,'.')
import data
F2=ImageFont.truetype(os.path.join(os.path.dirname(os.path.abspath(__file__)),'ttf/bvp-600.ttf'),21)
def hexrgb(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def dew(base,cx,cy,r):
    s=r*4; L=Image.new('RGBA',(s,s),(0,0,0,0)); d=ImageDraw.Draw(L); c=s//2
    sh=Image.new('RGBA',(s,s),(0,0,0,0)); ImageDraw.Draw(sh).ellipse([c-r+r*.25,c-r+r*.45,c+r+r*.25,c+r+r*.45],fill=(60,80,60,40)); sh=sh.filter(ImageFilter.GaussianBlur(r*.35)); L.alpha_composite(sh)
    for i in range(r,0,-1):
        t=i/r; d.ellipse([c-i,c-i,c+i,c+i],fill=(int(238-22*t),int(247-10*t),int(242-16*t),int((70+110*t**3)*.55)))
    d.ellipse([c-r,c-r,c+r,c+r],outline=(255,255,255,200),width=max(1,r//7))
    hr=r*.38; hx=c-r*.35; hy=c-r*.38; d.ellipse([hx-hr,hy-hr*.8,hx+hr,hy+hr*.8],fill=(255,255,255,245))
    d.ellipse([c+r*.25,c+r*.3,c+r*.5,c+r*.52],fill=(255,255,255,150))
    base.alpha_composite(L,(int(cx-c),int(cy-c)))
def leafline(d,x,y,ang,L,col,w=3):
    a=math.radians(ang); ca,sa=math.cos(a),math.sin(a)
    P=lambda u,v:(x+u*ca-v*sa,y+u*sa+v*ca)
    d.line([P(L*t,L*.22*math.sin(math.pi*t)) for t in [i/24 for i in range(25)]],fill=col,width=w)
    d.line([P(L*t,-L*.22*math.sin(math.pi*t)) for t in [i/24 for i in range(25)]],fill=col,width=w)
    d.line([P(0,0),P(L,0)],fill=col,width=w)
    for t in [.25,.42,.59,.76]:
        d.line([P(L*t,0),P(L*(t+.12),L*.17*math.sin(math.pi*(t+.1)))],fill=col,width=max(1,w-1)); d.line([P(L*t,0),P(L*(t+.12),-L*.17*math.sin(math.pi*(t+.1)))],fill=col,width=max(1,w-1))
FEM={'ngay-dau-ve','duong-tam-an','duong-nhan'}
ONLY=set(sys.argv[1:])  # python3 tools/scene.py <slug> để chỉ dựng 1 sản phẩm
for p in data.PRODUCTS:
    if ONLY and p['slug'] not in ONLY: continue
    random.seed(p['slug']); W=H=900; tint=hexrgb(p['tint']); fem=p['slug'] in FEM
    bg=Image.new('RGBA',(W,H)); dr=ImageDraw.Draw(bg)
    for y in range(H):
        t=(y/H); dr.line([(0,y),(W,y)],fill=(int(250-6*t),int(252-4*t),int(248-4*t),255))
    for box_,col_,al_ in [([-260,-260,520,460],(255,251,238),220),([520,560,1120,1120],(222,239,228),170),([560,-200,1100,300],(232,244,236),120)]:
        mk=Image.new('L',(W,H),0); ImageDraw.Draw(mk).ellipse(box_,fill=al_); mk=mk.filter(ImageFilter.GaussianBlur(90))
        bg.paste(Image.new('RGBA',(W,H),col_+(255,)),(0,0),mk)
    la=Image.new('RGBA',(W,H),(0,0,0,0)); ld=ImageDraw.Draw(la); lc=(120,170,135,38)
    for (x,y,a,L) in [(-20,120,-25,260),(820,700,150,250)]: leafline(ld,x,y,a,L,lc,3)
    bg.alpha_composite(la)
    box=Image.open(f"site/assets/img/products/{p['slug']}.webp").convert('RGBA'); bh=560; box=box.resize((int(box.width*bh/box.height),bh),Image.LANCZOS)
    box=ImageEnhance.Color(box).enhance(1.1); box=ImageEnhance.Brightness(box).enhance(1.05)
    bx=(W-box.width)//2; by=170
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).ellipse([bx+20,by+bh-18,bx+box.width-20,by+bh+22],fill=(40,80,60,60)); sh=sh.filter(ImageFilter.GaussianBlur(20)); bg.alpha_composite(sh)
    bg.alpha_composite(box,(bx,by))
    ings=p['ings'][:6]
    slots=[(150,215),(745,215),(120,470),(775,470),(160,725),(735,725)]
    if len(ings)<=4: slots=[(150,250),(745,250),(150,640),(745,640)]
    labo=(226,204,160,255)
    for i,ing in enumerate(ings):
        cx,cy=slots[i]; r=100 if i<2 else 86
        im=Image.open(f"site/assets/img/ing/{ing[0]}.webp").convert('RGBA').resize((2*r,2*r),Image.LANCZOS)
        im=ImageEnhance.Color(im).enhance(1.15); im=ImageEnhance.Brightness(im).enhance(1.05)
        m=Image.new('L',(2*r,2*r),0); ImageDraw.Draw(m).ellipse([0,0,2*r-1,2*r-1],fill=255)
        s2=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(s2).ellipse([cx-r,cy-r+12,cx+r,cy+r+16],fill=(40,80,60,30)); s2=s2.filter(ImageFilter.GaussianBlur(10)); bg.alpha_composite(s2)
        rg=Image.new('RGBA',(W,H),(0,0,0,0)); gd=ImageDraw.Draw(rg); gd.ellipse([cx-r-14,cy-r-14,cx+r+14,cy+r+14],fill=(255,255,255,120),outline=(255,255,255,235),width=3); gd.ellipse([cx-r-5,cy-r-5,cx+r+5,cy+r+5],fill=(255,255,255,255),outline=(214,230,220,255),width=2); bg.alpha_composite(rg)
        ly=Image.new('RGBA',(2*r,2*r),(0,0,0,0)); ly.paste(im,(0,0),m); bg.alpha_composite(ly,(cx-r,cy-r))
        txt=ing[1]+(f" {ing[2]}" if ing[2] else '')
        dd=ImageDraw.Draw(bg); tb=dd.textbbox((0,0),txt,font=F2); tw=tb[2]-tb[0]; lx=cx-tw//2-14; lyy=cy+r+2
        lab=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(lab).rounded_rectangle([lx,lyy,lx+tw+28,lyy+36],radius=18,fill=(255,255,255,248),outline=labo,width=2); bg.alpha_composite(lab)
        dd.text((lx+14,lyy+5),txt,font=F2,fill=(31,77,58))
        dew(bg,cx-r*.55+random.randint(-8,8),cy-r*.62,random.randint(12,16)); dew(bg,cx+r*.62,cy-r*.25+random.randint(-10,10),random.randint(8,11))
        if random.random()<.6: dew(bg,cx+r*.15,cy+r*.55,random.randint(6,9))
    for (x,y,r) in [(450,120,14),(300,820,10),(610,840,12),(80,360,9),(830,360,9),(bx+box.width-30,by+40,12),(bx+30,by+bh-80,9)]: dew(bg,x,y,r)
    bg.convert('RGB').save(f"site/assets/img/products/{p['slug']}-scene.webp",quality=86); print(p['slug'])
