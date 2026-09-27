import json
from datetime import datetime, timedelta

# Зареждане на съществуващите статии
try:
    with open('src/data/posts.json', 'r', encoding='utf-8') as f:
        posts = json.load(f)
except Exception as e:
    posts = []

# Нова седмична статия, генерирана от AI Telemetry Grid
new_post = {
    "slug": f"weekly-telemetry-dispatch-{datetime.now().strftime('%Y-%U')}",
    "title": f"Weekly Telemetry Dispatch: Market Probabilities & AI Consensus for Week {datetime.now().strftime('%U')}",
    "date": datetime.now().strftime("%B %d, %Y"),
    "author": "Jev Autonomous Grid",
    "category": "AI & Research",
    "image": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=1200&auto=format&fit=crop",
    "summary": "Automated weekly synthesis tracking shifts in global geopolitics, on-chain BTC reserves, and commercial space milestones.",
    "content": "As the global macro landscape evolves through this week, our multi-agent telemetry framework has registered significant probability shifts across key prediction sectors. Automated consensus models indicate heightened volatility in sovereign reserve allocations, while decentralized prediction terminals record record-breaking engagement volumes. Our background trading bots continue to map these signals directly into live operational strategies."
}

# Проверка дали такава статия вече съществува за тази седмица
if not any(p['slug'] == new_post['slug'] for p in posts):
    posts.insert(0, new_post) # Добавяме я на първо място (най-нова)
    with open('src/data/posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)
    print("✓ Успешно добавена нова седмична статия в блога!")
else:
    print("ℹ Статия за тази седмица вече съществува.")
