print("🔥 UPDATED LOADER IS RUNNING 🔥")

import requests
import csv
from io import StringIO

from schema import SURVEY_SCHEMA
from normalizers import normalize_work_hours, normalize_screen_time
from age_utils import get_age_bucket


def clean_text(raw):
    if raw is None:
        return None

    value = str(raw)

    # Remove Google Forms / Sheets bullet artifacts and bad UTF-8 encodings
    value = value.replace("â€¢", "")
    value = value.replace("â\x80¢", "")
    value = value.replace("•", "")

    # Normalize spacing
    value = value.replace("\xa0", " ")
    value = value.strip()
    value = " ".join(value.split())

    return value


GOOGLE_SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/1Ir1opx8pkzwq5ggCw5VodGnK5n2V7mwWwJq-LrTVnjM/export?format=csv"


def load_and_normalize(_=None):
    response = requests.get(GOOGLE_SHEET_CSV_URL)
    response.raise_for_status()

    csv_data = StringIO(response.text)
    reader = csv.DictReader(csv_data)

    records = []

    for row in reader:
        record = {}

        for key, meta in SURVEY_SCHEMA.items():
            raw = row.get(meta["column"])

            if raw is None or raw == "":
                record[key] = None
                continue

            value = clean_text(raw)

            if meta["type"] == "int":
                record[key] = int(float(value))

            elif key == "work_hours":
                record[key] = normalize_work_hours(value)

            elif key == "screen_time":
                record[key] = normalize_screen_time(value)

            else:
                record[key] = value

        # derived fields (AFTER all parsing)
        record["age_bucket"] = get_age_bucket(record.get("age"))

        records.append(record)

    return records