import json

import mistune
import neologdn

# 读取 Markdown 文件
with open("../../data/markdown/1Q84.md", "r", encoding="utf-8") as f:
    md_content = f.read()

# # 解析 Markdown 提取纯文本
# def extract_text(md):
#     # return mistune.html(md).replace("<br>", "\n").replace("<p>", "").replace("</p>", "\n").strip()
#     return mistune.html(md).replace("<br>", "\n").replace("<p>", "").replace("</p>", "\n").replace("\n","").strip()

# clean_text = extract_text(md_content)


def normalize_text(text):
    """对文本进行标准化处理"""
    return neologdn.normalize(text)


clean_text = normalize_text(md_content).replace("\n", "")

# 输出 JSONL 格式
jsonl_data = {"text": clean_text}
with open("../../data/markdown/1Q84_clean_data2.txt", "w", encoding="utf-8") as f:
    f.write(json.dumps(jsonl_data, ensure_ascii=False) + "\n")

print("✅ 数据清洗完成，已保存为 clean_data.jsonl")
