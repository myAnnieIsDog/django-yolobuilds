from django.contrib.messages.test import MessagesTestMixin
from django.test import TestCase


class MsgTestCase(MessagesTestMixin, TestCase):
    pass

# MessagesTestMixin.assertMessages(response, expected_messages, ordered=True)