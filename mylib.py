import numpy as np

class MyComplex():
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