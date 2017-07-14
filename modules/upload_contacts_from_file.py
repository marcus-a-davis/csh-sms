import csv
from management.models import Contact

def csv_upload(filepath):
	with open(filepath) as csvfile:
		reader = csv.DictReader(csvfile)
		
		for row in reader:
			name = row["Name"]
			phone_number = row["Phone Number"]
			alt_phone_number = row["Alternative Phone"]
			date_of_birth = row["Date of Birth"]
			date_of_sign_up = row["Date of Sign Up"]
			delay_in_days = row["Delay in days"]
			functional_date_of_birth = row["Functional DoB"]
			language_preference = row["Language Preference"]

			# Format date to ensure right date format is entered

			# Fix delay in days to fill blanks
			if not delay_in_days:
				delay_in_days = 0
			
			try:
				new_contact = Contact.objects.get(name=name,phone_number=phone_number)
			except Contact.DoesNotExist:
				new_contact = Contact.objects.get_or_create(name=name,phone_number=phone_number, 
					alt_phone_number=alt_phone_number, delay_in_days = delay_in_days,
					language_preference=language_preference)