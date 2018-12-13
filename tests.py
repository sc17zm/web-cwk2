import os
import unittest
from app import db, app
TEST_DB = 'tests.db'

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(os.path.abspath(os.path.dirname(__file__)), TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        pass

    def test_home(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_login(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_addbook(self):
        response = self.app.get('/addbook/<username>', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_searchbook(self):
        response = self.app.get('/searchbook/<username>', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_allthebooks(self):
        response = self.app.get('/allthebooks/<username>', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_editpassword(self):
        response = self.app.get('/editpassword/<username>', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

 



if __name__ == '__main__':
    unittest.main()
