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

Do not wrap the JSON inside markdown.

Do not use ```Json.

Do not explain everything.

Return exactly one json object.

The summary should capture every important idea

Do not omit important numbers.

Preserve names of people, organizations, places, and dates.

Return exactly this schema:

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

try:
    completion = client.chat.completions.create(
        model="nvidia/nemotron-3-ultra-550b-a55b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": article},
        ],
        response_format={"type":"json_object"},
        temperature=0.2,
    )
except Exception as e:
    print(e)
    exit()

response = completion.choices[0].message.content
response = response.strip()

if response.startswith("```"):
    response = response.split("```")[1]
    if response.startswith("json"):
        response = response[4:]

try:
    data = json.loads(response)
except json.JSONDecodeError:
    print("Model didn't return valid JSON. Raw response:")
    print(response)
    exit()

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

word_count = len(article.split())
reading_time = max(1, round(word_count / 200))

print("\nEstimated Reading Time: ")
print(f"{reading_time} min read ({word_count} words)")