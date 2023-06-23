# Нарисовать в консоли ёлку, спросив у пользователя количество рядов.

rows = int(input("Введите количество рядов: "))
spaces = rows-1
stars = 1
for i in range(rows):
    print(
              (' '*spaces) +
              ('*'*stars) 
          )
    stars += 2
    spaces -= 1