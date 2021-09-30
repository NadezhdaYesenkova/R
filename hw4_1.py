with open('t1.txt', 'w') as file:
	file.write('     The first line.')
	file.write('The second and the last line.    ')
file.close()
with open('t1.txt', 'r') as file1:
	for line in file1:
       		print(line.strip())
