import geopy.distance
import glob2
import json
from pprint import pprint

all_files = glob2.glob('data/**/*.json')

my_loc = (39.0, -77.0)

_5_miles = 0
_5_to_30_miles = 0
_30_to_100_miles = 0
_100_to_200_miles = 0
_200_or_more_miles = 0

for file in all_files:
    with open(file, 'r') as f:
        data = json.loads(f.readline())
        aircrafts = data.get('aircraft')
        for aircraft in aircrafts:
            if aircraft.get('lat') and aircraft.get('lon'):
                plane_loc = (aircraft.get('lat'), aircraft.get('lon'))
                distance = geopy.distance.vincenty(my_loc, plane_loc).miles
                if distance < 5:
                    _5_miles += 1
                elif 5 < distance < 30:
                    _5_to_30_miles += 1
                elif 30 < distance < 100:
                    _30_to_100_miles += 1
                elif 100 < distance < 200:
                    _100_to_200_miles += 1
                elif distance > 200:
                    _200_or_more_miles += 1

print('Positions found are messages with positions in them')
print('---------------------------------------------------')
print('Positions found within 5 miles: %s' % _5_miles)
print('Positions found between 5 and 30 miles: %s' % _5_to_30_miles)
print('Positions found between 30 and 100 miles: %s' % _30_to_100_miles)
print('Positions found between 100 and 200 miles: %s' % _100_to_200_miles)
print('Positions found past 200 miles: %s' % _200_or_more_miles)
