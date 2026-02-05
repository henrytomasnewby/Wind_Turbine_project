from ImportingData.ValidationAndUpload  import validate
from ImportingData.ImportingDataV2  import create_md_list
from SearchingForCurrentData.DataSearch import *
import time
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
    List.append([ row[0].strip(" "),row[1].strip(" "),row[2].strip(" "),row[3].strip(" "),row[4].strip(" "),row[5].strip(" "),float(row[6]) ])
from Menu import TheMenu
data = TheMenu.menu()


Turbine_data = create_md_list(List)
print(Turbine_data)
print(List)


if data == 1:
    
    start = time.time()
    Sites_unsort(Turbine_data)
    end = time.time()
    
    print(end-start)

elif data == 3:
    
    
    Turbine_unsort(Turbine_data)
