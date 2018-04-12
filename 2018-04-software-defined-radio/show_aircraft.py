import glob2
import json

all_files = glob2.glob('data/**/*.json')

flight_reports = []
altitude_reports = []
speed_reports = []
messages = 0

for file in all_files:
    with open(file, 'r') as f:
        data = json.loads(f.readline())
        aircrafts = data.get('aircraft')
        for aircraft in aircrafts:
            # Flights
            flight = aircraft.get('hex')
            flight_reports.append(flight)
            # Altitudes
            altitude = aircraft.get('altitude', 0)
            if type(altitude) is int:
                altitude_reports.append(altitude)
            # Speed
            speed = aircraft.get('speed', 0)
            speed_reports.append(speed)
            messages += aircraft.get('messages', 0)

print('Number of aircraft seen: %s' % len(set(flight_reports)))
average_altitute = int(sum(set(altitude_reports)) / len(set(altitude_reports)))
print('Average altitude seen: %s' % average_altitute)
print('Highest speed seen: %s' % max(speed_reports))
print('Total number of messages recieved: %s' % messages)
average_messages = int(messages / len(set(flight_reports)))
print('Average number of messages recieved: %s' % average_messages)
