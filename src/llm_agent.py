from openai import OpenAI, RateLimitError

client = OpenAI()

def llm_route_claim(fields, missing_fields):
    try:
        prompt = f"""
        FNOL Fields:
        {fields}

        Missing Fields:
        {missing_fields}

        Decide:
        1. Claim type
        2. Recommended route
        3. Short reasoning
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an insurance FNOL processing agent."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        content = response.choices[0].message.content

        return {
            "recommendedRoute": "LLM Decision",
            "reasoning": content.strip()
        }

    except RateLimitError:
        if missing_fields:
            return {
                "recommendedRoute": "Manual Review",
                "reasoning": "LLM unavailable due to quota. Mandatory FNOL fields are missing."
            }

        return {
            "recommendedRoute": "Straight Through Processing",
            "reasoning": "LLM unavailable due to quota. All mandatory FNOL fields present."
        }
