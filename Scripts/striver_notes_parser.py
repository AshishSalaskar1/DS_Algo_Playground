import json
import sys
import os
import re
import shutil

def clean_filename(filename):
    # Define a regular expression pattern to match characters not allowed in filenames
    invalid_chars_pattern = r'[\\/:"*?<>|]'
    # Use re.sub() to replace invalid characters with an empty string
    cleaned_filename = re.sub(invalid_chars_pattern, '', filename)
    return cleaned_filename


json_path = f"C://Users/ashis/Downloads/cleaned_items.json"
code_path = "D:\Github\DS_Algo_Playground\Track\DSA_A_to_Z"
with open(json_path, encoding='utf-8') as f:
    data = json.load(f)

total_refresh = False

if len(sys.argv) == 1:
    total_refresh = False
elif sys.argv[1] == "all":
    total_refresh = True

# iterate folders topic wise and then replace
for x in data:
    file_name = clean_filename(x["fileName"])
    topic_name = x["topic"]
    data = x["data"]

    print("FILE: ",file_name)
    print("TOPIC: ",topic_name)

    # preprocess topic name
    topic_name = topic_name.replace("Solve Problems on ","")
    if "[" in topic_name:
        topic_name = topic_name[:topic_name.find("[")].strip()

    if "/" in topic_name:
        topic_name = "others"
    else:
        dir_path = f"{code_path}/{topic_name}"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    dir_path = f"{code_path}/{topic_name}"
    file_path = f"{dir_path}/{file_name}.py"
    if not os.path.exists(dir_path): # create topic folder if it doesnt exist
        os.mkdir(dir_path)

    # check if file exists
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(data)
    elif os.path.exists(file_path) and total_refresh: # rewrite only if total refresh enabled
        with open(file_path, "w") as f:
            f.write(data)

    



