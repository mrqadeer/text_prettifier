import json

version_json = '''
{
 "date": "2024-05-02T00:00:00-0000",
 "dirty": false,
 "error": null,
 "full-revisionid": "45eafa102436b5935b0b4879804c7eb5d8a0bdc8",
 "version": "1.1.3"
}
'''  # END VERSION_JSON

def get_versions():
    return json.loads(version_json)
