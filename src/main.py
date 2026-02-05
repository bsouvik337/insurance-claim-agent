# src/main.py
import json
from extractor import extract_text, extract_fields
from validator import find_missing_fields
from llm_agent import llm_route_claim

INPUT_FILE = "data/fnol_sample.pdf"
OUTPUT_FILE = "output/result.json"

def main():
    text = extract_text(INPUT_FILE)
    fields = extract_fields(text)
    missing = find_missing_fields(fields)

    llm_result = llm_route_claim(fields, missing)

    result = {
        "extractedFields": fields,
        "missingFields": missing,
        **llm_result
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(result, f, indent=2)

    print("LLM-powered claim processed successfully")

if __name__ == "__main__":
    main()
