#Lorene Marques - 1615310013
v1 = [0,3,6,9,12,15,18,21,24,27]
v2 = [1,4,7,10,13,16,19,22,25,28]
v3 = [2,5,8,11,14,17,20,23,26,29]
v4 = []
x = 0
while x < 10:
    v4.append(v1[x])
    v4.append(v2[x])
    v4.append(v3[x])
    x += 1
print(v4)
