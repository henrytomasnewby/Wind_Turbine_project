
def importing(name_file):
    

    try:
        import csv
        txt = open(name_file,"r")
        csv = open("ImportingData/Wind.csv","w")
        

        new = txt.read()
        csv.write("S ID,Site,Postcode,T ID, date, time , reading,\n")
        csv.write(new)

        txt.close()
        csv.close()
        return
    except:
        print(f"file not found {name_file}")
        quit()

def add_turbine_reading(turbine_line):
    pass

def create_2d_list(List):
    
    MD_list = []
    sites = []
    for turbines in List:
        current = int(turbines[0])
        if current not in sites:
            sites.append(turbines[0])
            MD_list.append([current,turbines[1],turbines[2],[turbines[3],add_turbine_reading(turbines)]])
        else:
            
            if turbines[3] in MD_list[int(current)]:
                pass
