print ("Введите двузначные координаты X и Y (через пробел) первой точки отрезка")
first = input()
x1 = int(first[0]+ first[1])
y1 = int(first[3] + first[4])
print ("Введите двузначные координаты X и Y (через пробел) второй точки отрезка")
second = input()
x2 = int(second[0] + second[1])
y2 = int(second[3] + second[4])

def line_life (x1,y1,x2,y2):
    if x1 == x2 :
        if y1 == y2:
            print("Отрезок вырождается в точку")
        else:
            print("Отрезок вертикальный")
    elif y1 == y2 :
        print ("Отрезок горизонтальный")
    else:
        print ("Отрезок наклонный")
line_life(x1,y1,x2,y2)
            


