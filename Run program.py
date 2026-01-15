from ImportingData.ValidationAndUpload  import validate
from ImportingData.ImportingDataV2  import create_md_list
import csv

## start file




List = []
validate()
Wind = open("Wind_validated.csv","r")
pos = 0
file = csv.reader(Wind)
for row in file:
    if pos == 0:
        pos = 1
        continue
    List.append([ int(row[0]),row[1],row[2],row[3],int(row[4]),row[5],float(row[6]) ])



Turbine_data = create_md_list(List)
print(Turbine_data)
print(List)

menu()
