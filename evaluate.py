import os
import json

a = open('dataset/test.txt', 'r').readlines()
m = open('model/model.txt', 'r').readlines()
print(m)
os.mkdir('results')
f = open('results/metrics.json', 'w')
data = json.dumps({'a': 1})
f.write(data)
