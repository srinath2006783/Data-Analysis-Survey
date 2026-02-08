def get_age_bucket(age):
    if age is None:
        return None
    if 16 <= age <= 18:
        return "16–18"
    if 19 <= age <= 21:
        return "19–21"
    if 22 <= age <= 24:
        return "22–24"
    return "out_of_range"