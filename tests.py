import unittest
import requests
import json


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_sort_numbers(self):
        json_send = json.loads('{"data": "1,4,3,1,5,7,9,0,56,10"}')
        json_expected = json.loads('{"data": "0,1,1,3,4,5,7,9,10,56"}')
        response = requests.put('http://0.0.0.0:5000/', json=json_send)
        json_response = json.loads(response.text)
        print(f'\nJSON Sent : {json_send}\nExpected  : {json_expected}\nActual    : {json_response}')
        self.assertEqual(json_expected, json_response)

    def test_sort_alpha(self):
        json_send = json.loads('{"data": "1,4,3,1,5,799,9,0,56,10"}')
        json_expected = json.loads('{"data": "0,1,1,3,4,5,9,10,56,799"}')
        response = requests.put('http://0.0.0.0:5000/', json=json_send)
        json_response = json.loads(response.text)
        print(f'\nJSON Sent : {json_send}\nExpected  : {json_expected}\nActual    : {json_response}')
        self.assertEqual(json_expected, json_response)

    def test_sort_get(self):
        json_send = json.loads('{"data": "1,4,3,1,5,799,9,0,56,10"}')
        json_expected = json.loads('{"error": "Please use PUT or POST for your requests..."}')
        response = requests.get('http://0.0.0.0:5000/', json=json_send)
        json_response = json.loads(response.text)
        print(f'\nJSON Sent : {json_send}\nExpected  : {json_expected}\nActual    : {json_response}')
        self.assertEqual(json_expected, json_response)

    def test_sort_putting_NaN_in_request(self):
        json_send = json.loads('{"garbage": "asd,2,12,*,9,0,8,6,$,@,#,$,%,1,!,@,#"}')
        json_expected = json.loads('{"error": "Please use the following json format for your requests: {\'data\': \'0,1,2\'}"}')
        response = requests.put('http://0.0.0.0:5000/', json=json_send)
        json_response = json.loads(response.text)
        print(f'\nJSON Sent : {json_send}\nExpected  : {json_expected}\nActual    : {json_response}')
        self.assertEqual(json_expected, json_response)

    def test_sort_putting_garbage(self):
        json_send = b'52s3a6s1s\'2xA$as2'
        json_expected = json.loads('{"error": "Please use the following json format for your requests: {\'data\': \'0,1,2\'}"}')
        response = requests.put('http://0.0.0.0:5000/', json=json_send)
        json_response = json.loads(response.text)
        print(f'\nJSON Sent : {json_send}\nExpected  : {json_expected}\nActual    : {json_response}')
        self.assertEqual(json_expected, json_response)


if __name__ == '__main__':
    unittest.main()
