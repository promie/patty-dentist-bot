import json

def read_from_file():
    with open("api_v1/api/dentists.json", "r") as dentists:
        return json.loads(dentists.read())
