MANDATORY_FIELDS = [
    "policyNumber",
    "policyholderName",
    "date",
    "location",
    "description",
    "claimType",
    "estimatedDamage"
]

def find_missing_fields(extracted_fields):
    missing = []
    for field in MANDATORY_FIELDS:
        if not extracted_fields.get(field):
            missing.append(field)
    return missing
