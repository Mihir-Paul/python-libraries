import pandas as pd 

data = {
    "Name":['Ravi','Ishan','Srijan'],
    "Age":[20,22,24],
    "Salary":[40000,60000,120000]
}

df = pd.DataFrame(data,index=['Employee1','Employee2','Employee3'])

#Add a new column
df["Jobs"]=['Accountant','Window Opener','Slave1']

#Add a new row
new_row = pd.DataFrame({"Name":'Priyanshu',"Age":20,"Salary":200000,"Jobs":'Slave2'},index =['Employee4'])
df = pd.concat([df,new_row]) 

print(df)