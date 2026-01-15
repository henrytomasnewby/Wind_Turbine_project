
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
        if Desired_site != data[Site][1]:
            continue
        else:
            Search_reason = int(input("""why have you searched?
                                                                1)Energy output
                                                                2)Postcode

                                                                """))
            print(data[Site][1])
            
    
    
