# Linear Regresion 

Linear Regresion es utilizada para predecir un valor.
Basicamente tenemos muchos datos y los graficamos en un plano XY, a estos datos le creamos una linea que se ajuste mejor. La mejor línea es la que este menos alejada de los datos reales, para encontrarla utilizaremos la famosa **Cost Function**.

<img src="http://adit.io/imgs/regression/predicted_vs_actual_good_line.png" title=""/>


### Cost Function
Esta función nos dice que tan buena es nuestra linea.
Necesitamos dos numeros para hacer que la linea se ajuste a los datos, los llamaremos `theta_0` y `theta_1`, ambos pueden valer **cero**.

Estos valores crearán la ecuación de la recta de la forma:

<img src="https://latex.codecogs.com/gif.latex?y&space;=&space;0x&space;&plus;&space;x" title=""/>

Ahora calcularemos que tan alejados estamos (en promedio) de los datos actuales.Esto es llamado **cost function**.

A esta función le pasaremos los valores de `theta_0` y `theta_1` y te dirá que tan alejados estamos (el costo de utilizar esa linea).

En código sería algo como esto:

``` Octave 

% x is a list of square feet: [1000,2000,4000]
% y is the corresponding prices for the homes: [200000, 25000, 300000]

function distance = cost(theta_0, theta_1, x, y)
	distance = 0
	for i = 1:length(x)
		square_feet = x(i) %valor de x en la pos i
		predicted_value = theta_0 + theta_1 * square_feet
		actual_value = y(i) %valor de y en la pos i
		
		%que tan lejos estamos del 'predicted value'
		%(obtenemos el valor absoluto)
		
		distance = distance + abs(actual_value - predicted_value)
	end
	
	%vemos que tan lejos estamos en promedio
	distance = distance/length(x)
		
end
```

<img src="http://adit.io/imgs/regression/cost_function_math_formula.png" title=""/>

Basicamente este algoritmo obedece a la siguiente formula, donde `h(x)` es el `predicted value`.

`h(x) = theta_0 + theta_1*x`

Es la formula de la línea, si probamos con un valor especifico para `x`, obtendremos uno para `y`. Por lo tanto, `h(x) - y` nos da la diferencia entre el `predicted_value` y el `actual_value`. 

Para un valor dado de `theta_0` y `theta_1`, el `cost function` nos dirá que tan buenos son esos valores (que tan alejadas estan nuestras predicciones de nuestros datos reales). Pero entonces como encontramos los valores de `theta_0` y `theta_1` que dibujen mejor la linea?, para ello utilizamos **Gradient Descent** (gradiente descendente).


### Gradient Descent
Gradient Descent nos sirve para encontrar la mejor linea. 
Sabemos que tenemos los valores de `theta_0` y `theta_1`, probemos haciendo `theta_0 = 0` y variemos el valor de `theta_1`. Al final obtendremos una gráfica así:

<img src="http://adit.io/imgs/regression/cost_for_theta_1_callouts.png" title=""/>

Vemos que *Low Cost* es en realidad el costo mas bajo, este valor nos dará el valor mas bajo de `theta_1`.
Gradient Descent nos ayuda a encontrar el punto mas bajo en esta gráfica, lo hace iterando sobre el valor de `theta_1`, actualizandolo hasta llegar al mejor valor. Podemos iniciar con `theta_1 = 0`.

Iremos iterando en cada paso, recuerda que nuestra meta es llegar al fondo.

<img src="http://adit.io/imgs/regression/arrows_to_bottom.png" title=""/>

Pero como sabemos que ya estamos en el fondo?, bueno pues podemos derivar en ese punto, entonces podriamos derivar muchas veces.

Pero bueno, ahora, debemos encontrar los valores optimos para `theta_0` y `theta_1`. Por lo que la gráfica se vería algo así:

<img src="http://adit.io/imgs/regression/3d_plot_thetas.png" title=""/>

Aunque este en 3D la gráfica, seguimos haciendo lo mismo, ir paso a paso hasta llegar al fondo. Encontraremos los mejores valores de `theta_0` y `theta_1` que nos den el mejor ajuste de la linea iniciando con valores sugeridos e incrementarlos ahsta tener el menor costo.

Utilizaremos la formula de **Gradient Descent**:

<img src="http://adit.io/imgs/regression/gradient_descent_math_formula.png" title=""/>


*¿Pero que es esto tio?, posh nadaaa, que son derivadas parciales* usadas para actualizar  `theta_0` y otra para `theta_1`. Ambas son casi lo mismo, excepto que la derivada para `theta_1` tiene un `x` adicional al final.


## References
[Linear Regression In Pictures](http://adit.io/posts/2016-02-20-Linear-Regression-in-Pictures.html#what-is-linear-regression?)

[Eligiendo el Estimador correcto Scikit](http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html)
