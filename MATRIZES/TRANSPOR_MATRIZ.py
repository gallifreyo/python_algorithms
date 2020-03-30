

    
def transpor(m):
  mz = []
  l = len(m[0])
  c = len(m)
  for i in range(l):
    l = []
    for j in range(c):
      l.append(m[j][i])
    mz.append(l)
    
  return mz

               

