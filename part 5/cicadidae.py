from urllib.request import urlopen
import json

API_URL = "http://api.gbif.org/v1"

# @see API docs https://www.gbif.org/developer/summary
with urlopen(f"{API_URL}/occurrence/search?"
             'country=BG&'
             'limit=10&'
             'familyKey=6049') as response:
    body = response.read()
    parsed_res = json.loads(body)
    print(f"Found {parsed_res['count']} results.")
    for row in parsed_res['results']:
        name = row.get('acceptedScientificName', 'N/A')
        # row.get('basisOfRecord', 'N/A')
        date = row.get('eventDate', 'N/A')
        where = row.get('locality', 'N/A')
        who = row.get('recordedBy', 'N/A')
        print(f"'{name}' recorded by {who} on {date}, {where}")
