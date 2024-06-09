#Функція filter дає 
# можливість відфільтрувати
# елементи послідовності. 
# Приймає в ролі аргументів 
# функцію і послідовність, 
# яку необхідно відфільтрувати:


mixed = ['red', 'green', 'red', 'red', 'black', 'red', 'white', 'black', 'white', 'red']

zol = list(filter(lambda x: x == 'red', mixed))
print ("Filter: ", zol)

zol_2 = list(map(lambda x: x == 'red', mixed))
print ("Map: ", zol_2)

