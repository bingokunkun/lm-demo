import time

a = open('dataset/test.txt', 'r').readlines()
print('data', a)
open('saved_model/model.txt', 'w').write(str(time.time()))
