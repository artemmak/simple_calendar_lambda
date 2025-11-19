from datetime import date

def count_days_to_new_year(current_date: date) -> int:
    new_year = date(current_date.year + 1, 1, 1)
    return (new_year - current_date).days

def count_days_between(fist_date: date, second_date: date) -> int:
    return abs((second_date - fist_date).days)

def is_weekend(input_date: date) -> bool:
    return input_date.weekday() >= 5
