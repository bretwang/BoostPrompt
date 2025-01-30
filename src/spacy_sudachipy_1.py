import spacy

# 加载 GiNZA 模型（基于 spaCy）
nlp = spacy.load("ja_ginza")

# 解析文本
text = "国境の長いトンネルを抜けると雪国であった。 #小説 #文学 #雪国 #川端康成"
doc = nlp(text)

# 输出分词 + 依存关系
for token in doc:
    print(f"{token.text} - {token.dep_} -> {token.head.text}")
