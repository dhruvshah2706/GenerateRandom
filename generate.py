# this is the main part of the project which generates random numbes froma source file accepted from user

import pandas as pd
from random import randint
from csv import writer


def generate_numbers(lim, choice):
    choice = int(choice)
    df = pd.read_csv(f'data\Source file {choice}.csv')  #formatted string which generates random numbers from file chosen by user
    df = df.values.tolist()
    list1 = []  # it stores all numbers from source file
    list2 = [] # it stores all generated numbers
    for line in df:
        list1.append(int(line[0]))

    i = 0
    while i != lim:
        num = 0
        for j in range(0, 3): # degree of randomness increases
            num = num * 10 + randint(0, 9)
        if num in list1 and num not in list2:  # checks if generated number is valid
            ch = input('Press enter to get next number :')
            if len(ch) == 0 :
                print(num)
                i+=1
                list2.append(num)
    file1 = open(f'data\Result {choice}.csv', 'w', newline='')
    Writer = writer(file1)
    for i in range(0, len(list2)):
        line = [str(list2[i]), '']
        Writer.writerow(line)
    file1.close()

def generate():
    while True:
        print('Enter the number from which code you want to generate random numbers and enter 0 if you want to stop generating further numbers\nFor example if you want to generate random numbers from \'C1\' then enter 1\nThe file range is from 1 to 10')
        ch = int(input('Please enter your choice : '))
        if ch < 0 or ch > 10:
            print('Invalid input')
            continue  # this statement reiterates the loop
        elif ch == 0:
            return
        num = int(input('Enter the count of numbers you want to generate : '))
        if num < 0 : # We cannot generate negative count of numbers
            print('Invalid input')
            return # this statement ends the function
        generate_numbers(num, ch)
