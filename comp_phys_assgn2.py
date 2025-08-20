#Swayamjit Kundu, 2311196, Assignment 2 (Gauss Jordan)

from mylib import *

#Augmentation
f=read_matrix('coeff.txt')
f1=read_matrix('constant.txt')
L=[]
for i in f:
    for j in f1:
        if f.index(i)==f1.index(j):
            k=i+j
            L.append(k)
            k=[]
print(L)


print(Gauss_jordan_3(L))
