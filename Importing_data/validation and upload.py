import csv
import importing_data_v2 as Import

csv_file = open("Wind.csv","r")

def check_range(num,Range):
        if int(num) > Range[0] and int(num) < Range[1]:
            return "valid"
        else:
            return "invalid"
        
        

reader = csv.reader(csv_file)

loop_count = 0
for row in reader:
    if loop_count == 0:
        
        loop_count += 1
        continue
    loop_count += 1
    
    if check_range(row[0],[1,99999]) == "invalid":
        quit(f"invalid data at {loop_count}{row}")
csv_file.close()
    
    
    
    
    
    
        
        