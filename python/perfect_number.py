#perfect_number  :

# Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
# Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
#  Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

perfect = list()
for num in range(1,10000):
  toplam = list()
  for i in range(1,num):
    if num % i == 0:
      toplam.append(i)
  if sum(toplam) == num:
      perfect.append(num)
print(perfect)