#dict pratice
import json
student={}
n=int(input("enter the num of student:"))
for i in range(n):
    name=input("enter the name of student:")
    marks=[]
    subNum=int(input("enter how meny subjects:"))
    for numbers in range (subNum):
        n1=int(input("enter the marks:"))
        marks.append(n1)
    student[name]=marks
    
# print(student)
# for dv in student:
#     print('student name',dv," ",end='' )
#     total_marks=sum(student [dv])
#     per=total_marks/subNum
#     print(total_marks," ",per)
# with open ("C:\\Users\\LENOVO\\Desktop\\code01_2103\\student.json","w") as file:
#     file.write(str(student))

print(name)
# r={"d":[12,52,62]}
# s=sum(r["d"])
# print(s)
