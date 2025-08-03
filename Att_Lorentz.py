import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Num_Analysis.Methodesd_Euler import euler_exp_sys


# Définition du système d'équations
def lorenz(Y, t):
    x, y, z = Y
    sigma = 10
    rho = 28
    beta = 8/3
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return np.array([dx, dy, dz])

# Conditions initiales et temps d'intégration
Y0 = np.array([1.0, 1.0, 1.0])
t0 = 0.0
tf = 40.0
h = 0.01

# Résolution du système
t, Y = euler_exp_sys(lorenz, Y0, t0, tf, h)

# Tracé 3D de l'attracteur
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(Y[:,0], Y[:,1], Y[:,2], color='purple')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Attracteur de Lorenz (Euler explicite)")


# Courbes x(t), y(t), z(t)
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, Y[:,0], label='x(t)', color='blue')
plt.ylabel("x(t)")
plt.grid()
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, Y[:,1], label='y(t)', color='green')
plt.ylabel("y(t)")
plt.grid()
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, Y[:,2], label='z(t)', color='red')
plt.xlabel("Temps t")
plt.ylabel("z(t)")
plt.grid()
plt.legend()

plt.suptitle("Évolution temporelle de x(t), y(t), z(t) – Système de Lorenz")
plt.tight_layout()
plt.show()

