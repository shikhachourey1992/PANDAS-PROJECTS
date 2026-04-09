# import pandas as pd
#
# data = {
#
#     "Name": ["Amit", "Riya", "Sahil", "Neha", "Karan"],
#
#     "Subject": ["Math", "Science", "Math", "Science", "Math"],
#
#     "Marks": [78, 85, 67, 92, 74]
#
# }
#
# df = pd.DataFrame(data)
# print(df)
# print(df.head(3))
# print(df["Marks"].mean())
#
# print(df[(df["Subject"] == "Math") & (df["Marks"] > 75)])
# print(df["Marks"].max())
# print(df[df["Subject"] == "Math"].shape[0])
# # print(df)  Display the first 3 rows of the dataset.
# # Find the averag marks of all students.
# #Show students who scored more than 75 marks.
# #Count how many students are in Math subject.
# # Find the highest marks obtained.

import pandas as pd

data = {

    "Emp_ID": [101, 102, 103, 104, 105, 106],

    "Name": ["Asha", "Rohit", "Meena", "Kunal", "Pooja", "Rohit"],

    "Department": ["HR", "IT", "IT", "Sales", "HR", "Sales"],

    "Salary": [45000, 60000, 58000, 52000, 47000, 55000],

    "Rating": [4.2, 4.8, 3.9, 4.1, 4.5, 4.0],

    "City": ["Mumbai", "Pune", "Mumbai", "Delhi", "Pune", "Delhi"]

}


# Filtering & Conditions
# Show employees from IT department with salary greater than 55,000
# Display employees who work in Delhi and have rating ≥ 4
# Count how many employees are in HR department


# df=pd.DataFrame(data)
# print(df[(df["Department"] == "IT") & (df["Salary"] > 55000)
# print(df[(df["City"] == "Delhi")&(df["Rating"]>4)])
# print(df[(df["Department"] == "HR")].shape[0])

#  Sorting & Selection
#  Sort employees by Salary (descending)
# Display top 3 highest paid employees

df=pd.DataFrame(data)
# print(df.sort_values(by="Salary", ascending=False))
# print(df.sort_values(by="Salary", ascending=False).head(3))

#  GroupBy (Very Important)
# Find average salary for each department
# Find maximum rating in each department
# X Count number of employees per city

#print(df.groupby("Department")["Salary"].mean())
# print(df.groupby("Department")["Rating"].max())




#  Advanced Logic
# Add a new column Performance
# Rating ≥ 4.5 → Excellent
# Rating ≥ 4.0 → Good
# Else → Average
# Show employees whose salary is above department average
#  Data Cleaning
#
# Identify duplicate names
# Remove duplicate records

# df["Performance"]=df["Rating"]>=4.5
# df["Performance"]=df["Rating"]>=4.0
# print(df)
# print(df.drop_duplicates(subset=["Name","City","Department"],inplace=True))
#print(df[df["Name"].duplicated()])
# df=pd.DataFrame(columns=["Emp_ID,Name,Department,Salary,Rating,City"])
# print(df)
unique_df = df.drop_duplicates(subset="Name")
print(unique_df)
#unique_df = df.drop_duplicates(subset="City")
#print(unique_df)

#unique_df = df.drop_duplicates(subset="Department")
#print(unique_df)

















