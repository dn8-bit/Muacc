import cobra.test
import os
from os.path import join
from cobra.io import load_json_model
import matplotlib.pyplot as plt

dir = os.path.dirname(__file__)
CaminhoRotaA = os.path.join(dir, 'GEMs','RotaA.json')


RotaA=cobra.io.load_json_model(os.path.join(dir, 'GEMs','RotaA.json'))
RotaB=cobra.io.load_json_model(os.path.join(dir, 'GEMs','RotaB.json'))
RotaC1=cobra.io.load_json_model(os.path.join(dir, 'GEMs','RotaC1.json'))
RotaC2=cobra.io.load_json_model(os.path.join(dir, 'GEMs','RotaC2.json'))
RotaD=cobra.io.load_json_model(os.path.join(dir, 'GEMs','RotaD.json'))



RotaA.objective= RotaA.reactions.get_by_id("R_EX_ccmuac_e")
RotaB.objective= RotaB.reactions.get_by_id("R_EX_ccmuac_e")
RotaC1.objective= RotaC1.reactions.get_by_id("R_EX_ccmuac_e")
RotaC2.objective= RotaC2.reactions.get_by_id("R_EX_ccmuac_e")
RotaD.objective= RotaD.reactions.get_by_id("R_EX_ccmuac_e")

max_A=RotaA.optimize().objective_value
max_B=RotaB.optimize().objective_value
max_C1=RotaC1.optimize().objective_value
max_C2=RotaC2.optimize().objective_value
max_D=RotaD.optimize().objective_value

Flux_max=[max_A/10,max_B/10,max_C1/10, max_C2/10, max_D/10]
rotas=["Rota A", "Rota B","Rota C1","Rota C2","Rota D"]

plt.bar(rotas,Flux_max,color="darkcyan",width=0.5)
plt.xticks(rotas)
plt.ylabel("Fluxo de Ác. mucônico (mmol/gDW.h)")
plt.title("Rendimento máximo téorico (mol de Ác. Mucônico/mol glicose)")
plt.show()
