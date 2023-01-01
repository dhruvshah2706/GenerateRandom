# this code creates a file and stores numbers along with a code from C1 upto C10


import csv
from random import randint

def randomise():
    file = open('data\Project2.csv', 'w', newline='')
    Writer = csv.writer(file)
    list = ['Random', 'Code']
    final = []
    Writer.writerow(list)
    for i in range(0, 10000):
        code = randint(1, 10)
        num = 0
        for j in range(0,3) :
            num = num * 10 + randint(0, 9)
        code = f'C{code}'
        list = [num, code]
        Writer.writerow(list)
