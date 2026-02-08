import json

def generate_html_report(summary, article_text):
    summary_json = json.dumps(summary)

    article_html = "".join(
        f"<p>{p.strip()}</p>"
        for p in article_text.split("\n")
        if p.strip()
    )

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Stress & Burnout Survey Report</title>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>
body {{
    margin: 0;
    padding: 40px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, sans-serif;
    background: #f6f8fb;
    color: #2c3e50;
}}

.container {{
    max-width: 1100px;
    margin: auto;
}}

h1 {{
    font-size: 2.4rem;
}}

.subtitle {{
    color: #6b7280;
    margin-bottom: 40px;
}}

.section {{
    background: white;
    border-radius: 18px;
    padding: 28px;
    margin-bottom: 28px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
}}

.grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 24px;
}}

canvas {{
    max-height: 320px;
}}
</style>
</head>

<body>
<div class="container">

<h1>Stress, Burnout & Work–Life Balance</h1>
<p class="subtitle">
Pilot Survey • Ages 16–24 • {sum(summary["overall_risk"].values())} respondents
</p>

<div class="section">
<h2>Key Insights</h2>
<div style="font-size:1.05rem; line-height:1.7; color:#374151;">
{article_html}
</div>
</div>

<div class="section">
<h2>Overall Risk Distribution</h2>
<canvas id="overallRiskChart"></canvas>
</div>

<div class="section">
<h2>Risk Patterns</h2>
<div class="grid">
    <div>
        <h3>By Age Group</h3>
        <canvas id="ageChart"></canvas>
    </div>
    <div>
        <h3>By Role</h3>
        <canvas id="roleChart"></canvas>
    </div>
</div>
</div>

<div class="section">
<h2>Top Stress Causes (High Risk)</h2>
<ul>
"""

    for cause, count in summary["high_risk_causes"].items():
        html += f"<li><strong>{cause}</strong> — {count}</li>"

    html += """
</ul>
</div>

</div>

<script>
const summary = """ + summary_json + """;

// Overall risk
new Chart(document.getElementById("overallRiskChart"), {
    type: "doughnut",
    data: {
        labels: Object.keys(summary.overall_risk),
        datasets: [{
            data: Object.values(summary.overall_risk),
            backgroundColor: ["#2ecc71", "#f1c40f", "#e74c3c"]
        }]
    }
});

// Age-wise
const ageLabels = Object.keys(summary.age_risk);
const levels = ["Low", "Medium", "High"];

new Chart(document.getElementById("ageChart"), {
    type: "bar",
    data: {
        labels: ageLabels,
        datasets: levels.map(level => ({
            label: level,
            data: ageLabels.map(a => summary.age_risk[a][level] || 0),
            backgroundColor:
                level === "Low" ? "#2ecc71" :
                level === "Medium" ? "#f1c40f" : "#e74c3c"
        }))
    }
});

// Role-wise
const roleLabels = Object.keys(summary.role_risk);

new Chart(document.getElementById("roleChart"), {
    type: "bar",
    data: {
        labels: roleLabels,
        datasets: levels.map(level => ({
            label: level,
            data: roleLabels.map(r => summary.role_risk[r][level] || 0),
            backgroundColor:
                level === "Low" ? "#2ecc71" :
                level === "Medium" ? "#f1c40f" : "#e74c3c"
        }))
    }
});
</script>

</body>
</html>
"""
    return html