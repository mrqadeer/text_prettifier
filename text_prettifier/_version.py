import json

version_json = '''
{
 "date": "2024-05-02T00:00:00-0000",
 "dirty": false,
 "error": null,
 "full-revisionid": "f4c077b3cb914e1dc713ae127f2df68533682098",
 "version": "1.1.3"
}
'''  # END VERSION_JSON

def get_versions():
    return json.loads(version_json)
