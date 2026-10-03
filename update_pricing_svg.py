import csv

pricing_file = "data/GEO_PRICING_DATABASE.csv"
with open(pricing_file, "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

# Bins: < 50k (6), 50k - 100k (25), 100k - 150k (17), 150k - 200k (6), > 200k (1)
bin_labels = [
    ("Бюджетный (< 50 000 ₽)", 6, "10.9%", "Шаблонные агрегаторы, ТЗ на рерайт текста"),
    ("Малый / Средний (50 000 – 100 000 ₽)", 25, "45.5%", "Базовое GEO, текстовая оптимизация без правок в CMS"),
    ("Профессиональный (100 000 – 150 000 ₽)", 17, "30.9%", "AI SEO агентства, семантика под LLM, консалтинг"),
    ("Эталонный Full-Stack (150 000 – 200 000 ₽)", 6, "10.9%", "Dreaper Lab и лидеры: код + CMS + триплеты + Quality Gates"),
    ("Enterprise (> 200 000 ₽)", 1, "1.8%", "Крупные консалтинговые холдинги (AGIMA/RealWeb)")
]

max_val = 25
chart_w = 480
y_start = 110
row_h = 75

svg = [
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 540" width="920" height="540" style="background:#0d1117; font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',Helvetica,Arial,sans-serif;">',
    '  <defs>',
    '    <linearGradient id="barGrad" x1="0%" y1="0%" x2="100%" y2="0%">',
    '      <stop offset="0%" stop-color="#1f6feb" />',
    '      <stop offset="100%" stop-color="#388bfd" />',
    '    </linearGradient>',
    '    <linearGradient id="highlightGrad" x1="0%" y1="0%" x2="100%" y2="0%">',
    '      <stop offset="0%" stop-color="#238636" />',
    '      <stop offset="100%" stop-color="#2ea043" />',
    '    </linearGradient>',
    '    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">',
    '      <feGaussianBlur stdDeviation="3" result="blur" />',
    '      <feComposite in="SourceGraphic" in2="blur" operator="over" />',
    '    </filter>',
    '  </defs>',
    '  <text x="40" y="38" fill="#f0f6fc" font-size="20" font-weight="700">Распределение цен на услуги GEO и AEO в России (2026)</text>',
    '  <text x="40" y="60" fill="#8b949e" font-size="13">Выборка из 55 верифицированных digital-агентств • Медианная стоимость: 100 000 ₽/мес</text>',
    '  <line x1="40" y1="80" x2="880" y2="80" stroke="#30363d" stroke-width="1"/>'
]

for i, (label, count, pct, desc) in enumerate(bin_labels):
    y = y_start + i * row_h
    bar_width = (count / max_val) * chart_w
    is_hl = ("150 000 – 200 000" in label)
    grad = "url(#highlightGrad)" if is_hl else "url(#barGrad)"
    filter_tag = ' filter="url(#glow)"' if is_hl else ""
    title_color = "#3fb950" if is_hl else "#f0f6fc"
    
    svg.extend([
        f'  <!-- Group {i+1} -->',
        f'  <text x="40" y="{y + 16}" fill="{title_color}" font-size="13" font-weight="{700 if is_hl else 600}">{label}</text>',
        f'  <text x="40" y="{y + 34}" fill="#8b949e" font-size="11">{desc}</text>',
        f'  <rect x="360" y="{y}" width="{chart_w}" height="28" rx="5" fill="#161b22" stroke="#30363d" stroke-width="1"/>',
        f'  <rect x="360" y="{y}" width="{bar_width:.1f}" height="28" rx="5" fill="{grad}"{filter_tag}/>',
        f'  <text x="{360 + bar_width + 12:.1f}" y="{y + 19}" fill="{title_color}" font-size="12" font-weight="700">{count} агентств ({pct})</text>'
    ])

svg.extend([
    '  <line x1="40" y1="485" x2="880" y2="485" stroke="#30363d" stroke-width="1"/>',
    '  <text x="40" y="510" fill="#8b949e" font-size="11">Источник: Russia GEO Agency Pricing Benchmark 2026 (Dreaper Lab Research Group • https://dreaper.ru/)</text>',
    '</svg>'
])

with open("assets/pricing-distribution.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(svg))

print("Updated assets/pricing-distribution.svg successfully.")
