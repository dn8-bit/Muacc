import matplotlib.pyplot as plt
import FSEOF

resultados=['R_DHSKDH', 'R_GLYCLTt2rpp', 'R_KARA1', 'R_ASPTA', 'R_ADK3', 'R_GLUDy', 'R_G3PD2', 'R_PGAMT', 'R_EX_cl_LPAREN_e_RPAREN_', 'R_ILETA', 'R_ORPT', 'R_EX_mobd_LPAREN_e_RPAREN_', 'R_CATDOX', 'R_CAt6pp', 'R_EX_zn2_LPAREN_e_RPAREN_', 'R_SDPTA', 'R_EX_ca2_LPAREN_e_RPAREN_', 'R_IMPC', 'R_CTECOAI7', 'R_DHORTS', 'R_GLCt2pp', 'R_MOX', 'R_HEX1', 'R_GLYCLTtex', 'R_EX_fe3_LPAREN_e_RPAREN_', 'R_34dhbzDC', 'R_DHQTi', 'R_ASAD', 'R_AIRC3', 'R_HSDy', 'R_Htex', 'R_PPM', 'R_TRPAS2', 'R_EX_mg2_LPAREN_e_RPAREN_', 'R_TALA', 'R_EX_fe2_LPAREN_e_RPAREN_', 'R_EX_ccmuac_e', 'R_IPPMIb', 'R_IPPMIa', 'R_ACOAD5f', 'R_ACOAD4f', 'R_ACOAD7f', 'R_ACOTA', 'R_ACOAD6f', 'R_ACOAD1f', 'R_GLUR', 'R_ACOAD3f', 'R_ACOAD2f', 'R_MEOHtex', 'R_EX_cobalt2_LPAREN_e_RPAREN_', 'R_EX_so4_LPAREN_e_RPAREN_', 'R_EX_etoh_LPAREN_e_RPAREN_', 'R_DHQS', 'R_H2Otex', 'R_VPAMTr', 'R_ACt2rpp', 'R_FORtex', 'R_EX_mn2_LPAREN_e_RPAREN_', 'R_ACtex', 'R_AGPR', 'R_EX_co2_LPAREN_e_RPAREN_', 'R_ACKr', 'R_EX_nh4_LPAREN_e_RPAREN_', 'R_EX_k_LPAREN_e_RPAREN_', 'R_PPKr', 'R_H2Otpp', 'R_EX_cu2_LPAREN_e_RPAREN_', 'R_PGM', 'R_PGK', 'R_DDPA', 'R_MEOHtrpp', 'R_TKT1', 'R_PHETA1', 'R_VALTA', 'R_TYRTA', 'R_EX_ni2_LPAREN_e_RPAREN_', 'R_EX_pi_LPAREN_e_RPAREN_']
for i in resultados:
    lista=[]
    for j in FSEOF.lista_fluxos:
        lista.append(j[i])
    plt.plot(lista,'bo-')
    plt.ylabel('Fluxos')
    plt.xlabel(i)
    plt.savefig('todas/'+i+'.png')
    plt.show()
