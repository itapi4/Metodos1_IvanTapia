import numpy as np
import matplotlib.pyplot as plt
def es_primo(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return(False)
    return(True)

inicial=2
cont_primos=0
primos=[]

while cont_primos<1000:
    verificador=es_primo(inicial)
    if verificador:
        cont_primos+=1
        primos.append(inicial)
    inicial+=1
print(primos[:10])
x=np.arange(1,1001)
plt.figure(figsize=(10,10))
plt.plot(x,primos)
plt.show()



