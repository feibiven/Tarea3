#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Se extraen los datos de los archivos provistos por el profesor del curso.
# Notar que existe un archivo llamado "xymod", este se modifico para simplificar la extraccion de los datos.
# En el archivo "xymod" se elminaron la columna con los vectores "x" y la fila con los vectores "y".
# Estos vectores se volveran a agregar con linspace mas adelante.
# El profesor dio permiso y recomendo hacer esta modificacion.

import matplotlib.pyplot as plt
import pandas as pd
datosxyp = pd.read_csv('C:\\Users\\fabir\\Desktop\\Modelos\\xyp.csv')
print('Cantidad de filas en xyp.csv',len(datosxyp))
datosxymod = pd.read_csv('C:\\Users\\fabir\\Desktop\\Modelos\\xymod.csv')
print('Cantidad de filas en xy.csv',len(datosxymod))
print('Cantidad de columnas en xyp', len(datosxyp.columns))
print('Cantidad de columnas en xy', len(datosxymod.columns))


# In[2]:


import numpy as np

# Problema 1 - Calculo de funciones de densidad marginal para X y Y.
# Para extraer las funciones 

fmx = np.sum(datosxymod, axis=1)
print('El vector con la funcion marginal de X es:',fmx)

fmy = np.sum(datosxymod, axis=0)
print('El vector con la funcion marginal de Y es:',fmy)


# In[3]:


# Para encontrar la funcion marginal de X, se suman todas las filas xn y se obtiene un vector de 11 espacios - (Problema 1)
# Luego se crea un vector de 11 espacios del 5 al 15 para graficar la funcion marginal de X en 2D- (Problema 4)

plt.title('Curva para funcion marginal de X')
plt.ylabel('Valores')
x = np.linspace(5, 15, 11)
figfmx = plt.plot(x, fmx)


# In[4]:


# Para encontrar la funcion marginal de Y, se suman todas las filas xn y se obtiene un vector de 21 espacios (Problema 1)
# Luego se crea un vector de 11 espacios del 5 al 25 para graficar la funcion marginal de Y en 2D - (Problema 4)

plt.title('Curva para funcion marginal de Y')
plt.ylabel('Valores')
y = np.linspace(5, 25, 22)
figfmy = plt.plot(y, fmy)


# In[17]:


# De la Figura 1 se observa que la curva de mejor ajuste es de tipo Gaussiana.
# Se procede a calcular los parametros "mux" y "sigmax" a partir de la curva de mejor ajuste. - (Problema 1)

from scipy.optimize import curve_fit

xs = np.linspace(5, 15, 11)

def gaussiana (x, mu, sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp (-(x - mu)**2 /(2*sigma**2))

param, _ = curve_fit(gaussiana, xs, fmx)

print(param)


# In[6]:


# De la Figura 2 se observa que la curva de mejor ajuste es de tipo Gaussiana.
# Se procede a calcular los parametros "muy" y "sigmay" a partir de la curva de mejor ajuste. - (Problema 1)

from scipy.optimize import curve_fit

ys = np.linspace(5, 25, 22)

def gaussiana (x, mu, sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp (-(x - mu)**2 /(2*sigma**2))

param, _ = curve_fit(gaussiana, ys, fmy)

print(param)


# In[7]:


# Problema 2

# Analiticamente, y asumiendo independencia de X y Y, la funcion de densidad conjunta corresponde a la multiplicacion 
# de las funciones de densidad marginales para X y Y.


# In[8]:


# Problema 3 - Correlacion

df = pd.DataFrame(datosxyp)
correlacion = 0

for i in range (0, len(datosxyp)):
    correlacion = correlacion + (df.loc[i, 'x']*df.loc[i, 'y']*df.loc[i, 'p'])
print(correlacion)
# Como la correlacion es positiva, ambos vectores son colineales (paralelos).


# In[9]:


# Problema 3 - Covarianza

covarianza  = 0
mux = 9.90484381
muy = 15.64290662
for i in range (0, len(datosxyp)):
    covarianza = covarianza + ((df.loc[i, 'x']) - mux)*((df.loc[i, 'y']) - muy)*(df.loc[i, 'p'])
print(covarianza)
# Como la covarianza es positiva, hay dependencia directa (positiva), es decir, a grandes valores de x corresponden 
# grandes valores de y.


# In[10]:


#Problema 3 - Coeficiente de correlacion

sigmax = 3.29944287
sigmay = 5.92157896 
coefcorr = (covarianza)/(sigmax*sigmay)
print(coefcorr)
# Como el coeficiente de correlacion se encuentra en el ambito, 0 < p < 1, existe una correlacion positiva.

