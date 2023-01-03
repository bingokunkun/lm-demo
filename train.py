import os
import time

a = open('dataset/test.txt', 'r').readlines()
print('data', a)
os.mkdir('saved_model')
open('saved_model/model.txt', 'w').write(str(time.time()))
