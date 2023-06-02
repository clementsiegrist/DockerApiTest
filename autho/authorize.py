import os
import requests

# API address and port
api_address = 'localhost'
api_port = 8000

# Users, passwords and expected version access for tests
tests = [('alice', 'wonderland', ['/v1/sentiment', '/v2/sentiment']), ('bob', 'builder', ['/v1/sentiment'])]

for username, password, endpoints in tests:
    for endpoint in endpoints:
        # Sending the request
        response = requests.get(f'http://{api_address}:{api_port}{endpoint}', params={'username': username, 'password': password, 'sentence': 'test'})

        # Checking the response status
        if response.status_code == 200:
            print(f'SUCCESS: {username} has access to {endpoint} as expected.')
            result = 'SUCCESS'
        else:
            print(f'FAILURE: {username} access to {endpoint} test failed.')
            result = 'FAILURE'

        # Recording the results in the log file if LOG=1
        if os.environ.get('LOG') == '1':
            with open('api_test.log', 'a') as file:
                file.write(f'Authorization test for {username} on {endpoint}: {result}\n')
