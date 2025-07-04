
This is a terminal-based Japanese chatbot with two core features:
- 🧠 **Casual Chat with Kuro (クロ)** – An LLM-based assistant that responds in a simple, direct, and casual Japanese tone.
- 🈶 **Kanji to Hiragana Converter** – Instantly convert Japanese Kanji/Katakana text into Hiragana using `pykakasi`.

---

## 🛠 Features

- 🗣️ Live streaming chat with an LLM (supports `qwen3:1.7b` on Ollama server).
- ⛔ Press **P** during streaming to stop a long response.
- 🧠 Prompt includes full dialogue history.
- 🈳 Converts Kanji or Katakana into Hiragana for learning or clarification.

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/japanese_cht_bot.git
cd japanese_cht_bot
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\activate     # On Windows
# Or
source venv/bin/activate    # On Linux/macOS
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Bot

Make sure your Ollama server is running locally with `qwen3:1.7b` loaded.

```bash
ollama run qwen3:1.7b
```

Then in a second terminal, run:

```bash
python main.py
```

---

## 📦 Requirements

* Python 3.8+
* `requests`
* `pykakasi`
* `keyboard`
* Ollama with a local model like `qwen3:1.7b`

Install with:

```bash
pip install requests keyboard pykakasi
```

---

## 📝 Example Interaction

```
Please choose a number:
1. kanji to hiragana
2. normal chat
3. Exit

👤: こんにちは、クロ！
クロ: おはよう！元気？今日は何を話したい？
```

---
