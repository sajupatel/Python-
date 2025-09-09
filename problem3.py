import os

# specify the path (you can change this to any directory)
path = "/"

print(f"Contents of directory '{path}':")
for item in os.listdir(path):
    print(item)
