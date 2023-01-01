# this code separates every number with their code and stores them in separate source files from 1 to 10

import csv
import pandas as pd

def separate():
    file1 = open('data\Project2.csv', 'r', newline='')
    df = pd.read_csv(file1)
    df = df.values.tolist()
    for i in range(1,11):
        list1 = list2 = []
        file2 = open(f'data\Source file {i}.csv','w',newline='')
        Writer = csv.writer(file2)
        for line in df:
            lis = [line[0]]
            if line[1] == f'C{i}':
                Writer.writerow(lis)
