import mock
import json
from mock import patch
from django.test import TestCase

from modules.textlocalwrapper import TextLocal
from mock import patch

class TextLocalInboxesTests(TestCase):
	def test_create_object(self):
		textlocal = TextLocal(TEXTLOCAL_API, TEXTLOCAL_PRIMARY_ID)
		self.assertIsInstance(textlocal, TextLocal)

	def test_is_message_new(self):
		textlocal = TextLocal(TEXTLOCAL_API, TEXTLOCAL_PRIMARY_ID)
		new_message = {'number': '910987654321', 'message': 'New message',
			'isNew': True}
		old_message = {'number': '910987654321', 'message': 'Old message',
			'isNew': None}

		self.assertTrue(textlocal.is_message_new(new_message))
		self.assertFalse(textlocal.is_message_new(old_message))

	def test_new_messages_by_number(self):
		textlocal = TextLocal(TEXTLOCAL_API, TEXTLOCAL_PRIMARY_ID)
		new_message = {'number': '910987654321', 'message': 'New message',
			'isNew': True}
		new_message2 = {'number': '910987654321', 'message': 'Newer message',
			'isNew': True}
		old_message = {'number': '910987654321', 'message': 'Old message',
			'isNew': None}
		fake_num_message_dict = textlocal.new_messages_by_number([new_message, new_message2, old_message])
		one_message_num_dict = textlocal.new_messages_by_number([new_message2])

		self.assertIsInstance(fake_num_message_dict, dict)
		self.assertIsInstance(one_message_num_dict, dict)
		self.assertIsInstance(fake_num_message_dict['910987654321'], list)
		self.assertFalse(old_message['message'] in fake_num_message_dict['910987654321'])
		self.assertTrue(new_message['message'] in fake_num_message_dict['910987654321'])
		self.assertTrue(new_message2['message'] in fake_num_message_dict['910987654321'])
		self.assertTrue(new_message2['message'] in one_message_num_dict['910987654321'])

	@patch("modules.textlocalwrapper.request")
    def test_get_primary_inbox_messages(self, mock_request):
        class MockResponse():
            def read(self):
                return json.dumps({'messages': 'yay'}).encode('latin1')
        mock_request.urlopen.return_value = MockResponse()
        textlocal = TextLocal(apikey='mock_key', primary_id='mock_id')
        self.assertEqual(textlocal.get_primary_inbox_messages(), 'yay')

	
	@patch("modules.textlocalwrapper.TextLocal.get_primary_inbox_messages")
	def test_unicode_inbox_messages(self, mock_primary_inbox_messages):
		textlocal = TextLocal(TEXTLOCAL_API, TEXTLOCAL_PRIMARY_ID)
		mock_primary_inbox_messages.return_value = [{'id': '000000024', 'number': 1112223334, 'message': 'Testy test', 'date': '2017-07-30 06:52:09', 'isNew': None, 'status': '?'},
			{'id': '00000449', 'number': 0, 'message': 'Example message testy', 'date': '2017-08-05 21:12:07', 'isNew': None, 'status': '?'}]

		self.assertIsInstance(textlocal.unicode_inbox_messages(), list)
		self.assertEqual(textlocal.unicode_inbox_messages(), [{'id': '000000024', 'number': 1112223334, 'message': 'Testy test', 'date': '2017-07-30 06:52:09', 'isNew': None, 'status': '?'},
			{'id': '00000449', 'number': 0, 'message': 'Example message testy', 'date': '2017-08-05 21:12:07', 'isNew': None, 'status': '?'}])
		mock_primary_inbox_messages.return_value = [{'id': '000000024', 'number': 1112223334, 'message': 'Join Tina 10-09-10', 'date': '2017-07-30 06:52:09', 'isNew': None, 'status': '?'},
			{'id': '00000449', 'number': 0, 'message': 'Remind Tina 09-12-10', 'date': '2017-08-05 21:12:07', 'isNew': None, 'status': '?'},
			{'id': '00000449', 'number': 0, 'message': 'Remind Tina 10-12-09', 'date': '2017-08-05 21:12:07', 'isNew': None, 'status': '?'}]
		self.assertEqual(textlocal.unicode_inbox_messages(), [{'id': '000000024', 'number': 1112223334, 'message': 'Join Tina 10-09-10', 'date': '2017-07-30 06:52:09', 'isNew': None, 'status': '?'},
			{'id': '00000449', 'number': 0, 'message': 'Remind Tina 09-12-10', 'date': '2017-08-05 21:12:07', 'isNew': None, 'status': '?'},
			{'id': '00000449', 'number': 0, 'message': 'Remind Tina 10-12-09', 'date': '2017-08-05 21:12:07', 'isNew': None, 'status': '?'}])
		mock_primary_inbox_messages.return_value = [{'id': '000000024', 'number': 1112223334, 'message': 'Join Tina 10/09/10', 'date': '2017-07-30 06:52:09', 'isNew': None, 'status': '?'},
			{'id': '00000449', 'number': 0, 'message': 'Remind Tina 09/12/10', 'date': '2017-08-05 21:12:07', 'isNew': None, 'status': '?'},
			{'id': '00000449', 'number': 0, 'message': 'Remind Tina 10/12/09', 'date': '2017-08-05 21:12:07', 'isNew': None, 'status': '?'}]
		self.assertEqual(textlocal.unicode_inbox_messages(), [{'id': '000000024', 'number': 1112223334, 'message': 'Join Tina 10/09/10', 'date': '2017-07-30 06:52:09', 'isNew': None, 'status': '?'},
			{'id': '00000449', 'number': 0, 'message': 'Remind Tina 09/12/10', 'date': '2017-08-05 21:12:07', 'isNew': None, 'status': '?'},
			{'id': '00000449', 'number': 0, 'message': 'Remind Tina 10/12/09', 'date': '2017-08-05 21:12:07', 'isNew': None, 'status': '?'}])
