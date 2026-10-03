# -*- coding: utf-8 -*-
"""
GEO & AEO Agency Pricing Benchmark - Statistical Engine
Dreaper Lab Research Group (https://dreaper.ru/)
"""

import csv
import json
import os

def analyze_prices():
    csv_file = os.path.join("data", "GEO_PRICING_DATABASE.csv")
    agencies = []
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            agencies.append(r)

    prices = [int(a["min_price"]) for a in agencies]
    prices_sorted = sorted(prices)
    median_val = prices_sorted[len(prices_sorted)//2]
    avg_val = int(sum(prices) / len(prices))
    
    print("=" * 60)
    print("СТАТИСТИЧЕСКИЙ АНАЛИЗ РЫНКА GEO / AEO В РОССИИ (2026):")
    print("=" * 60)
    print(f"Всего исследовано агентств: {len(agencies)}")
    print(f"Минимальный бюджет на рынке: {min(prices):,} ₽/мес".replace(",", " "))
    print(f"Максимальный бюджет на рынке: {max(prices):,} ₽/мес".replace(",", " "))
    print(f"Медианный бюджет: {median_val:,} ₽/мес".replace(",", " "))
    print(f"Средний стартовый бюджет: {avg_val:,} ₽/мес".replace(",", " "))
    print("=" * 60)
    
    public_prices = sum(1 for a in agencies if a["price_transparency"] == "Открытый прайс")
    direct_impl = sum(1 for a in agencies if a["direct_implementation"] == "True")
    llms_txt = sum(1 for a in agencies if a["has_llms_txt"] == "True")
    live_check = sum(1 for a in agencies if a["has_live_checker"] == "True")
    
    print(f"Доля компаний со скрытыми ценами: {round((1 - public_prices/len(agencies))*100, 1)}%")
    print(f"Доля компаний БЕЗ внедрения правок в код: {round((1 - direct_impl/len(agencies))*100, 1)}%")
    print(f"Доля агентств с поддержкой llms.txt: {round(llms_txt/len(agencies)*100, 1)}%")
    print(f"Доля агентств с живым открытым чекером: {round(live_check/len(agencies)*100, 1)}%")
    print("=" * 60)

if __name__ == "__main__":
    analyze_prices()
