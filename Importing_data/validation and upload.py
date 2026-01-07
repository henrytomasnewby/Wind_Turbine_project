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
    
    
    month = int(date[4:6])
    day = int(date[6:8])
    
    if month not in range(1,13):
        
        return "invalid"
    else:
        
        if day in range(0,month_day[month]):
            
            return "valid"
        else:
            print("fail in if 2")
            return "invalid"
    
def valid_time(time):
    Hour = int(time[0:2])
    
    Min = int(time[3:5])
    
    if Hour not in range(0,24):
        return "invalid"
    if time[2] != ":":
        return "invalid"
    if Min not in range(0,60):
        return "invalid"
    return "valid"
    

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
    print(row)
    print("")
    if check_range(int(row[0]),[1,99999]) == "invalid":
        quit(f"invalid data at {loop_count}current loop the data is {row} with error occuring at {row[0]}")
    if check_range(row[1],(2,25))== "invalid":
        quit(f"invalid data at {loop_count}current loop the data is {row} with error occuring at {row[1]}")
    if check_format(row[2],"LLDDLDDLL") == "invalid":
        quit(f"invalid data at {loop_count}current loop the data is {row} with error occuring at {row[2]}")
    if check_format(row[3],"LLDDD") == "invalid":
        quit(f"invalid data at {loop_count}current loop the data is {row} with error occuring at {row[3]}")
    if valid_date(str(row[4])) == "invalid":
        quit(f"invalid data at {loop_count}current loop the data is {row} with error occuring at {row[4]}")
    if valid_time(str(row[5])) == "invalid":
        quit(f"invalid data at {loop_count}current loop the data is {row} with error occuring at {row[5]}")
    if check_range(float(row[6]),[-0.1,5.1]) == "invalid":
        quit(f"invalid data at {loop_count}current loop the data is {row} with error occuring at {row[6]}")
        
        
csv_file.close()
    
    
    
    
    
    
        
        