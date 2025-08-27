#Swayamjit Kundu, 2311196, Assignment 4 (Cholesky decomposition and Jacobi method)

from mylib import *
import numpy as np
A=read_matrix('coeff3.txt')
B=read_matrix('const3.txt')

    
print(cholesky(A)) # printing the cholesky matrix
'''
output:
    [[2.0, 0.5, 0.5, 0.5], [0.5, 1.7320508075688772, -0.5773502691896258, 0.5773502691896258],
     [0.5, -0.5773502691896258, 1.4142135623730951, 0.0], [0.5, 0.5773502691896258, 0.0,
                                                           1.4142135623730951]]'''
    
print(solve_LU(cholesky(A),B,len(B))) #printing the solution after cholesky decomposition

'''output:

    [[1.1225060113390457], [0.8028691734572702], [0.25881904510252085], [0.4482877360840266]]'''
    
print(jacobi(A,B,[0,0,0,0]))


'''output:

    [[1.1225060113390457], [0.8028691734572702], [0.25881904510252085], [0.4482877360840266]]'''




    
    
    