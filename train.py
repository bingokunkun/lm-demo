import time

a = open('model.txt', 'r').readlines()
b = open('data.txt', 'r').readlines()
print('data', b)
print(a)
open('model.txt', 'w').write(str(time.time()))
