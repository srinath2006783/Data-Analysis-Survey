from loader import load_and_normalize
from stress_index import compute_stress_index, classify_risk
from collections import Counter, defaultdict
from llm_explainer import generate_llm_article

data = load_and_normalize("data/responses.csv")

print("Total responses:", len(data))

results = []

for record in data:
    score = compute_stress_index(record)
    risk = classify_risk(score)

    record["stress_index"] = score
    record["risk_level"] = risk

    results.append(record)

# show one sample
print("\nSample response:")
print(results[0])

# summary
risk_counts = Counter(r["risk_level"] for r in results)

print("\nRisk distribution:")
for level, count in risk_counts.items():
    print(level, ":", count)

# --- GROUP BY AGE BUCKET ---
age_group_risk = defaultdict(Counter)

for r in results:
    age_group_risk[r["age_bucket"]][r["risk_level"]] += 1

print("\nRisk distribution by age group:")
for age_bucket, counter in age_group_risk.items():
    print(f"\nAge {age_bucket}:")
    for level, count in counter.items():
        print(f"  {level}: {count}")

# --- GROUP BY ROLE ---
role_group_risk = defaultdict(Counter)

for r in results:
    role_group_risk[r["role"]][r["risk_level"]] += 1

print("\nRisk distribution by role:")
for role, counter in role_group_risk.items():
    print(f"\nRole: {role}")
    for level, count in counter.items():
        print(f"  {level}: {count}")

# --- TOP STRESS CAUSES FOR HIGH-RISK USERS ---
high_risk_causes = Counter(
    r["stress_cause"] for r in results if r["risk_level"] == "High"
)

print("\nTop stress causes among HIGH-risk users:")
for cause, count in high_risk_causes.most_common():
    print(f"  {cause}: {count}")

# --- PREPARE SUMMARY FOR LLM EXPLAINER ---
summary = {
    "overall_risk": dict(risk_counts),
    "age_risk": {k: dict(v) for k, v in age_group_risk.items()},
    "role_risk": {k: dict(v) for k, v in role_group_risk.items()},
    "high_risk_causes": dict(high_risk_causes)
}

print("\nSummary object prepared for LLM explainer.")
print("Generating LLM-written insight article...")
article_text = generate_llm_article(summary)

# --- GENERATE HTML REPORT ---
from html_report import generate_html_report

html_report = generate_html_report(summary, article_text)

with open("report.html", "w") as f:
    f.write(html_report)

print("HTML report generated: report.html")