"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.template import Template, RequestContext
from tnote.noteapp.models import Entry
from tnote.noteapp.widgets import DynamicAmount
from django.conf import settings
import os


class CheckUrl(TestCase):
    """
    Check URLs
    """
    def test_index(self):
        """
        Test index url
        """
        response = self.client.get('/', HTTP_HOST='127.0.0.1',)
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        """
        Test /add/ url
        """
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 200)

    def test_asite(self):
        """
        Test /asite/ url
        Test independent widget that can be inserted in any page.
        """
        response = self.client.get('/asite/', HTTP_HOST='127.0.0.1',)
        strn = '<script src="http://127.0.0.1/randomnote/" '
        strn += 'type="text/javascript"></script>'
        self.assertEqual(response.status_code, 200)
        self.assertIn(strn, response.content)

    def test_randomnote(self):
        """
        Test /randomnote/ url
        """
        response = self.client.get('/randomnote/')
        self.assertEqual(response.status_code, 200)

    def test_admin(self):
        """
        Test /admin/ url
        """
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)


class CustomTests(TestCase):
    """
    Tests:
    - custom template tag
    - custom context processor
    - custom widget
    """
    def test_custom_template_tag(self):
        """
        Check custom template tag that will render one text note
        by given id of note.
        """
        Entry.objects.create(text='test_text_TemplateTagsTestCase', id=4)
        tmpl = Template('{% load custom_tags %}{% render_one_text_note 4 %}')
        rcont = RequestContext({})
        self.assertIn('test_text_TemplateTagsTestCase', tmpl.render(rcont))

    def test_custom_context_processor(self):
        """
        Test custom context processor which pass amount to templates.
        """
        Entry.objects.create(text='text of note')
        tmpl = Template('{{ total_count_of_notes }}')
        rcont = RequestContext({})
        count = Entry.objects.count()
        self.assertIn(str(count), tmpl.render(rcont))

    def test_custom_widget(self):
        """
        Test custom widget that extends Textarea widget.
        """
        widget = DynamicAmount()
        self.assertHTMLEqual(widget.render('msg', ''),
                '<textarea rows="10" cols="100" name="msg"></textarea>')
        widget = DynamicAmount(attrs={'rows': '50', 'cols': '50'})
        self.assertHTMLEqual(widget.render('msg', ''),
                '<textarea rows="50" cols="50" name="msg"></textarea>')


class TestsForm(TestCase):
    """
    Tests of form submission
    """
    def test_submit_success(self):
        """
        Test success submit without javascript.
        """
        sometext = u'simple_text_12345'
        response = self.client.post('/add/', {'text': sometext})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Note was successfully added.', response.content)
        self.assertTrue(Entry.objects.get(text=sometext))
        obj = Entry.objects.get(text=sometext)
        self.assertEqual(sometext, obj.text)

    def test_submit_fail(self):
        """
        Test fail submit without javascript.
        """
        sometext = u's_text'
        response = self.client.post('/add/', {'text': sometext})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Your note must be at least 10 characters.',
                                                              response.content)

    def test_ajax_submit_success(self):
        """
        Test success submit with enable javascript.
        """
        sometext = u'simple_text_12345'
        response = self.client.post('/add/', {'text': sometext},
                                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Note was successfully added.', response.content)
        self.assertTrue(Entry.objects.get(text=sometext))
        obj = Entry.objects.get(text=sometext)
        self.assertEqual(sometext, obj.text)

    def test_ajax_submit_fail(self):
        """
        Test success submit with enable javascript.
        """
        sometext = u's_text'
        response = self.client.post('/add/', {'text': sometext},
                                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Your note must be at least 10 characters.',
                                                              response.content)

    def test_upload_img(self):
        """
        Test success upload image with disable javascript.
        """
        sometext = u'simple_text_12345678'
        img = open(os.path.join(settings.PROJECT_ROOT,
                                            os.path.join('test', 'image.gif')))
        response = self.client.post('/add/', {'imagefile': img,
                                              'text': sometext}, )
        img.close()
        self.assertIn('Note was successfully added.', response.content)
        self.assertEqual(response.status_code, 200)
        obj = Entry.objects.get(text=sometext)
        obj.imagefile.delete()

    def test_ajax_upload_img(self):
        """
        Test success upload image with enable javascript.
        """
        sometext = u'simple_text_12345678'
        img = open(os.path.join(settings.PROJECT_ROOT,
                                            os.path.join('test', 'image.gif')))
        response = self.client.post('/add/',
                                    {
                                    'imagefile': img,
                                    'text': sometext
                                    },
                                     HTTP_X_REQUESTED_WITH='XMLHttpRequest', )
        img.close()
        self.assertIn('Note was successfully added.', response.content)
        self.assertEqual(response.status_code, 200)
        obj = Entry.objects.get(text=sometext)
        obj.imagefile.delete()

    def test_ajax_upload_fail_img(self):
        """
        Test fail upload image with enable javascript.
        """
        sometext = u'simple_text_12345678'
        notimg = open(os.path.join(settings.PROJECT_ROOT,
                                            os.path.join('test', 'notimg')))
        response = self.client.post('/add/',
                                    {
                                    'imagefile': notimg,
                                    'text': sometext
                                    },
                                     HTTP_X_REQUESTED_WITH='XMLHttpRequest', )
        notimg.close()
        self.assertIn('Some error with your image.', response.content)
        self.assertEqual(response.status_code, 200)
