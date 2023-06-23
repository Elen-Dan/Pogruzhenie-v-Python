'''Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке'''

for i in [[2, 3, 4, 5], [6, 7, 8, 9]]:
    if i != 0:
        print("")
    for j in range(2, 10):
        print('%s X %s = %s\t' % (i[0], j, i[0] * j if i[0] * j > 9 else ' ' + str(i[0] * j)),
              '%s X %s = %s\t' % (i[1], j, i[1] * j if i[1] * j > 9 else ' ' + str(i[1] * j)),
              '%s X %s = %s\t' % (i[2], j, i[2] * j if i[2] * j > 9 else ' ' + str(i[2] * j)),
              '%s X %s = %s\t' % (i[3], j, i[3] * j if i[3] * j > 9 else ' ' + str(i[3] * j)))