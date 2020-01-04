
def getPrimes(n):
	primes = [True for i in range(n+1)]
	ans = set()
	
	i = 2
	while( i*i<=n ):
		if primes[i]:
			for j in range(i*2,n+1,i):
				primes[j] = False
		
		i += 1
			
			
	primes[0],primes[1] = False,False
			
	for a,b in enumerate(primes):
		if b:
			ans.add(a)
			
	return ans
			
	
print(getPrimes(20))
