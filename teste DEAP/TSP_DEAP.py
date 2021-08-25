import matplotlib.pyplot as plt
import sys 
import array
import random
import numpy as np
from deap import algorithms
from deap import base
from deap import creator
from deap import tools

#setando cidades
numCidades=10
random.seed(169)
x= np.random.rand(numCidades)
y= np.random.rand(numCidades)
'''
print(x)
print(y)
plt.plot(x,y)
plt.show()
'''

#p/ minimizar a distancia, pesos devem ser negativos
creator.create('FitnessMin',base.Fitness,weights=(-1.0,))
#os individuos serão vetores de inteiros dimensão 1xnCidades)
creator.create('Individuo',array.array,typecode='i',fitness=creator.FitnessMin)

toolbox=base.Toolbox()

#gerando atributos
toolbox.register("indices",random.sample,range(numCidades),numCidades)
#print(random.sample(range(numCidades),numCidades))

toolbox.register('individuo',tools.initIterate,creator.Individuo,toolbox.indices)
toolbox.register('populacao',tools.initRepeat,list,toolbox.individuo)
toolbox.register('mate',tools.cxOrdered)
toolbox.register('mutate',tools.mutShuffleIndexes, indpb=0.005)
toolbox.register('select', tools.selTournament,tournsize=3)

def aval(i):
    print(i)
    diffx=np.diff(x[i])
    diffy=np.diff(y[i])
    distancia= np.sum(diffx**2+diffy**2)
    return distancia

toolbox.register('evaluate',aval)

def main():

    random.seed(169)
    pop=toolbox.populacao(n=300)
    hof=tools.HallOfFame(1)

    stats=tools.Statistics(lambda ind:ind.fitness.values)
    stats.register('avg',np.mean)
    stats.register('std',np.std)
    stats.register('min',np.min)
    stats.register('max',np.max)
    
    algorithms.eaSimple(pop,toolbox,0.7,0.2,140,stats=stats,halloffame=hof)

    ind=hof[0]
    plt.figure(2)
    plt.plot(x[ind],y[ind])
    plt.ion()
    plt.show()
    plt.pause(0.001)

    return pop,stats,hof

if __name__ =="__main__":
    main()
