'''input
5
'''	
l = int(input())
t = [5,3,4]
z = 1
for i in t:
	z *= i
for i in range(z):
	print((i//(t[2]*t[1]))%t[0],(i//t[2])%t[1],i%t[2])
	for j in range(3):
		p = i
		for k in range(j+1,3):
			p //=t[k]
		p %= t[j]
		print(p)