#Swayamjit Kundu, 2311196, Assignment 3 (LU decomposition)

from mylib import *

#reading the matrix from .txt file(Q1)
M=read_matrix('coeff2.txt')

#perfoming LU decomposition on matrix of question 1
LU_decom(M, 3)
print(M) #printing the stored LU matrix

'''Output:
    [[1.0, 2.0, 4.0], [3.0, 2.0, 2.0], [2.0, 1.0, 3.0]]
    '''

#reading the matrix from .txt file(Q2)
P=read_matrix('coeff1.txt')

#perfoming LU decomposition on matrix of question 2
LU_decom(P, 6)
print(P)

'''Output:
    [[1.0, -1.0, 4.0, 0.0, 2.0, 9.0], [0.0, 5.0, 2.0, 7.0, 8.0, 4.0],
 [1.0, 0.2, 0.5999999999999996, 5.6, -0.6000000000000001, -11.8], 
 [6.0, 1.0, -40.00000000000002, 220.0000000000001, -44.000000000000014, -522.0000000000002],
 [-4.0, -0.4, 28.000000000000018, -0.6772727272727274, -6.800000000000001, 17.463636363636397], 
 [0.0, 1.4, -6.333333333333337, 0.1393939393939394, 0.7156862745098039, -22.06818181818185]]'''
    
B=read_matrix('const2.txt')
print('solution=',solve_LU(P,B,6)) #solving Q2 by forward and backward substitution


'''output:
    
    solution= [[-1.761817043997862], [0.8962280338740133], [4.051931404116158], 
               [-1.6171308025395421], [2.041913538501913], [0.15183248715593525]]'''
    
    
    
    
    
    
    
    
    
    

