# new good version
def datas(data,Format):
    for i in range(0,len(data)):
            print(i)
            if Format[i] =="L" and False == data[i].isalpha():
                return "invalid"
            elif Format[i] =="D" and False == data[i].isdigit():
                return "invalid"
            elif Format[i] == "X" and data[i] != " ":
                return "invalid"
            else:
                continue
    return "valid"

# old bad version
def datas(data,Format):
    for i in range(0,len(data)):
            print(i)
            if Format[i] =="L" and False == data[i].isalpha():
                return "invalid"
            elif Format[i] =="D" and False == data[i].isdigit():
                return "invalid"
            else:
                continue
    return "valid"




print(datas("DA23F 34DS","LLDDLXDDLL"))