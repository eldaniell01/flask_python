
from flask import current_app
from flask_testing import TestCase
from flask import current_app, url_for

from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        
        return app
    
    def test_app(self):
        self.assertIsNotNone(current_app)
        
    def test_app_state(self):
        self.assertTrue(current_app.config['TESTING'])
        
    def test_index_hello(self):
        response = self.client.get(url_for('index'))
        self. assertRedirects(response, url_for('index'))
    def test_hello_(self):
        response = self.client.get(url_for('hello'))
        self. assert200(response) 
        
    def test_hello_post(self):
        fake_form={
            'username': 'fake',
            'passwork':'fake_pass'
        }
        response = self.client.psort(url_for('hello'), data=fake_form)
        self.assertRedirects(response, url_for('index'))    
   