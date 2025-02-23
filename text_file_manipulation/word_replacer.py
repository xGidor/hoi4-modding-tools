import os
import glob
import re

# Define the directory path and file extension
dir_path = 'C:/Users/User/Documents/modding/mod/countries'
file_ext = '*.txt'

# Define the words to replace and the string to replace them with
words_to_replace = {
    'old_ideology': 'new_ideology',
}

# Loop through each file in the directory with the specified extension
for file_path in glob.glob(os.path.join(dir_path, file_ext)):

    # Read the file into a string
    with open(file_path, 'r', encoding='utf-8') as f:
        file_text = f.read()

    # Replace the specified words with the provided string
    for word, replacement in words_to_replace.items():
        regex = r'(?<![^\W_]){word}(?![^\W_])'.format(word=word)
        file_text = re.sub(regex, replacement, file_text)

    # Write the modified text back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(file_text)
