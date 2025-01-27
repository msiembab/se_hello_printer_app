import unittest
from hello_world import app


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output_json(self):
        rv = self.app.get('/?output=json')
        self.assertEqual(b'{ "imie":"Natalia", "msg":"Hello World!"}', rv.data)

    def test_msg_with_output_xml(self):
        rv = self.app.get('/?output=xml')
        expected = (b"<greetings><msg>Hello World!</msg>" +
                    b"<name>Natalia</name></greetings>")
        self.assertEqual(expected, rv.data)
