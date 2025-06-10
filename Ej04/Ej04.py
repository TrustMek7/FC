import numpy as np
import matplotlib.pyplot as plt

def aceleracion(x1, y1, x2, y2, suave=0.001):
    dx = x1 - x2
    dy = y1 - y2
    r = np.sqrt(dx**2 + dy**2)
    if r == 0:
        return 0, 0
    factor = -1 / (r**3 + suave)
    return dx * factor, dy * factor


def main():
    # constantes
    cuerpos = [
        (2,3),
        (-1,-1),
        (3,-0.5)
    ]

    r = 1
    limit = 8

    # Graficar circunferencia 1
    theta = np.linspace(0, 2 * np.pi, 100)

    for i, (x, y) in enumerate(cuerpos):
        x1 = x + r * np.cos(theta)
        y1 = y + r * np.sin(theta)

        # Graficar circunferencia
        plt.plot(x1, y1, label=f'Cuerpo {i+1}')

    # Párametros para la simulación
    h = 0.01
    tfin = 100
    
    for vy0 in np.arange(0.9, 1.5, 0.05):
        vy = vy0
        vx = -0.45
        y = 1
        x = 0

        px = [x]
        py = [y]

        graficar = True

        for _ in np.arange(0, tfin, h):
            x = x + vx * h
            y = y + vy * h

            ax_total, ay_total = 0, 0

            for x1, y1 in cuerpos:
                # Calcular aceleración
                ax, ay = aceleracion(x, y, x1, y1)
                ax_total += ax
                ay_total += ay
            
            vx = vx + ax_total * h
            vy = vy + ay_total * h

            # Verificar límites
            if x > limit or x < -limit or y > limit or y < -limit:
                graficar = False
                break

            # Verificar colisión con los círculos
            stop = False
            for x1, y1 in cuerpos:
                if ((x - x1)**2 + (y - y1)**2) <= r**2:
                    stop = True

            if stop:
                break

            px.append(x)
            py.append(y)


        if graficar:
            plt.plot(px, py, label=f'Trajectoria (vy={vy0:.2f})')

    # Configuracion del gráfico
    plt.axis('equal')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-limit, limit)
    plt.ylim(-limit, limit)
    plt.axhline(0, color='black', lw=1, label='Eje X', linestyle='--')
    plt.axvline(0, color='black', lw=1, label='Eje Y', linestyle='--')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Trayectorias de partículas')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

