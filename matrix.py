def read_matrix(filename):
	''' reading the matrix elements from an external file and returns the data in the form of nested lists'''
	with open(filename,'r') as f:
		matrix=[]
		for line in f:
			row=[float(num) for num in line.strip().split()]
			matrix.append(row)
	return matrix

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



