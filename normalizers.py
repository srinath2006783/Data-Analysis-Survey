def normalize_work_hours(value):
    mapping = {
        "Less than 5": 4,
        "5–6": 5.5,
        "7–8": 7.5,
        "More than 8": 9
    }
    return mapping.get(value, None)


def normalize_screen_time(value):
    mapping = {
        "Less than 2 hours": 1,
        "2–4 hours": 3,
        "4–6 hours": 5,
        "More than 6 hours": 7
    }
    return mapping.get(value, None)