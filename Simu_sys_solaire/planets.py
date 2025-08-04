import numpy as np 
import matplotlib.pyplot as plt 
import constantes


class Planet:
    def __init__(self,name,weigth,position):
        self.name=name
        self.weigth=weigth
        self.position=position

    def rprime(r,M,a):
        return np.sqrt(constantes.G*M*(2/r-1/a))
        

    def calc_F_grav(self,other):
    
        dx = other.x - self.x
        dy = other.y - self.y
        distance = np.sqrt(dx**2 + dy**2)
        if distance == 0:
            return (0, 0)  

        force = constantes.G * self.weigth* other.weigth / (distance**2)
    # Vecteur unitaire dans la direction de 'other'
        fx = force * dx / distance
        fy = force * dy / distance

        return fx, fy

    def rrprime(self, other_planets):
 
    
        total_fx = 0
        total_fy = 0

        for other in other_planets:
            if other is self:
                continue  # On ignore soi-même

        fx, fy = self.calc_F_grav(other)
        total_fx += fx
        total_fy += fy

    # Accélération = force / masse
        ax = total_fx / self.mass
        ay = total_fy / self.mass

        return ax, ay

    

Mercure  = Planet("Mercure", 3.3011e23)
Venus    = Planet("Vénus",   4.8675e24)
Terre    = Planet("Terre",   5.9724e24)
Mars     = Planet("Mars",    6.4171e23)
Jupiter  = Planet("Jupiter", 1.8982e27)
Saturne  = Planet("Saturne", 5.6834e26)
Uranus   = Planet("Uranus",  8.6810e25)
Neptune  = Planet("Neptune", 1.0241e26)

