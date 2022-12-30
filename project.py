'''
Q.In this project you have to enter a range[A,B] and system will randomly pic any number from your
  given range and check the status of that given number.
  The properties to be checked are:
  1. Is that number is odd or even
  2. Is that number is positive or negative number
  3. Is that number is prime number or composite number
  After checking the status , you have to display all the properties followed by the randomly picked number

'''

import random
a=random.sample(range(1,12),1)
print("Number is :",a)

for i in a:
    if i%2==0:
         print(a,"is a even number")
    else:
        print(a,"is a odd number")

for i in a:
    if i>0:
        print(a,"is a positive number")
    else:
        print(a,"is a negative number")

for i in a:
    if i==1:
        print(a,"is neither prime nor composite")
    else:
        for divisor in range(2,(i//2)+1):
            if i%divisor==0:
                print(a,"is a composite number")
                break
        else:
            print(a,"is a prime number")
