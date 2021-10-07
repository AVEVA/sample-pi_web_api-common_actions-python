import json

# Try to open the configuration file
try:
    with open(
        'appsettings.json',
        'r',
    ) as f:
        config = json.load(f)
except Exception as error:
    print(f'Error: {str(error)}')
    print(f'Could not open/read file: appsettings.json')
    exit()

PIWEBAPI_URL = config.get('Resource')
AF_SERVER_NAME = config.get('AFServerName')
PI_SERVER_NAME = config.get('DataArchiveName')
USER_NAME = config.get('Username')
USER_PASSWORD = config.get('Password')
AUTH_TYPE = config.get('AuthType', 'kerberos')
VERIFY_SSL = config.get('VerifySSL', True)

