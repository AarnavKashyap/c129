import csv

data = []

with open("data_2.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
planet_data = data[1:]

for data in  planet_data:
    data[0] = data[0].lower()

planet_data.sort(key = lambda planet_data: planet_data[0])

with open("data_2_sorted.csv", "a+")as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)