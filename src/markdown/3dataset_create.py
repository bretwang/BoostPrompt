import spacy
import json

# 加载 spaCy 日语模型
nlp = spacy.load("ja_core_news_lg")

# 读取文本
with open("../../data/markdown/1Q84_clean_data.txt", "r", encoding="utf-8") as f:
    cleaned_text = f.read()

# 按字节长度分割文本
def split_text(text, max_bytes=49000):
    parts = []
    current_part = ""
    current_size = 0

    for sentence in text.split("。"):  # 句号拆分
        sentence += "。"  # 还原句号
        sentence_size = len(sentence.encode("utf-8"))  # 计算字节数

        if current_size + sentence_size > max_bytes:
            parts.append(current_part)
            current_part = sentence
            current_size = sentence_size
        else:
            current_part += sentence
            current_size += sentence_size

    if current_part:
        parts.append(current_part)

    return parts

# 拆分文本
text_parts = split_text(cleaned_text)

# 用 nlp.pipe() 处理多个文本块，提升性能
docs = list(nlp.pipe(text_parts))

knowledge_points = []

# 定义一个分类函数
def classify_sentence(entities):
    entity_types = [ent.label_ for ent in entities]
    
    if "DATE" in entity_types or "MONEY" in entity_types:
        return "fact"
    elif "PERSON" in entity_types or "ORG" in entity_types or "GPE" in entity_types:
        return "entity"
    else:
        return "concept"

# 处理所有句子
for doc in docs:
    for sent in doc.sents:
        entities = [ent for ent in sent.ents]
        if entities:  # 仅记录有实体的句子
            sentence_type = classify_sentence(entities)
            knowledge_points.append({
                "sentence": sent.text,
                "entities": [ent.text for ent in entities],
                "type": sentence_type
            })

# 输出 JSONL 文件
output_path = "../../data/markdown/1Q84_knowledge_points.jsonl"
with open(output_path, "w", encoding="utf-8") as f:
    for entry in knowledge_points:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

print(f"Processing complete. Output saved to {output_path}")