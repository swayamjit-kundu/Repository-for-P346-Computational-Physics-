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
    

def Gauss_jordan(l,n):
    '''solves a linear equation in n variables using gauss-jordan elimination. l= augmented matrix. Returns the solution as a list.'''
    a=[]
    p=[]
    for i in l:
        a.append(i[0])
    l[0],l[a.index(max(a))]=l[a.index(max(a))],l[0] #swapping the row having largest zeroth value with the top row 
    l[0]=list(np.array(l[0])/l[0][0])
    for j in range(1,n):
        for i in range(j,n):
            l[i]=list(np.array(l[i])-np.array(l[j-1])*l[i][j-1]) #making zeros
        if l[j][j]!=0:
            l[j]=list(np.array(l[j])/l[j][j]) #making the 1st non-zero element= 1
        else:
            for x in l[j]:
                if x!=0:
                    l[j],l[l[j].index(x)]=l[l[j].index(x)],l[j]
                    break
                else:
                    continue                
    for j in range(1,n):
        for i in range(j,n):
            l[n-i-1]=list(np.array(l[n-i-1])-np.array(l[n-j])*l[n-i-1][n-j])   # making the upper triangular matrix zero
    for i in l:
        p.append(i[-1])
    return p


def LU_decom(A,n):
    '''LU decomposition using Doolittle factorization'''
    L=[]
    U=[]
    sum1=0
    sum2=0
    for i in range(n):
        L.append([])
        U.append([])
        for j in range(n):
            L[i].append(0)
            U[i].append(0)
    for i in range(n):
        U[1][i]=A[1][i]
        L[i][i]=1
    for j in range(n):
        for i in range(1,j):
            for k in range(i-1):
                sum1+=L[k][j]*U[k][j]
            U[i][j]=A[i][j]-sum1
        for i in range(j+1,n):   
            for k in range(j-1):
                sum2+=L[k][j]*U[k][j]
            L[i][j]=(A[i][j]-sum2)/U[j][j]
    return L,U
    

    
    










