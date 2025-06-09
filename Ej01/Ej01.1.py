# Importar las bibliotecas necesarias
import matplotlib.pyplot as plt
import numpy as np

# Parámetros iniciales
h = 0.01    # Paso de tiempo
tfin = 10   # Tiempo final
x = -2  # Posicion inicial
vx = 0.5    # Velocidad inicial
ax = 2  # Aceleracion constante

# Listas para almacenar resultados
px = [x]
pv = [vx]
pt = [0]
pa = [ax]

for t in np.arange(0, tfin, h):
    # Actualizar velocidad
    vx += ax * h

    # Actualizar posicion
    x += vx * h

    px.append(x)
    pv.append(vx)
    pa.append(ax)
    pt.append(t)

# Graficar en 2D
plt.figure(figsize=(12, 8))

# Aceleración vs Tiempo
plt.subplot(2, 2, 1)
plt.plot(pt, pa, color='brown')
plt.grid(True)
plt.axhline(0, color='black', lw=1, label='Eje X', linestyle='--')
plt.axvline(0, color='black', lw=1, label='Eje Y', linestyle='--')
plt.xlabel('Tiempo (s)')
plt.ylabel('Aceleración (m/s²)')
plt.title('Aceleración vs Tiempo')

# Velocidad vs Tiempo
plt.subplot(2, 2, 2)
plt.plot(pt, pv, color='orange')
plt.grid(True)
plt.axhline(0, color='black', lw=1, label='Eje X', linestyle='--')
plt.axvline(0, color='black', lw=1, label='Eje Y', linestyle='--')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.title('Velocidad vs Tiempo')

# Posición vs Tiempo
plt.subplot(2, 2, 3)
plt.plot(pt, px, color='green')
plt.grid(True)
plt.axhline(0, color='black', lw=1, label='Eje X', linestyle='--')
plt.axvline(0, color='black', lw=1, label='Eje Y', linestyle='--')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.title('Posición vs Tiempo')

# Velocidad vs Posición
plt.subplot(2, 2, 4)
plt.plot(px, pv, color='blue')
plt.grid(True)
plt.axhline(0, color='black', lw=1, label='Eje X', linestyle='--')
plt.axvline(0, color='black', lw=1, label='Eje Y', linestyle='--')
plt.xlabel('Posición (m)')
plt.ylabel('Velocidad (m/s)')
plt.title('Velocidad vs Posición')

plt.suptitle(f"Movimiento con Velocidad Constante (a = {ax})", fontsize=16)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.show()
