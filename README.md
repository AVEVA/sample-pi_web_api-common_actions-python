# PI Web API Python Sample

**Version:** 1.0.33

[![Build Status](https://dev.azure.com/osieng/engineering/_apis/build/status/product-readiness/PI-System/aveva.sample-pi_web_api-common_actions-python?branchName=main)](https://dev.azure.com/osieng/engineering/_build/latest?definitionId=2663&branchName=main)

The sample code in this folder demonstrates how to utilize the PI Web API using Python. You must have already [installed Python](https://www.python.org/downloads/) in order to run this sample application.

## Getting Started

To run the sample code:

- Clone the GitHub repository
- Open the "sample-pi_web_api-common_actions-python" folder with your IDE
- Install the required modules by running the following command in the terminal: `pip install -r requirements.txt`
- Run the application using the following command in the terminal: `python .\program.py` where `program.py` is the program you want to run. e.g `python .\create_sandbox.py`

## Getting Started with Tests

To run the sample tests:

- The sample test is configured using the file [appsettings.placeholder.json](appsettings.placeholder.json). Before editing, rename this file to `appsettings.json`. This repository's `.gitignore` rules should prevent the file from ever being checked in to any fork or branch, to ensure credentials are not compromised.
- Open the test config file `appsettings.json`
- Replace the values with your system configuration.

For example:

```json
{
  "Resource": "PLACEHOLDER_REPLACE_WITH_PI_WEB_API_URL",
  "DataArchiveName": "PLACEHOLDER_REPLACE_WITH_DATA_ARCHIVE_NAME",
  "AFServerName": "PLACEHOLDER_REPLACE_WITH_AF_SERVER_NAME",
  "Username": "PLACEHOLDER_REPLACE_WITH_USERNAME",
  "Password": "PLACEHOLDER_REPLACE_WITH_PASSWORD",
  "AuthType": "kerberos",
  "VerifySSL": true
}
```

| Parameters      | Required | Type    | Description                                                                                               |
| --------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------- |
| Resource        | required | string  | The URL of the PI Web API                                                                                 |
| DataArchiveName | required | string  | The name of the PI Data Archive that is being sent to                                                     |
| AFServerName    | required | string  | The name of the AF server that is being sent to                                                           |
| Username        | required | string  | The username that is being used for authenticating to the PI Web API                                      |
| Password        | required | string  | The password that is being used for authenticating to the PI Web API                                      |
| AuthType        | optional | string  | The type of authentication to use when connecting to the PI Web API. By default this is set to "kerberos" |
| VerifySSL       | optional | boolean | A feature flag for verifying SSL when connecting to the PI Web API. By default this is set to true        |

- Each test file (prefixed as "test\_..."), can be run independently or all the tests can be run in a single instance via the `run_all_tests.py` file. **Note: while the tests can be ran individually, some test database, elements, templates, and attributes created within other tests or by the create_sandbox.py script. If these structures are not in place ahead of time, the tests will not function as intended and the API requests will likely return a 404 error**
- To run a single file, open the test file you wish to run: e.g. `.\test_batch.py`

- In the terminal, navigate to the test files and use the following command to run all the tests: `python .\run_all_tests.py` or to run a test individually: `python .\test_batch_call.py`

## System Configuration

In order to run this sample, you must configure PI Web API with the proper security to:

- Create an AF database
- Create AF categories
- Create AF templates
- Create AF elements with attributes
- Create PI Points associated with element attributes
- Write and read element attributes
- Delete all the above AF/PI Data Archive objects

In addition, PI Web API must be configured to allow CORS as follows:

| Attribute               | Value                                               | Type    |
| ----------------------- | --------------------------------------------------- | ------- |
| CorsExposedHeaders      | Allow,Content-Encoding,Content-Length,Date,Location | String  |
| CorsHeaders             | \*                                                  | String  |
| CorsMethods             | \*                                                  | String  |
| CorsOrigins             | [http://localhost:9876](http://localhost:9876)      | String  |
| CorsSupportsCredentials | True                                                | Boolean |
| DisableWrites           | False                                               | Boolean |

## Functionality

This sample shows basic functionality of the PI Web API, not every feature. The sample is meant to show a basic sample application that uses the PI Web API to read and write data to a PI Data Archive and AF. Tests are also included to verify that the code is functioning as expected.

The functionality included with this sample includes(recommended order of execution):

- Create an AF database
- Create a category
- Create an element template
- Create an element and associate the element's attributes with PI tags where appropriate
- Write a single value to the attribute
- Write 100 values to an attribute
- Perform a Batch (6 steps in 1 call) operation which includes:
  - Get the sample tag
  - Read the sample tag's snapshot value
  - Read the sample tag's last 10 recorded values
  - Write a value to the sample tag
  - Write 3 values to the sample tag
  - Read the last 10 recorded values from the sample tag only returning the value and timestamp
- Return all the values over the last 2 days
- Return timestamp and values over the last 2 days
- Delete the element
- Delete the element template
- Delete the sample database

---

For the main PI Web API Samples landing page [ReadMe](https://github.com/osisoft/OSI-Samples-PI-System/tree/main/docs/PI-Web-API-Docs)  
For the main PI System Samples landing page [ReadMe](https://github.com/osisoft/OSI-Samples-PI-System)  
For the main AVEVA Samples landing page [ReadMe](https://github.com/osisoft/OSI-Samples)
