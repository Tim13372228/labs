#Сибагатов Тимур ИПМбд 01-23 (лаб 5)

#Задание1
s = input('Введите строку: ')
count_upper = 0
count_lower = 0

for i in s:
    if i.isupper():
        count_upper += 1
    else:
        count_lower += 1

if count_upper > count_lower:
    print(s.upper())
elif count_upper < count_lower:
    print(s.lower())
else:
    print(s)


#Задание2
s = "объектно-ориентированный"
print(s[:6])
print(s[4:6] + s[7])
print(s[9:17])
print(s[16] + s[12] + s[13] + s[14] + s[19])
print(s[4] + s[7] + s[5])
print(s[1]+ s[7] + s[5])
print(s[6:8] + s[14] + s[19])
print(s[18:15:-1])
print(s[0]+s[4] + s[6] + s[7])


#Задание3

strr=input('Введите целые числа:')
if strr.isdigit():
    print(sum(list(map)(int, strr)))
else:
    count=0
    for i in strr:
        if i.isdigit():
            count += int(i)
    print(count)


#Задание4
def swap_keys_values(dictionary):
    dictionary_new = {}
    for key, value in dictionary.items():
        dictionary_new[value] = key
    return dictionary_new

dictionary = {
    1: 'объект',
    2: 'кто',
    3: 'ориентир',
    4: 'рента',
    5: 'кот',
    6: 'бот',
    7: 'нота',
    8: 'вор',
    9: 'окно',
}

print(swap_keys_values(dictionary))






