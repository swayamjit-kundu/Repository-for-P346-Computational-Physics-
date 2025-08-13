def random_normal(c,N,seed=0.1):
    '''generates a list of random numbers using the formula x_i+1=c*x_i*(1-x_i)'''
    L=[]
    x_i=seed
    L.append(x_i)
    for i in range(N-1):
        x_i_next=c*x_i*(1-x_i)
        L.append(x_i_next)
        x_i=x_i_next
    return L


import matplotlib.pyplot as plt
'''a=[]
for i in range(3000,5000,5):
        plt.figure(i+1)
        plt.plot(random_normal(c=(i+1)*0.001,N=500),'ro')'''
        


#plotting the generated random numbers for five values of c 
plt.figure(1)
plt.plot(random_normal(c=3.81,N=1000)[:500],'ro')
R1=random_normal(c=3.81,N=1000)
plt.title('c=3.81,N=500')
plt.figure(2)
plt.plot(random_normal(c=3.68,N=1000)[:500],'ro')
R2=random_normal(c=3.68,N=1000)
plt.title('c=3.68,N=500')
plt.figure(3)
plt.plot(random_normal(c=3.876,N=1000)[:500],'ro')
R3=random_normal(c=3.876,N=1000)
plt.title('c=3.876,N=500')
plt.figure(4)
plt.plot(random_normal(c=3.826,N=1000)[:500],'ro')
R4=random_normal(c=3.826,N=1000)
plt.title('c=3.826,N=500')
plt.figure(5)
plt.plot(random_normal(c=3.996,N=1000)[:500],'ro')
R5=random_normal(c=3.996,N=1000)
plt.title('c=3.996,N=500')

#plotting the correlation plots
plt.figure(6)
plt.plot(R1[:500],R1[5:505],'bo')
plt.title('correlation plot for c=3.81,N=500,k=5')
plt.figure(7)
plt.plot(R1[:500],R1[10:510],'bo')
plt.title('correlation plot for c=3.81,N=500,k=10')
plt.figure(8)
plt.plot(R1[:500],R1[15:515],'bo')
plt.title('correlation plot for c=3.81,N=500,k=15')
plt.figure(9)
plt.plot(R2[:500],R2[5:505],'bo')
plt.title('correlation plot for c=3.68,N=500,k=5')
plt.figure(10)
plt.plot(R2[:500],R2[10:510],'bo')
plt.title('correlation plot for c=3.68,N=500,k=10')
plt.figure(11)
plt.plot(R2[:500],R2[15:515],'bo')
plt.title('correlation plot for c=3.68,N=500,k=15')
plt.figure(12)
plt.plot(R3[:500],R3[5:505],'bo')
plt.title('correlation plot for c=3.876,N=500,k=5')
plt.figure(13)
plt.plot(R3[:500],R3[10:510],'bo')
plt.title('correlation plot for c=3.876,N=500,k=10')
plt.figure(14)
plt.plot(R3[:500],R3[15:515],'bo')
plt.title('correlation plot for c=3.876,N=500,k=15')
plt.figure(15)
plt.plot(R4[:500],R4[5:505],'bo')
plt.title('correlation plot for c=3.826,N=500,k=5')
plt.figure(16)
plt.plot(R4[:500],R4[10:510],'bo')
plt.title('correlation plot for c=3.826,N=500,k=10')
plt.figure(17)
plt.plot(R4[:500],R4[15:515],'bo')
plt.title('correlation plot for c=3.826,N=500,k=15')
plt.figure(18)
plt.plot(R5[:500],R5[5:505],'bo')
plt.title('correlation plot for c=3.996,N=500,k=5')
plt.figure(19)
plt.plot(R5[:500],R5[10:510],'bo')
plt.title('correlation plot for c=3.996,N=500,k=10')
plt.figure(20)
plt.plot(R5[:500],R5[15:515],'bo')
plt.title('correlation plot for c=3.996,N=500,k=15')


		