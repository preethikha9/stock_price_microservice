#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
GetStockPrice
"""

from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/stock/<symbol>')
def get_stock_price(symbol):
    """
    GetStockPrice 
    """

    url = 'https://finance.yahoo.com/quote/{symbol}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        current_span = soup.find('span', string='Current')
        price_element = current_span.find_next_sibling('span')
        if price_element:
            stock_price = price_element.text
            return jsonify({'symbol': symbol, 'price': stock_price})
        else:
            return (jsonify({'error': 'Failed to fetch stock price'}),
                    500)
    else:
        return (jsonify({'error': 'Failed to fetch stock price'}), 500)

if __name__ == '__main__':
    app.run(debug=True)
