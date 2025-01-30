import requests

from similarity import filter_relevant_data_by_similarity, load_jsonl


def generate_answer(question):
    url = "http://localhost:11434/api/generate"

    # 加载数据文件
    data_file_path = (
        "../../data/markdown/1Q84_knowledge_points.jsonl"  # 请替换为你的 JSONL 文件路径
    )
    data = load_jsonl(data_file_path)

    # 使用 filter_relevant_data_by_similarity 函数处理数据
    relevant_data = filter_relevant_data_by_similarity(data, question)

    # print(relevant_data)

    # 构建提示模板
    prompt = f"""
      以下の知識ポイントに基づいて質問に答えてください：
      {chr(10).join(relevant_data)}
      
      質問：{question}
      """

    # 请求的 payload 数据（通常是字典格式）
    data = {"model": "deepseek-r1:14b", "prompt": prompt, "stream": False}

    # 可选的 HTTP 头部信息
    headers = {
        "Content-Type": "application/json",  # 如果是 JSON 格式
        # 'Authorization': 'Bearer YOUR_API_KEY'
    }

    # 发送 POST 请求
    response = requests.post(url, json=data, headers=headers)

    # # 打印返回的状态码和响应内容
    # print('Status Code:', response.status_code)
    # print('Response Body:', response.text)

    return response.text


print(
    generate_answer(
        "青豆が育った宗教団体と「さきがけ」の関係性にはどのようなものがあるのでしょうか？"
    )
)
