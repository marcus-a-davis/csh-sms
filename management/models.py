from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
import datetime
from modules import visit_date_helper

# Create your models here.
class Contact(models.Model):

	# Vitals
	name = models.CharField(max_length=50)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
		message="Phone number must be entered in the format: '+9199999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], blank=False,
		max_length=20, default="012345") # validators should be a list
	alt_phone_number = models.CharField(validators=[phone_regex], blank=False,
		max_length=20, default="012345")
	date_of_birth = models.DateField(auto_now=False, auto_now_add=False,
		default=datetime.date.today)
	date_of_sign_up = models.DateField(auto_now=False, auto_now_add=False,
		default=datetime.date.today)
	delay_in_days = models.SmallIntegerField(default=0, blank=True)
	functional_date_of_birth = models.DateField(blank=True,auto_now=False,
		auto_now_add=False, default=datetime.date.today)

	# Personal Info
	gender = models.CharField(max_length=2, blank=True)
	mother_tongue = models.CharField(max_length=50, blank=True)
	state = models.CharField(max_length=20, blank=True)
	division = models.CharField(max_length=20, blank=True)
	district = models.CharField(max_length=20, blank=True)
	city = models.CharField(max_length=20, blank=True)
	monthly_income_rupees = models.IntegerField(blank=True, default=999999)
	religion = models.CharField(max_length=20, blank=True)
	children_previously_vaccinated = models.NullBooleanField()
	not_vaccinated_why = models.CharField(max_length=100, blank=True)
	mother_first_name = models.CharField(max_length=30, blank=True)
	mother_last_name = models.CharField(max_length=30, blank=True)
	
	# Type of Sign Up
	method_of_sign_up = models.CharField(max_length=20, blank=True)
	org_sign_up = models.CharField(max_length=20, blank=True)
	hospital_name = models.CharField(max_length=30, blank=True)
	doctor_name = models.CharField(max_length=30, blank=True)
	url_information = models.URLField(max_length=200, blank=True)


	def has_been_born(self):
		today = datetime.date.today()
		diff = today - self.date_of_birth
		return  diff >= datetime.timedelta(0)


	# System Identification
	telerivet_contact_id = models.CharField(max_length=50, blank=True)
	trial_id = models.CharField(max_length=20, blank=True)
	trial_group = models.CharField(max_length=20, blank=True)
	

	def set_visit_dates(self):
		standard_dates = visit_date_helper.get_modified_dates(self.date_of_birth)
		functional_dates = visit_date_helper.get_modified_dates(self.functional_date_of_birth)

		return standard_dates, functional_dates


	# Language Choices
	ENGLISH = "ENG"
	HINDI = "HIN"
	GUJARATI = "GUJ"
	LANGUAGE_CHOICES = (
		(ENGLISH, "English"),
		(HINDI, "Hindi"),
		(GUJARATI, "Gujarati")
		)

	language_preference = models.CharField(max_length=20, choices=LANGUAGE_CHOICES,
		default=ENGLISH)

	# Message References
	preferred_time = models.CharField(max_length=20, blank=True)
	script_selection = models.CharField(max_length=20, blank=True)
	telerivet_sender_phone = models.CharField(max_length=100, blank=True)
	telerivet_time_created = models.DateField(auto_now=False, auto_now_add=False,
		default=datetime.date.today)
	last_heard_from = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
	last_contacted = models.DateTimeField(auto_now=False, auto_now_add=False,default=timezone.now)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)


class Group(models.Model):
	name = models.CharField(max_length=50)
	contacts = models.ManyToManyField(Contact)


	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)


"""
List of Pre-existing groups in Telerivet
-----------------------
Telerivet Blocked
Cancelled Contacts
Cancelled Contacts - English
Cancelled Contacts - Hindi
Cancelled Contacts - Text Sign Ups
Cancelled Contacts - Text Sign Ups - English
Cancelled Contacts - Text Sign Ups - Hindi
Cancelled Contacts - Text Sign Ups - undefined
Cancelled Contacts - undefined
Everyone - English
Everyone - Gujarati	Everyone - Hindi
Everyone - Online Form
Everyone - Text Default Time
One Time Sign Up Message 06-02-17
Online Form
Online Form - English
Online Form - English - ENG
Online Form - English - ENG - Text Default Time
Online Form - Gujarati
Online Form - Gujarati - GUJ
Online Form - Gujarati - GUJ - Text Default Time
Online Form - Hindi
Online Form - Hindi - HND
Online Form - Hindi - HND - Text Default Time
Sample Contacts
Text Sign Ups
Text Sign Ups - English
Text Sign Ups - English - ENG
Text Sign Ups - English - ENG - Text Default Time
Text Sign Ups - Hindi
"""

class VisitDate(models.Model):
	contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
	name = models.CharField(max_length=50, blank=True)
	date = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return " - ".join(self.name, self.date)

	class Meta:
		ordering = ('name',)

class Message(models.Model):
	contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)
	body = models.CharField(max_length=300)

	# Message direction is Incoming or Outgoing
	direction = models.CharField(max_length=10)



	def __str__(self):
		return self.name
