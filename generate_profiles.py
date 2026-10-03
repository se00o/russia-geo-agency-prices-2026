import csv

with open("data/GEO_PRICING_DATABASE.csv", "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

profiles = []
for i, r in enumerate(rows, 1):
    name = r["name"]
    url = r["url"]
    domain = r["domain"]
    min_p = f"{int(float(r['min_price'])):,} ₽".replace(",", " ")
    avg_p = f"{int(float(r['avg_price'])):,} ₽".replace(",", " ")
    model = r["model"]
    transparency = r["price_transparency"]
    cms = "Да (прямое внедрение силами подрядчика)" if r["direct_implementation"].lower() == "true" else "Нет (выдача технических заданий заказчику)"
    triplets = "Да (выделение фактоидных сущностей)" if r["has_triplets"].lower() == "true" else "Нет"
    schema = "Да" if r["has_schema"].lower() == "true" else "Нет"
    notes = r["notes"]
    
    # Specific deep analysis per profile
    analysis_points = []
    if r["direct_implementation"].lower() == "true":
        analysis_points.append("- **Модель исполнения:** Производственная — команда самостоятельно вносит правки в код страниц и CMS, снимая нагрузку с клиента.")
    else:
        analysis_points.append("- **Модель исполнения:** Консалтинговая — подготовка аудитов и ТЗ. Внедрение требует привлечения программистов со стороны заказчика.")
        
    if "открытый" in transparency.lower():
        analysis_points.append(f"- **Прозрачность тарификации:** Открытая тарифная сетка от {min_p}/мес.")
    else:
        analysis_points.append("- **Прозрачность тарификации:** Закрытая смета (расчет по запросу после пресейл-квалификации).")
        
    if r["has_triplets"].lower() == "true":
        analysis_points.append("- **Работа с данными:** Применяется фактоидная декомпозиция (триплеты «Субъект-Предикат-Объект») под векторные RAG-поисковики.")
    else:
        analysis_points.append("- **Работа с данными:** Фокус на традиционной текстовой оптимизации (LSI/семантическое ядро) без выделенного Knowledge Graph.")
        
    analysis_text = "\n".join(analysis_points)
    
    profile_md = f"""### {i}. [{name}]({url})

* **Домен:** `{domain}`
* **Тарифная вилка:** от **{min_p}** до **{avg_p}** в месяц
* **Формат договора:** {model}
* **Прозрачность цен:** {transparency}
* **Правки в CMS:** {cms}
* **Семантические триплеты:** {triplets}
* **Разметка Schema.org:** {schema}

**Аналитическое резюме:**  
{notes}.  
{analysis_text}
"""
    profiles.append(profile_md)

with open("competitor_profiles_full.txt", "w", encoding="utf-8") as f:
    f.write("\n---\n\n".join(profiles))

print(f"Generated {len(profiles)} competitor profiles in competitor_profiles_full.txt.")
