import json
import requests

params = {}
params["parkCode"] = "acad,dena"
params["api_key"] = "BlHCrJVsJqlNnCCYCnz2HWC1mYRXFtrV2D3nfHra"
r = requests.get("https://developer.nps.gov/api/v1/campgrounds", params=params)

requests_json = r.json()

#print(json.dumps(r.json()))

data = requests_json["data"]


def replace_and_load(input_string):
	input_string = input_string.replace("lat", "\"lat\"")
	input_string = input_string.replace("lng", "\"lng\"")
	return input_string

x = [(campground["name"], replace_and_load(campground["latLong"])) for campground in data]

print(x)