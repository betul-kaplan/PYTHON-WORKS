#derslerin not ortalamaları alınarak kalan geçen dosyası oluşturulmuştur.

with open("dosya.txt","r",encoding = "utf-8") as notlar :
  file1 = notlar.readlines()

gecen = []
kalan = []

for i in file1 :
  a = (i.strip("\n")).split(",")
  ort = str(int(int(a[1])*0.3 + int(a[2])*0.3 + int(a[3])*0.4))
  a.append(ort)
  if a[4] >= "50" :
    b = ",".join(a)
    b += "\n"
    gecen.append(b)
  else :
    c = ",".join(a)
    c += "\n"
    kalan.append(c)

with open("kalan.txt","w",encoding = "utf-8") as file1 :
  file1.writelines(kalan)

with open("gecen.txt","w",encoding = "utf-8") as file2 :
  file2.writelines(gecen)