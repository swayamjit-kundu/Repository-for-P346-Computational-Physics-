# Swayamjit Kundu, roll- 2311196, Comp_Phys_Assignment_0

# adding the first 20 odd numbers
sum=0
for  i in range(20):
	b=(2*i)+1
	print(b, end= ' ')
	sum+=b
print('\n Sum of first 20 odd numbers: ',sum)

print('#####################')

# calculating the factorial of 8
a=0
c=1		
for i in range(8):
	a+=1
	c=c*a
print('factorial of 8 = ',c)	

print('#####################')

# GP terms summation for first 15 terms
initial=1.25
count=0
for i in range(15):
	x=initial*(0.5)
	print(initial,end=' ')
	count+=initial
	initial=x
print('\n sum of first 15 terms of GP =',count)

print('#####################')

# HP terms summation for first 15 terms
initial=1.25
count_0=0
initial_new=1/initial
for i in range(15):
	x=initial + 1.5
	p=1/x
	print(initial_new,end=' ')
	count_0+=initial_new
	initial_new=p
	initial=x

print('\n sum of first 15 terms of HP =',count_0)

print('#####################')

def read_matrix(filename):
	''' reading the matrix elements from an external file and returns the data in the form of nested lists'''
	with open(filename,'r') as f:
		matrix=[]
		for line in f:
			row=[float(num) for num in line.strip().split()]
			matrix.append(row)
	return matrix

matA=read_matrix('asgn0_matA')
print(matA)

print('#####################')

matB=read_matrix('asgn0_matB')
print(matB)

print('#####################')

vecC=read_matrix('asgn0_vecC')
print(vecC)

print('#####################')

vecD=read_matrix('asgn0_vecD')
print(vecD)

print('#####################')

def matrix_mult(A,B):
	'''checks whether matrix multiplication is possible or not and performs the matrix multiplication AB (if possible)'''
	list=[]
	list1=[]
	count1=0
	if len(A[0])==len(B):
		print('matrix multiplication is possible.')
		for i in range(len(A)):
			for j in range(len(B[0])):
				for k in range(len(A[0])):
					c=A[i][k]*B[k][j]
					count1+=c
				list.append(count1)
				count1=0
			list1.append(list)
			list=[]
		return list1
	else:
		print('matrix multiplication is not possible.')

print('matrix multiplication AB= ',matrix_mult(matA,matB)) 

print('#####################')

print('matrix multiplication BC= ',matrix_mult(matB,vecC)) 

print('#####################')

def vec_dot_prod(A,B):
	'''checks if the given vectors(column matrix) are of the same dimension and if dot product possible, then performs dot product A.B'''
	import numpy as np
	C=np.zeros_like(A)
	C=list(C)
	if len(A)==len(B) and len(A[0])==len(B[0])==1:
		print('dot product is possible.')
		for i in range(len(A)):
			C[i]=A[i][0]*B[i][0]
		return C
	else:
		print('dot product is not possible.')


print('dot product D.C=',vec_dot_prod(vecD,vecC))


'''Final Output:

1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39
 Sum of first 20 odd numbers:  400
#####################
factorial of 8 =  40320
#####################
1.25 0.625 0.3125 0.15625 0.078125 0.0390625 0.01953125 0.009765625 0.0048828125 0.00244140625 0.001220703125 0.0006103515625 0.00030517578125 0.000152587890625 7.62939453125e-05
 sum of first 15 terms of GP = 2.4999237060546875
#####################
0.8 0.36363636363636365 0.23529411764705882 0.17391304347826086 0.13793103448275862 0.11428571428571428 0.0975609756097561 0.0851063829787234 0.07547169811320754 0.06779661016949153 0.06153846153846154 0.056338028169014086 0.05194805194805195 0.04819277108433735 0.0449438202247191
 sum of first 15 terms of HP = 2.4139570733659186
#####################
[[2.0, -3.0, 1.4], [2.5, 1.0, -2.0], [-0.8, 0.0, 3.1]]
#####################
[[0.0, -1.0, 1.0], [1.5, 0.5, -2.0], [3.0, 0.0, -2.0]]
#####################
[[-2.0], [0.5], [1.5]]
#####################
[[1.0], [0.0], [-1.0]]
#####################
matrix multiplication is possible.
matrix multiplication AB=  [[-0.3000000000000007, -3.5, 5.2], [-4.5, -2.0, 4.5], [9.3, 0.8, -7.0]]
#####################
matrix multiplication is possible.
matrix multiplication BC=  [[1.0], [-5.75], [-9.0]]
#####################
dot product is possible.
dot product D.C= [-2.0, 0.0, -1.5]
'''









	





















