import json
import sys
import os


json_path = f"C://Users/ashis/Downloads/cleaned_items.json"
code_path = "D:\Github\DS_Algo_Playground\Track\Striver_180"
with open(json_path) as f:
    data = json.load(f)

total_refresh = False

if len(sys.argv) == 1:
    total_refresh = False
elif sys.argv[1] == "all":
    total_refresh = True

# iterate folders topic wise and then replace
for x in data:
    file_name = x["fileName"]
    topic_name = x["topic"]
    data = x["data"]

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


    



