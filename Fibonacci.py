from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
def fibonacci(n:int)->int:
    anterior=1
    presente=1
    listafibo=[0]
    for a in range(1,n):
        anterior,presente=presente,anterior+presente
        listafibo.append(anterior)
    return listafibo

listafibo_20=fibonacci(20)
print(listafibo_20)
plt.figure(figsize=(10,10))
plt.plot(listafibo_20)
plt.show()
numeroaureo=listafibo_20[-1]/listafibo_20[-2]
print('El numero aureo calculado para una secuencia de 20 numeros es: '+str(numeroaureo))
aureoreal=(1+sqrt(5))/2
print('El numero aureo real es: '+str(aureoreal))
porcentaje_error=(abs(numeroaureo-aureoreal))/aureoreal
print('El porcentaje de error fue de: '+str(porcentaje_error)+' por tanto con solo 20 datos ya se aproxima mucho')