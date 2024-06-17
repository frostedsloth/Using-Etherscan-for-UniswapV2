import requests

# Define the address and API key
address = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f'
api_key = 'x'

# Define the URL for the API request
url = f'https://api.etherscan.io/api?module=account&action=tokentx&address={address}&startblock=0&endblock=99999999&sort=asc&apikey={api_key}'

# Send the request and get the response
response = requests.get(url)
data = response.json()

# Check if the response contains the result
if 'result' in data:
    for tx in data['result']:
        print(f"Token: {tx['tokenSymbol']}, Value: {tx['value']}, From: {tx['from']}, To: {tx['to']}, TimeStamp: {tx['timeStamp']}")
else:
    print("No transactions found or there was an error in the request.")
