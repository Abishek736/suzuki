a,b=input().split()
xl=len(a)
yl=len(b)
m=abs(xl-yl)
if xl<=yl:
  s=a
  l=b
else:
  s=b
  l=a
if len(s)==1:
  print(m)
else:
  for i in range(len(s)):
    if s[i]!=l[i]:
      m+=1
  print(m)
