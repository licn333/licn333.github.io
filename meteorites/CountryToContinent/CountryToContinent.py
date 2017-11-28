from geonamescache.mappers import country
import csv

mapper = country(from_key = 'name', to_key = 'continentcode')

with open("meteor-fell-before.csv", "rb") as csvdata, open("meteor-fell.csv", "wb") as out:
    input = csv.reader(csvdata, delimiter=',')
    out = csv.writer(out, delimiter=',')

    header = input.next()
    header.append('Continent')
    out.writerow(header)
    index = header.index("Country")

    for row in input:
        row.append(mapper(row[index]))
        out.writerow(row)