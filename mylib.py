import numpy as np

'''class MyComplex():
	def __init__ ( self , real ,imag=0.0):
        self.r=real
        self.i=imag
	def display_cmplx( self ):
		print( self.r , ',' , self.i , 'j' ,sep=' ' )
	def add_cmplx(self ,c1 ,c2 ):
        self.r=c1.r+c2.r
 		self.i=c1.i+c2.i
 		return MyComplex( self )
	def sub_cmplx(self ,c1 ,c2 ):
        self.r=c1.r - c2.r
 		self.i=c1.i - c2.i
 		return MyComplex( self )
	def mul_cmplx(self ,c1 ,c2 ):
        self.r=c1.r*c2.r-c1.r*c2.i
 		self.i=c1.i*c2.r + c1.r*c2.i
 		return MyComplex( self )
	def mod_cmplx( self ):
        return np.sqrt( self.r**2 + self.i**2)
    '''
    

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
	C=np.zeros_like(A)
	C=list(C)
	if len(A)==len(B) and len(A[0])==len(B[0])==1:
		print('dot product is possible.')
		for i in range(len(A)):
			C[i]=A[i][0]*B[i][0]
		return C
	else:
		print('dot product is not possible.')

def random_normal(c,N,seed=0.1):
    '''generates a list of random numbers using the formula x_i+1=c*x_i*(1-x_i).  N= number of random numbers to be generated. '''
    L=[]
    x_i=seed
    L.append(x_i)
    for i in range(N-1):
        x_i_next=c*x_i*(1-x_i)
        L.append(x_i_next)
        x_i=x_i_next
    return L

def random_gen_LCG(a=1103515245,c=12345,m=32768,N=1000,seed=10):
    '''generates a list of random numbers using linear congruential generator. N= number of random numbers to be generated.'''
    L=[]
    x_i=seed
    L.append(x_i)
    for i in range(N-1):
        x_i_next=(a*x_i + c)%m
        L.append(x_i_next)
        x_i=x_i_next
    return L
    

    















