import neologdn

def normalize_text(text):
    """对文本进行标准化处理"""
    return neologdn.normalize(text)

text = "私は　東京都に　住んで　います！"
normalized_text = normalize_text(text)
print(normalized_text)  # "私は東京都に住んでいます!"
