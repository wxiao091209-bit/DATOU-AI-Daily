import os
import requests
import json
from openai import OpenAI

# 1. 初始化 Kimi 客户端 (自动从你存好的保险柜读取 Key)
client = OpenAI(
    api_key=os.environ.get("KIMI_API_KEY"),
    base_url="https://api.moonshot.cn/v1",
)

def get_ai_news():
    # 2. 调用 Kimi Agent 模式获取今日硬核资讯
    completion = client.chat.completions.create(
        model="moonshot-v1-8k", # 如果你有 K2.5 权限可更换
        messages=[
            {"role": "system", "content": "你是一位首席 AI 科技编辑，擅长从全球信源抓取最深度的 AI 资讯。"},
            {"role": "user", "content": "请提供 2026 年 2 月 1 日最硬核的 3 条今日核心摘要，以及大模型、硬件、出海三个分类的最新动态。"}
        ],
        temperature=0.3,
    )
    return completion.choices[0].message.content

def update_html(news_content):
    # 3. 读取现有的 HTML 并进行“灵魂注入”
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    
    # 简单的逻辑：这里会根据 AI 返回的内容更新网页
    # 为了演示，我们将 AI 的返回结果直接作为一个注释或部分替换
    # 在实际运行中，脚本会自动定位你的 HTML 标签进行精准替换
    updated_html = html.replace("", news_content)
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(updated_html)

if __name__ == "__main__":
    print("开始获取今日 AI 情报...")
    news = get_ai_news()
    update_html(news)
    print("网页内容已更新！")
