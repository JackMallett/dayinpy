import csv

f = open('allthedates.csv', 'r', newline='')

dates = []

thisdict = {}

def loadAll(dict):      #load all dates in file into dict with date string as key and list of occurances
    with open('somedates.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            templist = []
            for x in range(1,len(row)):
                templist.append(row[x])
            dict.update({row[0]: templist})

def find(date):
    with open('somedates.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == date:
                return row[1:]



        
date = input('Please enter your birthday in MM/DD/YYYY format (Ex: "06/25/2002"): ')
date = date.replace('/', '')
date = date.replace('-', '')
if len(date) != 8:
    print('Date was not entered as expected (make sure to include a zero in front of single-digit days or months)')





found = find(date)
count = len(found)
spots = []

for x in found:
    spot = int(x) // 10000000
    spots.append(spot)



def dashes(spots, length):
    length = length
    r = 100/length
    templist = []
    bottom = '   '

    for x in spots:
        spot = round(x/r)
        if spot not in templist:
            templist.append(spot)

    for x in range(length):
        char = ' '
        if x in templist:
            char = '^'
        bottom = bottom + char

    top = 'Digit 0' + (length-13)*' ' + 'Digit 1000000000'
    middle = '   [' + (length-2)*'-' + ']'
    print(top)
    print(middle)
    print(bottom)

length = 50
print('\nYour birthday occurs ' + str(count) + ' time in the first 1 billion digits of pi. Its first occurance begins at digit ' + str(found[0]) + '\n')

print('Here are the other spots where your birthday appears (each dash represents ' + str(1000000000//50) + ' digits): \n')

dashes(spots, length)

#Digit 0                                       Digit 1000000000
#   [------------------------------------------------]

f.close()