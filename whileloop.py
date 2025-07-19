List = ['I', 'want', 'to', 'print', 'each', 'element']

#method 1
print("{}\n{}\n{}\n{}\n{}\n{}".format(List[0], List[1], List[2], List[3], List[4], List[5]))

i=0
while i!=len(List):
    print(List[i])
    i+=1
i=1
while i<=10:
    print(i)
    i+=1
g=2
while g<=20:
    print(g)
    g+=2
f=1
while f<=53:
    print(f)
    f+=2
for i in range(9):
  if i==3:
      continue
  print(i)