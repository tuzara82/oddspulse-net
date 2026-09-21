import json
import random
from datetime import datetime

file_path = 'src/data/predictions.json'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    data = []

# 1. Симулиране на леки промени в съществуващите пазари
for item in data:
    # Премахваме старите "New entry" маркети след време или ги променяме
    if item.get('change') == 'New entry':
        item['change'] = '+1% this week'
    
    # Случайна промяна на процентите с -2% до +2%
    delta = random.choice([-2, -1, 1, 2])
    item['odds'] = max(10, min(98, item['odds'] + delta))
    
    sign = f"+{delta}% this week" if delta > 0 else f"{delta}% this week"
    item['change'] = sign

# 2. Нови актуални AI и технологични предложения (генерирани на база свежи тенденции)
new_ai_ideas = [
    {
        "title": "Will Agentic AI workflows handle over 50% of enterprise software tasks by end of 2027?",
        "slug": "agentic-ai-enterprise-tasks-2027",
        "category": "AI & Tech",
        "odds": 68,
        "change": "New entry",
        "summary": "As autonomous AI agents evolve past simple chatbots, market analysts project widespread integration into core corporate software infrastructure for complex multi-step automation."
    },
    {
        "title": "Will commercial Edge AI chips achieve 100 TOPS per watt efficiency before 2028?",
        "slug": "edge-ai-chips-efficiency-2028",
        "category": "AI & Tech",
        "odds": 54,
        "change": "New entry",
        "summary": "Hardware manufacturers are rapidly optimizing silicon architectures to bring high-performance neural processing directly to everyday consumer devices with minimal power draw."
    }
]

# Добавяме ново предложение на ротационен принцип или разбъркваме
if new_ai_ideas:
    # Добавяме първото ново предложение в началото на списъка
    candidate = new_ai_ideas[random.randint(0, len(new_ai_ideas) - 1)]
    # Проверяваме да няма дубликат по slug
    if not any(d['slug'] == candidate['slug'] for d in data):
        data.insert(0, candidate)

# Записваме обратно в JSON файла
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Market telemetry successfully updated at {datetime.now()}")
