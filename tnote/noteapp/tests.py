"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.template import Context, Template
from tnote.noteapp.models import Entry


class MyTests(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 200)

    def test_admin(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)


class EntryTestCase(TestCase):
    def setUp(self):
        self.one = Entry.objects.create(text="text_1")
        self.two = Entry.objects.create(text="text_2")

    def testInBase(self):
        self.assertEqual(self.one.__unicode__(), 'text_1')
        self.assertEqual(self.two.__unicode__(), 'text_2')


class TemplateTagsTestCase(TestCase):
    def setUp(self):
        self.obj = Entry.objects.create(
                         text='test_text_TemplateTagsTestCase', id=4)

    def testViewsForObject(self):
        t = Template('{% load custom_tags %}{% render_one_text_note 4 %}')
        c = Context({'obj': self.obj})
        self.assertIn('test_text_TemplateTagsTestCase', t.render(c))
