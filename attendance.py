list=[]
list1=[]
p='p'
a='a'
print("Avengers Attendance")
print("Present-p:::Absent-a")
print("-"*100)
x=input("Capten America:::")
if x==p:
 list.append("Captain America")
else:
 list1.append("Captain America")
b=input("Thor:::")
if b==p:
 list.append("Thor")
else:
 list1.append("Thor")
c=input("Iron Man:::")
if c==p:
 list.append("Iron man")
else:
 list1.append("Iron man")
d=input("Hulk:::")
if d==p:
 list.append("Hulk")
else:
 list1.append("Hulk")
e=input("Black widow:::")
if e==p:
 list.append("Black widow")
else:
 list1.append("Black widow")
f=input("Hawkeye:::")
if f==p:
 list.append("Hawkeye")
else:
 list1.append("Hawkeye")
g=input ("War machine:::")
if g==p:
 list.append("War machine")
else:
 list1.append("War machine")
print("\n")
print("LIST OF PRESENT:")
for i in(list):
 print(i)
print("\n")
print("LIST OF ABSENT:")
for j in(list1):
 print(j)
