#5 year service bonus  :

salary=int(input("Enter your salary"))
service=int(input("how many year your service"))
if service >= 5 :
  bonus=salary+(salary*(5/100))
  print(f"congragulatıons you won {bonus} bonus ")
else:
  print(f"sorry you must work {5-service} more year for bonus"