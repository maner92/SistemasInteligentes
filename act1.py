import numpy as np
from matplotlib import pyplot
from numpy.random import uniform

def var (x): 
    return x**2

def plot():
    #se definen los limites
    limites=(-10,19)
    #valores a tomar las x
    x_inputs=np.arange(limites[0],limites[1],0.1)
    #evaluar cada valor en la funcion y se generaran en una lista de comprension
    y_inputs=[var(x) for x in x_inputs]
    #Creacion de la grafica
    pyplot.plot(x_inputs,y_inputs,'--')
    # pyplot.savefig("grafica.png")
    pyplot.show()
    
#plot()
    
# Generar una solucion por defecto
def hill_climbing(objetivo,limites,n_iter,step):
    solucion=uniform(low=limites[0],
                        high=limites[1])
    eval=objetivo(solucion)

