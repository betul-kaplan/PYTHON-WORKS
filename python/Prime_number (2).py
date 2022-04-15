#Prime_Number  :

number=int(input("Enter a number and see if it is prime or not :"))
flag = True
for i in range(2,number):
  if number % i == 0:
    flag=False
    break
if flag ==True  and number > 1:
  print ("yes! It is a prime number...")
else:
  print("ıt is not a prime number") 


#2. way  :

n = int(input("Enter a positive int number to check if it is a Prime Number."))

counter = 0

for i in range(1, n+1) :
    if n % i == 0 :
        counter += 1
        
if (n == 0) or (n == 1) or (counter >= 3) :
    print(n, " is not a Prime Number.")
    
else :
    print(n, " is a Prime Number.")