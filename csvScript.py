import csv
mergeData=[]
with open("myFile0.csv",'r') as data:
    reader=csv.reader(data)
    # print(data)
    for row in reader:
        if row[0]=="id":
            mergeData.append([row[0],"Name",row[3]])
        else:
            temp=[row[0],row[1]+" "+row[2],row[3]]
        # mergeData.append(reader[0][0],"Name",reader[0][2])
            mergeData.append(temp)
with open("New.csv",'w',newline='') as Ndata:
    writer=csv.writer(Ndata)
    for temp in mergeData:
        # print(temp)
        writer.writerow(temp)