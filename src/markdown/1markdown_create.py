from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("../../data/files/1Q84.pdf")
# print(result.text_content)

with open("../../data/markdown/1Q84.md", "w", encoding="utf-8") as file:
    file.write(result.text_content)
