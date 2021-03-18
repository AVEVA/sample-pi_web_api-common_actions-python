import configparser

config = configparser.ConfigParser()
config.read('test_config.ini')
app_config = {}
app_config['url'] = config.get('Configuration', 'PIWEBAPI_URL')
app_config['af'] = config.get('Configuration', 'AF_SERVER_NAME')
app_config['pi'] = config.get('Configuration', 'PI_SERVER_NAME')
app_config['user'] = config.get('Configuration', 'USER_NAME')
app_config['password'] = config.get('Configuration', 'USER_PASSWORD')
app_config['auth'] = config.get('Configuration', 'AUTH_TYPE')
