import csv
import json
import requests

with open("Meteorite_Landings_Revised.csv","rb") as data, open("Meteorite_Landings_Country.csv", "wb") as out:
    data = csv.reader(data, delimiter=',')
    out = csv.writer(out, delimiter=',')
    url = 'https://maps.googleapis.com/maps/api/geocode/json'

    latlng = "0,0"
    accessKey = "AIzaSyAURFtxm542qcbZ1Rk09MQd5ck5IHMBvPY"

    header = data.next()
    header.append('Country')
    out.writerow(header)

    index = header.index("GeoLocation")

    for row in data:
        latlng = row[index][1:-1]

        params = {'latlng': latlng, 'language' : "en", 'result_type' : 'country', 'key' : accessKey}
        r = requests.get(url, params=params)

        status = r.json()['status']

        if status == 'OK':
            results = r.json()['results']
            for e in results[0]:
                if(e=="address_components"):
                    row.append(results[0][e][0]['long_name'])
                    out.writerow(row)