import math
num = int(input('Please enter the number you want to check the range up to: '))
for x in range(2 , num+1) :
    for i in range (2 , int(math.sqrt(x)+1)) :
       if x % i == 0 :
           break
    else :
        print(f'{x} is one of our prime numbers ^-^')
