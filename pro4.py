a,b=map(str,input().split())
y=0
if len(a)>len(b):
	a,b=b,a
z=0
while z<len(a):
	  y+=(ord(b[z])-ord(a[z]))
	  z+=1
for z in range(z,len(b)):
	  y+=ord(b[z])-ord('a')+1
print(y)
