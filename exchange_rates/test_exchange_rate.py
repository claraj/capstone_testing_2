import unittest 
from unittest import TestCase
from unittest.mock import patch 

import exchange_rate

class TestExchangeRates(TestCase):

    @patch('exchange_rate.request_rates')
    def test_dollars_to_target(self, mock_rates):
        mock_rate = 12.34567   # Any number will do.  
        # As long as the JSON contains the data the program needs, it does not need to be a complete response
        example_api_response = {'base': 'USD', 'date': '2019-02-04', 'rates': {'EUR': mock_rate}}  
        mock_rates.side_effect = [ example_api_response ] 
        # 100 dollars is 1234.567 Euros at this made up exchange rate 
        converted = exchange_rate.convert_dollars_to_target(100, 'EUR')
        self.assertEqual(1234.567, converted)



    # Alternative test - patch the requests.get method, and also the json() method
    # Which one do you prefer?
    @patch('requests.get')
    def test_dollars_to_target_2(self, mock_requests_get):
        mock_rate = 123.4567
        example_api_response = {"rates":{"CAD": mock_rate},"base":"USD","date":"2020-10-02"}

        # Another mock for the mock_requests_get - the .json() method needs to return the example response
        mock_requests_get().json.return_value = example_api_response
        
        converted = exchange_rate.convert_dollars_to_target(100, 'CAD')
        expected = 12345.67
        self.assertEqual(expected, converted)



    # todo - test error conditions 
    # Currency symbol is not found,
    # Dollar value is not a number,
    # Connection errors to exchange rate API,
    # what else?


if __name__ == '__main__':
    unittest.main()
