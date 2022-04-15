# fibonacci
fibo=[1,1]
for i in range(5):
  fibo.append(fibo[i]+fibo[i+1])
print(fibo)



#number of sequence of Fibonaccci

n = int(input("enter number of sequence of Fibonaccci :"))
fibo=[1,1]
for i in range(n-2):
  fibo.append(fibo[i]+fibo[i+1])
print(fibo) 
