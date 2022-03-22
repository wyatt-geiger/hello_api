"This program uses unit tests to test bitcoing_price_api.py. It includes testing for user inputs, print statements, and API requests "
" to ensure that the program rejects invalid or unusual input."

import unittest 
from unittest import TestCase
from unittest.mock import patch 

import bitcoin_price_api

class TestBitcoinPriceAPI(TestCase):

    # this test tests user input from bitcoin_price_api.py
    @patch('builtins.input', side_effect=['2']) # side_effect inputs 2 in the test
    def test_get_bitcoin_amount(self, mock_input): # mock_input is required as an argument here or else program would crash
        amount = bitcoin_price_api.get_bitcoin_amount()
        self.assertEqual(2, amount)
        # 2 is equal to 2, so this test passes. if side_effect and assertEqual do not match test will fail

    # this test is similar to the one above, however it also inputs responses that should be rejected, namely non-numeric inputs
    @patch('builtins.input', side_effect=['test', 'ninja', 'testy1234', '2'])
    def test_get_bitcoin_amount_reject_non_numeric(self, mock_input):
        amount = bitcoin_price_api.get_bitcoin_amount()
        self.assertEqual(2, amount)

    # this test looks at values less than or equal to 0
    @patch('builtins.input', side_effect=['-1', '-1000', '0', '2'])
    def test_get_bitcoin_amount_reject_less_zero(self, mock_input):
        amount = bitcoin_price_api.get_bitcoin_amount()
        self.assertEqual(2, amount)

    # this test looks at the print statement and ensures it is correct
    @patch('builtins.print')
    def test_display_results(self, mock_print):
        bitcoin_price_api.display_results(10)
        mock_print.assert_called_once_with('Your bitcoin is currently worth: 10')

    # testing an api response using sample information
    @patch('bitcoin_price_api.get_api_response')
    def test_calculate_bitcoin(self, mock_rates):
        mock_rate = 123.4567
        example_api_response = {"bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"40,628.4720","description":"United States Dollar","rate_float":mock_rate}}}
        mock_rates.side_effect = [ example_api_response["bpi"]["USD"]["rate_float"] ]
        converted = bitcoin_price_api.calculate_bitcoin(100)
        expected = 12345.67
        self.assertEqual(expected, converted)

    # alternate method of coding the test above using requests.Response.json
    @patch('requests.Response.json')
    def test_calculate_bitcoin(self, mock_requests_json):
            mock_rate = 123.4567
            example_api_response = {"bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"40,628.4720","description":"United States Dollar","rate_float":mock_rate}}}
            mock_requests_json.return_value = example_api_response
            converted = bitcoin_price_api.calculate_bitcoin(100)
            expected = 12345.67
            self.assertEqual(expected, converted)


if __name__ == '__main__':
    unittest.main()