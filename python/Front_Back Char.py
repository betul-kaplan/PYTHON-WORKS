###FRONT-BACK CHAR  (ÖN ARKA KARAKTER)###
def front_back(word):
      if len(word)<=1:
              return word
            a= word[1:len(word)-1]
              b=word[len(word)-1]
                c=word[0]
                  return b+a+c
              front_back("clarusway")