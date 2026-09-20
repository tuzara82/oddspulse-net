import json
import random
import os

DATA_PATH = "src/data/predictions.json"

NEW_TOPICS_POOL = [
    {
        "title": "Will artificial intelligence present an existential threat to humanity within the next 10 years?",
        "category": "AI & Tech",
        "summary": "Experts and alignment researchers debate the long-term containment risks of autonomous recursive self-improvement and superhuman general intelligence.",
        "odds": 10
    },
    {
        "title": "Will commercial nuclear fusion generate stable net electricity to the grid by 2032?",
        "category": "Space & Science",
        "summary": "Recent plasma confinement breakthroughs and private capital injections are pushing magnetic confinement fusion closer to pilot commercial viability."
    },
    {
        "title": "Will global electric vehicle sales exceed 60% of total new car sales worldwide?",
        "category": "Economy",
        "summary": "Rapid battery cost deflation and aggressive manufacturing scale-up across Asian and European markets are accelerating mass adoption."
    },
    {
        "title": "Will a sovereign nation adopt Bitcoin as an official national reserve asset by the end of 2027?",
        "category": "Crypto",
        "summary": "Macroeconomic pressures and sovereign debt concerns are prompting emerging economies to explore decentralized digital reserves.",
        "odds": 38
    },
    {
        "title": "Will humanity successfully establish a permanent crewed habitat on the surface of Mars before 2040?",
        "category": "Space",
        "summary": "Heavy-lift reusable rocketry and autonomous ISRU (In-Situ Resource Utilization) trials are accelerating interplanetary colonization timelines.",
        "odds": 45
    },
    {
        "title": "Will an autonomous AI system successfully orchestrate a major multinational cyber-defense grid intervention?",
        "category": "Geopolitics",
        "summary": "Nation-states are increasingly delegating real-time critical infrastructure security to advanced neural defence agents amid escalating state-sponsored attacks.",
        "odds": 55
    }
]

def update_predictions():
    if not os.path.exists(DATA_PATH):
        print("Error: predictions.json not found!")
        return

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        delta = random.randint(-2, 2)
        if delta == 0:
            delta = 1
            
        new_odds = max(2, min(98, item["odds"] + delta))
        item["odds"] = new_odds
        
        if delta > 0:
            item["trend"] = f"+{delta}% this week"
            item["trendUp"] = True
        else:
            item["trend"] = f"{delta}% this week"
            item["trendUp"] = False

        if "history" not in item:
            item["history"] = [item["odds"] - delta, item["odds"]]
        else:
            item["history"].append(new_odds)
            if len(item["history"]) > 6:
                item["history"] = item["history"][-6:]

    existing_titles = [p["title"] for p in data]
    for topic in NEW_TOPICS_POOL:
        if topic["title"] not in existing_titles:
            slug = topic["title"].lower().replace(" ", "-").replace("?", "").replace(",", "")[:40]
            initial_odds = topic.get("odds", random.randint(20, 60))
            new_entry = {
                "slug": slug,
                "title": topic["title"],
                "odds": initial_odds,
                "trend": "New entry",
                "trendUp": True,
                "category": topic["category"],
                "summary": topic["summary"],
                "history": [initial_odds - 2, initial_odds - 1, initial_odds]
            }
            data.append(new_entry)
            print(f"Added new market prediction: {topic['title']}")

    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("Market telemetry updated successfully with new geopolitical and crypto domains!")

if __name__ == "__main__":
    update_predictions()
