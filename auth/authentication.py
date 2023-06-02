import os
import requests

#API address and port
api_address = 'localhost'
api_port = 8000

# Users and passwords for tests
credentials = [('alice', 'wonderland', 200), ('bob', 'builder', 200), ('clementine', 'mandarine', 403)]

for username, password, expected_status in credentials:
    # Sending the request
    response = requests.get(f'http://{api_address}:{api_port}/permissions', params={'username': username, 'password': password})
    
    # Checking the response status
    if response.status_code == expected_status:
        print(f'SUCCESS: {username} was authenticated as expected.')
        result = 'SUCCESS'
    else:
        print(f'FAILURE: {username} authentication test failed.')
        result = 'FAILURE'

    # Recording the results in the log file if LOG=1
    if os.environ.get('LOG') == '1':
        with open('api_test.log', 'a') as file:
            file.write(f'Authentication test for {username}: {result}\n')
