# my_list = ['Вася', 'Маша', 'Витя', 'Коля']
# n = 0
# for i in range(len(my_list)):
#     if my_list[i] == 'Маша':
#         i += n
#         my_list.insert(i, '*')
#         n += 1
# print(f'{my_list[0]}{int(my_list[i]):02}')
#
# print(my_list)
# new_list = ''.join(my_list)
# print(new_list)

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for i in my_list:
    if i.replace('+', '').replace('-', '').isdigit(): # Если элемент списка состоит из чисел то '+' и '-' заменяем на ''
        if i.isdigit(): # если i состоит из чисел
            new_list.append(f'"{int(i):02}"') # добавляем 0 перед числом каждого элемента списка (числового)
        else:
            new_list.append(f'"{i[0]}{int(i[1:]):02}"') # Для нечисловых элементов списка. Первый индекс элемента
            # сцепляем с этим же элементов начиная со второго символа и со вставленным перед 0.
    else:
        new_list.append(i)

print(new_list)
print(' '.join(new_list))

# phrase = "Don't panic!"
# plist = list(phrase)
# print(phrase)
# # print(plist)
#
# plist = plist[1:8]
# space = plist.pop(4)
# plist.insert(2, space)
# plist.remove("'")
# plist.insert(-1, plist.pop(-1))
#
# new_phrase = ''.join(plist)
# # print(plist)
# print(new_phrase)
