def main():
  print("Hello learners!")

def addmultiplenumbers(numbers):
  return sum(numbers)

def multiplymultiplenumbers(numbers):
  if not numbers:
    return 0
  resultado = 1
  for num in numbers:
    resultado *= num
  return resultado

def isiteven(num):
  if not isitaninteger(num):
   return False
  
  return int(num) % 2 == 0

  

def isitaninteger(num):
  if isinstance(num, int):
    return True
  if isinstance(num, float):
    return num.is_integer()
  try:
    return float(num).is_integer()
  except:
    return False




  if __name__=="__main__":
    main()