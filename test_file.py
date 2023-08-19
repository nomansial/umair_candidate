import pprint

import requests
from assertpy import assert_that

from utilities.configurations import *

config = getConfig()

url = config['API']['endpoint']
headers = {'Content-Type': 'application/json'}

response = requests.get(url, headers=headers)

# Decode response.json() method to a python dictionary and use the data
response_data = response.json()
response_data = [dict(PlaneNumber=k1["plateNo"], DriverName=k1["driverName"], lat=k1["lat"],
                      lng=k1["lng"], location=k1["location"],
                      lastUpdated=k1['lastUpdated']) for k1 in response_data]

pprint.pprint(sorted(response_data, key=lambda x: x['lastUpdated'], reverse=True))

for x in response_data:
    assert_that(x).is_not_empty()


