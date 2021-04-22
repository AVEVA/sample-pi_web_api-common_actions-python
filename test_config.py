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
    PIWEBAPI_URL = config.get('resource')
    AF_SERVER_NAME = config.get('asset-server-name')
    PI_SERVER_NAME = config.get('data-server-name')
    USER_NAME = config.get('username')
    USER_PASSWORD = config.get('password')
    AUTH_TYPE = config.get('auth-type')
    VERIFY_SSL = config.get('verify-ssl')
    break
