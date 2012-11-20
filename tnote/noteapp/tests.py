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
from django.conf import settings


class CheckThatTheURLisAccessible(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 200)

    def test_asite(self):
        response = self.client.get('/asite/', HTTP_HOST='127.0.0.1',)
        c = '<script src="http://127.0.0.1/randomnote/" '
        c += 'type="text/javascript"></script>'
        self.assertEqual(response.status_code, 200)
        self.assertIn(c, response.content)

    def test_randomnote(self):
        response = self.client.get('/randomnote/')
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


class Forms_Submission_TestCase(TestCase):
    def test_add_note_success(self):
        _sometext = u'simple_text_12345'
        response = self.client.post('/add/', {'text': _sometext})

        self.assertEqual(response.status_code, 200)
        self.assertIn('Note was successfully added.', response.content)
        self.assertTrue(Entry.objects.get(text=_sometext))
        obj = Entry.objects.get(text=_sometext)
        self.assertEqual(_sometext, obj.text)

    def test_add_note_fail(self):
        _sometext = u's_text'
        response = self.client.post('/add/', {'text': _sometext})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Your note must be at least 10 characters.',
                                                              response.content)

    def test_ajax_add_note_success(self):
        _sometext = u'simple_text_12345'
        response = self.client.post('/add/', {'text': _sometext},
                                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Note was successfully added.', response.content)
        self.assertTrue(Entry.objects.get(text=_sometext))
        obj = Entry.objects.get(text=_sometext)
        self.assertEqual(_sometext, obj.text)

    def test_ajax_add_note_fail(self):
        _sometext = u's_text'
        response = self.client.post('/add/', {'text': _sometext},
                                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Your note must be at least 10 characters.',
                                                              response.content)

    def test_upload_img(self):
        _sometext = u'simple_text_12345678'
        f = open(settings.PROJECT_ROOT + '/test/image.gif')
        response = self.client.post('/add/', {'imagefile': f,
                                              'text': _sometext}, )
        f.close()
        self.assertIn('Note was successfully added.', response.content)
        self.assertEqual(response.status_code, 200)
        obj = Entry.objects.get(text=_sometext)
        self.assertTrue(settings.MEDIA_ROOT + obj.imagefile.name)
        obj.imagefile.delete()

    def test_ajax_upload_img(self):
        _sometext = u'simple_text_12345678'
        f = open(settings.PROJECT_ROOT + '/test/image.gif')
        response = self.client.post('/add/', {'imagefile': f,
                                              'text': _sometext},
                                        HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                    )
        f.close()
        self.assertIn('Note was successfully added.', response.content)
        self.assertEqual(response.status_code, 200)
        obj = Entry.objects.get(text=_sometext)
        self.assertTrue(settings.MEDIA_ROOT + obj.imagefile.name)
        obj.imagefile.delete()

    def test_ajax_upload_bad_img(self):
        _sometext = u'simple_text_12345678'
        f = open(settings.PROJECT_ROOT + '/test/text')
        response = self.client.post('/add/', {'imagefile': f,
                                              'text': _sometext},
                                        HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                    )
        f.close()
        self.assertIn('Some error with your image.', response.content)
        self.assertEqual(response.status_code, 200)
