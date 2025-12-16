name_file = "Wind.txt"
txt = open(name_file,"r")
csv = open("Wind.csv","w")
try:
    import csv
    
    

    new = txt.read()
    csv.write(new)

    txt.close()
    csv.close()
    quit()
except:
    print(f"file not found {name_file}")


