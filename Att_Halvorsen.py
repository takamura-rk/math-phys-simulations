import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def halvorsen(t,Y):
    x,y,z=Y
    a=1.4
    dx=-a*x-4*y-4*z-y*y
    dy=-a*y-4*z-4*x-z*z
    dz=-a*z-4*x-4*y-x*x
    return [dx,dy,dz]

Y0=[0.1,0,0]
t_span=(0,300)
t_eval=np.linspace(0,300,10000)


sol = solve_ivp(
    fun=  halvorsen,
    t_span=t_span,
    y0=Y0,
    t_eval=t_eval,
   method='RK45')

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(sol.y[0], sol.y[1], sol.y[2], color='red', lw=0.5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Attracteur d'Halvorsen")

fig, axs = plt.subplots(3, 1, figsize=(10, 6), sharex=True)

axs[0].plot(sol.t, sol.y[0], 'b')
axs[0].set_ylabel('x(t)')
axs[0].set_title('Évolution temporelle des composantes')

axs[1].plot(sol.t, sol.y[1], 'g')
axs[1].set_ylabel('y(t)')

axs[2].plot(sol.t, sol.y[2], 'r')
axs[2].set_ylabel('z(t)')
axs[2].set_xlabel('Temps')

for ax in axs:
    ax.grid()

plt.tight_layout()
plt.show()
