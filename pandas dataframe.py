
#PANDAS

import pandas as pd
data={
    "name":["jhon","jene","ruhi","shanu","shivi","nammo","kayu","shruti"],
    "age":[20,15,18,35,20,19,22,18],
    "grade":["A","B","C","D","E","F","G","H"],
    "marks":[60,70,80,50,66,90,85,75]
}
students=pd.DataFrame(data)
print(students)
print(students.head())
print(students.tail())
print(students.info())
print(students.describe())
print(students[["name","marks"]])
print(students.loc[1])
students["passed"]=students["marks"]>=40
print(students)
students.drop("grade",axis=1,inplace=True)
print(students)
print(students["marks"].max())
print(students["marks"].min())
print(students["marks"].mean())
print(students[students["marks"]>80])

#creat empty data frame
# df=pd.DataFrame(columns=['Name','Age',"Class","Marks"])
# print(df)


# Create a DataFrame containing:
# Name, Roll No, Class, Maths Marks, Science Marks.
# Task 2 Print:First 2 rows
# Last row
# Only the “Name” and “Maths Marks” columns
# Task 3 Add a new column: Total Marks
# Task 4
# Find:Highest scorer in Maths
# Average Science Marks
# Task 5 Filter students scoring > 80 in both subjects

#Create a DataFrame containing:
# Name, Roll No, Class, Maths Marks, Science Marks.
# data={"name":["pooja","shivani","veeni","nammo","shanu"],
#     "Roll No":[12,10,20,25,6],
#       "Class":[9,10,7,8,9],
#       "Maths Marks":[50,60,75,80,90],
#       "Science Marks":[80,90,60,50,65]
#
#
# }
# students=pd.DataFrame(data)
# print(students)
# print(students.head(2))
# print(students.tail(1))
# print(students[["name","Maths Marks"]])
# students["Total Marks"]=students["Maths Marks"]+students["Science Marks"]
# print(students)
# print(students["Maths Marks"].max())
# print(students["Science Marks"].mean())
# print(students[students["Maths Marks"]>80])
# print(students[students["Science Marks"]>80])

