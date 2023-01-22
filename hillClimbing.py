import numpy as np
from matplotlib import pyplot
from numpy.random import uniform


#Metauristica
class HillClimbing:
    def __init__(self,objetivo,limites,step_size,n_inter):
        self.objetivo = objetivo
        self.limites = limites
        self.step_size = step_size
        self.n_inter = n_inter

    def show(self):
        # self.limites=(-10,10)
        #valores a tomar las x
        x_inputs=np.arange(self.limites[0],self.limites[1],0.1)
        #evaluar cada valor en la funcion y se generaran en una lista de comprension
        y_inputs=[self.objetivo(x) for x in x_inputs]
        #Creacion de la grafica
        pyplot.plot(x_inputs,y_inputs,'--')
        #Graficar Soluciones
        best,eval_best,soluciones = self.solve()
        pyplot.plot(soluciones,[self.objetivo(x) for x in soluciones],'o',color="black")
        # pyplot.savefig("grafica.png")
        pyplot.show()
    
    def solve(self):
        #Solucion son todos los valores que estan dentro del dominio 
        #np.ramdom.uniform() hace una seleccion uniforme de unos limites dados
        solucion = np.random.uniform(low=self.limites[0],high=self.limites[1])
        eval = self.objetivo(solucion)
        soluciones = []
        soluciones.append(solucion)
        
        for i in range(self.n_inter):
            vecino = np.random.uniform(low=self.limites[0],high=self.limites[1])
            eval_v = self.objetivo(vecino)
            
            if eval_v <= eval:
                solucion,eval = vecino,eval_v
                soluciones.append(solucion)

        print("solucion",solucion)
        
        return(solucion,eval,soluciones)
    
