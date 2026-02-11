import csv
# get site desired
# search site
#

data = "thing,thing,somthingn/"
File = open("Test_file.csv","w")
Wind = open("ImportingData/Wind.txt","r")
data = Wind.read()

File.write(data)



#writer = csv.writer(File)

#writer.writerow(data)

File.close()