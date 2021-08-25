import cobra.test
from cobra.io import read_sbml_model, write_sbml_model
from collections import namedtuple


def FSEOF(self):
    self.text4.delete(0.0, END)
    fseof_target =self.combox1.get()
    ntimes =self.combox2.get()
    cobra_model.optimize(solver='gurobi')


    '''
    cálculo do vj(inicial) pela maximização da formação de biomassa

    '''
    cobra_model.objective ='ExBiomass_e' #Função objetivo
    cobra_model.optimize(solver='gurobi')
    v_biomass=cobra_model.solution.f
    vin=cobra_model.solution.x_dict
    tu=namedtuple('v_initial',['rxn_name','rxn_flux_ini'])
    v_fluxes_ini=[]