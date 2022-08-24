import numpy as np
import matplotlib.pyplot as plt
pi_2=np.pi*2
tetha=np.linspace(0,pi_2,20000)
posicion=np.zeros((20000,2))
def ObtenerPosicion():
    posicion[:,0]=tetha*np.cos(tetha)
    posicion[:,1]=tetha*np.sin(tetha)
ObtenerPosicion()
plt.figure(figsize=(10,10))
plt.plot(posicion[:,0],posicion[:,1])
plt.show()

