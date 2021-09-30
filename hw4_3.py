import zipfile
with zipfile.ZipFile('/Users/Nadya/Downloads/main.zip') as my_zip_file:
	my_zip_file.extractall('/Users/Nadya/Downloads/main_unzip')
my_zip_file.close()
answer = open('f1.txt', 'w')
array = []
import os
for current_dir, dirs, files in os.walk("/Users/Nadya/Downloads/main_unzip"):
	list_files = files
	for f in files:
		filename, file_extension = os.path.splitext(f)
		if file_extension == '.py':
			array.append(os.path.abspath(f))
array.sort()
for a in array:
	answer.write(a + '\n')
answer.close()
		
