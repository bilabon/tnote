"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class MyTests(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_admin(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)

from django.utils import unittest
from tnote.noteapp.models import Entry


class EntryTestCase(unittest.TestCase):
    def setUp(self):
        self.one = Entry.objects.create(title="title_1", text="text_1",
                                       date="2012-7-07 19:21:36.369778")
        self.two = Entry.objects.create(title="title_2", text="text_2",
                                       date="2012-8-07 19:21:36.369778")

    def testInBase(self):
        self.assertEqual(self.one.__unicode__(), 'title_1')
