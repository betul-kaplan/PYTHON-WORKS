#Factorial  :


def fakt(x):

   
        if (x == 1 or x == 0):
          return 1
        else :
          return x * fakt(x - 1)

fakt(5)

#Factorial  :

def factorial(x) :
    number = 1
    for i in range(1,x+1) :
         number *= i
    return number
a=int(input("enter a number and see it's factorial :"))
factorial(a) 