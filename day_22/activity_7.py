import os

contents = os.listdir('.')

print(f"Total items in {os.getcwd()}: {len(contents)}")