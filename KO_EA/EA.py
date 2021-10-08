import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
from deap import algorithms, base, creator, tools
import random, operator, time, itertools, math
import numpy as np
import cobra.test
import os
from os.path import join
from cobra.io import load_json_model


cobra_model= cobra.io.load_json_model(os.path.join(os.path.dirname(__file__), 'GEMs','RotaA.json'))

solution=cobra_model.optimize()


def gerar_individuo(n):
    return list(np.random.randint(0, len(cobra_model.reactions)+1,n))


def evaluation(individual):
    cobra_model.reactions[individual[0]].knock_out()
    cobra_model.reactions[individual[1]].knock_out()
    cobra_model.reactions[individual[2]].knock_out()
    sol= cobra_model.optimize().fluxes
    return sol["R_EX_ccmuac_e"]
a=gerar_individuo(3)
print(evaluation(a))
print(a)
