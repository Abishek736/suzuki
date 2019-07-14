a = int(input())
strn1 = []
for b in range(0,a):
    strn = input()
    strn1.append(strn)

b = 0
r = 0
flag = True
for b in range(0,len(strn1[0])):
    if(flag==False):
        break
    m=1
    while(m<a and strn1[0][b]==strn1[m][b]):
        m+=1
    if(m==a):
        r+=1
    else:
        flag = False
        break
    
for b in range(0,r):
    print(strn1[0][b],end="")
