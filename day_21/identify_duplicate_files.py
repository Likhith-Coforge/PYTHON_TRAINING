import zipfile as zf

"""
with zf.ZipFile('zip_1.zip','w') as file:
	file.write('t1.txt')
	file.write('t2.txt')
	file.write('t3.txt')
	file.write('t4.txt')
"""
with zf.ZipFile('zip_1.zip','r') as file:
	files = file.namelist()

contents_list = []
contents_dict = {}

for file in files:
	with open(file,'r') as f:
		text = f.read()
		contents_list.append(text)
		contents_dict[file] = text
		if contents_list.count(text) > 1:
			parent_file = [k for k,v in contents_dict.items() if v==text ]
			print(file," is a duplicate file of ",parent_file[0])

print(contents_list)