from datetime import datetime

DATE_FORMAT = "%d/%m/%Y"

def is_valid_text(text):
    return bool(text and text.strip())

def is_valid_date(text):
    try:
        datetime.strptime(text, DATE_FORMAT)
        return True
    except (ValueError, TypeError):
        return False

def is_valid_amount(amount):
    try:
        return float(amount) > 0
    except (ValueError, TypeError):
        return False

def is_not_future_date(text):
    if not is_valid_date(text):
        return False
    date = datetime.strptime(text, DATE_FORMAT)
    return date.date() <= datetime.now().date()
