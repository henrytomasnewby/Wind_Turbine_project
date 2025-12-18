
def importing(name_file):
    

    try:
        import csv
        txt = open(name_file,"r")
        csv = open("Wind.csv","w")
        

        new = txt.read()
        csv.write("S ID,Site,Postcode,T ID, date, time , reading")
        csv.write(new)

        txt.close()
        csv.close()
        return
    except:
        print(f"file not found {name_file}")
        quit()
