import csv
import importing_data_v2 as Import

csv_file = open("Wind.csv","r")

def check_range(csv_file,Range):
    correct = 0
    length = 0
    for row in csv_file:
        length += 1
        
        if row == 0:
            correct += 1
        elif int(row[0]) > Range[0] and int(row[0]) < Range[1]:
            correct = 0
        else:
            correct += 1
        print(correct)
    if correct == length:
        return True
    else:
        return False
        print(length)
    
                


Import.importing("Wind.txt")
reader = csv.reader(csv_file)

print(check_range(csv_file,[1,99999]))
        
        