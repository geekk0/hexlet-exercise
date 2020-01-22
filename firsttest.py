def print_with_exlamation(word):
    print (word +"!")
print_with_exlamation("Велком")
print_with_exlamation("в программу")
print_with_exlamation("проверка типа вводимых данных")
import sys
import string
print ("Введите два целых числа от 0 до 10 через клавишу Enter ")
ruslet = 'а,б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я'
a=input()
b=input()
if a in string.ascii_letters or b in string.ascii_letters :
    print("цифры должны быть, не лат буквы")
    sys.exit()
elif a in ruslet or b in ruslet :
    print("цифры должны быть, не рус буквы")
    sys.exit()
elif len(a) >=3 or len(b) >=3 :
    print ("Многовато символов")
    sys.exit()
else:
    a=int(a);
    b=int(b);
if a == b :
    print ("Ввведите разные числа")
    sys.exit()
elif a<0 or b<0 : 
    print ("Числа от 0")
    sys.exit()
elif a>10 or b>10 :
    print ("Числа до 10")
    sys.exit()
else :
    print ("Введите желаемое арифметическое действие")
    action = str(input());
if  action == 'сложение':
    c = a+b
    print("Результат :",c)
elif action == 'умножение':
    d = a*b
    print("Результат :",d)
elif action == 'деление':
    if b == 0 :
        print("На 0 делить нельзя")
        sys.exit()
    else:
        e = a/b
        print("Результат :",e)
elif action == 'вычитание':
    f = a-b
    print("Результат :",f)
else :
    print("Корректно введите действие")
    sys.exit()




     
    
    
    
    
   
 


