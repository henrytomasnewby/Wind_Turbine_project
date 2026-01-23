from ImportingData.ValidationAndUpload  import validate
from ImportingData.ImportingDataV2  import create_md_list
from SearchingForCurrentData.DataSearch import *

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
        
    List.append([ str(row[0]),row[1],row[2],row[3],int(row[4]),row[5],float(row[6]) ])



Turbine_data = create_md_list(List)
print(Turbine_data)
print(List)
from Menu import TheMenu
data = TheMenu.menu()
if data == 1:
    Sites_unsort(Turbine_data)



