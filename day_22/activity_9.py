import os

starting_dir = os.getcwd()

os.mkdir('temp_folder')

os.chdir('temp_folder')

print(f"Starting at: {starting_dir}")

print(f"Now in: {os.getcwd()}")

os.chdir(starting_dir)

print(f"Returned to: {os.getcwd()}")