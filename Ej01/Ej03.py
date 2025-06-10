import numpy as np
import matplotlib.pyplot as plt

# Constantes físicas
G = 6.67430e-11          # Constante de gravitación universal (m^3 kg^-1 s^-2)
M = 5.972e24             # Masa de la Tierra (kg)
R_tierra = 6.371e6       # Radio de la Tierra (m)

def aceX(x, y):
    r = np.sqrt(x**2 + y**2)
    return -G * M * x / r**3

def aceY(x, y):
    r = np.sqrt(x**2 + y**2)
    return -G * M * y / r**3



def main():
    h = 1                 # Paso de tiempo (s)
    tfin = 2000000         # Tiempo total de simulación (s)

    # Condiciones iniciales
    x = 0
    y = R_tierra          # Partimos desde la superficie terrestre (eje Y)
    vx = 10000
    vy = 100

    px = [x]
    py = [y]

    for _ in np.arange(0, tfin, h):
        x += vx * h
        y += vy * h

        if np.sqrt(x**2 + y**2) < R_tierra:
            print("La nave ha colisionado con la Tierra.")
            break

        ax = aceX(x, y)
        ay = aceY(x, y)

        vx += ax * h
        vy += ay * h

        px.append(x)
        py.append(y)

    # Dibujar la Tierra
    theta = np.linspace(0, 2 * np.pi, 300)
    tierra_x = R_tierra * np.cos(theta)
    tierra_y = R_tierra * np.sin(theta)

    plt.figure(figsize=(8, 8))
    plt.plot(tierra_x, tierra_y, 'b', label='Tierra')
    plt.plot(px, py, 'r', label='Trayectoria de la nave')
    plt.axis('equal')
    plt.grid(True)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Simulación de trayecto de nave desde la Tierra')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()


