#most_freq_number  :

def most_freq(*given_list):
  
   result= given_list.count(max(given_list,key=given_list.count))
   if result > 1:
     return result
   else:
     return 0

most_freq(8,8,8,8)   