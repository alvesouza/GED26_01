/*Funcao para maximizar o lucro*/
max: 1638.95 * Xoleo_milho + 1415.53 * Xoleo_soja + 1522.99 * Xoleo_amendoim
 + 1293.88 * Xgordura + 1925.78 * Xmargarina_soja + 2015.7 * Xmargarina_milho
 - 1107.79 * Xoleo_bruto_milho - 995.99 * Xoleo_bruto_soja - 1098.17 * Xoleo_bruto_amendoim
 - 1115.33 * Xestearina_residuais - 1000 * Xleite_demais - 47.95 * Xneut_sharp 
 - 47.95 * Xneut_laval - 21.92 * Xfrigorificacao - 30.07 * Xclari_sharp - 30.07 * Xclari_laval
 - 13.89 * Xdeso_ws - 16.99 * Xdeso_ew - 23.01 * Xhidr_gor - 30.18 * Xclari_gor
 - 18.97 * Xacon_gor - 61.85 * Xacon_oleo - 31.89 * Xprep_marga - 135 * Xacon_marga;
 
/*Equações dos fluxos dos processos*/
/***********************************************/
/*Neutralização de Sharples*/
/*Milho*/
C1: Xneut_sharp_milho - 0.882 * Xoleo_bruto_milho = 0;

/*Amendoim*/
/*Oleo bruto de amendoim vai para Sharples e Laval*/
C2: Xoleo_bruto_amendoim_to_sharp + Xoleo_bruto_amendoim_to_laval - Xoleo_bruto_amendoim = 0;
C3: Xneut_sharp_amendoim - 0.882 * Xoleo_bruto_amendoim_to_sharp = 0;

/***********************************************/
/*Neutralização de Laval*/
/*Amendoim*/
C4: Xneut_laval_amendoim - 0.882 * Xoleo_bruto_amendoim_to_laval = 0;

/*Soja*/
C5: Xneut_laval_soja - 0.882 * Xoleo_bruto_soja = 0;

/***********************************************/
/*Frigorificacao*/
C6: Xfrigorificacao_milho - Xneut_sharp_milho = 0;

/***********************************************/
/*Clarificacao de Sharples*/
/*Milho*/
C7: Xclari_sharp_milho - 0.995 * Xfrigorificacao_milho = 0;

/*Amendoim*/
C8: Xclari_sharp_amendoim - 0.995 * Xneut_sharp_amendoim = 0;

/***********************************************/
/*Clarificacao de Laval*/
/*Amendoim*/
C9: Xclari_laval_amendoim - 0.995 * Xneut_laval_amendoim = 0;

/*Soja*/
C10: Xclari_laval_soja - 0.995 * Xneut_laval_soja = 0;

/***********************************************/
/*Clarificacao de Sharples vai para hidrogenacao de gordura e desodorizacao(ws)*/
/*Milho*/
C11: Xsharp_milho_to_hidro + Xsharp_milho_to_deso - Xclari_sharp_milho = 0;
/*Amendoim*/
C12: Xsharp_amendoim_to_hidro + Xsharp_amendoim_to_deso - Xclari_sharp_amendoim = 0;

/***********************************************/
/*Clarificacao de Laval vai para hidrogenacao de gordura e desodorizacao*/
/*Soja*/
C13: Xlaval_soja_to_hidro + Xlaval_soja_to_deso - Xclari_laval_soja = 0;

/***********************************************/
/*Hidrogenacao de gorduras*/
/*Milho*/
C14: 0.16 * Xhidr_gor - Xsharp_milho_to_hidro = 0;
/*Amendoim*/
C15: 0.41 * Xhidr_gor - Xsharp_amendoim_to_hidro = 0;
/*Soja*/
C16: 0.19 * Xhidr_gor - Xlaval_soja_to_hidro = 0;
/*Estearina*/
C17 : 0.24 * Xhidr_gor - Xestearina_residuais = 0;

/************************************************/
/*Desodorizacao(WS)*/
/*Milho*/
C18: Xdeso_milho - 0.991 * Xsharp_milho_to_deso = 0;
/*Amendoim que eh a soma da clarificacao de Sharples e de Laval*/
C19: Xdeso_amendoim - 0.991 * Xsharp_amendoim_to_deso - 0.991 * Xclari_laval_amendoim = 0;
/*Soja*/
C20: Xdeso_soja - 0.991 * Xclari_laval_soja = 0;

/*XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX*/
/*Geracao de gordura*/
/************************************************/
/*Clarificacao de gorduras*/
C21: Xclari_gor - 0.9683 * Xhidr_gor = 0;
/************************************************/
/*Desodorizacao(EW) de gordura*/
C22: Xdeso_gor - 0.991 * Xclari_gor = 0;
/************************************************/
/*Acondicionamento de gorduras*/
C23: Xacon_gor - Xdeso_gor = 0;
C24: Xgordura - Xacon_gor = 0;


/*XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX*/
/************************************************/
/*Desodorizacao(WS) se divide para aondicionamento e preparacao de margarina*/
/*Milho*/
C25: Xmilho_to_acon_oleo + Xmilho_to_prep_marga - Xdeso_milho = 0;
/*Soja*/
C26: Xsoja_to_acon_oleo + Xsoja_to_prep_marga - Xdeso_soja = 0;
/************************************************/
/*Acondicionamento de oleo*/
/*Milho*/
C27: Xacon_oleo_milho - Xmilho_to_acon_oleo = 0;
C28: Xoleo_milho - Xacon_oleo_milho = 0;
/*Amendoim*/
C29: Xacon_oleo_amendoim - Xdeso_amendoim = 0;
C30: Xoleo_amendoim - Xacon_oleo_amendoim = 0;
/*Soja*/
C31: Xacon_oleo_soja - Xsoja_to_acon_oleo = 0;
C32: Xoleo_soja - Xacon_oleo_soja = 0;
/************************************************/
/*Preparacao de margarina*/
/*Milho*/
C33: Xprep_marga_milho - Xmilho_to_prep_marga = 0;

/*Soja*/
C34: Xprep_marga_soja - Xsoja_to_prep_marga = 0;

/************************************************/
/*Acondicionamento de margarina*/
/*Milho*/
C35: 0.83 * Xmargarina_milho - Xprep_marga_milho = 0;
C36: 0.17 * Xmargarina_milho - Xleite_para_milho = 0;

/*Soja*/
C37: 0.83 * Xmargarina_soja - Xprep_marga_soja = 0;
C38: 0.17 * Xmargarina_soja - Xleite_para_soja = 0;

/*Quantidade de leite usado*/
C39: Xleite_demais - Xleite_para_soja - Xleite_para_milho = 0;

/*XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX*/
/************************************************/
/*Limites de mercado*/
/*Gordura*/
C40: Xgordura <= 800;
C41: Xgordura >= 400;

/*Margarina de soja*/
C42: Xmargarina_soja <= 1500;
C43: Xmargarina_soja >= 1000;

/*Margarina de soja*/
C44: Xmargarina_milho <= 700;
C45: Xmargarina_milho >= 400;

/*Oleo de milho*/
C46: Xoleo_milho <= 2000;
C47: Xoleo_milho >= 1400;

/*Oleo de soja*/
C48: Xoleo_soja <= 3000;
C49: Xoleo_soja >= 1500;

/*Oleo de amendoim*/
C50: Xoleo_amendoim <= 1000;
C51: Xoleo_amendoim >= 600;
/*XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX*/
/************************************************/
/*Limites de RECURSOS PRODUTIVOS*/
/*Neutralização de Sharples*/
C52: Xneut_sharp - Xneut_sharp_amendoim - Xneut_sharp_milho = 0;
/*Milho*/
C53: Xneut_sharp_milho <= 3000;
/*Amendoim*/
C54: Xneut_sharp_amendoim <= 4000;

/*Neutralizacao de Laval*/
C55: Xneut_laval - Xneut_laval_amendoim - Xneut_laval_soja = 0;
C56: Xneut_laval <= 5000;

/************************************************/
/*Frigorificacao*/
C57: Xfrigorificacao - Xfrigorificacao_milho = 0;
C58: Xfrigorificacao <= 2400;

/***********************************************/
/*Clarificacao de Sharples*/
C59: Xclari_sharp - Xclari_sharp_milho - Xclari_sharp_amendoim = 0;
C60: Xclari_sharp <= 3000;

/***********************************************/
/*Clarificacao de Laval*/
C61: Xclari_laval - Xclari_laval_amendoim - Xclari_laval_soja = 0;
C62: Xclari_laval <= 4500;

/***********************************************/
/*Desodorizacao (WS)*/
C63: Xdeso_ws - Xdeso_milho - Xdeso_amendoim = 0;
C64: Xdeso_ws <= 6000;/*Correcao 4000 -> 6000*/

/***********************************************/
/*Desodorizacao (EW)*/
C65: Xdeso_ew - Xdeso_gor = 0;
C65: Xdeso_ew <= 3000;

/***********************************************/
/*Hidrogenacao de gorduras*/
C66: Xhidr_gor <= 2000;

/***********************************************/
/*Clarificacao de gorduras*/
C67: Xclari_gor <= 1750;

/***********************************************/
/*Acondicionamento de gorduras*/
C68: Xacon_gor <= 2000;

/***********************************************/
/*Acondicionamento de oleos*/
C69: Xacon_oleo - Xoleo_milho - Xoleo_amendoim - Xoleo_soja = 0;
C70: Xacon_oleo <= 6000;

/***********************************************/
/*Preparacao de margarina*/
C71: Xprep_marga - Xprep_marga_milho - Xprep_marga_soja = 0;
C72: Xprep_marga <= 2000;

/***********************************************/
/*Acondicionamento de margarina*/
C72: Xacon_marga -  Xmargarina_milho - Xmargarina_soja = 0;
C73: Xacon_marga <= 2750;

/*XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX*/
/************************************************/
/*Adquirir materia prima, limites*/
C74: Xoleo_bruto_milho <= 2500;
C75: Xoleo_bruto_milho >= 0;

C76: Xoleo_bruto_amendoim <= 1500;
C77: Xoleo_bruto_amendoim >= 0;

C78: Xoleo_bruto_soja <= 4500;
C79: Xoleo_bruto_soja >= 0;

/*XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX*/
/************************************************/
/*Lower bound para as divisões dos fluxos, pois estes poderiam acabar se tornando menor que zero*/
/*Oleo bruto de amendoim vai para Sharples e Laval*/
C80: Xoleo_bruto_amendoim_to_sharp >= 0;
C81: Xoleo_bruto_amendoim_to_laval >= 0;
/*Clarificacao de Sharples vai para hidrogenacao de gordura e desodorizacao(ws)*/
/*Milho*/
C82: Xsharp_milho_to_hidro >= 0;
C83: Xsharp_milho_to_deso >= 0;
/*Amendoim*/
C84: Xsharp_amendoim_to_hidro >= 0;
C85: Xsharp_amendoim_to_deso >= 0;

/***********************************************/
/*Clarificacao de Laval vai para hidrogenacao de gordura e desodorizacao*/
/*Soja*/
C86: Xlaval_soja_to_hidro >= 0;
C87: Xlaval_soja_to_deso >= 0;

/***********************************************/
/*Desodorizacao(WS) se divide para aondicionamento e preparacao de margarina*/
/*Milho*/
C88: Xmilho_to_acon_oleo >= 0;
C89: Xmilho_to_prep_marga >= 0;
/*Soja*/
C90: Xsoja_to_acon_oleo >= 0;
C91: Xsoja_to_prep_marga >= 0;

