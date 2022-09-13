def maxArea(A, Len) :
    area = 0
    for i in range(Len) :
        for j in range(i + 1, Len) :
           
            # Calculating the max area
            area = max(area, min(A[j], A[i]) * (j - i))
    return area
x=int(input("Enter the size of the array"))
a=[]
for i in range(x):
    x=int(input())
    a.append(x)
 
len1 = len(a)
print(maxArea(a, len1))
 
