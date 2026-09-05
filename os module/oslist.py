import os 
folders = os.listdir("data")

print(os.getcwd())
print(folders)
for folder in folders:
    print(os.listdir(f"data/{folder}"))