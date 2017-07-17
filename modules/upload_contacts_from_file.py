import csv
import re
from modules import utils, visit_date_helper
from management.models import Contact

def csv_upload(filepath):
	with open(filepath) as csvfile:
		reader = csv.DictReader(csvfile)
		
		for row in reader:
			new_dict = make_contact_dict(row)
			
			try:
				new_contact = Contact.objects.get(name=new_dict["name"],phone_number=new_dict["phone_number"])
			except Contact.DoesNotExist:
				new_contact = Contact.objects.get_or_create(**new_dict)

def make_contact_dict(row):
	new_dict = {}
	new_dict["name"] = row["Name"]
	new_dict["phone_number"] = row["Phone Number"]
	new_dict["alt_phone_number"] = row["Alternative Phone"]
	new_dict["delay_in_days"] = parse_or_create_delay_num(row["Delay in days"])
	new_dict["language_preference"] = row["Language Preference"]
	
	new_dict["date_of_birth"] = entered_date_string_to_date(row["Date of Birth"])
	new_dict["date_of_sign_up"] = entered_date_string_to_date(row["Date of Sign Up"])
	new_dict["functional_date_of_birth"] = parse_or_create_functional_dob(row["Functional DoB"], new_dict["date_of_birth"], new_dict["delay_in_days"])

	# Personal Info
	new_dict["gender"] = row["Gender"]
	new_dict["mother_tongue"] = row["Mother Tongue"]
	new_dict["language_preference"] = row["Language Preference"]
	new_dict["religion"] = row["Religion"]
	new_dict["state"] = row["State"]
	new_dict["division"] = row["Division"]
	new_dict["district"] = row["District"]
	new_dict["city"] = row["City"]
	new_dict["monthly_income_rupees"] = monthly_income(row["Monthly Income"])
	new_dict["children_previously_vaccinated"] = previous_vaccination(row["Previously had children vaccinated"])
	new_dict["not_vaccinated_why"] = row["If not vaccinated why"]
	new_dict["mother_first_name"] = row["Mother's First"]
	new_dict["mother_last_name"] = row["Mother's Last"]


	# Type of Sign Up
	new_dict["method_of_sign_up"] = row["Method of Sign Up"]
	new_dict["org_sign_up"] = row["Org Sign Up"]
	new_dict["hospital_name"] = row["Hospital Name"]
	new_dict["doctor_name"] = row["Doctor Name"]
	new_dict["url_information"] = row["URL information"]

	# System Identification
	new_dict["telerivet_contact_id"] = row["Telerivet Contact ID"]
	new_dict["trial_id"] = row["Trial ID"]
	new_dict["trial_group"] = row["Trial Group"]

	# Message References
	new_dict["preferred_time"] = row["Preferred Time"]
	new_dict["script_selection"] = row["Script Selection"]
	new_dict["telerivet_sender_phone"] = row["Sender Phone"]

	# DateTimes to be fixed
	new_dict["last_heard_from"] = parse_contact_time_references(row["Last Heard From"])
	new_dict["last_contacted"] = parse_contact_time_references(row["Last Contacted"])
	new_dict["time_created"] = parse_contact_time_references(row["Time Created"])

	return new_dict


def previous_vaccination(row_entry):
	if "Y".lower() in row_entry:
		bool_val = True
	elif "N".lower() in row_entry:
		bool_val = False
	else:
		bool_val = None

	return bool_val

def monthly_income(row_entry):
	if not row_entry:
		inc_val = 999999
	elif re.search("\D+", row_entry):
		inc_val = 999999
	else:
		inc_val = int(row_entry)

	return inc_val

def parse_or_create_delay_num(row_entry):
	if not row_entry:
		delay = 0
	elif re.search("\D+", row_entry):
		delay = 0
	else:
		delay = int(row_entry)

	return delay

def entered_date_string_to_date(row_entry):
	try:
		ymd = utils.date_string_ymd_to_date(row_entry)
		return ymd
	except ValueError:
		mdy = utils.date_string_mdy_to_date(row_entry)
		return mdy

def parse_or_create_functional_dob(row_entry, date_of_birth, delay):
	if not row_entry:
		func_dob = visit_date_helper.add_or_subtract_days(date_of_birth, delay)
	else:
		func_dob =  entered_date_string_to_date(row_entry)

	return func_dob

def parse_contact_time_references(row_entry):
	if not row_entry:
		return utils.get_current_time()
	else:
		return utils.datetime_string_mdy_to_datetime(row_entry)