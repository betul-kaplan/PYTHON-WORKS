def equall(* arg ):
  num=list( arg)

  result=num.count(max(num,key=num.count))

  if result > 1 :
    return result
  else:
    return 0  
equall(4,4,4,9,9,7,0)