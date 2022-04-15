def fizz_buzz(num):

    if num % 3 == 0:
      print("Fizz")
    if num % 5 == 0:
      print("Buzz")
    if (num%3 == 0 and num%5==0):
      print("FizzBuzz")
j=0
for j in range(1,100):
  j+=1
  
  a=fizz_buzz(j)