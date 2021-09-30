array = ['Line one', 'Line two', 'Line Three', 'Oh no, this is the last']
file_name = open('t2.txt', 'w')
def write_array(array, file_name):
	if len(array) != 0:
		file_name.write(array[0] + '\n')
		write_array(array[1::], file_name)
	pass
write_array(array, file_name)
file_name.close()
