
# menu

possible = ["Search sites-unsorted","Search turbines unsorted","Search sites-sorted","Search turbines sort","Update data","analysis selected turbines or sites"]


def menu(mem):
    menu = []
    print_menu = ""
    print("")
    blacklist = []
    if possible[0:3] not in mem:
        blacklist.append("analysis selected turbines or sites")
    
    for i in range(0,len(possible)):
        if possible[i] in blacklist:
            continue
        menu.append(possible[i])
        print_menu += str(i+1)+") "+possible[i] + "\n"
    Use =  str(input(print_menu+f"\n INPUT: "))
    for Use not in menu:
        print("Please input somthing inside in the displayed menu")
        Use = str(input(print_menu+f"\n INPUT: "))
        
    return Use


