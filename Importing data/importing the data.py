import csv
i = 0
data_segment = str("")
current_list = []
file = open("Wind.txt","r")
data = file.read()
print(type(data))

while i in range(0,len(data)):
    data[i].strip()
    if data[i] == ",":
        current_list.append(data_segment)
        data_segment = ""
    else:
        data_segment = str(data_segment)
        current_data = str(data[i])
        
        data_segment = data_segment + current_data
    i += 1
    
print(current_list)
file.close