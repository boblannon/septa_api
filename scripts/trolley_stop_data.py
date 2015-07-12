import csv
import requests

endpoint = 'http://www3.septa.org/hackathon/Stops/{}'

trolleys = [
    10,
    11,
    13,
    15,
    34,
    36,
    101,
    102
]


def get_all_stops(trolleys):
    for trolley in trolleys:
        resp = requests.get(endpoint.format(trolley))
        for stop in resp.json():
            stop['trolley'] = trolley
            yield stop

trolley_stops = [s for s in get_all_stops(trolleys)]

dw = csv.DictWriter(open('trolley_stops.csv', 'w'),
                    fieldnames=['lat', 'lng', 'stopid', 'stopname', 'trolley'])

dw.writeheader()
dw.writerows(trolley_stops)
