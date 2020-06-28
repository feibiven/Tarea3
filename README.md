# Tarea3
Solucion a la Tarea 3 del curso Modelos Probabilisticos de Senales y Sistemas

Nota:
Se extraen los datos de los archivos provistos por el profesor del curso.
Notar que existe un archivo llamado "xymod", este se modifico para simplificar la extraccion de los datos.
En el archivo "xymod" se elminaron la columna con los vectores "x" y la fila con los vectores "y".
Estos vectores se volveran a agregar con linspace mas adelante.
El profesor dio permiso y recomendo hacer esta modificacion.

Problema 1:
Una vez que se subieron los archivos "xymod" y "xyp", desde el archivo "xymod" se extraen las funciones de densidad marginales
"fmx" y "fmy" con el comando "np.sum", en el que fmx y fmy corresponden a 2 vectores de 11 y 21 espacios respectivamente, con 
la suma por fila y columna.

Una vez obtenidos estos vectores que contienen las funciones de densidad marginales, se procede a crear dos vectores con el comando 
"linspace" de 5 a 15 y de 5 a 25 para graficar. Una vez que se grafican las funciones de densidad marginales se determina que
estas tienen forma de distribucion normal o Gaussiana. Luego, con el comando "curve_fit" se proceden a calcular los parametros "mu"
y "sigma" para cada funcion de densidad marginal.

Problema 2:

Analiticamente, y asumiendo independencia de X y Y, la funcion de densidad conjunta corresponde a la multiplicacion  de las funciones
de densidad marginales para X y Y.

Problema 3:

Para el calculo de la correlacion se crea un ciclo For que recorre todas las filas multiplicando los valores asociados para X, Y y su 
respectiva probabilidad y sumando los resultados. Se obtiene una covarianza de alrededor de 149. Como la correlacion es positiva, se 
concluye que ambos vectores son colineales (paralelos).

Para el calculo de la covarianza se crea un ciclo For que recorre todas las filas multiplicando los valores asociados para X y Y, pero
en este caso a diferencia del anterior se resta su valor medio "mu" respectivo y luego se multiplica este resultado por su respectiva
probabilidad y se suman los resultados. Se obtiene una covarianza de 0.05 aproximadamente, por lo tanto como la covarianza es positiva, 
hay dependencia directa (positiva), es decir, a grandes valores de X corresponden grandes valores de Y.

Ya con los parametros "sigmax" y "sigmay" de cada funcion de densidad, se procede a calcular el coeficiente de correlacion dividiendo la
covarianza obtenida en el calculo anterior por la multiplicacion de los dos parametros sigma. Se obtiene un coeficiente de correlacion de
0.0025, por lo tanto se concluye que como el coeficiente de correlacion se encuentra en el ambito, 0 < p < 1, existe una correlacion positiva.

Problema 4:
Las graficas de las funciones de densdiad marginales en 2D para X y Y se muestran en el repositorio de este archivo README.md.
