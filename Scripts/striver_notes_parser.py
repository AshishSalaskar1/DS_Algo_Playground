import json


json_path = f"C://Users/ashis/Downloads/cleaned_items.json"
with open(json_path) as f:
    data = json.load(f)

print(data[0]["data"])

with open("test.py","w") as f:
    f.write(data[2]["data"])