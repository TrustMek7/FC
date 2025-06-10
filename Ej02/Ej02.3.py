# Importar las bibliotecas necesarias
import matplotlib.pyplot as plt
import numpy as np

# Parámetros iniciales
h = 0.00001    # Paso de tiempo
tfin = 10   # Tiempo final
x, y = 0, 0 # Posiciones iniciales
v = 5    # Velocidad inicial
theta = 60 # Ángulo de lanzamiento en grados
ay = -10  # Aceleracion constante (gravedad)

vx = v * np.cos(np.radians(theta))  # Componente horizontal de la velocidad
vy = v * np.sin(np.radians(theta))  # Componente vertical de la velocidad

# Listas para almacenar resultados
px = [x]
py = [y]

for t in np.arange(0, tfin, h):
    # Actualizar velocidad
    vy += ay * h

    # Actualizar posicion
    x += vx * h
    y += vy * h

    px.append(x)
    py.append(y)

# Graficar en 2D
plt.figure(figsize=(12, 8))
plt.plot(px, py, color='brown', label='Trayectoria')  # Trazo del movimiento
plt.xlabel('x (m)')
plt.ylabel('y (m) - Altura')
plt.title('Movimiento parabólico en 2D')
plt.grid(True)
plt.axhline(0, color='black', lw=1, label='Eje X', linestyle='--')
plt.axvline(0, color='black', lw=1, label='Eje Y', linestyle='--')
plt.legend()
plt.show()
