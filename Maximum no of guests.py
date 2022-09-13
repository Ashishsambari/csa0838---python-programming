N=int(input("N="))
g=[]
h=[]
print("E=")
for i in range(N):
    x=int(input())
    g.append(x)
print("T=")
for i in range(N):
    y=int(input())
    h.append(y)
sum=0
max=sum
for i in range(N):
    sum=sum+g[i]-h[i]
    if(max<sum):
        max=sum
print("Maximum number of guests on cruise at instance",max)
