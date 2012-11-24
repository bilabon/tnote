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
from django.core.urlresolvers import reverse

INDEX_URL = reverse('index')
ADD_URL = reverse('add')
ASITE_URL = reverse('asite')
RANDOMNOTE_URL = reverse('randomnote')


class CheckAccessURL(TestCase):
    """
    Check access URLs.
    """
    def test_access_index_url(self):
        """
        Check index url.
        """
        response = self.client.get(INDEX_URL, HTTP_HOST='127.0.0.1',)
        self.assertEqual(response.status_code, 200)

    def test_access_add_url(self):
        """
        Check adding note URL.
        """
        response = self.client.get(ADD_URL)
        self.assertEqual(response.status_code, 200)

    def test_access_asite_url(self):
        """
        Check ASITE_URL url.
        Test independent widget that can be inserted in any page.
        """
        response = self.client.get(ASITE_URL, HTTP_HOST='127.0.0.1', )
        widget_line = '<script src="http://127.0.0.1/randomnote/" '
        widget_line += 'type="text/javascript"></script>'
        self.assertEqual(response.status_code, 200)
        self.assertIn(widget_line, response.content)

    def test_access_randomnote_page(self):
        """
        Check url that use widget for return random note
        """
        response = self.client.get(RANDOMNOTE_URL)
        self.assertEqual(response.status_code, 200)

    def test_access_admin_page(self):
        """
        Check /admin/ url
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
        template = Template('''{% load custom_tags %}
                                               {% render_one_text_note 4 %}''')
        context = RequestContext({})
        self.assertIn('test_text_TemplateTagsTestCase',
                                                      template.render(context))

    def test_custom_context_processor(self):
        """
        Test custom context processor which pass
        total count of notes to templates.
        """
        Entry.objects.create(text='text of note')
        template = Template('{{ total_count_of_notes }}')
        context = RequestContext({})
        count = Entry.objects.count()
        self.assertIn(str(count), template.render(context))

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


class NoteFormTests(TestCase):
    """
    Tests note form submit:
    -check submit form note without javascript.
    -check submit form note with enable javascript.
    -check submit form note with attached image without javascript.
    -check submit form note with attached image with enable javascript.
    """
    def test_submit_note_success(self):
        """
        Test success submit form note without javascript.
        """
        sometext = u'simple_text_12345'
        response = self.client.post(ADD_URL, {'text': sometext})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Note was successfully added.', response.content)
        obj = Entry.objects.get(text=sometext)
        self.assertEqual(sometext, obj.text)

    def test_submit_note_fail(self):
        """
        Test fail submit form note without javascript.
        """
        sometext = u's_text'
        response = self.client.post(ADD_URL, {'text': sometext})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Your note must be at least 10 characters.',
                                                              response.content)

    def test_ajax_submit_note_success(self):
        """
        Test success submit form note with enable javascript.
        """
        sometext = u'simple_text_12345'
        response = self.client.post(ADD_URL, {'text': sometext},
                                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Note was successfully added.', response.content)
        obj = Entry.objects.get(text=sometext)
        self.assertEqual(sometext, obj.text)

    def test_ajax_submit_note_fail(self):
        """
        Test fail submit form note with enable javascript.
        """
        sometext = u's_text'
        response = self.client.post(ADD_URL, {'text': sometext},
                                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Your note must be at least 10 characters.',
                                                              response.content)

    def test_upload_img(self):
        """
        Test success submit form note with attached image
        with disable javascript.
        """
        sometext = u'simple_text_12345678'
        img = open(os.path.join(settings.PROJECT_ROOT,
                                            os.path.join('test', 'image.gif')))
        response = self.client.post(ADD_URL, {'imagefile': img,
                                              'text': sometext}, )
        img.close()
        self.assertIn('Note was successfully added.', response.content)
        self.assertEqual(response.status_code, 200)
        obj = Entry.objects.get(text=sometext)
        obj.imagefile.delete()

    def test_ajax_upload_img(self):
        """
        Test success submit form note with attached image
        with enable javascript.
        """
        sometext = u'simple_text_12345678'
        img = open(os.path.join(settings.PROJECT_ROOT,
                                            os.path.join('test', 'image.gif')))
        response = self.client.post(ADD_URL,
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
        Test submit form note with attached fail image
        with enable javascript.
        """
        sometext = u'simple_text_12345678'
        notimg = open(os.path.join(settings.PROJECT_ROOT,
                                            os.path.join('test', 'notimg')))
        response = self.client.post(ADD_URL,
                                    {
                                    'imagefile': notimg,
                                    'text': sometext
                                    },
                                     HTTP_X_REQUESTED_WITH='XMLHttpRequest', )
        notimg.close()
        self.assertIn('Some error with your image.', response.content)
        self.assertEqual(response.status_code, 200)
