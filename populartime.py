import populartimes as pt
import json
import csv

# Google API key goes here 
key = " "

# Some places' latitudes and longditudes 
weybrige = (51.371647361061285, -0.45789862797850234)
romford = (51.57663036646349, 0.1773901549118097)

wandsworth = (51.45776244897419, -0.1876677526206532)
vauxhall = (51.48631022518863, -0.12181357251614632)

putney = (51.45904037312932, -0.21278629073928298)
city = (51.510212872865345, -0.08513867435070359)

wimbledon = (51.41962648727805, -0.22901660517886052)
stratford = (51.54711411281706, -0.008190931982966429)

# gets data on bars within given coordiante bounds 
def data_in_area():
    return pt.get(key, ["bar"], wimbledon, stratford, 8)

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

# DEPRECATED Write list to text file 
def write_text(popularity_list):
    output_file = open('data.txt', 'w')
    for element in popularity_list:
        output_file.write(str(element[1]) + " " + element[0])
        output_file.write('\n')
    output_file.close()

# Write list to cvs file 
def write_cvs(popularity_list):
    header = ['Name', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Total']
    output_file = open('data.cvs', 'w')
    writer = csv.writer(output_file)
    
    writer.writerow(header)
    for x in popularity_list:
        data = [x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]]
        writer.writerow(data)
    output_file.close()
    
# Essentailly just runs write_cvs(), can be removed 
def run():
    list = popularity()
    # write_text(list)
    # print("TEXT FILE WRITTEN")
    write_cvs(list)
    print("CVS FILE WRITTEN")
        

