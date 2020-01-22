print("Введите слово")
read = input()
def polindrom (read):
    reversed_read = read[::-1]
    if read == reversed_read:
        print("Yes")
    else: print("Not")
polindrom(read)

            