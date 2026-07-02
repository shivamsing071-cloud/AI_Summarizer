# Article Summarizer + Classifier

A CLI tool that takes any article — via URL or pasted text — and returns a structured summary using NVIDIA's Nemotron 3 Ultra model. Extracts title, summary, key points, sentiment, category, and estimated reading time.

---

## Demo

```
Enter 'url' or 'text': url
Enter article URL: https://example.com/some-article

Title:
OpenAI Announces GPT-5 With Reasoning Capabilities

Summary:
OpenAI has unveiled GPT-5, its most capable model to date, featuring
native reasoning and a 1M token context window. The model outperforms
all existing benchmarks on coding, math, and long-document tasks...

Key Points:
- GPT-5 achieves state-of-the-art results on AIME 2025 and SWE-Bench
- Context window expanded to 1 million tokens
- Available via API starting at $15 per million input tokens
- Sam Altman confirmed rollout begins Q3 2025

Sentiment:
Positive

Category:
Artificial Intelligence

Estimated Reading Time:
4 min read (812 words)
```

---

## Features

- **URL mode** — paste any article link, newspaper4k extracts the clean text automatically
- **Text mode** — paste any block of text directly into the terminal
- **Structured JSON output** — model returns title, summary, key points, sentiment, and category
- **Preserves details** — names, dates, numbers, and organizations are kept intact
- **Reading time** — calculated locally from word count (no extra API call)
- **Robust error handling** — graceful failure on bad URLs, failed extractions, and malformed model responses
- **JSON enforcement** — uses `response_format` + markdown stripping as a fallback to guarantee parseable output

---

## Tech Stack

- Python 3.10+
- [NVIDIA NIM API](https://build.nvidia.com) — Nemotron 3 Ultra 550B (free tier)
- [openai](https://pypi.org/project/openai/) Python SDK (OpenAI-compatible client)
- [newspaper4k](https://pypi.org/project/newspaper4k/) — article extraction
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/article-summarizer.git
cd article-summarizer
```

### 2. Install dependencies

```bash
pip install openai newspaper4k python-dotenv
```

### 3. Get your free NVIDIA API key

Go to [build.nvidia.com](https://build.nvidia.com). Sign in with a free NVIDIA Developer account (no credit card required). Open any model, click **Get API Key**, and copy your `nvapi-` key.

### 4. Set up your API key

Create a file called `.env` in the project root:

```
NVIDIA_API_KEY=nvapi-your_actual_key_here
```

### 5. Run the tool

```bash
python summarizer.py
```

---

## Usage

**URL mode** — fetches and parses the article automatically:
```
Enter 'url' or 'text': url
Enter article URL: https://yourlink.com/article
```

**Text mode** — paste any text, press Enter twice to submit:
```
Enter 'url' or 'text': text
Paste your article (press Enter twice to finish):
> [paste your text here]
>
```

---

## Project Structure

```
article-summarizer/
├── summarizer.py    # main application
├── .env             # your API key (never committed)
├── .gitignore       # excludes .env from git
└── README.md        # this file
```

---

## Why Nemotron 3 Ultra?

Nemotron 3 Ultra is a 550B parameter MoE model from NVIDIA with a 1M token context window — meaning it can handle extremely long articles without truncation. It's available completely free via the NVIDIA NIM API with no billing setup required, making it ideal for learning projects that need a powerful model without the cost.

---

## Why newspaper4k over BeautifulSoup?

BeautifulSoup gives you raw HTML parsing — you have to manually write logic to extract article text and filter out navbars, ads, footers, and everything else. `newspaper4k` is purpose-built for articles and handles all of that automatically, returning clean article text, title, authors, and publish date in one function call.

---

## What I Learned Building This

- How to use an OpenAI-compatible API with a different provider (NVIDIA NIM) — just swap `base_url` and `api_key`
- How `response_format: json_object` enforces structured output at the API level
- Why prompts need to be explicit — the difference between "return JSON" and spelling out the exact schema, forbidden behaviors, and preservation rules
- How article scraping works and why purpose-built libraries beat manual HTML parsing for this use case
- Defensive JSON parsing — always use `.get()` with fallbacks, never assume the model returned every key

---

## What I'd Improve Next

- Save output to a `.json` file with a timestamped filename
- Add a `--compare` flag that runs the same article through two different models and shows the output side by side
- Build a Streamlit UI so non-technical users can use it without the terminal
- Batch mode — accept a list of URLs from a `.txt` file and summarize all of them in sequence

---

## License

MIT
