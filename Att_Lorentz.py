import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Paramètres du système de Lorenz
sigma = 10
rho = 28
beta = 8 / 3

# Définition du système d'équations
def lorenz(t, state):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Conditions initiales et temps d'intégration
t_span = (0, 40)
t_eval = np.linspace(*t_span, 10000)
initial_state = [1, 1, 1]

# Résolution du système
solution = solve_ivp(lorenz, t_span, initial_state, t_eval=t_eval)

# Tracé 3D de l'attracteur
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(solution.y[0], solution.y[1], solution.y[2], lw=0.5)
ax.set_title("Attracteur de Lorenz")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
