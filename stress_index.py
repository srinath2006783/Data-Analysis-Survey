def compute_stress_index(record):
    score = 0

    # stress level (1–5)
    if record.get("stress_level") is not None:
        score += record["stress_level"]

    # burnout
    burnout = record.get("burnout", "").lower()
    if burnout == "yes":
        score += 3
    elif burnout == "maybe":
        score += 1.5

    # personal time
    personal_time = record.get("personal_time", "").lower()
    if personal_time == "no":
        score += 3
    elif personal_time == "sometimes":
        score += 1.5

    return round(score, 1)


def classify_risk(score):
    if score >= 8:
        return "High"
    elif score >= 4:
        return "Medium"
    else:
        return "Low"