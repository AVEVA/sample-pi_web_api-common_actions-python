import json

# Try to open the configuration file
try:
    with open(
        'test_config.json',
        'r',
    ) as f:
        config = json.load(f)
except Exception as error:
    print(f'Error: {str(error)}')
    print(f'Could not open/read file: test_config.json')
    exit()

for endpoint in config['endpoints']:
  if(endpoint.get("endpoint-type").upper() == 'PI'):
    PIWEBAPI_URL = endpoint.get('resource')
    AF_SERVER_NAME = endpoint.get('asset-server-name')
    PI_SERVER_NAME = endpoint.get('data-server-name')
    USER_NAME = endpoint.get('username')
    USER_PASSWORD = endpoint.get('password')
    AUTH_TYPE = endpoint.get('auth-type', 'kerberos')
    VERIFY_SSL = endpoint.get('verify-ssl', True)
    break
