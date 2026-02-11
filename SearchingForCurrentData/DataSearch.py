

def search(current_layer:list,ID:str):
    start = 0
    # checks data
    alpha = type(current_layer)
    if  alpha == str:
        alpha = type(current_layer)
        while alpha == str:
            alpha = type(current_layer)
            if alpha == str:
                start += 1
            else:
                continue
            
    length = len(current_layer)
    for pos in range(start,length):
        possible=str(current_layer[pos][0])
        if possible is ID:
            return possible,pos
        else:
            continue
    return "null",0

def Sites_unsort(data):
    
    sites = ""
    for num in range(len(data)):
        sites += data[num][1] + ", "
    
    
    Desired_site = str(input(f"input the site you want to search for {sites}"))
    # validate to be done
    #
    
    for Sites in range(len(data)):
        debuging = data[Sites][1]
        if Desired_site != data[Sites][1]:
            
            continue
        else:
            Search_reason = int(input("""why have you searched?
1)Energy output
2)Postcode

"""))
            
            match Search_reason:
                case 1:
                    print(data[Sites][1])
                    for Item in data[Sites]:
                        power_total = 0
                        if type(Item) != list:
                            continue
                        else:
                            
                            for record in Item:
                                if type(record) == str:
                                    continue
                                power_total += record[2]
                                
                            
                            
                            
                                
                            print(f"Turbine {Item[0]} produced an averge of {round(power_total/len(Item),2)}")
                    return ""
                case 2:
                   print(f"{data[Sites][1]} has a postcode of {data[Sites][2]})")
                   return ""
            
           
            
    
    print("site not in file")
    
    
def Turbine_unsort(data):
    
    turbine = ""
    for num in range(len(data)):
        turbine += " "+data[num][1] +" ["
        for site_turbines in range(3,len(data[num])):
            turbine += data[num][site_turbines][0]+","
        turbine += "]"
            
    
    print(f"input the turbine you want to search for {turbine}")    
    Desired_turbine = str(input("INPUT:"))
    # validate to be done
    #
    
    for Site in data:
        for site_turbines in range(3,len(Site)):
            if Site[site_turbines][0] != Desired_turbine:
                continue
            else:
                desired_Site = Site
    
    
    for Sites in range(len(data)):
        Turbine = 0
        for Turbine in range(3,len(data[Sites])):
            turbine_file = data[Sites][Turbine][0]
            if turbine_file != Desired_turbine:
                continue
            else:
                power  = 0
                for record in range(1,len(data[Sites][Turbine])):
                    power += data[Sites][Turbine][record][2]
                    ###
                    print(f"in {str(data[Sites][Turbine][record][0])[0:4]} on the {str(data[Sites][Turbine][record][0])[6:8]} day of the {str(data[Sites][Turbine][record][0])[4:6]} month this turbine produced {data[Sites][Turbine][record][2]}")
                print(f"for a average of {round(power/record-1,2)} and a total output of {round(power,2)}")
                return""
                
            
            
           
            
    
    print("site not in file")
    
def get_values(data):
    sites_num = len(data)
    Site_effic = []
    
    for s in range(sites_num):
        # this is the site layer
        
        Site_turbines = []
        count_values = 0
        turbine_num = len(data[s])
        site_avarege = 0
        for t in range(3,turbine_num):
            # this is the turbine layer
            record_num = len(data[s][t])
            Turbine_total = 0
            for r in range(1,record_num):
                #record layer
               count_values += 1
               Turbine_total +=data[s][t][r][2]
               site_avarege += data[s][t][r][2]
               
            # this makes a turbine layer
            Turbine_average = Turbine_total 
            Site_turbines.append([data[s][t][0],round(Turbine_average,3)])
        # this makes the site layer
        
        Site_effic.append([data[s][1],round(site_avarege,3),Site_turbines])
        print(Site_effic)
        
    #this code pulls for all turbines in every site and gets there average scorces into a total list
        
    return Site_effic

def swap(List):
    List.insert()
    
    # need to finish the swap function



def least_sort(data):
    sort_refrence = get_values(data)
    new_data = []
    
    for i in range(len(data)):
        current = sort_refrence[i]
        
        comparer = sort_refrence[i+1]
        if comparer[1] == current[1]:
            continue
        elif comparer[1] <= current[1]:
            continue
        elif comparer[1] >= current[1]:
            data = swap(data)
            data = swap(sort_refrence)
        print(current)
        pass
    
    

print(least_sort([['66808', 'Windy Heights', ' QX65Q 20YO', [' NC383', [20230504, ' 11:00', 3.2], [20230306, ' 06:30', 4.7], [20230324, ' 22:30', 2.2], [20230324, ' 03:00', 2.2]], [' AB233', [20231026, ' 22:30', 2.0], [20230701, ' 01:00', 3.9], [20230919, ' 19:30', 2.9], [20230614, ' 06:00', 3.8]], [' JG593', [20230914, ' 21:00', 3.0], [20230223, ' 15:00', 1.0], [20231113, ' 18:00', 3.6], [20230918, ' 05:00', 3.4]]], ['78329', 'Breezy Plains', ' ZY26O 38RV', [' VP991', [20230415, ' 12:00', 0.3], [20230817, ' 15:00', 3.0], [20231119, ' 00:00', 0.4], [20230412, ' 00:00', 1.5]], [' QZ184', [20230503, ' 21:00', 3.3], [20230604, ' 08:00', 0.2], [20230408, ' 21:30', 2.6], [20230114, ' 05:00', 0.4]], [' AH593', [20231015, ' 03:00', 2.3], [20230925, ' 06:30', 3.6], [20231224, ' 04:30', 1.7], [20230428, ' 20:30', 2.2]]],['70102', 'Gale Point', ' IC85M 81LY', [' JB568', [20230421, ' 16:30', 4.0], [20230405, ' 00:30', 1.4], [20231223, ' 05:00', 3.8], [20230715, ' 20:30', 3.0]], [' GV152', [20230427, ' 02:30', 1.0], [20231120, ' 16:30', 1.6], [20230125, ' 02:00', 3.3], [20230104, ' 09:00', 3.2]], [' EQ729', [20230205, ' 05:30', 2.6], [20230325, ' 13:00', 1.8], [20230607, ' 14:00', 4.9], [20230315, ' 07:00', 1.4]]]]))
