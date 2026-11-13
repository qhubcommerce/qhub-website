# Dựng lá nền nhòe (xanh tươi) riêng cho từng loại trà từ ảnh nguyên liệu thật. Chạy từ _qhubherbal: python3 tools/leaves.py
import numpy as np, os
from PIL import Image, ImageFilter, ImageEnhance
O='site/assets/img/'; DEC=os.path.join(os.path.dirname(os.path.abspath(__file__)),'decor')
SRC={
 'ca-gai-diep-ha-chau':[('d','branch'),('i','diep-ha-chau'),('i','giao-co-lam')],
 'nam-vuong':[('i','kim-tien-thao'),('i','kim-tien-thao'),('i','kim-tien-thao')],
 'xau-ho-tim-tam-sen':[('d','mimosa'),('d','lotus'),('i','dinh-lang')],
 'ngay-dau-ve':[('i','ngai-cuu'),('i','ich-mau'),('d','gung')],
 'la-oi-mix-la-sen':[('d','guava'),('d','lotus'),('i','giao-co-lam')],
 'duong-tam-an':[('i','lac-tien'),('d','cuc'),('i','dinh-lang')],
 'duong-nhan':[('i','hoa-hong'),('i','tia-to'),('d','lotus')],
}
def ss(e0,e1,x): t=np.clip((x-e0)/(e1-e0),0,1); return t*t*(3-2*t)
def cutout(path):
    im=Image.open(path).convert('RGBA'); a=np.asarray(im).astype(np.float32)
    rgb=a[...,:3]; al=a[...,3]/255.
    inside=al>0.9; bg=np.median(rgb[inside][:4000] if inside.sum()>0 else rgb.reshape(-1,3),0)
    # nền kem: lấy mẫu ở vành trong của vòng tròn
    h,w=al.shape; yy,xx=np.mgrid[:h,:w]; r=np.hypot(yy-h/2,xx-w/2); ring=(r>w*0.40)&(r<w*0.47)&inside
    if ring.sum()>50: bg=np.median(rgb[ring],0)
    mx=rgb.max(-1); mn=rgb.min(-1); S=(mx-mn)/np.maximum(mx,1)
    L=rgb@np.array([.2126,.7152,.0722]); bL=float(bg@np.array([.2126,.7152,.0722]))
    bS=float((bg.max()-bg.min())/max(bg.max(),1))
    A=np.maximum(ss(bS+.10,bS+.26,S), ss(.42,.62,(bL-L)/255.))*al*(r<w*0.485)
    out=np.dstack([rgb,A*255]).astype(np.uint8); return Image.fromarray(out,'RGBA')
def soft(pad,blur):
    arr=np.asarray(pad).astype(np.float32)/255.; al=arr[...,3:4]; pm=arr[...,:3]*al
    P=Image.fromarray((np.concatenate([pm,al],-1)*255).astype('uint8'),'RGBA').filter(ImageFilter.GaussianBlur(blur))
    b=np.asarray(P).astype(np.float32)/255.; al2=b[...,3:4]; col=np.where(al2>1e-4,b[...,:3]/np.maximum(al2,1e-4),0)
    return Image.fromarray((np.concatenate([np.clip(col,0,1),al2],-1)*255).astype('uint8'),'RGBA')
def make(kind,name,out,rot,blur,flip,size=620):
    im=Image.open(f'{DEC}/{name}.webp').convert('RGBA') if kind=='d' else cutout(f'{O}ing/{name}.webp')
    if flip: im=im.transpose(Image.FLIP_LEFT_RIGHT)
    bb=im.getbbox(); im=im.crop(bb); w,h=im.size; s=size/max(w,h); im=im.resize((int(w*s),int(h*s)),Image.LANCZOS)
    pad=Image.new('RGBA',(im.width+140,im.height+140),(0,0,0,0)); pad.alpha_composite(im,(70,70)); pad=pad.rotate(rot,resample=Image.BICUBIC,expand=True)
    rgb=ImageEnhance.Color(pad.convert('RGB')).enhance(1.18); rgb=ImageEnhance.Brightness(rgb).enhance(1.03)
    pad=Image.merge('RGBA',(*rgb.split(),pad.getchannel('A'))); pad=soft(pad,blur); pad=pad.crop(pad.getbbox())
    pad.save(O+out,quality=82,method=6)
PAR=[(16,5,False),(-24,8,True),(140,6,False)]
import sys
ONLY=set(sys.argv[1:])
for slug,L in SRC.items():
    if ONLY and slug not in ONLY: continue
    for i,(k,n) in enumerate(L):
        r,b,f=PAR[i]; make(k,n,f'leaf-p-{slug}-{i+1}.webp',r,b,f)
    print(slug)
