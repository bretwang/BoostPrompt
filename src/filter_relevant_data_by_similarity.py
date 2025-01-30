from sentence_transformers import SentenceTransformer
import numpy as np

# 加载 Sentence-BERT 模型
model = SentenceTransformer('all-MiniLM-L6-v2')

def filter_relevant_data_by_similarity(data, query, max_tokens=2000):
    # 获取查询的嵌入表示
    query_embedding = model.encode([query])[0]

    relevant_data = []
    total_tokens = 0

    for entry in data:
        # 获取当前条目的嵌入表示
        entry_embedding = model.encode([entry["text"]])[0]
        
        # 计算查询与条目的余弦相似度
        similarity = np.dot(query_embedding, entry_embedding) / (np.linalg.norm(query_embedding) * np.linalg.norm(entry_embedding))
        print(similarity)
        if similarity > 0.7:  # 假设相似度大于0.7的条目相关
            print(entry["text"])
            token_count = len(entry["tokens"])
            if total_tokens + token_count <= max_tokens:
                relevant_data.append(entry["text"])
                total_tokens += token_count
            else:
                break

    return " ".join(relevant_data)

# 假设你有查询和数据
query = "日本の首都"
data = [
    {"text": "私は東京都に住んでいます。", "tokens": ["私", "は", "東京都", "に", "住ん", "で", "い", "ます", "。"]},
    {"text": "東京は日本の首都です。", "tokens": ["東京", "は", "日本", "の", "首都", "です", "。"]}
]

# 过滤相关数据
context = filter_relevant_data_by_similarity(data, query)
print(context)
