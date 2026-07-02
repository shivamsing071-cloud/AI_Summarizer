from openai import OpenAI
from dotenv import load_dotenv
import json
import os

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

SYSTEM_PROMPT = """
You are an expert article summarizer.

Return ONLY valid JSON.

{
    "title":"",
    "summary":"",
    "key_points":[],
    "sentiment":"",
    "category":""
}
"""

print("Paste your article (press Enter twice to finish):")

lines = []

while True:
    line = input()

    if line == "":
        break

    lines.append(line)

article = "\n".join(lines)

completion = client.chat.completions.create(
    model="nvidia/nemotron-3-ultra-550b-a55b",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": article},
    ],
    temperature=0.2,
)

response = completion.choices[0].message.content

data = json.loads(response)

print("\nTitle: ")
print(data["title"])

print("\nSummary: ")
print(data["summary"])

print("\nKey Points: ")
for point in data["key_points"]:
    print("-", point)

print("\nSentiment: ")
print(data["sentiment"])

print("\nCategory: ")
print(data["category"])