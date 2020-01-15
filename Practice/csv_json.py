import csv
import json

csvFile =  open("C:/Users/406822/Desktop/MDS_Data/mds_15min.csv", 'r')
jsonFile = open("C:/Users/406822/Desktop/MDS_Data/mds_15min.json", 'w')

fieldnames = ("bikeid","lat","lon","unixtime","company")
reader = csv.DictReader(csvFile,fieldnames)
for row in reader:
    json.dump(row, jsonFile)
    jsonFile.write('\n')