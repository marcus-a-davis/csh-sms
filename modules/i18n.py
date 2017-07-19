#TODO: Verify Hindi code.

def msg_subscribe(language):
    if language == "English":
        return "has been subscribed to CSH health reminders. Text STOP to unsubscribe."
    else:
        return "\xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xb7\xe0\xa4\xae\xe0\xa4\xbe \xe0\xa4\x95\xe0\xa4\xb0\xe0\xa5\x87\xe0\xa4\x82, \xe0\xa4\xb9\xe0\xa4\xae\xe0\xa4\xa8\xe0\xa5\x87 \xe0\xa4\x89\xe0\xa4\xb8 \xe0\xa4\xb8\xe0\xa4\x82\xe0\xa4\xa6\xe0\xa5\x87\xe0\xa4\xb6 \xe0\xa4\x95\xe0\xa5\x8b \xe0\xa4\xa8\xe0\xa4\xb9\xe0\xa5\x80\xe0\xa4\x82 \xe0\xa4\xb8\xe0\xa4\xae\xe0\xa4\x9d\xe0\xa4\xbe \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82. \xe0\xa4\xb8\xe0\xa4\xa6\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xa4\xe0\xa4\xbe \xe0\xa4\xb0\xe0\xa4\xa6\xe0\xa5\x8d\xe0\xa4\xa6 \xe0\xa4\x95\xe0\xa4\xb0\xe0\xa4\xa8\xe0\xa5\x87 \xe0\xa4\x95\xe0\xa5\x87 \xe0\xa4\xb2\xe0\xa4\xbf\xe0\xa4\x8f STOP \xe0\xa4\xb2\xe0\xa4\xbf\xe0\xa4\x96\xe0\xa5\x87\xe0\xa4\x82."


def msg_unsubscribe(language):
    if language == "English":
        return "You have been unsubscribed from CSH health reminders."
    else:
        return "\xe0\xa4\x86\xe0\xa4\xaa\xe0\xa4\x95\xe0\xa5\x80 \xe0\xa4\xb8\xe0\xa4\xa6\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xa4\xe0\xa4\xbe \xe0\xa4\xb8\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xaa\xe0\xa5\x8d\xe0\xa4\xa4 \xe0\xa4\x95\xe0\xa4\xb0 \xe0\xa4\xa6\xe0\xa5\x80 \xe0\xa4\x97\xe0\xa4\xaf\xe0\xa5\x80 \xe0\xa4\xb9\xe0\xa5\x88."


def msg_placeholder_child(language):
    if language == "English":
        return "Your child"
    if language == "Hindi":
        return "\xe0\xa4\x86\xe0\xa4\xaa\xe0\xa4\x95\xe0\xa4\xbe \xe0\xa4\xb6\xe0\xa4\xbf\xe0\xa4\xb6\xe0\xa5\x81"
    if language == "Gujarati":
        return "\xe0\xaa\xa4\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xb0\xe0\xab\x81\xe0\xaa\x82 \xe0\xaa\xac\xe0\xaa\xbe\xe0\xaa\xb3\xe0\xaa\x95"


def msg_failure(language):
    if language == "English":
        return "Sorry, we didn't understand that message. Text STOP to unsubscribe."
    else:
        return "\xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xb7\xe0\xa4\xae\xe0\xa4\xbe \xe0\xa4\x95\xe0\xa4\xb0\xe0\xa5\x87\xe0\xa4\x82, \xe0\xa4\xb9\xe0\xa4\xae\xe0\xa4\xa8\xe0\xa5\x87 \xe0\xa4\x89\xe0\xa4\xb8 \xe0\xa4\xb8\xe0\xa4\x82\xe0\xa4\xa6\xe0\xa5\x87\xe0\xa4\xb6 \xe0\xa4\x95\xe0\xa5\x8b \xe0\xa4\xa8\xe0\xa4\xb9\xe0\xa5\x80\xe0\xa4\x82 \xe0\xa4\xb8\xe0\xa4\xae"


def msg_failed_date(language):
    if language == "English":
        return "Sorry, the date format was incorrect. An example message is 'Remind Sai 14-01-17' where 'Sai' is your child's first name and '14-01-17'' is their birthday."
    else:
        return "\xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xb7\xe0\xa4\xae\xe0\xa4\xbe \xe0\xa4\x95\xe0\xa5\x80\xe0\xa4\x9c\xe0\xa4\xbf\xe0\xa4\xaf\xe0\xa5\x87, \xe0\xa4\xa4\xe0\xa4\xbe\xe0\xa4\xb0\xe0\xa5\x80\xe0\xa4\x96 \xe0\xa4\x95\xe0\xa4\xbe \xe0\xa4\xaa\xe0\xa5\x8d\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xb0\xe0\xa5\x82\xe0\xa4\xaa \xe0\xa4\x97\xe0\xa4\xb2\xe0\xa4\xa4 \xe0\xa4\xb9\xe0\xa5\x88."


def hindi_remind():
    return "\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xae\xe0\xa4\xb0\xe0\xa4\xa3"

def hindi_information():
    return "\xe0\xa4\x87\xe0\xa4\xa4\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa4\xbf\xe0\xa4\xb2\xe0\xa4\xbe"

def subscribe_keywords(language):
    if language == "English":
        return ["remind", "join"]
    elif language == "Hindi":
        return [hindi_remind(), hindi_information()]
    else:
        return []
