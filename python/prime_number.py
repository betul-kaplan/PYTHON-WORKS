min = 1
max = 100
prime_list=[]
for number in range(min,(max + 1)):
   if number > 1:
       for i in range(2,number):
           if (number % i) == 0:
               break
       else:
         prime_list.append(number)
print(prime_list)