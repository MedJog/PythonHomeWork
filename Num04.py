# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

m = int(input('Введите число долек: '))
n = int(input('Введите число долек: '))
k = int(input('Введите число долек: '))
if k % n == 0 or k % m == 0:
    print(f'От шоколадки {n} на {m} долек можно отломить {k} долек.')
else: 
    print(f'От шоколадки {n} на {m} долек нельзя отломить {k} долек.')