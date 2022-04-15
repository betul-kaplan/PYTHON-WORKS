# 1/10 discount for 1000

quantity=int(input("enter how much spent  :"))
if quantity >= 1000 :
  cost = quantity - (quantity*1/10)
else:
  cost = quantity
print(cost)