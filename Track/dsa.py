import pandas as pd

names = []

df = pd.read_csv("C:/Users/ashis/Desktop/Dataset-Indian-Names-master/Indian-Male-Names.csv")
arr = [str(x).split(" ")[0] for x in df["name"].tolist()]
names.extend(arr)

df = pd.read_csv("C:/Users/ashis/Desktop/Dataset-Indian-Names-master/Indian-Female-Names.csv")
arr = [str(x).split(" ")[0] for x in df["name"].tolist()]
names.extend(arr)


names = set(names)

def get_all_chunks(name):
    res = []
    for chunk_size in range(1,len(name)):
        for i in range(len(name)-chunk_size):
            res.append(name[i:i+chunk_size+1])
    return res

def name_gen(n1, n2):
    res = []
    n1_chunks = get_all_chunks(n1)
    n2_chunks = get_all_chunks(n2)
    for x in n1_chunks:
        for y in n2_chunks:
            res.append(x+y)


    res = filter(lambda x:len(x)>3 and x in names, res)
    return list(res)

res = name_gen("akshata", "anil")
print(res)

res = name_gen("anil", "akshata")
print(res)