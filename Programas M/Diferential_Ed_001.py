import numpy as np
import matplotlib.pyplot as plt

# Definimos la función que describe la ecuación diferencial
def f(x, y):
    return np.sin(x)

# Implementamos el método de Euler
def euler_approximation(f, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]
    for i in range(1, n+1):
        x = x_values[-1] + h
        y = y_values[-1] + h * f(x_values[-1], y_values[-1])
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values

# Parámetros iniciales
x0 = 0  # Valor inicial de x
y0 = 0  # Valor inicial de y

# Paso de muestreo intermedio
h_medium = 0.8  # Tamaño del paso intermedio
n_medium = int((10 - x0) / h_medium)  # Número de pasos para el paso intermedio

# Paso de muestreo pequeño
h_small = 0.3  # Tamaño del paso pequeño
n_small = int((10 - x0) / h_small)  # Número de pasos para el paso pequeño

# Paso de muestreo muy pequeño
h_very_small = 0.001  # Tamaño del paso muy pequeño
n_very_small = int((10 - x0) / h_very_small)  # Número de pasos para el paso muy pequeño

# Calculamos la aproximación de Euler para el paso intermedio
x_values_medium, y_values_medium = euler_approximation(f, x0, y0, h_medium, n_medium)

# Calculamos la aproximación de Euler para el paso pequeño
x_values_small, y_values_small = euler_approximation(f, x0, y0, h_small, n_small)

# Calculamos la aproximación de Euler para el paso muy pequeño
x_values_very_small, y_values_very_small = euler_approximation(f, x0, y0, h_very_small, n_very_small)

# Graficamos los resultados
plt.figure(figsize=(10, 12))

# Gráfico para el paso intermedio
plt.subplot(3, 1, 1)
plt.plot(x_values_medium, y_values_medium, label='Aproximación de Euler (dt = 0.8)', color='blue')
plt.scatter(x_values_medium, y_values_medium, color='blue', s=10)  # Agrega puntos
plt.plot(x_values_small, -np.cos(x_values_small) + 1, label='Solución exacta: -cos(x) + 1', linestyle='--', color='red', linewidth=3)
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.title('Aproximación de Euler (dt = 0.8) vs. Solución exacta')
plt.legend()
plt.grid(True)

# Gráfico para el paso pequeño
plt.subplot(3, 1, 2)
plt.plot(x_values_small, y_values_small, label='Aproximación de Euler (dt = 0.3)', color='blue')
plt.scatter(x_values_small, y_values_small, color='blue', s=10)  # Agrega puntos
plt.plot(x_values_small, -np.cos(x_values_small) + 1, label='Solución exacta: -cos(x) + 1', linestyle='--', color='red', linewidth=3)
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.title('Aproximación de Euler (dt = 0.3) vs. Solución exacta')
plt.legend()
plt.grid(True)

# Gráfico para el paso muy pequeño
plt.subplot(3, 1, 3)
plt.plot(x_values_very_small, y_values_very_small, label='Aproximación de Euler (dt = 0.001)', color='blue')
plt.scatter(x_values_very_small, y_values_very_small, color='blue', s=10)  # Agrega puntos
plt.plot(x_values_small, -np.cos(x_values_small) + 1, label='Solución exacta: -cos(x) + 1', linestyle='--', color='red', linewidth=3)
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.title('Aproximación de Euler (dt = 0.001) vs. Solución exacta')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

