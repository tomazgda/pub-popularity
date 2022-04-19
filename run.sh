#!/usr/bin/env python3

import populartimes as pt
import json
import csv
import sys

# Google API key goes here 
key = str(sys.argv[1])

pos1 = (float(sys.argv[2]), float(sys.argv[3]))
pos2 = (float(sys.argv[4]), float(sys.argv[5]))

print("Key =", key)
print("First Position =", pos1)
print("Second Position =", pos2)

# key = "AIzaSyAO02v5qlRonEysxlE_KlYl8r_T2R_69LM"

# gets data on bars within given coordiante bounds 
def data_in_area():
    return pt.get(key, ["Pubs & Bars"], pos1, pos2, 8, 1000, False)

# Function to sort list in descending order of value of 8th (ninth) term  
def Sort(sub_li):
    return(sorted(sub_li, key = lambda x: x[8], reverse=True))    

def popularity():
    data = data_in_area()
    list = []
    for i in range(len(data)):
        total_popularity = 0 
        x = data[i]
        y = x['populartimes']
        for i in range(len(y)):
            days_info = y[i]
            days_data = days_info['data']
            total_popularity += sum(days_data)
            if i == 0:
                mon = sum(days_data)
            elif i == 1:
                tue = sum(days_data)
            elif i == 2:
                wed = sum(days_data)
            elif i == 3:
                thu = sum(days_data)
            elif i == 4:
                fri = sum(days_data)
            elif i == 5:
                sat = sum(days_data)
            elif i == 6:
                sun = sum(days_data)
        name = x['name']
        info = [name, mon, tue, wed, thu, fri, sat, sun, total_popularity]
        list.append(info)
    return Sort(list)


# Write list to cvs file 
def write_csv(popularity_list):
    header = ['Name', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Total']
    output_file = open('data.csv', 'w')
    writer = csv.writer(output_file)
    
    writer.writerow(header)
    for x in popularity_list:
        data = [x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]]
        writer.writerow(data)
    output_file.close()
    
# Essentailly just runs write_cvs(), can be removed 
def run():
    list = popularity()
    write_csv(list)
    print("CSV FILE WRITTEN")

run()
