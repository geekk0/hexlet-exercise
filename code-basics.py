def get_even_numbers_up_to(number):
    counter = 1
    result = ''
    while counter < number:
        if counter % 2 == 0:
            result = result + str(counter)+","
        elif counter % 2 == 0 and counter == number or counter == (number-1):
            result = result + str(counter)+"."
        counter += 1
    return result
print(get_even_numbers_up_to(17))