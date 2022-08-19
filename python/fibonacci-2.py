fibonacci_list = [1, 1]
for i in range(8):
    number = fibonacci_list[i] + fibonacci_list[i + 1]
    fibonacci_list.append(number)
    # print(number, fibonacci_list)

print("fibonacci list: ", fibonacci_list)

************************************************************


fibo = [1, 1]

for i in range(8) :
    fibo.append(fibo[i] + fibo[i+1])
fibo



*************************************************************

list = []

x, y = 1, 1



while x <= 55 :

    list.append(x)

    x, y = y, y + x

print(list)