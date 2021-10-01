import cobra

results=[ 'R_KARA1', 'R_ASPTA', 'R_ADK3', 'R_GLUDy', 'R_G3PD2', 'R_PGAMT' , 'R_ILETA', 'R_ORPT',  'R_SDPTA', 'R_IMPC', 'R_CTECOAI7', 'R_DHORTS',  'R_MOX', 'R_HEX1', 'R_ASAD', 'R_AIRC3', 'R_HSDy',  'R_PPM', 'R_TRPAS2',  'R_TALA', 'R_IPPMIb', 'R_IPPMIa', 'R_ACOAD5f', 'R_ACOAD4f', 'R_ACOAD7f', 'R_ACOTA', 'R_ACOAD6f', 'R_ACOAD1f', 'R_GLUR', 'R_ACOAD3f', 'R_ACOAD2f',  'R_DHQS', 'R_VPAMTr' , 'R_AGPR', 'R_ACKr', 'R_PPKr',  'R_PGM', 'R_PGK', 'R_DDPA', 'R_TKT1', 'R_PHETA1', 'R_VALTA', 'R_TYRTA' ]

transporte=['R_EX_mg2_LPAREN_e_RPAREN_','R_EX_fe2_LPAREN_e_RPAREN_','R_EX_cu2_LPAREN_e_RPAREN_','R_EX_ni2_LPAREN_e_RPAREN_','R_EX_cl_LPAREN_e_RPAREN_','R_EX_mobd_LPAREN_e_RPAREN_','R_EX_zn2_LPAREN_e_RPAREN_','R_EX_ca2_LPAREN_e_RPAREN_', 'R_EX_mn2_LPAREN_e_RPAREN_','R_EX_fe3_LPAREN_e_RPAREN_','R_EX_k_LPAREN_e_RPAREN_','R_EX_nh4_LPAREN_e_RPAREN_','R_EX_cobalt2_LPAREN_e_RPAREN_','R_EX_pi_LPAREN_e_RPAREN_','R_EX_co2_LPAREN_e_RPAREN_','R_EX_so4_LPAREN_e_RPAREN_','R_EX_etoh_LPAREN_e_RPAREN_']

pp=['R_GLYCLTt2rpp','R_CAt6pp','R_GLCt2pp','R_ACt2rpp','R_H2Otpp','R_MEOHtrpp']

tex=['R_GLYCLTtex','R_Htex','R_MEOHtex','R_H2Otex', 'R_FORtex','R_ACtex']

heterologa=['R_DHSKDH', 'R_CATDOX', 'R_34dhbzDC', 'R_DHQTi','R_EX_ccmuac_e']

cobra_model= cobra.io.load_json_model('/home/daniel/github/Muacc/KO_EA/GEMs/RotaA.json')

sel=[]
nsel=[]
print(f'resultados totais: {len(results)}')
print(f'reacoes periplasma: {len(pp)}')
print(f'reacoes transporte: {len(tex)}')
print('-------------------------------------------------------------------------------- \n')
for i in results:
    r=cobra_model.reactions.get_by_id(i)
    print(r)
    for k in list(r.metabolites.keys()):
        print(k.name)
    a=input('guarda? :')
    if a=='y':
        sel.append(i)
    else:
        nsel.append(i)
    print('-------------------------------------------------------------------------------- \n')

with open('resultados_selecionados.txt', 'w') as out_file:
    out_file.writelines(str(sel))

with open('resultados_nselecionados.txt', 'w') as out_file:
    out_file.writelines(str(nsel))
