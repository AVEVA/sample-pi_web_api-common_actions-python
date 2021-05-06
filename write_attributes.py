""" This script writes values through the PI Web API.

This python script requires some pre-requisites:
1.  A back-end server with PI WEB API with CORS enabled.
"""

import json
import getpass
import random
import requests
from urllib.parse import urlparse

from datetime import date, time, datetime, timedelta
from requests.auth import HTTPBasicAuth
from requests_kerberos import HTTPKerberosAuth

OSI_AF_ATTRIBUTE_TAG = 'OSIPythonAttributeSampleTag'
OSI_AF_DATABASE = 'OSIPythonDatabase'
OSI_AF_ELEMENT = 'OSIPythonElement'


def call_headers(include_content_type):
    """ Create API call headers
        @includeContentType boolean: Flag determines whether or not the
        content-type header is included
    """
    if include_content_type is True:
        header = {
            'content-type': 'application/json',
            'X-Requested-With': 'XmlHttpRequest'
        }
    else:
        header = {
            'X-Requested-With': 'XmlHttpRequest'
        }

    return header


def call_security_method(security_method, user_name, user_password):
    """ Create API call security method
        @param security_method string: Security method to use: basic or kerberos
        @param user_name string: The user's credentials name
        @param user_password string: The user's credentials password
    """

    from requests.auth import HTTPBasicAuth
    from requests_kerberos import HTTPKerberosAuth

    if security_method.lower() == 'basic':
        security_auth = HTTPBasicAuth(user_name, user_password)
    else:
        security_auth = HTTPKerberosAuth(mutual_authentication='REQUIRED',
                                         sanitize_mutual_error_response=False)

    return security_auth


def create_test_data():
    """ Create sample data used by subsequent calls """
    requestBody = []
    today = date.today()
    midnight = time()
    timestamp = datetime.combine(today - timedelta(days=+2), midnight)

    for _ in range(100):
        requestData = {
            'Timestamp': timestamp.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'Value': '{:.4f}'.format(random.random() * 10)
        }
        requestBody.append(requestData)
        timestamp -= timedelta(minutes=+5)

    return requestBody


def write_single_value(piwebapi_url, asset_server, user_name, user_password,
                       piwebapi_security_method, verify_ssl):
    """ Write a single value to the sampleTag
        @param piwebapi_url string: The URL of the PI Web API
        @param asset_server string: Name of the Asset Server
        @param user_name string: The user's credentials name
        @param user_password string: The user's credentials password
        @param piwebapi_security_method string: Security method: basic or kerberos
        @param verify_ssl: If certificate verification will be performed
    """
    print('writeSingleValue')

    #  create security method - basic or kerberos
    security_method = call_security_method(
        piwebapi_security_method, user_name, user_password)

    #  Get the sample tag
    request_url = '{}/attributes?path=\\\\{}\\{}\\{}|{}'.format(
        piwebapi_url, asset_server, OSI_AF_DATABASE, OSI_AF_ELEMENT, OSI_AF_ATTRIBUTE_TAG)
    response = requests.get(request_url, auth=security_method, verify=verify_ssl)

    #  Only continue if the first request was successful
    if response.status_code == 200:
        #  Deserialize the JSON Response
        data = json.loads(response.text)

        #  Create the data for this call
        data_value = random.randint(1, 100)
        request_body = {
            'Value': data_value
        }

        #  Create the header
        header = call_headers(True)

        #  Write the single value to the tag
        response = requests.post(data['Links']['Value'], auth=security_method,
                                 verify=verify_ssl, json=request_body, headers=header)

        if response.status_code == 202:
            print('Attribute SampleTag write value ' + str(data_value))
        else:
            print(response.status_code, response.reason, response.text)
    else:
        print(response.status_code, response.reason, response.text)
    return response.status_code


def write_data_set(piwebapi_url, asset_server, user_name, user_password, piwebapi_security_method, verify_ssl):
    """ Write a set of recorded values to the sampleTag
        @param piwebapi_url string: The URL of the PI Web API
        @param asset_server string: Name of the Asset Server
        @param user_name string: The user's credentials name
        @param user_password string: The user's credentials password
        @param piwebapi_security_method string: Security method: basic or kerberos
        @param verify_ssl: If certificate verification will be performed
    """
    print('writeDataSet')

    #  create security method - basic or kerberos
    security_method = call_security_method(
        piwebapi_security_method, user_name, user_password)

    # Get the sample tag
    request_url = '{}/attributes?path=\\\\{}\\{}\\{}|{}'.format(
        piwebapi_url, asset_server, OSI_AF_DATABASE, OSI_AF_ELEMENT, OSI_AF_ATTRIBUTE_TAG)
    url = urlparse(request_url)

    # Validate URL
    assert url.scheme == 'https'
    assert url.geturl().startswith(piwebapi_url)

    response = requests.get(url.geturl(), auth=security_method, verify=verify_ssl)

    #  Only continue if the first request was successful
    if response.status_code == 200:
        #  Deserialize the JSON Response
        data = json.loads(response.text)

        #  Get the data for this call
        dataset = create_test_data()

        #  Create the header
        header = call_headers(True)

        url = urlparse(piwebapi_url + '/streams/' +
                       data['WebId'] + '/recorded')
        # Validate URL
        assert url.scheme == 'https'
        assert url.geturl().startswith(piwebapi_url)

        #  write the set of values to the tag
        response = requests.post(url.geturl(),
                                 auth=security_method, verify=verify_ssl, json=dataset, headers=header)

        if response.status_code == 202:
            print('Attribute SampleTag streamed 100 values')
        else:
            print(response.status_code, response.reason, response.text)
    else:
        print(response.status_code, response.reason, response.text)
    return response.status_code


def update_attribute_value(piwebapi_url, asset_server, user_name, user_password,
                           piwebapi_security_method, verify_ssl):
    """ Update an element attribute value
        @param piwebapi_url string: The URL of the PI Web API
        @param asset_server string: Name of the Asset Server
        @param user_name string: The user's credentials name
        @param user_password string: The user's credentials password
        @param piwebapi_security_method string: Security method: basic or kerberos
        @param verify_ssl: If certificate verification will be performed
    """
    print('updateAttributeValue')

    #  create security method - basic or kerberos
    security_method = call_security_method(
        piwebapi_security_method, user_name, user_password)

    #  Get the active attribute for the sample tag
    request_url = '{}/attributes?path=\\\\{}\\{}\\{}|Active'.format(
        piwebapi_url, asset_server, OSI_AF_DATABASE, OSI_AF_ELEMENT)
    response = requests.get(request_url, auth=security_method, verify=verify_ssl)

    #  Only continue if the first request was successful
    if response.status_code == 200:
        #  Deserialize the JSON Response
        data = json.loads(response.text)

        #  Create the data for this call
        request_body = {
            'Value': True
        }

        #  Create the header
        header = call_headers(True)

        #  Write the value to the Active attribute of the sample tag
        response = requests.put(data['Links']['Value'], auth=security_method,
                                verify=verify_ssl, json=request_body, headers=header)

        if response.status_code == 204:
            print('Attribute Active value set to true')
        else:
            print(response.status_code, response.reason, response.text)
    else:
        print(response.status_code, response.reason, response.text)
    return response.status_code


def main():
    """ Main method. Receive user input and call the write value methods """
    piwebapi_url = str(input('Enter the PI Web API url: '))
    af_server_name = str(input('Enter the Asset Server Name: '))
    piwebapi_user = str(input('Enter the user name: '))
    piwebapi_password = str(getpass.getpass('Enter the password: '))
    piwebapi_security_method = str(
        input('Enter the security method, Basic or Kerberos: '))
    piwebapi_security_method = piwebapi_security_method.lower()
    verify_ssl_string = str(input('Verify certificates? (Y/N): '))

    if (verify_ssl_string.upper() == "N"):
        print('Not verifying certificates poses a security risk and is not recommended')
        verify_ssl = False
    else:
        verify_ssl = True

    # Comment the method calls below when running unit tests
    write_data_set(piwebapi_url, af_server_name, piwebapi_user, piwebapi_password,
                   piwebapi_security_method, verify_ssl)
    write_single_value(piwebapi_url, af_server_name, piwebapi_user, piwebapi_password,
                       piwebapi_security_method, verify_ssl)
    update_attribute_value(piwebapi_url, af_server_name, piwebapi_user, piwebapi_password,
                           piwebapi_security_method, verify_ssl)


if __name__ == '__main__':
    main()
