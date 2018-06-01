## Librerias para ML y RL

### Pandas

Entre las librerias que usaremos tenemos:

* **Pandas** que sirve para cargar data, por ejemplo leer archivos **.csv**. Pero tambien tiene algunas herramientas de análisis, utilizando el método `.describe()` podemos obtener cuantos elementos hay, la media, desviación estandard, etc.

Mas sobre Pandas:

- [10 minutes to Pandas](https://pandas.pydata.org/pandas-docs/stable/10min.html#min)
- [Pandas tutorials](https://pandas.pydata.org/pandas-docs/stable/tutorials.html)
- [Cheat sheet Pandas](https://pbs.twimg.com/media/C65MaMpVwAA3v0A.jpg)

Iniciamos importando Pandas.

``` Python
import pandas as pd
data = pd.read_csv("train.csv", index_col='PassengerId') # this yields 
a pandas.DataFrame #<--- es una tabla 2d 
```

Hay operaciones basicas como seleccionar **10** filas:

``` Python
# Selecting rows
head = data[:10]
```

Y solo la fila **4**:

``` Python
# select a single row
print(data.loc[4])
```

Seleccionar la columna `Age`:

``` Python
ages = data["Age"]
```

Seleccionar múltiples columnas, del elemento 5 al 10, columnas *Fare* y *Pclass*:

``` Python
data.loc[5:10, ("Fare", "Pclass")]    
# alternatively: 
data[["Fare","Pclass"]].loc[5:10]
```

Tambien podemos obtener las dimesiones de la tabla:

``` Python
data.shape
```

### Numpy 

Permite hacer calculos con vectores, matrices y otras cosas relacionadas.
Numpy comparado con Python es mucho mas rápido.

> Un array de 1M de elementos python tardaria en procesarlos 2.14s vs 108ms de Numpy.

[NumPy Cheat sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)

``` Python
import numpy as np

a = np.array([1,2,3,4,5]) #Declaramos un Array
b = np.array([5,4,3,2,1])
print("a = ",a)			   #Mostramos sus elementos
print("b = ",b)

# math and boolean operations can applied to each element of an array
print("a + 1 =", a + 1)
print("a * 2 =", a * 2)
print("a == 2", a == 2)
# ... or corresponding elements of two (or more) arrays
print("a + b =",a + b)
print("a * b =",a * b)
```

Output:

```
a =  [1 2 3 4 5]
b =  [5 4 3 2 1]
a + 1 = [2 3 4 5 6]
a * 2 = [ 2  4  6  8 10]
a == 2 [False  True False False False]
a + b = [6 6 6 6 6]
a * b = [5 8 9 8 5]
```

### Matplotlib

Usamos esta libreria para visualizar los datos, graficarlos. 
Para [instalarla](https://matplotlib.org/2.0.2/faq/installing_faq.html#install-osx-binaries), ingresamos en la terminal:

> pip install matplotlib

[Tutoriales](https://matplotlib.org/2.0.2/users/pyplot_tutorial.html)

[Cheat sheet](https://api.ning.com/files/ix5EiwUaTp0E5*jp7eiswyccuIvY2ZsTZtw4N00CRgaI9Y5fMQEYTahMiecJ8nwooZZHezoGsTkJ-duNPnb39c9Qmgg9hX4L/dc1.png)

``` Python
import matplotlib.pyplot as plt
%matplotlib inline  
# ^-- this "magic" tells all future matplotlib plots to be drawn inside notebook and not in a separate window.

# line plot
plt.plot([0,1,2,3,4,5],[0,1,4,9,16,25])
```

### Scikit-learn

Es una libreria la cual puede:

- Create: `model = sklearn.whatever.ModelNameHere(parameters_if_any)`
- Train: `model.fit(X,y)`
- Predict: `model.predict(X_test)`

[Cheat sheet](http://scikit-learn.org/stable/_static/ml_map.png)
[Tutorials](http://scikit-learn.org/stable/tutorial/index.html)
[Examples](http://scikit-learn.org/stable/auto_examples/index.html)






