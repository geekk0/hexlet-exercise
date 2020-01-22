print("ВВедите три значения через пробел")
triple_list = input()
triple = (triple_list[0], triple_list[2], triple_list[4])
print(triple)
print("Направление переориентации тройки")
direction = input()


def rotate_left(triple):
    rotated_left = (triple[1], triple[2], triple[0])
    return rotated_left


def rotate_right(triple):
    rotated_right = (triple[2], triple[0], triple[1])
    return rotated_right


if direction == "Вправо":
    print(rotate_right(triple))
elif direction == "Влево":
    print(rotate_left(triple))
else:
    print("Направления только Вправо и Влево")
