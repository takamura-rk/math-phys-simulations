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
        
    
    