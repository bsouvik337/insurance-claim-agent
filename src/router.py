def route_claim(fields, missing_fields):
    description = (fields.get("description") or "").lower()

    if missing_fields:
        return "Manual Review", "Mandatory fields missing"

    if any(word in description for word in ["fraud", "staged", "inconsistent"]):
        return "Investigation Flag", "Suspicious keywords detected"

    if fields.get("claimType") == "injury":
        return "Specialist Queue", "Injury related claim"

    try:
        damage = int(fields["estimatedDamage"].replace(",", ""))
        if damage < 25000:
            return "Fast-track", "Low estimated damage"
    except:
        pass

    return "Manual Review", "Default routing applied"
