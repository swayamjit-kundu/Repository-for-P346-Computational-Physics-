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

#applying gauss jordan for question 1
print('solution=',Gauss_jordan(L,3))



#Augmentation
f2=read_matrix('coeff1.txt')
f3=read_matrix('const2.txt')
K=[]
for i in f2:
    for j in f3:
        if f2.index(i)==f3.index(j):
            k=i+j
            K.append(k)
            k=[]

#applying gauss jordan for question 2
print('solution=',Gauss_jordan(K,6))


'''final output:
    
    solution= [-2.0, -2.0, 1.0]
    solution= [-4.215544188689968, -7.813678128256133, 0.0, 1.1252249692147385, 3.7049824760822205, 0.8879890120299325]
'''