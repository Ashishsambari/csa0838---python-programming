#pgm_to_find_good_pairs..

#function_to_return_no.of_combo's
def goodPair(ints):
    count = 0
    for i in range(0,len(ints)):
        for j in range(i+1,len(ints)):
            if(ints[i]==ints[j]):
                count += 1
    return count
ints = input('String :')
print('Good pairs are :',goodPair(ints))
