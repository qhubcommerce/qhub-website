import glob,re,sys
BAN=['chữa','điều trị','trị dứt','trị mụn','thần dược','cam kết 100','tráng dương','cường dương','ích tinh','bổ thận tráng','điều hòa kinh nguyệt','đặc trị','khỏi bệnh','hết bệnh','giảm cân','tăng cường sinh lý']
ALLOW=['thay thế điều trị','điều trị sớm','khám và điều trị','có tác dụng chữa bệnh','sửa chữa','giảm cân hoặc','sụt cân','thuốc chữa bệnh','đang điều trị','hướng điều trị','phương pháp điều trị','thay thế thuốc','không phải thuốc trị mụn','sản phẩm giảm cân','thuốc điều trị','điều trị hiệu quả','có những phương pháp điều trị','đang được điều trị','sau điều trị']
bad=0; tot=0
for f in sorted(glob.glob('content/long/*.md')):
    t=open(f,encoding='utf-8').read(); body=t.split('+++')[-1]; tot+=1
    n=len(body.split())
    for line in t.split('\n'):
        l=line.lower()
        for b in BAN:
            if b in l and not any(a in l for a in ALLOW):
                print(f.split('/')[-1], '|', b, '|', line.strip()[:140]); bad+=1
    if n<1200: print('SHORT', f, n)
    if 'minh họa' not in t and re.search(r'^(Chị|Anh|Cô|Bà|Ông) [A-ZĐ]', body, re.M): print('NOLABEL?', f)
print('files',tot,'issues',bad)
