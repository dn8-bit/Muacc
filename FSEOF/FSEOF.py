import cobra
import pandas as pd
import numpy as np
import os



cobra_model= cobra.io.load_json_model('/home/daniel/github/Muacc/KO_EA/GEMs/RotaA.json')
biomass_id='R_Ec_biomass_iJO1366_core_53p95M'
alvo="R_EX_ccmuac_e"
n_vezes=10
#minimo
cobra_model.objective=biomass_id
fluxos_iniciais= cobra_model.optimize().fluxes
biomassa_0= fluxos_iniciais[biomass_id]
v_0=fluxos_iniciais[alvo]

#maximização

cobra_model.objective=alvo
fluxos_maximo=cobra_model.optimize().fluxes
biomassa_final=fluxos_maximo[biomass_id]
v_final=fluxos_maximo[alvo]

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

for item in fluxos_forcados:
    i+=1
    reacao_alvo.upper_bound=item
    reacao_alvo.lower_bound=item
    simulacao= cobra_model.optimize().fluxes
    lista_fluxos.append(simulacao)
    a=[]
    for reacao in cobra_model.reactions:
        if lista_fluxos[i-1][reacao.id]<lista_fluxos[i][reacao.id] and lista_fluxos[i][reacao.id]*lista_fluxos[i-1][reacao.id]>=0:
            a.append(reacao.id)
    lista_selecionadas.append(a)

for r in lista_selecionadas:
    #print(f'{r} : {lista_fluxos[0][r]} -> {lista_fluxos[-1][r]}')
    print(len(r))
