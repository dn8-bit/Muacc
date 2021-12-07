from mewpy.simulation import SimulationMethod, get_simulator
from mewpy.problems import RKOProblem, ROUProblem
from mewpy.optimization.evaluation import BPCY, BPCY_FVA,WYIELD, AggregatedSum,TargetFlux
from mewpy.optimization import EA
from cobra.io import load_json_model
from collections import OrderedDict
from mewpy.util.constants import EAConstants
import time
import csv


EAConstants.NUM_CPUS = 8
start_time = time.time()
model= load_json_model('RotaA.json')

biomassa="R_Ec_biomass_iJO1366_core_53p95M"
produto="R_DHSKDH"
o2="R_EX_o2_LPAREN_e_RPAREN_"
glc="R_EX_glc_LPAREN_e_RPAREN_"

envcond={glc: (-10.000,-9.99999),o2:(-10.000,-9.99999)}
model.objective="R_Ec_biomass_iJO1366_core_53p95M"

simulation=get_simulator(model,envcond=envcond)
res=simulation.simulate(method='FBA')
reference=res.fluxes

evaluator= TargetFlux(produto,biomass=biomassa, min_biomass_value=0.02) 
problem=RKOProblem(model,fevaluation=[evaluator],envcond=envcond,candidate_max_size=5)

ea=EA(problem,max_generations=10000 ,visualizer=False,mp=True,algorithm='SPEA2')

final_pop=ea.run()
print(final_pop)
print("--- %s seconds ---" % (time.time() - start_time))
with open('filename', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(final_pop)