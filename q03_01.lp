/*Funcao para minimizar o custo da passagem*/
min: 24.0 XSFS_JAL + 33.0 XSFS_POP + 42.0 XSFS_AND + 30.0 XPOP_FER + 93.0 XPOP_OLP + 80.0 XPOP_BAR + 30.0 XJAL_FER + 66.0 XJAL_AND + 48.0 XJAL_ART + 58.0 XFER_SJP + 46.0 XAND_ART + 68.0 XAND_PPD + 48.0 XART_PPD + 72.0 XART_MAR + 42.0 XART_SJP + 18.0 XPPD_MAR + 18.0 XPPD_ASS + 26.0 XASS_TQB + 48.0 XASS_BTT + 50.0 XBTT_CAP + 28.0 XBTT_SOR + 14.0 XBTT_TQB + 22.0 XBTT_API + 8.0 XMAR_ASS + 48.0 XMAR_BAU + 28.0 XBAU_ARQ + 22.0 XBAU_BTT + 38.0 XSJP_OLP + 46.0 XSJP_CAT + 68.0 XOLP_BAR + 64.0 XOLP_RBP + 26.0 XOLP_CAT + 18.0 XBAR_RBP + 44.0 XBAR_PCD + 28.0 XRBP_ARQ + 42.0 XRBP_SCL + 50.0 XRBP_PCD + 46.0 XCAT_MAR + 74.0 XCAT_BAU + 60.0 XCAT_ARQ + 58.0 XCAT_RBP + 12.0 XARQ_SCL + 36.0 XSCL_PCD + 86.0 XSCL_CAP + 38.0 XSCL_BTT + 90.0 XPCD_CJD + 76.0 XPCD_CAP + 50.0 XCJD_CGT + 30.0 XCJD_SJC + 50.0 XCAP_CJD + 46.0 XCAP_SJC + 4.0 XCAP_JUN + 30.0 XCAP_SOR + 4.0 XSPO_SBC + 22.0 XJUN_SPO + 20.0 XSOR_JUQ + 18.0 XSOR_SPO + 26.0 XSOR_SBC + 12.0 XTQB_API + 14.0 XAPI_SOR + 24.0 XAPI_JUQ + 30.0 XJUQ_SBC + 40.0 XJUQ_SAN + 40.0 XSBC_SJC + 24.0 XSBC_SAN + 48.0 XSBC_CGT + 22.0 XSAN_CGT + 18.0 XSJC_CGT;

/*O numero de saidas da cidade SFS eh 1*/
C1: XSFS_JAL + XSFS_POP + XSFS_AND = 1;

/*O numero de saidas da cidade SPO eh 1, assim garantindo que passa por SPO*/
C2: XSPO_SBC = 1;

/*O numero de entrada pela cidade CGT eh 1, assim garantindo que passa por SPO*/
C3: XCJD_CGT + XSBC_CGT + XSAN_CGT + XSJC_CGT = 1;

/*O numero de entradas deve ser o mesmo que o de saida*/
/*Para a cidade POP*/
C4: XPOP_FER + XPOP_OLP + XPOP_BAR - XSFS_POP = 0;
/*Para a cidade JAL*/
C5: XJAL_FER + XJAL_AND + XJAL_ART - XSFS_JAL = 0;
/*Para a cidade FER*/
C6: XFER_SJP - XPOP_FER - XJAL_FER = 0;
/*Para a cidade AND*/
C7: XAND_ART + XAND_PPD - XSFS_AND - XJAL_AND = 0;
/*Para a cidade ART*/
C8: XART_PPD + XART_MAR + XART_SJP - XJAL_ART - XAND_ART = 0;
/*Para a cidade PPD*/
C9: XPPD_MAR + XPPD_ASS - XAND_PPD - XART_PPD = 0;
/*Para a cidade ASS*/
C10: XASS_TQB + XASS_BTT - XPPD_ASS - XMAR_ASS = 0;
/*Para a cidade BTT*/
C11: XBTT_CAP + XBTT_SOR + XBTT_TQB + XBTT_API - XASS_BTT - XBAU_BTT - XSCL_BTT = 0;
/*Para a cidade MAR*/
C12: XMAR_ASS + XMAR_BAU - XART_MAR - XPPD_MAR - XCAT_MAR = 0;
/*Para a cidade BAU*/
C13: XBAU_ARQ + XBAU_BTT - XMAR_BAU - XCAT_BAU = 0;
/*Para a cidade SJP*/
C14: XSJP_OLP + XSJP_CAT - XFER_SJP - XART_SJP = 0;
/*Para a cidade OLP*/
C15: XOLP_BAR + XOLP_RBP + XOLP_CAT - XPOP_OLP - XSJP_OLP = 0;
/*Para a cidade BAR*/
C16: XBAR_RBP + XBAR_PCD - XPOP_BAR - XOLP_BAR = 0;
/*Para a cidade RBP*/
C17: XRBP_ARQ + XRBP_SCL + XRBP_PCD - XOLP_RBP - XBAR_RBP - XCAT_RBP = 0;
/*Para a cidade CAT*/
C18: XCAT_MAR + XCAT_BAU + XCAT_ARQ + XCAT_RBP - XSJP_CAT - XOLP_CAT = 0;
/*Para a cidade ARQ*/
C19: XARQ_SCL - XBAU_ARQ - XRBP_ARQ - XCAT_ARQ = 0;
/*Para a cidade SCL*/
C20: XSCL_PCD + XSCL_CAP + XSCL_BTT - XRBP_SCL - XARQ_SCL = 0;
/*Para a cidade PCD*/
C21: XPCD_CJD + XPCD_CAP - XBAR_PCD - XRBP_PCD - XSCL_PCD = 0;
/*Para a cidade CJD*/
C22: XCJD_CGT + XCJD_SJC - XPCD_CJD - XCAP_CJD = 0;
/*Para a cidade CAP*/
C23: XCAP_CJD + XCAP_SJC + XCAP_JUN + XCAP_SOR - XBTT_CAP - XSCL_CAP - XPCD_CAP = 0;
/*Para a cidade SPO*/
C24: XSPO_SBC - XJUN_SPO - XSOR_SPO = 0;
/*Para a cidade JUN*/
C25: XJUN_SPO - XCAP_JUN = 0;
/*Para a cidade SOR*/
C26: XSOR_JUQ + XSOR_SPO + XSOR_SBC - XBTT_SOR - XCAP_SOR - XAPI_SOR = 0;
/*Para a cidade TQB*/
C27: XTQB_API - XASS_TQB - XBTT_TQB = 0;
/*Para a cidade API*/
C28: XAPI_SOR + XAPI_JUQ - XBTT_API - XTQB_API = 0;
/*Para a cidade JUQ*/
C29: XJUQ_SBC + XJUQ_SAN - XSOR_JUQ - XAPI_JUQ = 0;
/*Para a cidade SBC*/
C30: XSBC_SJC + XSBC_SAN + XSBC_CGT - XSPO_SBC - XSOR_SBC - XJUQ_SBC = 0;
/*Para a cidade SAN*/
C31: XSAN_CGT - XJUQ_SAN - XSBC_SAN = 0;
/*Para a cidade SJC*/
C32: XSJC_CGT - XCJD_SJC - XCAP_SJC - XSBC_SJC = 0;
/*Xi_j se for 1, significa que passara pela aresta de i e j, ou seja, eles só podem ser 0 ou 1*/
bin XSFS_JAL;
bin XSFS_POP;
bin XSFS_AND;
bin XPOP_FER;
bin XPOP_OLP;
bin XPOP_BAR;
bin XJAL_FER;
bin XJAL_AND;
bin XJAL_ART;
bin XFER_SJP;
bin XAND_ART;
bin XAND_PPD;
bin XART_PPD;
bin XART_MAR;
bin XART_SJP;
bin XPPD_MAR;
bin XPPD_ASS;
bin XASS_TQB;
bin XASS_BTT;
bin XBTT_CAP;
bin XBTT_SOR;
bin XBTT_TQB;
bin XBTT_API;
bin XMAR_BAU;
bin XBAU_ARQ;
bin XSJP_OLP;
bin XSJP_CAT;
bin XOLP_BAR;
bin XOLP_RBP;
bin XOLP_CAT;
bin XBAR_RBP;
bin XBAR_PCD;
bin XRBP_ARQ;
bin XRBP_SCL;
bin XRBP_PCD;
bin XCAT_ARQ;
bin XARQ_SCL;
bin XSCL_PCD;
bin XSCL_CAP;
bin XPCD_CJD;
bin XPCD_CAP;
bin XCJD_CGT;
bin XCJD_SJC;
bin XCAP_SJC;
bin XCAP_JUN;
bin XCAP_SOR;
bin XSPO_SBC;
bin XSOR_JUQ;
bin XSOR_SBC;
bin XTQB_API;
bin XAPI_JUQ;
bin XJUQ_SBC;
bin XJUQ_SAN;
bin XSBC_SJC;
bin XSBC_SAN;
bin XSBC_CGT;
bin XSAN_CGT;
