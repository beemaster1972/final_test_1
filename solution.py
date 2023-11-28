from re import split

with open("text.txt", encoding='utf8') as text:
    list_1 = split('\W+', text.read())
list_2 = [element for element in list_1 if len(element) <= 3]
print(f'Длина первого списка = {len(list_1)} \nДлина отфильтрованного списка =  {len(list_2)}')
print(list_2)
