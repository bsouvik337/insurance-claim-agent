# Insurance Claim Agent (FNOL)

A lightweight Python-based agent for processing First Notice of Loss (FNOL)
documents using rule-based validation and an LLM-powered decision layer.

## Features
- Extracts key FNOL fields from PDF/text documents
- Identifies missing or inconsistent information
- Routes claims to appropriate workflows
- Provides human-readable reasoning
- LLM integration with graceful fallback (quota-safe)

## Project Structure
insurance_claim_agent/
├── data/
│ └── fnol_sample.pdf
├── output/
│ └── result.json
├── src/
│ ├── extractor.py
│ ├── validator.py
│ ├── router.py
│ ├── llm_agent.py
│ └── main.py
├── requirements.txt
└── README.md

The system integrates with OpenAI GPT as a lightweight decision agent. If API quota is unavailable, the agent falls back to rule-based routing while preserving the same interface. This ensures reliability and production-ready behavior.

## How to Run
```bash
pip install -r requirements.txt
python src/main.py
