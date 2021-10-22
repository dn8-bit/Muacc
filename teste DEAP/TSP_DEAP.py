import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
from deap import algorithms, base, creator, tools, gp
import random, operator, time, itertools, math
import numpy as np
import cobra
import os
import time
start_time = time.time()
cobra_model= cobra.io.load_json_model('RotaA.json')

def gerar_individuo(n):
    return list(np.random.randint(0, len(cobra_model.reactions),n))

toolbox=base.Toolbox()
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox.register("indices", gerar_individuo, 3)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutUniformInt, low=0,up=len(cobra_model.reactions)-1,indpb=0.1)


def evaluation(individual):
    cobra_model.reactions[individual[0]].knock_out()
    cobra_model.reactions[individual[1]].knock_out()
    cobra_model.reactions[individual[2]].knock_out()
    sol= cobra_model.optimize().fluxes
    print(sol["R_EX_ccmuac_e"])
    return (sol["R_EX_ccmuac_e"],)


toolbox.register("evaluate", evaluation)
toolbox.register("select", tools.selTournament, tournsize=3)
pop = toolbox.population(n=200)
result, log = algorithms.eaSimple(pop, toolbox,cxpb=0.8, mutpb=0.2,ngen=10000, verbose=False)
best_individual = tools.selBest(result, k=1)[0]
print('Fitness of the best individual: ', evaluation(best_individual)[0])
print("--- %s seconds ---" % (time.time() - start_time))
