>>> import csv
>>> with open('vehicleinput.csv', newline='') as csvfile:
...     reader = csv.DictReader(csvfile)
...     for row in reader:
...             print(row['A_BODY_FORMAT'], row['A_CDL_S'], row['A_IMP1_FORMAT'])
