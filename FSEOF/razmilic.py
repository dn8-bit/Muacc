import cobra.test
from cobra.io import read_sbml_model, write_sbml_model
from collections import namedtuple


def FSEOF(self):
    self.text4.delete(0.0, END)
    fseof_target =self.combox1.get()
    ntimes =self.combox2.get()
    cobra_model.optimize(solver='gurobi')


    '''
    1. Cálculo do vj(inicial) pela maximização da formação de biomassa
    '''
    cobra_model.objective ='ExBiomass_e' #Função objetivo
    cobra_model.optimize(solver='gurobi')
    v_biomass=cobra_model.solution.f
    vin=cobra_model.solution.x_dict
    tu=namedtuple('v_initial',['rxn_name','rxn_flux_ini'])
    v_fluxes_ini=[]
    for item in vin:
        vj_name=str(item)
        vj_ini=vin[item]
        v_flux_ini=tu(rxn_name=vj_name,rxn_flux_ini=vj_ini)
        v_fluxes_ini.append(v_flux_ini)
        if vj_name ==fseof_target:
            vTarget_ini=vin[item]
        if vj_name== 'rx0155':
            print(vin[item])
    
    '''
    2. Cálculo do máximo teórico do metabólito
    '''

    cobra_model.objective=fseof_target
    cobra_model.optimize(solver='gurobi')
    vmax_Target=cobra_model.solution.f

    '''
    3. Aplicação FSEOF
    '''

    v_bio=[]
    rxn=cobra_model.reactions.get_by_id(fseof_target)
    vprod_enforced_list=[]
    n=float(ntimes)+1
    for k in range(1,int(ntimes)+1):
        vprod_enforced=vTarget_ini+(k/n)*(vmax_Target-vTarget_ini)
        vprod_enforced_list.append(vprod_enforced)
    i=0
    enf={}
    enf_rx={}
    fva_rx={}
    #v_enforced_list=[]
    v_list_rxn_enforced=[]
    rr_list=[]
    fva_list=[]
    for item in vprod_enforced_list:
        i+=1
        rxn.lower_bound=item
        rxn.upper_bound=item
        cobra_model.objective='ExBiomass_e'
        cobra_model.optimize(solver='gurobi')
        v_biom=cobra_model.solution.f
        v_bio.append(cobra_model.solution.f)
        vj_2=cobra_model.solution.x_dict
        enf[i]=namedtuple("v_enforced"+str(i),['rxn_name','rxn','genes','rxn_flux_ini', 'rxn_flux_enf'])
        fva_result = cobra.flux_analysis.flux_variability_analysis(cobra_model,cobra_model.reactions[:len(cobra_model.reactions)],fraction_of_optimum=1)
        enf_rx[i]=namedtuple('v_enforced'+str(i),['rxn_name','vprodChax','fva_min','fva_max'])
        for obj in vj_2:
            vj_2name=str(obj)
            rr=cobra_model.reactions.get_by_id(obj)
            react=rr.reaction
            gen=rr.gene_reaction_rule
            vj_au=vj_2[obj]
            for obj2 in v_fluxes_ini:
                if vj_2name==obj2.rxn_name:
                    vj_init=obj2.rxn_flux_ini
                    if abs(vj_au)>abs(vj_init) and vj_au*vj_init>=0:
                        if str(rr) not in rr_list:
                            rr_list.append(str(rr))
                    v_list2=enf_rx[i](rxn_name=vj_2name,rxn=react,genes=gen,rxn_flux_ini=vj_init,rxn_fluz_enf=vj_au)
                    v_list_rxn_enforced.append(v_list2)
                    rx_fva=fva_result[str(rr)]
                    rx_fva_min=rx_fva['minimum']
                    rx_fva_max=rx_fva['maximum']
                    fva_data=fva_rx[i](rxn_name=vj_2name,vprodChax=item,fva_min=rx_fva_min,fva_max=rx_fva_max)
                    fva_list.append(fva_data)

