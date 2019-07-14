s,p=input().strip().split(" ")
p=int(p)
c=0
while c<len(s)-1 and p:
	if(s[c]>s[c+1]):
		p-=1
		s=s[:c]+s[c+1:]
		if(c!=0):
			c-=1
	else:
		c+=1
z=s[:len(s)-p]
print(z)
