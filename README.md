# AI-agent-homework
AUO AI Agent實戰班課後作業

# AI Agent Homework (1-4)

This repository implements homework 1-4 from `課後作業_v1.pdf` using Python.

## Environment

- Python 3.10+
- OpenAI API key (`OPENAI_API_KEY`)

Install dependencies:

```bash
pip install -r requirements.txt
```

Set environment variables (PowerShell):

```powershell
$env:OPENAI_API_KEY = "your_key"
# Optional:
# $env:OPENAI_MODEL = "gpt-4o-mini"
# $env:OPENAI_EMBEDDING_MODEL = "text-embedding-3-small"
```

## Run

Use `PYTHONPATH=src` so local packages can be imported.

PowerShell:

```powershell
$env:PYTHONPATH = "src"
```

### Homework 1: Role chatbot (English vocabulary tutor)

```bash
python -m hw1_role_chatbot.main
```

### Homework 2: Calculator function calling

```bash
python -m hw2_calculator_fc.main
```

Tool schema and implementation are in:
- `src/hw2_calculator_fc/tools/calculator.py`

### Homework 3: RAG (Programming languages + ChromaDB)

Seed knowledge base:

```bash
python -m hw3_rag.seed_db
```

Run retrieval tests (3 query styles):

```bash
python -m hw3_rag.search_test
```

### Homework 4: Time + Weather tools

```bash
python -m hw4_multi_tools.main
```

Expected tool behavior examples:
- "現在幾點？" -> calls `get_current_time`
- "台北天氣如何？" -> calls `get_weather`
- "現在幾點？台北天氣好嗎？" -> calls both tools in one round

## Notes

- Weather data uses Open-Meteo public API (no weather API key required).
- ChromaDB persists under `data/chroma/`.

