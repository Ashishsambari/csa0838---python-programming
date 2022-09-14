def employee_comb(p):
 for i in range(3):
        for j in range(3):
            for k in range(3):
                if (i!=j and j!=k and i!=k):
                    print(p[i], p[j], p[k])
digits=[]
print('Enter 3 valid ints :')
for i in range(3):
    a=int(input())
    digits.append(a)
employee_comb(digits)
