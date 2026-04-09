
#  Part B: Filtering & Sorting
#  Filter students from Class 10A only.
#  Display students who scored more than 75 in Maths.
#  Sort students by Marks in descending order.
# Sort the data by Class and then by Attendance (descending).
#
#  Part C: GroupBy & Aggregation
#  Find the average marks for each subject.
#  Calculate the total attendance for each class.
#  Find the maximum marks scored in each subject.
#  Count how many students appear in each class.
#
#  Part D: Analysis & Thinking
# Which subject has the highest average marks?
# Which student has the highest total marks (consider all subjects)?
# Which class performs better on average?

import pandas as pd
data = {

    "Student": ["Ayaan", "Riya", "Kabir", "Ananya", "Rohan", "Meera", "Ayaan", "Riya"],

    "Class": ["10A", "10A", "10B", "10A", "10B", "10B", "10A", "10A"],

    "Subject": ["Maths", "Maths", "Science", "Science", "Maths", "Science", "Science", "Science"],

    "Marks": [78, 85, 67, 92, 74, 88, 81, 90],

    "Attendance": [90, 95, 80, 85, 88, 92, 90, 95]
}
#Q1part A: Easy
#  Display only Student, Subject, and Marks columns.
#  Find the highest and lowest marks scored.
#  Count the total number of records in the dataset.
#  Show all students who scored more than 80 marks.

df=pd.DataFrame(data)
print(df)
print(df["Student"],df["Subject"],df["Marks"])
print(df["Marks"].max())
print(df["Marks"].min())
print(df["Marks"].sum())
print(df[df["Marks"]>80])

#Q2 Part B: Filtering & Sorting
#  Filter students from Class 10A only.
# x Display students who scored more than 75 in Maths.
#  Sort students by Marks in descending order.
# Sort the data by Class and then by Attendance (descending).


# df=pd.DataFrame(data)
# print(df)
# print(df[df["Class"] == "10A"])
# #cate=df.groupby("Maths")["Marks"]>75
# #print(cate)
# df_sort=df.sort_values("Attendance", ascending=False)
# print(df_sort)
# df_sort=df.sort_values("Marks", ascending=False)
# print(df_sort)


#Part C: GroupBy & Aggregation
#  Find the average marks for each subject.
#  Calculate the total attendance for each class.
# x Find the maximum marks scored in each subject.
# x Count how many students appear in each class.

# df=pd.DataFrame(data)
# print(df)
# print(df["Marks"].mean())
# print(df["Class"],df["Attendance"])
# print(df["Marks"].max())

 #Part D: Analysis & Thinking
# Which subject has the highest average marks?
#x Which student has the highest total marks (consider all subjects)?
# xWhich class performs better on average?

df = pd.DataFrame(data)
print(df)
print(df["Marks"].max().mean())
Max_mark=df.groupby("Subject")["Marks"].max()
print(Max_mark)
total_marks=df.groupby("Subject")["Marks"].sum()
print(total_marks)
print(total_marks.max())
maths_above_75 = df[(df["Subject"] == "Maths") & (df["Marks"] > 75)]
print(maths_above_75)
print(df.groupby("Class")["Marks"].mean())
class_count=df["Class"].value_counts()
print(class_count)




