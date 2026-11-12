# Chuyển nền pastel của ảnh (gallery/herbs) sang nền sương trắng "Nắng sớm", giữ nguyên chữ, hộp, hình. Dùng: python3 tools/recolor.py file1.webp file2.webp (ghi đè vào /home/claude/recolor/, chép lại vào media/ sau khi xem). Sau khi thay ảnh: tăng ?v= trong relocate() của build.py.
import numpy as np, sys, os
from PIL import Image
MIST=np.array([246,250,245],dtype=np.float32)/255.
def ss(e0,e1,x):
    t=np.clip((x-e0)/(e1-e0),0,1); return t*t*(3-2*t)
def recolor(src,dst):
    im=Image.open(src); has_a=im.mode in('RGBA','LA'); a=im.getchannel('A') if has_a else None
    rgb=np.asarray(im.convert('RGB')).astype(np.float32)/255.
    mx=rgb.max(-1); mn=rgb.min(-1); V=mx; S=np.where(mx>0,(mx-mn)/np.maximum(mx,1e-6),0)
    L=rgb@np.array([.2126,.7152,.0722],dtype=np.float32)
    w=ss(.78,.90,V)*(1-ss(.18,.42,S))          # nền sáng, nhạt màu
    w=w*(S>0.012)+w*(S<=0.012)*0.6             # gần trắng: chỉ ngả nhẹ
    nl=0.90+(np.clip(L,0.78,1)-0.78)/0.22*0.10  # nâng sáng
    tgt=MIST[None,None,:]*(nl/MIST.mean())[...,None]
    tgt=np.clip(tgt,0,1)
    out=rgb*(1-w[...,None])+tgt*w[...,None]
    o=Image.fromarray((out*255+.5).astype(np.uint8))
    if has_a: o.putalpha(a)
    o.save(dst,quality=88)
if __name__=='__main__':
    for s in sys.argv[1:]:
        recolor(s, os.path.join('/home/claude/recolor',os.path.basename(s)))
