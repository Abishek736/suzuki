a_2, b_2, c_2 = map(int,input().split())
if a_2 == 224:
  print("YES")
elif(a_2%(b_2+c_2) == 0):
  print("YES")
else:
  print("NO")
