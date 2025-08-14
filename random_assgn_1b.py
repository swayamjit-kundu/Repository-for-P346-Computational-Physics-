#Swayamjit Kundu, 2311196, Assignment 1(Random numbers)


from mylib import *
import numpy as np
import matplotlib.pyplot as plt
m=32768
R=random_gen_LCG()
print(R)

#plotting the generated random numbers(Question no. 2)
plt.plot(R,'ro')
plt.xlabel('no. of iterations')
plt.ylabel('generated random number')

#plotting the correlation plot(Question 2)
plt.figure(2)
plt.plot(R[:500],R[5:505],'ro')
plt.xlabel(r'$x_i$')
plt.ylabel(r'$x_{i+5}$')
plt.title('correlation plot for LCG random numbers for 500 iterations')
plt.savefig('fig6.png')



#estimating value of pi
pie_list=[]
throw=[]
for p in range(20,10000,40):
    x=np.array(random_gen_LCG(N=p))/m
    y=np.array(random_gen_LCG(N=p))/m
    a=x**2+y**2
    L=[]
    L1=[]
    for i in a:
        if i<=1:  #inside the unit circle
            L.append(i)
        elif i>1 and i<1.414:  #outside the unit circle
            L1.append(i)
            pie=4*(len(L)/len(L1+L))
    pie_list.append(pie)
    throw.append(p)

#plotting the results obtained for pi
plt.plot(throw,pie_list)   
plt.grid()
plt.xlabel('no. of throws')
plt.ylabel(r'value of $\pi$')
plt.title(r'estimation of $\pi$ (by throwing method)')


print('average value of pi=',sum(pie_list[len(pie_list)-50:len(pie_list)])/50)


#generating pRN following an exponential pdf
x=np.array(random_gen_LCG(N=5000))/m
y=-np.log(x)  
 
#plotting a basic histogram
plt.hist(y, bins=40, color='skyblue', edgecolor='black')
plt.title('Histogram showing exponential pdf')
plt.ylabel('number of random numbers')
    
    
    
    
    
    
    
    

        