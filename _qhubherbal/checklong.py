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

# ---- Kiểm tra quy định quảng cáo (xem plan/QUY-TAC-QUANG-CAO.md) ----
# Câu có nhắc tên sản phẩm QHUB mà gán công dụng sức khỏe / từ tuyệt đối / y tế bảo chứng.
PROD = re.compile(r'(trà (cà gai|nam vương|xấu hổ tím|ngày dâu về|lá ổi mix|dưỡng tâm an|dưỡng nhan)|qhub herbal|sản phẩm (của )?qhub)', re.I)
CLAIM = re.compile(r'(giúp (bạn |cơ thể |chị em |anh |em )?(ngủ|dễ ngủ|ngon giấc|giảm|hạ|mát gan|thanh lọc|giải độc|tiêu hóa|nhẹ bụng|đẹp da|trắng da|bổ|tăng|khỏe|hết|ấm bụng|an thần|ổn định)|an thần|mát gan|giải độc|thải độc|thanh lọc|hạ men gan|bảo vệ gan|hạ đường huyết|ổn định đường huyết|hạ huyết áp|giảm mỡ|tiêu mỡ|giảm đau|hết đau|ngủ ngon|chống lão hóa|trẻ hóa|đẹp da|trắng da|tăng sức bền|tăng sức đề kháng|tăng cường miễn dịch|kháng viêm|bổ thận|mạnh gân cốt|sinh lý|phòng bệnh|ngăn ngừa)', re.I)
SUPW = re.compile(r'(tốt nhất|số 1\b|số một|duy nhất|hàng đầu|uy tín nhất|an toàn tuyệt đối|không (có )?tác dụng phụ|thần kỳ|kỳ diệu)', re.I)
OKCTX = re.compile(r'(không phải là thuốc|không thay thế|không thay được|không làm|không giúp|không có tác dụng|không phải thuốc|không hứa|không phải giải pháp|theo quan niệm phương đông|kinh nghiệm dân gian|người xưa|dân gian|truyền thống)', re.I)
MEDEND = re.compile(r'((bác sĩ|dược sĩ|lương y|y tá|chuyên gia)[^.]{0,60}(khuyên|kê|giới thiệu|chỉ định)[^.]{0,40}(\btrà\b|qhub))|(bộ y tế[^.]{0,30}(cấp phép|chứng nhận|công nhận)[^.]{0,40}qhub)', re.I)
ads = 0
for f in sorted(glob.glob('content/long/*.md')):
    t = open(f, encoding='utf-8').read()
    for i, line in enumerate(t.split('\n'), 1):
        if 'không có tác dụng thay thế thuốc chữa bệnh' in line: continue
        for s in re.split(r'(?<=[.!?;])\s+', line):
            if re.search(r'tr[àa] an th[ầa]n', s, re.I) and 'thuốc an thần' not in s.lower():
                print('ADS', f.split('/')[-1], i, '| gọi trà là "trà an thần" |', s.strip()[:160]); ads += 1; continue
            if MEDEND.search(s):
                print('ADS', f.split('/')[-1], i, '| nhân viên y tế/Bộ Y tế bảo chứng |', s.strip()[:160]); ads += 1; continue
            if PROD.search(s) and not s.strip().endswith('?'):
                if SUPW.search(s):
                    print('ADS', f.split('/')[-1], i, '| từ tuyệt đối với sản phẩm |', s.strip()[:160]); ads += 1
                elif CLAIM.search(s) and not OKCTX.search(s):
                    print('ADS', f.split('/')[-1], i, '| gán công dụng cho sản phẩm |', s.strip()[:160]); ads += 1
print('ads-warnings', ads)
