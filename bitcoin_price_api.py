import requests

bitcoin = float(input('How much bitcoin do you have? '))

try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    data = response.json()
    price = data['bpi']['USD']['rate_float']
    print(f'The current price of bitcoin is: {price}')
    print(f'Your bitcoin is currently worth: {price * bitcoin}')

except Exception as e:
    print(e)
    print('There was an error')

