import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#première simulation du système de Lotka-Volterra en me basant de ce que j'ai trouver sur https://fr.wikipedia.org/wiki/%C3%89quations_de_pr%C3%A9dation_de_Lotka-Volterra 

alpha=2 # taux de reproduction intrinsèque des proies
beta=0.2 # taux de mortalité des proies dû aux prédateurs rencontrés 
delta=0.15 # taux de reproduction des prédateurs en fonction des proies rencontrées et mangées
gama=20 # taux de mortalité intrinsèque des prédateurs

def lot_vol(t, state):
    x, y = state 
    dxdt = x * (alpha - beta * y)
    dydt = y * (delta * x - gama)
    return [dxdt, dydt]

# Conditions intials
t_span = (0, 30)
t_eval = np.linspace(*t_span, 10000)
initial_state = [100, 60]

solution = solve_ivp(lot_vol, t_span, initial_state, t_eval=t_eval)

plt.figure(figsize=(10, 6))
plt.plot(solution.y[0], solution.y[1], lw=0.8, label="Trajectoire (x(t), y(t))")
plt.title("Système de Lotka-Volterra")
plt.xlabel("x (proie)")
plt.ylabel("y (prédateur)")
plt.grid(True)
plt.legend()
plt.show()