import cobra
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt



cobra_model= cobra.io.load_json_model('/home/daniel/github/Muacc/KO_EA/GEMs/RotaA.json')
biomass_id='R_Ec_biomass_iJO1366_core_53p95M'
alvo="R_EX_ccmuac_e"
n_vezes=10


#Condicoes ambientais
oxigenio=cobra_model.reactions.get_by_id("R_EX_o2_LPAREN_e_RPAREN_")
glc=cobra_model.reactions.get_by_id("R_EX_glc_LPAREN_e_RPAREN_")
glc.upper_bound=-9.99
glc.lower_bound=-10.0
oxigenio.upper_bound=-9.99
oxigenio.lower_bound=-10.0

#minimo
cobra_model.objective=biomass_id
fluxos_iniciais= cobra_model.optimize().fluxes
biomassa_0= fluxos_iniciais[biomass_id]
v_0=fluxos_iniciais[alvo]
fluxos_iniciais.to_csv('fluxos/Fluxos Iniciais')
#maximização

cobra_model.objective=alvo
fluxos_maximo=cobra_model.optimize().fluxes
biomassa_final=fluxos_maximo[biomass_id]
v_final=fluxos_maximo[alvo]
fluxos_maximo.to_csv('fluxos/Fluxos Maximos')
#calculo dos passos
fluxos_forcados=[]
n=float(n_vezes)+1
for k in range(1, int(n_vezes)+1):
    v_forcado=v_0+(k/n)*(v_final-v_0)
    fluxos_forcados.append(v_forcado)

i=0
cobra_model.objective=biomass_id
reacao_alvo=cobra_model.reactions.get_by_id(alvo)
lista_fluxos=[fluxos_iniciais]
lista_selecionadas=[]
lista_fva=[]

for item in fluxos_forcados:
    i+=1
    reacao_alvo.upper_bound=item
    reacao_alvo.lower_bound=item
    simulacao= cobra_model.optimize().fluxes
    simulacao.to_csv(f'fluxos/Fluxos iteracao {i}')
    lista_fluxos.append(simulacao)
    a=[]
    for reacao in cobra_model.reactions:
        if lista_fluxos[i-1][reacao.id]<lista_fluxos[i][reacao.id] and lista_fluxos[i][reacao.id]*lista_fluxos[i-1][reacao.id]>=0:
            a.append(reacao.id)
    fva=cobra.flux_analysis.flux_variability_analysis(cobra_model,reaction_list=a)
    fva.to_csv(f'FVA/FVA iteracao {i}')
    lista_fva.append(fva)
    lista_selecionadas.append(a)

with open('resultados.txt', 'w') as out_file:
    for a in lista_selecionadas:
        out_file.writelines(str(a)+' \n')
lista_fluxos.append(fluxos_maximo)
