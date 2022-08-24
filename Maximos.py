import numpy as np
data=np.loadtxt('datosmaximos.txt')
axis_x=data[:,0]
axis_y=data[:,1]
maximos=[]
for i in range(1,len(axis_y)-1):
    if axis_y[i]>=axis_y[i-1] and axis_y[i]>=axis_y[i+1]:
        maximos.append(axis_x[i])
print('Los maximos locales son: ')
print(maximos)