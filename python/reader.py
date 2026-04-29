from openai import OpenAI

# 1. 叫门卫，给地址
client = OpenAI(
    api_key="sk-uczqtpbvdihozplibyuvumlnmmhcaxuehogxbefxluykyfjm",
    base_url="https://api.siliconflow.cn/v1",
)

print("📂 正在潜入硬盘，读取 test.txt...")

# 2. 核心语法：安全打开物理文件并读取内容
with open("test.txt", "r", encoding="utf-8") as file:
    file_content = file.read()

print(f"✅ 读取成功！一共读取了 {len(file_content)} 个字符。")

# 3. 核心语法：使用 f-string 组装给 AI 的命令
my_prompt = f"""
你是一个温柔且专业的职业规划导师。
请用 100 个字左右，总结下面这段文字的核心信息。不要废话，直接给结果。

要总结的文字如下：
{file_content}
"""

print("🚀 正在呼叫 AI 进行暴躁总结...\n")

# 4. 把组装好的请求发给 AI
response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3", messages=[{"role": "user", "content": my_prompt}]
)

# 5. 打印最终结果
print("🤖 暴躁总编：")
print(response.choices[0].message.content)
