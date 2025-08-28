#Swayamjit Kundu, 2311196, Assignment 4 (Cholesky decomposition and Jacobi method)

from mylib import *


#reading the coefficient and constant matrix
A=read_matrix('coeff3.txt') 
B=read_matrix('const3.txt')

    
print(cholesky(A)) # printing the cholesky decomposed matrix(lower matrix)
 
'''
output:
    [[2.0, 0, 0, 0], [0.5, 1.6583123951777, 0, 0], [0.5, -0.753778361444409,
    1.087114613009218, 0], [0.5, 0.45226701686664544, 0.08362420100070905,
                            1.2403473458920844]]'''
    
print(solve_chols(A, B)) #solving question 1 using cholesky decomposition
'''output:

    [[0.0], [1.0], [1.0], [1.0000000000000002]]'''
    
#reading the coefficient and constant matrix
A=read_matrix('coeff3.txt')
B=read_matrix('const3.txt')
print(jacobi(A,B,[0,0,0,0])) #prints the solution matrix using jacobi method(Question 2)


'''output:

    [[0.0], [0.9999994039535522], [0.9999997019767761], [0.9999997019767761]]'''




    
    
    