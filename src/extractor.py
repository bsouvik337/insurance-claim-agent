import pdfplumber
import os

def extract_text(file_path):
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    elif file_path.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text

    else:
        raise ValueError("Unsupported file format")
import re

def extract_fields(text):
    fields = {}

    patterns = {
        "policyNumber": r"POLICY NUMBER[:\s]*([A-Z0-9\-]+)",
        "policyholderName": r"NAME OF INSURED.*?:\s*(.*)",
        "date": r"DATE OF LOSS[:\s]*([\d/]+)",
        "time": r"TIME[:\s]*(AM|PM|[\d:]+)",
        "location": r"LOCATION OF LOSS[:\s]*(.*)",
        "description": r"DESCRIPTION OF ACCIDENT[:\s]*(.*)",
        "estimatedDamage": r"ESTIMATE AMOUNT[:\s]*₹?([\d,]+)",
        "claimType": r"(injury|vehicle|property)"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        fields[key] = match.group(1).strip() if match else None

    return fields
