import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Définition du système d'équations
def aizawa(t,Y):
    x,y,z=Y
    a=0.95
    b=0.7
    c=0.6
    d=3.5
    e=0.25
    f=0.1
    dx=(z-b)*x-d*y
    dy=d*x+(z-b)*y
    dz=c+a*z-z**3/3-x**2+f*z*x**3
    return [dx,dy,dz]

# Conditions initiales et temps d'intégration
Y0 = [0.1, 0.0, 0.0]
t_span = (0, 5000)                     # intégration totale
t_eval = np.linspace(0, 5000, 500000)   # pas ~0.01
t_transient = 100.0                   # on éliminera t < 100

# Résolution du système
sol = solve_ivp(
    fun=  aizawa,
    t_span=t_span,
    y0=Y0,
    t_eval=t_eval,
   method='RK45',
    rtol=1e-8,
    atol=1e-10
)

mask = sol.t >= t_transient
t = sol.t[mask]
x = sol.y[0, mask]
y = sol.y[1, mask]
z = sol.y[2, mask]

# Tracé 3D de l'attracteur
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(sol.y[0], sol.y[1], sol.y[2], color='purple', lw=0.5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Attracteur d'Aizawa")

fig, axs = plt.subplots(3, 1, figsize=(10, 6), sharex=True)

axs[0].plot(t, x, 'b')
axs[0].set_ylabel('x(t)')
axs[0].set_title('Évolution temporelle des composantes')

axs[1].plot(t, y, 'g')
axs[1].set_ylabel('y(t)')

axs[2].plot(t, z, 'r')
axs[2].set_ylabel('z(t)')
axs[2].set_xlabel('Temps')

for ax in axs:
    ax.grid()

plt.tight_layout()
plt.show()

