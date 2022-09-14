from itertools import permutations

#input_from_user...
my_list = []
size = int(input('Enter size of list :'))
for i in range(0,size):
    a = int(input())
    my_list.append(a)

my_list = list(dict.fromkeys(my_list))   
permutate = permutations(my_list) 
for i in list(permutate): 
    print (i) 
print(type(permutate))
