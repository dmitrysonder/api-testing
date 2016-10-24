import requests
import json
import jsonschema

schema = open("schema.json").read()

url = 'http://appybuy.korbit.eu:8080/magnoliaPublic/.rest/appybuy/v1/charities'
payload = {'count':222, 'start':0, 'sort':'richest', 'lang':'eng'}

r = requests.get(url, params=payload)

try:
    v = jsonschema.Draft4Validator(json.loads(schema))
    for error in sorted(v.iter_errors(json.loads(r.text)), key=str):
        print(error.message)
except jsonschema.ValidationError as e:
    print(e.message)


