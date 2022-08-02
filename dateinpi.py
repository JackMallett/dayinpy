import csv
import ahocorasick_rs


patterns = []

startyear, endyear = 1900, 2023

for y in range(startyear, endyear):      #loop to create string for all dates within given range
    for m in range(1,13):
        for d in range(1,32):
            x = str(m).zfill(2) + str(d).zfill(2) + str(y).zfill(4)     #adds leading zeros if needed to create string of constant length
            patterns.append(x)


file = open('Pi - Dec.txt', 'r')    #open txt file containing first billion digits of pi

pi = file.read()
file.close()
searcher = ahocorasick_rs.AhoCorasick(patterns)
results = searcher.find_matches_as_indexes(pi)      #searches for all occurances of all dates within patterns list


f = open('allthedates.csv', 'w', newline='')

writer = csv.writer(f)
rows = []   #stores rows for csv write
used = []   #stores dates for easier searching of index for repeats

for x in results:
    key = patterns[x[0]]    #date that was matched
    ind = x[1]              #index within pi of occurance
    row = [key, ind]        #row to be written if non-repeat
    if key not in used:
        rows.append(row)    #add to output list
        used.append(key)    #add date to list of dates done
    else:
        rows[used.index(key)].append(ind)   #adds repeats onto the end of the existing row

rows.sort(key=lambda a : a[0][2:4])     #sort by day
rows.sort(key=lambda a : a[0][0:2])     #sort by month
rows.sort(key=lambda a : a[0][4:8])     #sort by year

writer.writerows(rows)
f.close()
