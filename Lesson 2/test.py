my_list = ['Вася', 'Маша', 'Витя', 'Коля']
n = 0
for i in range(len(my_list)):
    if my_list[i] == 'Маша':
        i += n
        my_list.insert(i, '*')
        n += 1
print(f'{my_list[0]}{int(my_list[i]):02}')

print(my_list)
new_list = ''.join(my_list)
print(new_list)