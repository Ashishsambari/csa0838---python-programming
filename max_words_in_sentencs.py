# function_definition_for_max_words_in_the_sentence
def max_words(my_list):
    max_ = 0
    empty = []
    for i in  my_list:
         current = len(i.split(' '))
         #print(current)
         if(current > max_):
             max_ = current
    return max_
             

        
listOfSentences = []
sizeOfList = int(input("May I know the size of list :"))
print("Start entering sentences limit is :", sizeOfList)
for i in range(1,sizeOfList+1):
    newSentence = input()
    listOfSentences.append(newSentence)

print("The sentence with max words that are :",max_words(listOfSentences))
 
