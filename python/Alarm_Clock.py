# alarm saat hafta içi 7 00 da hafta sonu 10 00 da  tatilde haftaici 10 00 da hafta sonu calmasın

days = 1 #pazrt
vacation = True
clock =""

if days in range(1,6) :
  clock ="7 :00"
else:
  clock = "10:00"
if vacation and days in range(1,6):
  clock ="10 :00" 
elif vacation and (days == 0 or days == 6):
  clock ="off"
print(clock) 