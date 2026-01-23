
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

def search(current_layer:list,ID:str):
    start = 1
    # checks data
    alpha = list
    if len(current_layer)>2:
        alpha = type(current_layer[0])
    if  alpha == str:
        while alpha == str:
            alpha = type(current_layer[start])
            if alpha == str:
                start += 1
            else:
                continue
            
    length = len(current_layer)
    for pos in range(start,length):
        possible=str(current_layer[pos][0])
        if possible in ID:
            return possible,pos
        else:
            continue
    return "null",0
## data data
def add_turbine_reading(turbine_line):
    Reading = [turbine_line[4],turbine_line[5],turbine_line[6]]
    return Reading

def add_turbine(turbine_line):
    
 turbine = [turbine_line[3],add_turbine_reading(turbine_line)]
 return turbine


def add_site(row):
    List = [row[0],row[1],row[2],add_turbine(row)]
    return List

def create_md_list(List):
    
    MD_list = [[]]

    for turbines in List:
        current_site = turbines[0]
        search_debug =search(MD_list,current_site)
        if current_site not in (search_debug[0]):
            
            MD_list.append(add_site(turbines))
        else:
            
            # the MD is starting with [[ but should have [
            
        
            if turbines[3] not in search(MD_list[search_debug[1]],turbines[3])[0]:
                
                MD_list[search_debug[1]].append(add_turbine(turbines))
                
            else:
                MD_list[search(MD_list,current_site)[1]][search(MD_list[search(MD_list,current_site)[1]],turbines[3])[1]].append(add_turbine_reading(turbines))
    
    del (MD_list[0])
    return MD_list
    

