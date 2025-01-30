from sudachipy import Dictionary

# 加载 Sudachi 词典
tokenizer = Dictionary().create()

text = "国境の長いトンネルを抜けると雪国であった。 #小説 #文学 #雪国 #川端康成"

# 选择不同分词粒度（A, B, C）
for mode in ["A", "B", "C"]:
    print(f"--- Mode {mode} ---")
    tokens = tokenizer.tokenize(text, mode)
    for token in tokens:
        print(f"{token.surface()} \t {token.part_of_speech()}")  # 词性
