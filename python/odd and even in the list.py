#Find even and odd number in the given list:

for i in [1,2,3,4]  :
  print(i,":",(lambda x: "odd" if x%2==0 else "even")(i))