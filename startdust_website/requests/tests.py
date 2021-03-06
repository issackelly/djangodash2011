from django.test import TestCase
from requests.models import Request
from requests.forms import RequestForm


class RequestFormTestCase(TestCase):

    def test_request_form_should_use_request_model(self):
        '''
        RequestForm should use Request model
        '''
        self.assertEqual(Request, RequestForm._meta.model)

class RequestModelTestCase(TestCase):

    def test_request_model_should_have_url_attribute(self):
        '''
        Request model should have url attribute
        '''
        self.assertFieldIn('url', Request._meta.fields)

    def test_request_model_should_have_date_attribute(self):
        '''
        Request model should have date attribute
        '''
        self.assertFieldIn('date', Request._meta.fields)

    def test_request_model_should_be_related_with_project(self):
        '''
        Request model shoudl be related with Project model
        '''
        self.assertFieldIn('project', Request._meta.fields)

    def test_request_should_be_ordered_by_date(self):
        '''
        Request model should be ordered by date
        '''
        self.assertIn('date', Request._meta.ordering)

    def assertFieldIn(self, expected_field, field_list):
        '''
        assert if field in a field list
        '''
        self.assertTrue(expected_field in [field.name for field in field_list])
