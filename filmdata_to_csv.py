
# This script will:
######## 1. Read film permit JSON from NYC Open Data

import json
with open('nyc_film_permits.json', 'r') as data:
    permits = json.load(data)

#check to see if we got our data in:
# print(permits)

# 2. Pull dateTimes from film permit JSON

#dates = [permit['startdatetime'] for permit in permits]
#print (dates)

# 3. Pull zip codes from film permit JSON

# 4. Pull zip code DB from zip code - lat/lon DB
import csv
zip_geo_dict = {}
with open('us_zips.csv', 'r') as us_zips:
    reader = csv.reader(us_zips, delimiter = ',')#skipinitialspace=True)
    for row in reader:
        #print(row)
        zip_geo_dict[row[0]] = (row[1], row[2])
        
# print(zip_geo_dict['11225'])
# this zip geo dict is our rosetta stone from zips to lat/lon.

# 5. Pair zip from film permit JSON to lat/lon from zip code DB


with open('film_locations.csv', mode='w') as film_locations_file:
    locations_writer = csv.writer(film_locations_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    locations_writer.writerow(['tpep_production_datetime','latitude','longitude'])
    for permit in permits:
        try:
            locations_writer.writerow([permit['startdatetime'],zip_geo_dict[permit['zipcode_s'][:5]][0], zip_geo_dict[permit['zipcode_s'][:5]][1]]) # (zip_geo_dict[permit['zipcode_s'][:5]])
        except KeyError:
            pass