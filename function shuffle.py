a=int(input("size 1  "))
l1=[]
l2=[]
for i in range(a):
    ip=int(input("Enter the element  "))
    l1.append(ip)
b=int(input("SIZE 2  "))
for j in range(b):
    p=int(input("Enter the element   "))
    l2.append(p)
def shuffle(l1,l2):
    if len(l1) < len(l2):
        minlength = len(l1)
    else:
        minlength = len(l2)
    shuffled = []
    for i in range(minlength):
        shuffled.append(l1[i])
        shuffled.append(l2[i])
    shuffled = shuffled + l1[minlength:] + l2[minlength:]
    return(shuffled)
print(shuffle(l1,l2))
