import requests

# 目标 URL
url = 'http://localhost:11434/api/generate'

# 请求的 payload 数据（通常是字典格式）
data = {
  "model": "deepseek-r1:14b",
  "prompt": "9.11 和 9.8 哪个大",
  "stream": False
}

# 可选的 HTTP 头部信息
headers = {
    'Content-Type': 'application/json',  # 如果是 JSON 格式
    'Authorization': 'Bearer YOUR_API_KEY'
}

# 发送 POST 请求
response = requests.post(url, json=data, headers=headers)

# 打印返回的状态码和响应内容
print('Status Code:', response.status_code)
print('Response Body:', response.text)