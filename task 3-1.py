numbers = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eigth': 'восемь',
    'nine': 'девять',
    'ten:': 'десять'
}

def num_translate(user_number):
    return numbers.get(user_number)

print(num_translate(input('Введите число на английском: ')))