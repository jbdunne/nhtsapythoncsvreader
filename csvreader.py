>>> import csv
>>> with open('Downloads/FARS2019NationalCSV/VEH_AUX_use.csv', newline='') as csvfile:
...     reader = csv.DictReader(csvfile)
...     for row in reader:
...             print(row['A_BODY_FORMAT'], row['A_CDL_S'], row['A_IMP1_FORMAT'])
