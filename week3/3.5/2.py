import csv

results = dict()
with open("Crimes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[2][6:10] == "2015":
            results[row[5]] = results.get(row[5], 0) + 1

max_time = max(results.values())
for k, v in results.items():
    if v == max_time:
        print(k)