# Data Analysis survey
# Data-Analysis-Survey  
### Stress, Burnout & Work–Life Balance Analysis (Age 16–24)

This project is a data-driven analysis of stress, burnout, and work–life balance among individuals aged 16–24.  
It combines structured survey analysis with a locally hosted Large Language Model (LLM) to produce a **newspaper-style explanatory report**, inspired by the tone of publications like *The Hindu* and *The Times of India*.

Rather than functioning as a dashboard, the system is designed to behave like a **data journalism pipeline** — transforming raw responses into readable, analytical insights.

---

## ✨ Key Features

- 📊 **Survey Data Analysis**
  - Processes Google Form responses exported as CSV
  - Computes stress indices and risk categories (Low / Medium / High)

- 🧠 **LLM-based Editorial Explainer**
  - Uses a local Ollama model (no cloud dependency)
  - Generates calm, analytical, newspaper-style explanations
  - Avoids advice, moralising, or therapeutic language

- 📰 **Narrative HTML Report**
  - Apple-style, minimal, aesthetic layout
  - Charts paired with contextual explanations
  - Designed to read like an editorial data feature, not a dashboard

- 🔁 **Repeatable & Live-Friendly**
  - Re-running the pipeline regenerates the report
  - Designed to reflect new form responses with minimal friction

---

## 🧱 Project Structure

```text
Data-Analysis-Survey/
├── main.py              # Orchestrates the full pipeline
├── loader.py            # Loads and cleans survey data
├── schema.py            # Defines expected data structure
├── normalizers.py       # Normalizes raw form inputs
├── stress_index.py      # Computes stress scores and risk levels
├── age_utils.py         # Age bucketing logic
├── llm_explainer.py     # Local LLM prompt + generation logic
├── html_report.py       # HTML report generator
├── .gitignore
└── README.md
