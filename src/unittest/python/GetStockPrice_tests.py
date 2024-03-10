"""
GetStockPRice_tests 
"""

import unittest, requests_mock
from get_stock_price import app


class TestGetStockPrice(unittest.TestCase):
    """
    TestGetStockPrice
    """

    def test_get_stock_price_success(self):
        """
        test_get_stock_price_success ()
        """
        symbol = "AAPL"
        expected_price = "170.73"
        with requests_mock.Mocker() as mocker:
            url = f"https://finance.yahoo.com/quote/AAPL"
            text = "<span>Current</span><span>170.73</span>"
            x = mocker.get(url, text=text)
            response = app.test_client().get(f"/stock/AAPL")
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data["symbol"], symbol)
            #self.assertEqual(data["price"], expected_price)

    def test_get_stock_price_failure(self):
        """
        test_get_stock_price_failure
        """
        symbol = "AAPL"
        with requests_mock.Mocker() as mocker:
            mocker.get(f"https://finance.yahoo.com/quote/AAPL", status_code=404)
            response = app.test_client().get(f"/stock/AAPL")
            data = response.get_json()
            self.assertEqual(response.status_code, 500)
            self.assertEqual(data["error"], "Failed to fetch stock price")


if __name__ == "__main__":
    unittest.main()
