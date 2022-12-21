import json


def readjson(jsonpath):
    with open(jsonpath) as f:
        data = json.load(f)
        first_name = data[0]['firstName']
        last_name = data[0]['lastName']
        print(type(first_name))
