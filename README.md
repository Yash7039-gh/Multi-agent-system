## 🧠 How It Works

You enter a topic
      │
      ▼
🔍 Researcher Agent  →  Gathers facts & trends
      │
      ▼
✍️  Writer Agent     →  Writes a structured report
      │
      ▼
✅ Reviewer Agent    →  Reviews & scores the report
      │
      ▼
📄 output/final_report.md
```

---

## 🚀 Quickstart

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Get FREE Groq API key
👉 https://console.groq.com → Sign up → Create API Key

### 3. Setup .env file
```bash
# Rename .env.example to .env
# Open .env and paste your key:
GROQ_API_KEY=your_key_here
```

### 4. Run!
```bash
python main.py
```

---

## 📁 Project Structure

```
multi-agent-v2/
├── main.py              ← Run this
├── llm_config.py        ← Groq API setup
├── requirements.txt     ← Only 3 packages!
├── .env.example         ← API key template
├── agents/
│   ├── researcher.py    ← Agent 1
│   ├── writer.py        ← Agent 2
│   └── reviewer.py      ← Agent 3
└── output/
    └── final_report.md  ← Generated report
```

---

## ⚙️ Tech Stack
- **Python 3.14+** ✅
- **Groq API** (free, ultra fast LLaMA 3)
- **python-dotenv**

