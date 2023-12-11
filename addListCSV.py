import csv
import pandas as pd
def addListCsv(file_name,data):
    with open(file_name, 'w', newline='') as csvfile:
            pass
    with open(file_name,'a',newline='') as csvfile:
        writer=csv.writer(csvfile)
        for d in data:
            writer.writerow(d)
data=[["reg_no","Name","sem","clg","cgpa"],["ABC123","ganesh kumar","s8","ABC","9.8"],]
addListCsv('fn.csv',data)
df=pd.read_csv('fn.csv')
num_rows,num_col=df.shape
print(num_rows,num_col)
num_rows=len(df.axes[0])
num_col=len(df.axes[1])
print(num_rows,num_col)
df.