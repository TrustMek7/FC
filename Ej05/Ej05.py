import numpy as np
import matplotlib.pyplot as plt

# Parámetros
l = 2
n = 3
o = 6

k1, m1 = l**2, 1
k2, m2 = n**2, 1
k3, m3 = o**2, 1

# Condiciones iniciales
x, vx = 1, 2.36
y, vy = 1, 2.36
z, vz = 1, 2.36

# Tiempo de simulación
h = 0.01
tfin = 50
t = np.arange(0, tfin + h, h)

# Inicialización
px = np.zeros_like(t)
py = np.zeros_like(t)
pz = np.zeros_like(t)
px[0], py[0], pz[0] = x, y, z

# Simulación con método de Euler
for i in range(len(t)):
    ax = -k1/m1 * x
    ay = -k2/m2 * y
    az = -k3/m3 * z

    vx += h * ax
    vy += h * ay
    vz += h * az

    x += h * vx
    y += h * vy
    z += h * vz

    px[i] = x
    py[i] = y
    pz[i] = z

# Gráficos
fig = plt.figure(figsize=(12, 10))

# Subplot 3D
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax1.plot(px, py, pz, color='brown')
ax1.set_title(f'Lissajous 3D: l={l}, n={n}, z={o}')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

# Subplot XY
ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(px, py, color='red')
ax2.set_title(f'Plano XY (l={l}, n={n})')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.axis('equal')
ax2.grid(True)

# Subplot XZ
ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(px, pz, color='green')
ax3.set_title(f'Plano XZ (l={l}, o={o})')
ax3.set_xlabel('x')
ax3.set_ylabel('z')
ax3.axis('equal')
ax3.grid(True)

# Subplot YZ
ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(py, pz, color='blue')
ax4.set_title(f'Plano YZ (n={n}, o={o})')
ax4.set_xlabel('y')
ax4.set_ylabel('z')
ax4.axis('equal')
ax4.grid(True)

plt.tight_layout()
plt.show()
