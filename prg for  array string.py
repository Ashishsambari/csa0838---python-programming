integer = int(input('Don\'t enter any  negative integer : '))
answer = []
for i in range(1, integer+1):
    if(i%5==0 and i%3==0):
        answer.append('FizzBuzz')
    elif(i%3==0):
        answer.append('Fizz')
    elif(i%5==0):
        answer.append('Buzz')
    else:
        answer.append(str(i))
print(answer)
