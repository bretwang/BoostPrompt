import json
import numpy as np
from sentence_transformers import SentenceTransformer

# 加载 Sentence-BERT 模型
model = SentenceTransformer("all-MiniLM-L6-v2")

def load_jsonl(file_path):
    """读取 JSONL 文件并返回数据列表"""
    data = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            data.append(json.loads(line.strip()))
    return data

def filter_relevant_data_by_similarity(data, query, max_tokens=2000, similarity_threshold=0.7):
    """基于相似度筛选相关数据"""
    query_embedding = model.encode([query])[0]
    relevant_data = []
    total_tokens = 0
    
    for entry in data:
        entry_text = entry["sentence"]
        entry_embedding = model.encode([entry_text])[0]
        
        # 计算余弦相似度
        similarity = np.dot(query_embedding, entry_embedding) / (
            np.linalg.norm(query_embedding) * np.linalg.norm(entry_embedding)
        )
        
        if similarity > similarity_threshold:
            token_count = len(entry_text)  # 直接用字符长度作为近似 token 数量
            if total_tokens + token_count <= max_tokens:
                relevant_data.append(entry_text)
                total_tokens += token_count
            else:
                break
    return relevant_data
    # return "\n".join(relevant_data)

# def save_output_to_file(output, output_file):
#     """将筛选后的文本写入文件"""
#     with open(output_file, "w", encoding="utf-8") as file:
#         file.write(output)

# # 示例用法
# file_path = "../../data/markdown/1Q84_knowledge_points.jsonl"  # 请替换为你的 JSONL 文件路径
# output_file = "../../data/markdown/1Q84_prompt.txt"  # 结果输出文件
# query = "青豆が育った宗教団体と「さきがけ」の関係性にはどのようなものがあるのでしょうか？"
# data = load_jsonl(file_path)
# context = filter_relevant_data_by_similarity(data, query)
# save_output_to_file(context, output_file)
# print(f"筛选后的结果已保存到 {output_file}")
