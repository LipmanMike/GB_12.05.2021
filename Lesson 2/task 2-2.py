my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

n = 0 # переменнная для смещения индекса элементов

for i in range(len(my_list)): # присваиваем i индекс каждого элемента списка
    if my_list[i] == '5':
        i += n
        my_list.insert(i, '"')
        n += 1
        if my_list[i][0] == '+' or my_list[i][0] == '-':
            i += n
            my_list[i][0].insert(i, int('0'))
            # f'{my_list[i][0]}{(int(my_list[i]):02)}'
            n += 1

print(my_list)
# new_list = ''.join(my_list)
# print(new_list)




