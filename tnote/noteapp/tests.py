"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.template import Context, Template, RequestContext
from tnote.noteapp.models import Entry
from tnote.noteapp.utils.context_processors import total_count_of_notes
from tnote.noteapp.widgets import DynamicAmountOfSymbols
from django.test.client import Client


class CheckThatTheURLisAccessible(TestCase):
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


class ContextProcessorsTestCase(TestCase):
    def setUp(self):
        self.obj = Entry.objects.create(text='text of note')

    def testTotalCountOfNotes(self):
        t = Template('{{ total_count_of_notes }}')
        c = RequestContext({'obj': self.obj})
        q = Entry.objects.count()
        self.assertIn(str(q), t.render(c))


class FormsWidgetsTestCase(TestCase):
    def test_dynamic_amount_of_symbols(self):
        w = DynamicAmountOfSymbols()
        self.assertHTMLEqual(w.render('msg', ''),
                '<textarea rows="10" cols="100" name="msg"></textarea>')
        w = DynamicAmountOfSymbols(attrs={'rows': '50', 'cols': '50'})
        self.assertHTMLEqual(w.render('msg', ''),
                '<textarea rows="50" cols="50" name="msg"></textarea>')
