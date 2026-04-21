# 🚀 AlphaEngine – AI-Powered Financial Analysis Agent

AlphaEngine is a multi-agent financial intelligence system designed to analyze stocks using fundamentals, technicals, valuation, and news signals, powered by LLMs and structured data pipelines.

---

## ✨ Features

- 📊 Multi-agent architecture:
  - Fundamental Analysis Agent
  - Technical Analysis Agent
  - Valuation Agent
  - News & Sentiment Agent
- 🧠 LLM-powered reasoning (ReAct / tool-calling)
- ⚡ Parallel agent execution for faster insights
- 📈 Structured output (Markdown / JSON)
- 🔌 Extensible via MCP (Model Context Protocol) tools
- 📰 Custom-trained news sentiment model (LoRA)

---

## 🏗️ Architecture

User Query
    ↓
LangGraph Orchestrator
    ↓
-------------------------------------------------
| Fundamental | Technical | Valuation | News AI |
-------------------------------------------------
    ↓
Summarizer Agent
    ↓
Final Investment Report

## 📦 Installation

### 1. Clone repo
```bash
git clone git@github.com:<your-username>/AlphaEngine.git
cd AlphaEngine
```
### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4.Set Environment Variables
```bash
OPENAI_API_KEY=your_key
HUGGINGFACE_TOKEN=your_token
```
### 5.Model Training
```bash
python train_qwen_risk.py
python train_qwen_sentiment.py
```
### 6. Test the trained model 
```bash
cd a-share-mcp-is-just-i-need
pip install baostock
python test_baostock.py
```


### 7. Usage
```bash
cd Financial-MCP-Agent
python main.py

example query
analyze("NVDA stock outlook for next 6 months")
```

### 8.Modeßl Details
Base model: Qwen / LLaMA
•	Method: LoRA fine-tuning
•	Dataset: Financial news with risk labels you could download from - risk data：https://huggingface.co/datasets/benstaf/risk_nasdaq
- sentiment data：https://huggingface.co/datasets/benstaf/



