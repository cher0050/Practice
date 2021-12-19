rings=input()#"B0R0G0R9R0B0G0"

res=0
s=[set() for i in range(10)]

for i in range(0,len(rings),2):
	if s[int(rings[i+1])]=={'X'}: continue
	s[int(rings[i+1])].add(rings[i])
	if len(s[int(rings[i+1])])==3:
		s[int(rings[i+1])]={'X'}
		res+=1
print(res)
