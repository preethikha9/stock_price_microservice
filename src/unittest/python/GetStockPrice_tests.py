import unittest
from unittest.mock import patch
import requests_mock
from bs4 import BeautifulSoup
from get_stock_price import app  # Import the Flask app

class GetStockPriceTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()  # Create test client from the Flask app

    def test_get_stock_price(self):
        symbol = 'AAPL'
        expected_price = '170.73'
        with requests_mock.Mocker() as mocker:
            mocker.get(f"https://finance.yahoo.com/quote/{symbol}", text='<span>Current</span><span>170.73</span>')
            response = self.client.get(f'/stock/{symbol}')
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['symbol'], symbol)
            self.assertEqual(data['price'], expected_price)

    '''
    def test_get_stock_price_failure(self):
        symbol = 'AAPL'
        with requests_mock.Mocker() as mocker:
            mocker.get(f"https://finance.yahoo.com/quote/{symbol}", status_code=404)
            response = self.client.get(f'/stock/{symbol}')
            data = response.get_json()
            self.assertEqual(response.status_code, 500)
            self.assertEqual(data['error'], 'Failed to fetch stock price')
    '''
    
if __name__ == '__main__':
    unittest.main()
