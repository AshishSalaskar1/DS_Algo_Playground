N = int(input())
n = N-1
print("*"*((2*N)-1))

ind = 1

for i in range(1,N):
    print("*"*n+" "*ind+"*"*n)
    ind += 2
    n -= 1
n = 1
ind = ind-2
for i in range(1,N):
    print("*"*n+" "*ind+"*"*n)
    ind -= 2
    n += 1

print("*"*((2*N)-1))




