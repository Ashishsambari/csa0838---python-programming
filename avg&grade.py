sub1 = int(input("enter the marks in sub1"))
sub2 = int(input("enter the marks in sub2"))
sub3 = int(input("enter the marks in sub3"))
sub4 = int(input("enter the marks in sub4"))
sub5 = int(input("enter the marks in sub5"))
avg = (sub1+sub2+sub3+sub4+sub5)/5
print("average:",avg)
if (avg>=90):
    print("grade : A")
elif(avg>=80&avg<=90):
    print("grade : B")
elif(avg>=70&avg<=80):
    print("grade : C")
elif(avg>=60&avg<=70):
    print("grade : D")
elif(avg>=50&avg<=60):
    print("grade : E")
else:
    print("grade : F")
    


