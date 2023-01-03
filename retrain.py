import os
import time

a = open('dataset/test.txt', 'r').readlines()
m = open('model/model.txt', 'r').readlines()
print(m)
os.mkdir('saved_model')
f = open('saved_model/model.txt', 'w')
f.write(str(time.time()))
f.writelines(a)
