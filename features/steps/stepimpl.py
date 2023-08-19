import pprint

import requests
from assertpy import assert_that
from behave import *

from utilities.configurations import *

config = getConfig()


@given(u'api url is provided')
def step_impl(context):
    context.url = config['API']['endpoint']
    context.headers = {'Content-Type': 'application/json'}


@when(u'user hits api url')
def step_impl(context):
    context.get_response = requests.get(context.url, headers=context.headers)


@then(u'response is retrieved')
def step_impl(context):
    # Decode response.json() method to a python dictionary and use the data for assertion and sorting
    response_data = context.get_response.json()
    response_data = [dict(PlaneNumber=k1["plateNo"], DriverName=k1["driverName"], lat=k1["lat"],
                          lng=k1["lng"], location=k1["location"],
                          lastUpdated=k1['lastUpdated']) for k1 in response_data]

    pprint.pprint(sorted(response_data, key=lambda st: st['lastUpdated'], reverse=True))

    for x in response_data:
        assert_that(x).is_not_empty()
