from zipfile import ZipFile as zf,ZIP_DEFLATED as zd,ZIP_BZIP2 as zb

with zf("arch.zip","x") as z:
	z.write('ss.png')


with zf("arch_1.zip","w",compression = zd) as zipf:
	zipf.write('t1.txt')
	zipf.write('t2.txt')


with zf("arch.zip",'r') as z:
	files = z.extractall("extracted_arch")

print(files)

with zf("arch.zip",'r') as z:
	files = z.namelist()
print(files)


with zf("arch.zip",'r') as z:
	text = z.infolist()

print(text)

with zf("arch.zip",'r') as z:
	text = z.printdir()

print(text)


with zf("arch.zip",'r') as z:
	text = z.getinfo('t1.txt')

print(text)


with zf("arch.zip",'r') as z:
	file = z.extract('t1.txt')



user_input_dir = input("Enter the dir name: ")

with zf(user_input_dir,'r') as z:
	files = z.namelist()

print(files)



with zf('arch.zip','r') as z:
	files = z.namelist()
print(f"I have these files: {files}")
if "foo.txt" in files:
	print(f"foo.txt Found")
else:
	print("foo.txt is Missing!")



with zf('zip_3_files.zip','w') as z:
	z.write("t1.txt")
	z.write("t2.txt")
	z.write("t3.txt")

with zf('zip_3_files.zip','r') as ez:
	files = ez.namelist()

print(files)

with zf('zip_bzip2_3files.zip','w',compression=zb) as z:
	z.write("t1.txt")
	z.write("t2.txt")
	z.write("t3.txt")

with zf('zip_bzip2_3files.zip','r') as f:
	files = f.namelist()

with zf('zip_bzip2_3files.zip','r') as f:
	for file in files:
		print(f"{file} => {f.getinfo(files[0]).file_size} bytes")