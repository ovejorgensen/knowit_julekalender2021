import requests
import csv
from shapely.wkt import loads
from tqdm import tqdm
from math import radians, cos, sin, asin, sqrt

data = requests.get('https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBOUT09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--7bb23c39ab7eb5b367e3b0841b86e0667756397f/cities.csv?disposition=inline')
lines = data.text.split('\n')
reader = csv.reader(lines[1:-1])
parsed_csv = list(reader)
parsed_csv.insert(0, ['NorthPole', 'POINT(0 90)'])
filtered = [[row[0], loads(row[1])] for row in parsed_csv]

def distance(lat1, lat2, lon1, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return(c * r)

total_dist = 0
current_location = filtered[0]
filtered.remove(filtered[0])
while len(filtered) > 0:
    shortest_dist = [float('inf'), ""]
    for row in filtered:
        point = row[1]

        dist = distance(current_location[1].y, point.y, current_location[1].x,  point.x)

        if dist < shortest_dist[0]:
            shortest_dist = [dist, row]

    total_dist += shortest_dist[0]

    current_location = shortest_dist[1]
    filtered.remove(current_location)

north_pole = loads('POINT(0 90)')
total_dist += distance(current_location[1].y, north_pole.y, current_location[1].x,  north_pole.x)

print("\n", total_dist)
