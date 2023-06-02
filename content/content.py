import os
import requests

# API address and port
api_address = 'localhost'
api_port = 8000

# Users, passwords and expected version access for tests
tests = [('life is beautiful', 1), ('that sucks', -1)]

for sentence, expected_score in tests:
    for version in ['/v1/sentiment', '/v2/sentiment']:
        # Sending the request
        response = requests.get(f'http://{api_address}:{api_port}{version}', params={'username': 'alice', 'password': 'wonderland', 'sentence': sentence})

        # Checking the response status
        if 'score' in response.json() and response.json()['score'] == expected_score:
            print(f'SUCCESS: The sentence "{sentence}" was scored as expected on {version}.')
            result = 'SUCCESS'
        else:
            print(f'FAILURE: The sentence "{sentence}" scoring test on {version} failed.')
            result = 'FAILURE'

        # Save results in Log file if LOG=1
        if os.environ.get('LOG') == '1':
            with open('api_test.log', 'a') as file:
                file.write(f'Content test for "{sentence}" on {version}: {result}\n')
