import csv
import importing_data_v2 as Import

csv_file = open("Wind.csv","r")

def check_range(num,Range):
        
        if str == type(num):
            num = len(num)
        if (num) > Range[0] and (num) < Range[1]:
            return "valid"
        else:
            return "invalid"
    
    
def valid_date(date):
    month_day = {
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
        }
    
    month = int(date[4:5])
    day = int(date[6:7])
    if month not in range(1,12):
        return "invalid"
    else:
        if day in range(0,month_day[month]):
            return "valid"
        else:
            return "invalid"
    

def check_format(data,Format):
    
 
    for i in range(0,len(data)):
            if Format[i] =="L" and False == data[i].isalpha():
                return "invalid"
            elif Format[i] =="D" and False == data[i].isdigit():
                return "invalid"
            else:
                return "valid"

reader = csv.reader(csv_file)

loop_count = 0
for row in reader:
    if loop_count == 0:
        
        loop_count += 1
        continue
    loop_count += 1
    
    if check_range(int(row[0]),[1,99999]) == "invalid":
        quit(f"invalid data at {loop_count}{row}{row[0]}")
    if check_range(row[1],(2,25))== "invalid":
        quit(f"invalid data at {loop_count}{row}{row[1]}")
    if check_format(row[2],"LLDDLDDLL") == "invalid":
        quit(f"invalid data at {loop_count}{row}{row[2]}")
    if check_format(row[3],"LLDDD") == "invalid":
        quit(f"invalid data at {loop_count}{row}{row[3]}")
    if valid_date(str(row[4])) == "invalid":
        quit(f"invalid data at {loop_count}{row}{row[4]}")
        
        
        
csv_file.close()
    
    
    
    
    
    
        
        