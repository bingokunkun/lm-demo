import os
import time

a = open('dataset/test.txt', 'r').readlines()
m = open('model/model.txt', 'r').readlines()
print(m)
os.mkdir('results')
f = open('results/metrics.json', 'w')
f.write("{'a': 1}")
