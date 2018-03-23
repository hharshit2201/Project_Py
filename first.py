import csv
from collections import defaultdict

columns=defaultdict(list)
#with open('C:\Users\HARSHIT\Desktop\Project2\All.txt') as f:
 #   reader=csv.DictReader(f) #read a row in dictionary format
  #  for row in reader:  #read a row as {column1:val 1,col 2:val 2}
   #     for(k,v) in row.items():#go over each column name and value
    #        columns[k].append(v)
     #   print (columns[ 'latitude' ])
#print columns['speed']

with open('C:\Users\HARSHIT\Desktop\Project2\Newest.csv') as f:
    reader = csv.reader(f,delimiter=',')
    reader.next()
    for row in reader:
        for (i,v) in enumerate(row):
            columns[i].append(v)

    print columns[3][137]


