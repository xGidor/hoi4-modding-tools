import os
import glob
import re

# Define the directory path and file extension
dir_path = 'C:/Users/User/Documents/modding/mod/countries'
file_ext = '*.txt'

# Define the strings to remove
strings_to_remove = ['recruit_character = DEF_philip_kirchner', 'recruit_character = DEF_andrew_wiles']

# Loop through each file in the directory with the specified extension
for file_path in glob.glob(os.path.join(dir_path, file_ext)):

    # Read the file into a list of lines
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Remove the specified strings from each line
    lines = [line for line in lines if not any(string in line for string in strings_to_remove)]
    print("file done")
    # Write the modified lines back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)



