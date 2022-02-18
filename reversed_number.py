def turn_over(user_number):
    inverted_number = ''
    for i in user_number:
        inverted_number = i + inverted_number
    return inverted_number

user_number = input('Введите число: ')
print('inverted_number1')
print('inverted_number =', int(turn_over(user_number)))



