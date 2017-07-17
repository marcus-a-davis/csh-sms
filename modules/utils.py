from datetime import datetime

def quote(word):
    return "`" + str(word) + "`"

def date_string_to_date(date_string):
    return datetime.strptime(date_string, "%d/%m/%y")

def date_is_valid(date_string):
    try:
        date_string_to_date(date_string)
        return True
    except ValueError:
        return False

def date_string_ymd_to_date(date_string):
	return datetime.strptime(date_string.strip(), "%Y-%m-%d").date()


def date_string_mdy_to_date(date_string):
	return datetime.strptime(date_string.strip(), "%m-%d-%Y").date()

def datetime_string_mdy_to_datetime(date_string):
	return datetime.strptime(date_string.strip(), "%m/%d/%Y %I:%M:%S %p")

def get_current_time():
	return datetime.now()