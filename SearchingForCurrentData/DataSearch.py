

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
    
