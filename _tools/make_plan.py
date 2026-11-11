#!/usr/bin/env python3
"""Sinh _src/plan.csv từ _tools/plan_titles.py: 500 bài, 20 bài/đêm, xen kẽ chủ đề."""
import csv, os, re, sys, unicodedata
sys.path.insert(0, os.path.dirname(__file__))
from plan_titles import T
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PER_NIGHT = 20
def slugify(s):
    s = s.replace("Đ", "D").replace("đ", "d")
    s = unicodedata.normalize("NFD", s); s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
    if len(s) > 70:
        s = s[:70]
        s = s[:s.rfind("-")] if "-" in s else s
    parts = s.strip("-").split("-")
    while len(parts) > 3 and parts[-1] in {"va", "cho", "tren", "voi", "de", "khi", "nhung", "cua", "la", "o", "the", "nao", "gi", "tu", "den"}:
        parts.pop()
    return "-".join(parts)
def intent(title, kw):
    t = (title + " " + kw).lower()
    if re.search(r"thuê|agency|dịch vụ|báo giá|đơn vị|hợp đồng", t): return "thuong-mai"
    if re.search(r"phí|chi phí|giá|bao nhiêu", t): return "tim-hieu-chi-phi"
    if re.search(r"cách|hướng dẫn|làm sao|thế nào|từng bước|checklist|kịch bản|lộ trình|quy trình", t): return "huong-dan"
    return "kien-thuc"
queues = {k: [l.split("||") for l in v.strip().splitlines() if l.strip()] for k, v in T.items()}
total = sum(len(q) for q in queues.values()); assert total == 500, total
# xen kẽ: mỗi vòng lấy 1 bài từ chủ đề còn nhiều bài nhất theo tỷ lệ
order, taken = [], {k: 0 for k in queues}
while len(order) < total:
    k = max((k for k in queues if taken[k] < len(queues[k])), key=lambda k: (len(queues[k]) - taken[k]) / len(queues[k]))
    order.append((k, *[x.strip() for x in queues[k][taken[k]]])); taken[k] += 1
seen = set(); rows = []
for i, (topic, title, kw) in enumerate(order):
    slug = slugify(title)
    while slug in seen: slug += "-2"
    seen.add(slug)
    rows.append({"id": i + 1, "night": i // PER_NIGHT + 1, "topic": topic, "slug": slug, "title": title, "keyword": kw, "intent": intent(title, kw)})
with open(os.path.join(ROOT, "_src", "plan.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(len(rows), "bài,", rows[-1]["night"], "đêm")
