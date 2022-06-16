import os

a_vals = [0.1, 0.2, 0.3, 0.4,0.5]
l1_vals = [0.1, 0.2, 0.3, 0.4,0.5]

for a in a_vals:
    for l1 in l1_vals:
        os.system(f"python simple.py -a {a} -l1 {l1}")