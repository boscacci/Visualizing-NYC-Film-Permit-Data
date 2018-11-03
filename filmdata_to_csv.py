import requests, io, csv #,json

## 1. Read film permit JSON from NYC Open Data

def api_request_json(url):
    api_data = requests.get(url).json()
    return api_data

## 2. Make dict with key = zip_codes and values = (lat,lon)

def get_usa_zips(url):
    usa_zips = {}
    census_zip_latlon = io.StringIO(requests.get(url).text)
    dialect = csv.Sniffer().sniff(census_zip_latlon.read(1024))
    census_zip_latlon.seek(0)
    reader = csv.reader(census_zip_latlon, dialect)
    for row in reader:
        usa_zips[row[0]] = (row[1], row[2])
    return usa_zips
        
## 3. Make a CSV file for upload to kepler.gl

def write_out_csv(permits, usa_zips):
    with open('film_locations.csv', mode='w') as film_locations_file:
        
        locations_writer = csv.writer(film_locations_file, delimiter=',', 
                                                           quotechar='"', 
                                                           quoting=csv.QUOTE_MINIMAL)

        ## The sample data set I got from the kepler github repo had rows named like so:
        locations_writer.writerow(['tpep_production_datetime','latitude','longitude'])
        omissions = 0
        for permit in permits:
            try:
                locations_writer.writerow([permit['startdatetime'],usa_zips[permit['zipcode_s'][:5]][0], usa_zips[permit['zipcode_s'][:5]][1]])
            except KeyError:
                omissions += 1
        print(f"\nWriter made {omissions} line omissions.\n")

### fn calls

permits = api_request_json('https://data.cityofnewyork.us/resource/6aka-uima.json')
usa_zips = get_usa_zips(r'https://goo.gl/oYwpRM')
write_out_csv(permits, usa_zips)