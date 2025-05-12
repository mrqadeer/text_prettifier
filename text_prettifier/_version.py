import json

version_json = '''
{ "date": "2024-05-03T00:00:00-0000",
 "dirty": false,
 "error": null,
 "full-revisionid": "83553a370d543990a0d3c352ea373926d4132dcb",
 "version": "2.0.1"
}
'''  # END VERSION_JSON

def get_versions():
    return json.loads(version_json)
