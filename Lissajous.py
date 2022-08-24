import numpy as np
import matplotlib.pyplot as plt
def ObtenerPosicion(x,y):
    posicion[:,0]=np.sin(x*tetha)
    posicion[:,1]=np.sin(y*tetha)
pi_2=np.pi*2
tetha=np.linspace(0,pi_2,20000)
k=1
for x in range(0,5):
    for y in range(x,5):
        posicion=np.zeros((20000,2))
        ObtenerPosicion(x,y)
        plt.subplot(5, 5, k)
        plt.plot(posicion[:,0],posicion[:,1])
        k+=1
plt.show()