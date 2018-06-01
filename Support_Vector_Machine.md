# Support Vector Machines (SVM) algorithm

### ¿En que consiste?

**SVM** es un alg. de clasificación.

Tenemos datos de diferentes clases, y queremos ver como separarlos por una linea. Entonces buscamos aquella linea que maximice la distancia a los puntos mas cercanos, esta distancia la llamaremos el **Margin** o margen.

![](margin.png)

**SVM** primero clasifica bien los valores, y una vez que ya tiene la clasificación, intenta maximizar el margin.

![](clasification.png)

Ventajas:
- Efectivo en espacios dimensionales altos
- Sigue siendo efectivo en casos donde el numero de dimensiones es mas grande que el numero de muestras.
- Usa un subconjunto de puntos de entrenamiento en la función de decision, llamados "support vectors", por lo tanto también es eficiente en memoria.

Desventajas:
- 





















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

### Scikit-learn

Es una libreria la cual puede:

- Create: `model = sklearn.whatever.ModelNameHere(parameters_if_any)`
- Train: `model.fit(X,y)`
- Predict: `model.predict(X_test)`

[Cheat sheet](http://scikit-learn.org/stable/_static/ml_map.png)
[Tutorials](http://scikit-learn.org/stable/tutorial/index.html)
[Examples](http://scikit-learn.org/stable/auto_examples/index.html)






