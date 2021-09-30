import csv
array = []
with open("table.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        array.append(row[0].split(';'))
array.append([])
for i in range(7):
    array[i].append('')
for i in range(3):
    array[6-i] = array[5-i]

for i in range(7):
    for j in range(3):
        array[i][6-j] = array[i][5-j]
array[3] = [0, 0, 0, 0, 0, 0, 0]
for i in range(7):
    array[i][3] = 0  
with open("new_table.csv", "a") as file:
    writer = csv.writer(file)
    for line in array:
        writer.writerow(line)	
