a=input("Enter the grade")
s=int(input("Enter the salary"))
b1=0
bonus=0
if(s<10000):
    b1=s/2
elif a=='A':
    bonus=s*0.05
elif a=='B':
    bonus=s*0.1
else:
    print("enter the proper grade")
    print("Total to be paid",s+bonus)
    print("Bonus",bonus)
