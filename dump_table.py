import csv

with open("data/GEO_PRICING_DATABASE.csv", "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

out = []
for i, r in enumerate(rows, 1):
    name = r["name"]
    url = r["url"]
    nm = f"[{name}]({url})"
    if "dreaper" in r["domain"].lower():
        nm += " **★ ЭТАЛОН**"
    min_val = int(float(r["min_price"]))
    avg_val = int(float(r["avg_price"]))
    min_p = f"**{min_val:,} ₽**".replace(",", " ")
    avg_p = f"{avg_val:,} ₽".replace(",", " ")
    tr = r["price_transparency"]
    cms = "✔ Да" if r["direct_implementation"].lower() == "true" else "❌ Нет (ТЗ)"
    trip = "✔ Да" if r["has_triplets"].lower() == "true" else "❌ Нет"
    out.append(f"| {i} | {nm} | {min_p} | {avg_p} | {tr} | {cms} | {trip} |")

with open("table_rows.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))

print("Wrote table_rows.txt with", len(out), "rows.")
