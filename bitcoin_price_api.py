"This is program asks the user how much bitcoin they have, and then makes an API request to retrieve some information. The API it calls"
"stores information on the current exchange rate for bitcoin. With this exchange rate information, the program calculates how much the user's"
"bitcoin is worth in dollars."

from multiprocessing.sharedctypes import Value
import requests

def main():
    
        bitcoin = get_bitcoin_amount()
        result = calculate_bitcoin(bitcoin)
        display_results(result)

def get_bitcoin_amount(): # mock 1

    while True:
        try:
            amount = float(input('How much bitcoin do you have? '))
            if amount <= 0:
                raise ValueError('You must enter a value greater than 0.')
            return amount
        except:
            print('Please enter a valid number.')

def get_api_response(): # mock 2
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    return data['bpi']['USD']['rate_float']

def calculate_bitcoin(bitcoin):
    rate = get_api_response()
    answer = bitcoin * rate
    return answer

def display_results(result): # mock 3
    return print(f'Your bitcoin is currently worth: {result}')


if __name__ == '__main__':
    main()