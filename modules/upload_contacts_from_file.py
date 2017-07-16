import csv
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
	new_dict["delay_in_days"] = row["Delay in days"]
	new_dict["language_preference"] = row["Language Preference"]
	
	# Dates to be handled to ensure right date format is entered, YYYY-MM-DD
	# new_dict["date_of_birth"] = row["Date of Birth"]
	# new_dict["date_of_sign_up"] = row["Date of Sign Up"]
	# new_dict["functional_date_of_birth"] = row["Functional DoB"]


	# Fix delay in days to fill blanks
	if not new_dict["delay_in_days"]:
		new_dict["delay_in_days"] = 0
		
	return new_dict