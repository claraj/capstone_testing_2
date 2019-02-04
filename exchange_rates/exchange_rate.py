""" Uses exchangeratesapi.io to get exchange rates
Validation, error handling omitted for clarity.  """

import requests

def main():
    currency = get_target_currency()
    dollars = get_dollar_amount()
    converted = convert_dollars_to_target(dollars, currency)
    display_result(dollars, currency, converted)

""" User input functions """
    
def get_target_currency():
    """ Get target currency, and return as uppercase symbol. 
    TODO add validation, error handling """
    currency = input('Enter target currency code e.g. EUR, CAD: ')
    return currency.upper()


def get_dollar_amount():
    """ Get number of dollars. 
    TODO add validation, error handling """
    return float(input('Enter amount of dollars to convert: '))


def convert_dollars_to_target(dollars, target_currency):
    """ Convert amount of dollars to target currency """
    exchange_rate = get_exchange_rate(target_currency)
    converted = convert(dollars, exchange_rate)
    return converted


def get_exchange_rate(currency):
    """ Call API and extra data from response """
    response = request_rates(currency)
    rate = extract_rate(response, currency)
    return rate 


def request_rates(currency):
    """ Perform API request, return response. TODO add error handling """
    params = {'base': 'USD', 'symbols': currency}
    url = 'https://api.exchangeratesapi.io/latest'
    return requests.get(url, params=params).json()


def extract_rate(rates, currency):
    """ Process the JSON response from the API, extract rate data. TODO add error handling  """
    print(rates, currency)
    return rates['rates'][currency]


def convert(amount, exchange_rate):
    """ Convert using the given exchange rate """
    return amount * exchange_rate


def display_result(dollars, currency, converted):
    """ Format and display the result """
    print(dollars, currency, converted )
    print(f'${dollars:.2f} is equivalent to {currency} {converted:.2f}')


if __name__ == '__main__':
    main()
