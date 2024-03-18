vetor = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
par = []
impar = []

for i in vetor:
  if i % 2 == 0:
    par.append(i)
  else:
    impar.append(i)
print(vetor)
print(par)
print(impar)