import json
import random
from datetime import datetime

# Налични пазари за прогнози (синхронизирани с predictions.json)
MARKETS_POOL = [
    "Will commercial Edge AI chips achieve 100 TOPS per watt efficiency before 2028?",
    "Will SpaceX successfully land an uncrewed Starship on Mars before the end of 2026?",
    "Will the James Webb Space Telescope confirm atmospheric biosignatures on a rocky exoplanet by 2027?",
    "Will global renewable energy capacity surpass coal and gas combined in G20 nations by 2028?",
    "Will decentralized prediction markets exceed $10B in cumulative annual settlement volume by 2027?"
]

OUTCOMES = ["YES", "NO"]
SOURCES = ["System 1 Direct", "Jev Neural Core", "On-Chain Heuristic", "Macro Quant Model"]

def execute_jev_trade():
    # Зареждане на съществуващите сделки
    try:
        with open('src/data/trades.json', 'r', encoding='utf-8') as f:
            trades = json.load(f)
    except Exception as e:
        trades = []

    # Генериране на ново автономно решение в стил jev-trader
    market = random.choice(MARKETS_POOL)
    outcome = random.choice(OUTCOMES)
    confidence = round(random.uniform(85.0, 98.5), 1)
    size_usdc = random.choice([10, 25, 50, 100, 250])
    source = random.choice(SOURCES)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_trade = {
        "market": market,
        "outcome": outcome,
        "confidence": confidence,
        "sizeUsdc": size_usdc,
        "source": source,
        "timestamp": timestamp
    }

    # Добавяне на сделката най-отгоре и ограничаване до последните 5
    trades.insert(0, new_trade)
    trades = trades[:5]

    # Запис обратно в JSON файла за фронтенда
    with open('src/data/trades.json', 'w', encoding='utf-8') as f:
        json.dump(trades, f, indent=2, ensure_ascii=False)

    print(f"[{timestamp}] 🤖 Jev-Trader Decision Executed: BUY {outcome} on '{market[:30]}...' | Conf: {confidence}% | Size: ${size_usdc} USDC")

if __name__ == "__main__":
    execute_jev_trade()
