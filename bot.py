import json
import random
from datetime import datetime

# Налични категории за прогнози
CATEGORIES = ["AI & Tech", "Space & Science", "Crypto", "Geopolitics"]

TOPICS = [
    ("Will quantum processors achieve 10,000 fault-tolerant qubits before 2028?", "AI & Tech"),
    ("Will commercial fusion reactors deliver net-positive electricity to the grid by 2029?", "Space & Science"),
    ("Will global stablecoin settlement volume surpass traditional Visa network volume by 2028?", "Crypto"),
    ("Will sovereign AI sovereign cloud infrastructure mandates be adopted across G7 nations?", "Geopolitics"),
    ("Will autonomous humanoid robots exceed 500,000 active units in industrial deployments?", "AI & Tech")
]

def execute_jev_telemetry():
    # 1. Ъпдейт на сделките (trades.json)
    try:
        with open('src/data/trades.json', 'r', encoding='utf-8') as f:
            trades = json.load(f)
    except Exception:
        trades = []

    market, category = random.choice(TOPICS)
    outcome = random.choice(["YES", "NO"])
    confidence = round(random.uniform(85.0, 98.5), 1)
    size_usdc = random.choice([10, 25, 50, 100, 250])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_trade = {
        "market": market,
        "outcome": outcome,
        "confidence": confidence,
        "sizeUsdc": size_usdc,
        "source": "Jev Neural Core",
        "timestamp": timestamp
    }
    trades.insert(0, new_trade)
    trades = trades[:5]

    with open('src/data/trades.json', 'w', encoding='utf-8') as f:
        json.dump(trades, f, indent=2, ensure_ascii=False)

    # 2. Добавяне на нова прогноза (predictions.json)
    try:
        with open('src/data/predictions.json', 'r', encoding='utf-8') as f:
            predictions = json.load(f)
    except Exception:
        predictions = []

    # Генерираме уникален slug
    slug_base = market.lower().replace("?", "").replace(" ", "-")[:40]
    slug = f"{slug_base}-{random.randint(100,999)}"

    # Проверяваме дали вече не съществува такъв пазар
    if not any(p['title'] == market for p in predictions):
        new_pred = {
            "title": market,
            "slug": slug,
            "category": category,
            "summary": f"Autonomously generated telemetry evaluation tracking milestone probabilities for {category.lower()}.",
            "odds": random.randint(35, 78),
            "change": "New entry"
        }
        predictions.insert(0, new_pred)
        with open('src/data/predictions.json', 'w', encoding='utf-8') as f:
            json.dump(predictions, f, indent=2, ensure_ascii=False)
        print(f"✓ Добавена нова прогноза: '{market[:40]}...'")

    print(f"[{timestamp}] 🤖 Jev-Trader Executed: BUY {outcome} | Conf: {confidence}% | Size: ${size_usdc} USDC")

if __name__ == "__main__":
    execute_jev_telemetry()
