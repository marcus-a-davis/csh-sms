import logging
import string

from django.utils import timezone

from management.models import Contact, Group
from modules.texter import send_text
from modules.utils import quote, add_contact_to_group
from modules.date_helper import date_is_valid, date_string_to_date
from modules.i18n import msg_subscribe, msg_unsubscribe, msg_placeholder_child, msg_failure, \
                         msg_failed_date, subscribe_keywords


class TextProcessor(object):
    def create_contact(self, child_name, date, language, phone_number):
        created_at = datetime.now(tzinfo=timezone.get_default_timezone())
        contact, _ = Contact.objects.update_or_create(name=child_name,
                                                      phone_number=phone_number,
                                                      time_created=created_at,
                                                      delay_in_days=0,
                                                      language_preference=language,
                                                      date_of_birth=date,
                                                      date_of_sign_up=datetime.now().date(),
                                                      functional_date_of_birth=date,
                                                      method_of_sign_up="Text")

        for group_name in ["Text Sign Ups",
                           "Text Sign Ups - " + language,
                           "Everyone - " + language]:
            add_contact_to_group(contact, group_name)
        # TODO: Assign visit date


    def process_subscribe(self, keyword, child_name, date, language, phone_number):
        # TODO: Store data in the system
        return msg_subscribe(language).format(name=child_name)


    def process_unsubscribe(self, keyword, child_name, date, language, phone_number):
        # TODO: Mark data in the system as cancelled.
        return msg_unsubscribe(language)


    def process_failure(self, keyword, child_name, date, language, phone_number):
        return msg_failure(language)


    def process_failed_date(self, keyword, child_name, date, language, phone_number):
        return msg_failed_date(language)


    def get_data_from_message(self, message):
        """Get the keyword, child name, and the date from the message.
            A text will look like `<KEYWORD> <CHILD> <DATE OF BIRTH>`, like
            `REMIND NATHAN 25/11/2015`. Sometimes the child name is omitted."""
        message = message.lower().split(" ")
        if len(message) == 1:
            keyword = message[0]
            date = None
            child_name = None
        elif len(message) == 2:
            keyword, date = message
            child_name = None
        else:
            keyword, child_name, date = message[0:3]
        date = date_string_to_date(date) if date and date_is_valid(date) else None
        return (keyword, child_name, date)


    def process(self, message, phone_number):
        # TODO: Run this continuously to monitor incoming texts.
        """This is the main function that is run on an incoming text message to process it."""
        keyword, child_name, date = self.get_data_from_message(message)
        if keyword in subscribe_keywords("English"):
            language = "English"
            logging.info("Subscribing " + quote(message) + "...")
            action = self.process_subscribe
        elif keyword in subscribe_keywords("Hindi"):
            language = "Hindi"
            logging.info("Subscribing " + quote(message) + "...")
            action = self.process_subscribe
        elif keyword == "stop":
            language = "English"  # TODO: Language will have to be determined from database.
            logging.info("Unsubscribing " + quote(message) + "...")
            action = self.process_unsubscribe
        else:
            logging.error("Keyword " + quote(keyword) + " in message " + quote(message) +
                          " was not understood by the system.")
            language = "English" if keyword[0] in string.ascii_lowercase else "Hindi"
            action = self.process_failure

        if action == self.process_subscribe:
            if child_name is None:
                # If a child name is not found, we call them "your child".
                child_name = msg_placeholder_child(language)
            else:
                child_name = child_name.title()

            if date is None:
                logging.error("Date in message " + quote(message) + " is invalid.")
                action = self.process_failed_date

        response_text_message = action(keyword=keyword,
                                       child_name=child_name,
                                       date=date,
                                       language=language,
                                       phone_number=phone_number)
        send_text(message=response_text_message,
                  phone_number=phone_number)  # TODO: Actually implement this.
        return response_text_message
