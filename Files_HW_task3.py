import os

current_dir = os.getcwd()
folder_name = 'files'

file_path = os.path.join(current_dir, folder_name)
files = os.listdir(file_path)


file_dict = {}
for x in files:
    name = os.path.join(file_path,x)
    with open(name, encoding='utf-8') as file:
        lines = file.readlines()
        text = []
        len_text = len(lines)
        for line in lines:
            text.append(line.strip())
        file_dict[x] = (len_text, text)

sorted_values = sorted(file_dict.values())
sorted_dict = {}

for n in sorted_values:
    for k in file_dict.keys():
        if file_dict[k] == n:
            sorted_dict[k] = file_dict[k]
            break

with open('final.txt', "w", encoding='utf-8') as file:
    for key, value in sorted_dict.items():
        file.write(f"{key}\n")
        file.write(f"{value[0]}\n")
        for val in value[1]:
            file.write(f"{val}\n")