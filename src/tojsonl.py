import json

data = [
    {
        "text": "私は東京都に住んでいます。",
        "tokens": ["私", "は", "東京都", "に", "住ん", "で", "い", "ます", "。"],
    },
    {
        "text": "東京は日本の首都です。",
        "tokens": ["東京", "は", "日本", "の", "首都", "です", "。"],
    },
]

with open("../data/train_data.jsonl", "w", encoding="utf-8") as f:
    for entry in data:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
