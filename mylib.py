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
	'''checks whether matrix multiplication is possible or not and performs the 
    matrix multiplication AB (if possible)'''
	list=[]
	list1=[]
	count1=0
	if len(A[0])==len(B):
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
	'''checks if the given vectors(column matrix) are of the same dimension and
    if dot product possible, then performs dot product A.B'''
	C=np.zeros_like(A)
	C=list(C)
	if len(A)==len(B) and len(A[0])==len(B[0])==1:
		for i in range(len(A)):
			C[i]=A[i][0]*B[i][0]
		return C
	else:
		print('dot product is not possible.')

def random_normal(c,N,seed=0.1):
    '''generates a list of random numbers using the formula x_i+1=c*x_i*(1-x_i). 
    N= number of random numbers to be generated. '''
    L=[]
    x_i=seed
    L.append(x_i)
    for i in range(N-1):
        x_i_next=c*x_i*(1-x_i)
        L.append(x_i_next)
        x_i=x_i_next
    return L

def random_gen_LCG(a=1103515245,c=12345,m=32768,N=1000,seed=10):
    '''generates a list of random numbers using linear congruential generator. 
    N= number of random numbers to be generated.'''
    L=[]
    x_i=seed
    L.append(x_i)
    for i in range(N-1):
        x_i_next=(a*x_i + c)%m
        L.append(x_i_next)
        x_i=x_i_next
    return L
    

def Gauss_jordan(l,n):
    '''solves a linear equation in n variables using gauss-jordan elimination. l= augmented matrix.
    Returns the solution as a list.'''
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
    '''performs LU decomposition using Doolittle factorization. A= input matrix, n= dimension of square matrix. 
    Modifies the original matrix to contain the L_ij's and U_ij's, and returns the modified matrix.'''
    L=[]
    U=[]
    sum1=0
    sum2=0
    for i in range(n):
        L.append([])
        U.append([])
        for j in range(n): #creating a zero matrix of the same size as A
            L[i].append(0)
            U[i].append(0)
    for i in range(n):
        L[i][i]=1 # setting diagonal elements L_ii=1
    for i in range(n):
        for j in range(n):
            if i>j:
                for k in range(j):
                    sum2+=L[i][k]*U[k][j]
                L[i][j]=(A[i][j]-sum2)/U[j][j] #computing L_ij
                sum2=0
            elif i<=j:
                for k in range(i):
                    sum1+=L[i][k]*U[k][j]
                U[i][j]=A[i][j]-sum1 #computing U_ij
                sum1=0
    for i in range(n): #for there is no need to store L_ii's 
        L[i][i]=0
    for i in range(n):
        for j in range(n):
            A[i][j]=L[i][j]+U[i][j] #storing the modified matrix(LU) in place of A
    return A

def zero_matrix(m,n):
    '''creates a zero matrix of the size= m x n'''
    L=[]
    for i in range(m):
        L.append([])
        for j in range(n): 
            L[i].append(0)
    return L           
            

def solve_LU(A,B,n):
    '''solves a LU decomposed matrix A (of dimensions n x n) using forward and backward
    substitution. B is the column matrix containing the constants in the set of 
    linear equations.'''
    y=zero_matrix(len(B),1) #creating matrices with all values = 0
    x=zero_matrix(len(B),1)
    y[0][0]=B[0][0] #assigning initial value
    sum1=0
    sum2=0
    for i in range(1,n):
        for j in range(i):
            sum1+=A[i][j]*y[j][0]
        y[i][0]=B[i][0]-sum1 #forward substitution
        sum1=0
    x[n-1][0]=y[n-1][0]/A[n-1][n-1] #calculation of initial value(lower most variable in the variable column matrix)
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            sum2+=A[i][j]*x[j][0]
        x[i][0]=(y[i][0]-sum2)/A[i][i] #backward substitution
        sum2=0
    return x

def cholesky(A):
    '''performs cholesky decomposition of a given matrix A'''
    n = len(A)
    L = zero_matrix(n, n)

    for i in range(n):
        for j in range(i+1):
            if i == j:  # Diagonal elements calculation
                sum1 = sum(L[i][k] ** 2 for k in range(j))
                L[i][i] = np.sqrt(A[i][i] - sum1)
            else:   #Off-diagonal elements calculation
                sum2 = sum(L[i][k] * L[j][k] for k in range(j))
                L[i][j] = (A[i][j] - sum2) / L[j][j]
    for i in range(n):
        for j in range(n):
            A[i][j]=L[i][j] #storing the decomposed matrix in the same place as of A
    return A

def sq_mat_transpose(A):
    '''returns the transpose of the given square matrix A'''
    L=zero_matrix(len(A), len(A))
    for i in range(len(A)):
        for j in range(len(A)):
            L[i][j]=A[j][i] #L_ij=A_ji, L= transpose of A
    return L

def solve_chols(A,B):
    '''solves system of linear equations by forward-backward
    substitution and returns the solution as a list.
    A= Cholesky decomposed (lower) matrix of the coefficient matrix,
    B= matrix containing constants of linear equations.'''
    A_t=sq_mat_transpose(A) #taking transpose for creating the upper matrix
    n=len(A)
    y=zero_matrix(len(B),1) #creating matrices with all values = 0
    x=zero_matrix(len(B),1)
    y[0][0]=B[0][0]/A[0][0] #assigning initial value
    sum1=0
    sum2=0
    for i in range(1,n):
        for j in range(i):
            sum1+=A[i][j]*y[j][0]
        y[i][0]=(B[i][0]-sum1)/A[i][i] #forward substitution
        sum1=0
    x[n-1][0]=y[n-1][0]/A[n-1][n-1] #calculation of initial value(lower most variable in the variable column matrix)
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            sum2+=A_t[i][j]*x[j][0]
        x[i][0]=(y[i][0]-sum2)/A_t[i][i] #backward substitution
        sum2=0
    return x


def jacobi(A,B,i_guess,E=10**(-6),max_iter=50):
    '''solves linear equations using jacobi method. A= matrix containing coefficients, 
    B= matrix containing constants of the linear equations, i_guess= list containing 
    initial guesses for the variables. E= tolerance/precision, max_iter= max no. of iterations
    to be performed.'''
    n=len(A)
    sum1=0
    l=[]
    x=zero_matrix(n, 1) # making the variable matrices of the same dimensions as of B
    x_new=zero_matrix(n,1)
    for i in range(len(i_guess)):
        x[i][0]=i_guess[i] 
    for itr in range(max_iter):
        for i in range(n):
            for j in range(n):
                if i!=j:
                    sum1+=A[i][j]*x[j][0]
            x_new[i][0]=(B[i][0]-sum1)/A[i][i]   #calculation of new guess
            sum1=0
            for k in range(n):
                l.append(abs(x_new[k][0]-x[k][0])<E) #appending true or false
        if all(l):   #checking the achieved precision
            return x_new
            break
        l=[]
        x = [row[:] for row in x_new] #updating guess
        if itr==max_iter-1:
            print('"Jacobi method did not converge within max_iter"')
            











