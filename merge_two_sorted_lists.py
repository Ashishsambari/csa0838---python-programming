 #function_to_take_input..
def insert_list(l,s):
    for i in range(1,s+1):
        data = int(input())
        l.append(data)

#function_to-merge_lists..
def merged(l1, l2):
    l1.sort()
    l2.sort()
    l1 += l2
    l1.sort()
    return l1

s1 = int(input('size-1 :'))
s2 = int(input('size-2 :'))
firstList = []
secondList = []
print("Enter ",s1," elements :")
insert_list(firstList,s1) #insert_data into list1
print("Enter ",s2," elements :")
insert_list(secondList,s2)  #insert_data into list2

print(merged(firstList, secondList))




