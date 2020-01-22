def binary (number):
    result=''
    if number == 0:
     result+='0'
    else:
     while number>0: 
      modulo = number % 2
      result = str(modulo)
      number = number//2
     return result
print(binary(7))
        