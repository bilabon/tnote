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

    def test_renderbytag(self):
        response = self.client.get('/renderbytag/')
        self.assertEqual(response.status_code, 200)

    def test_admin(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)


from tnote.noteapp.models import Entry


class EntryTestCase(TestCase):
    def setUp(self):
        self.one = Entry.objects.create(title="title_1", text="text_1",
                                       date="2012-7-07 19:21:36.369778")
        self.two = Entry.objects.create(title="title_2", text="text_2",
                                       date="2012-8-07 19:21:36.369778")

    def testInBase(self):
        self.assertEqual(self.one.__unicode__(), 'title_1')
        self.assertEqual(self.two.__unicode__(), 'title_2')

from django.template import Context
from django.template import Template


class TemplateTagsTestCase(TestCase):

    def setUp(self):
        self.obj = Entry.objects.create(text='test_text')

    def testViewsForObject(self):
        t = Template('{% load custom_tags %}{% render_one_text_note %}')
        c = Context({'obj': self.obj})
        self.assertEqual(t.render(c), '<ul><li>test_text</li></ul>\n')
