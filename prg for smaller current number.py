x=int(input("Enter the size of the array"))
nums=[]
result=[]
for i in range(x):
    y=int(input())
    nums.append(y)
for i in range(x):
    z=0
    for j in range(x):
        if nums[j]<nums[i]:
            z=z+1
    result.append(z)
print(result)
