/*Funcao para minimizar o tamanho das arestas*/
min: 1 XA_B + 4 XA_C + 8 XA_D + 3 XB_C + 3 XB_F + 7 XC_D + 7 XC_E + 6 XC_F + 4 XD_E + 5 XD_G + 2 XD_H + 8 XE_F + 3 XE_G + 2 XE_H + 4 XF_K + 6 XG_H + 3 XG_I + 4 XG_J + 2 XH_J + 4 XH_K + 7 XH_L + 5 XI_J + 6 XJ_L + 2 XK_L;
/*O numero de arestas de um arvore minima é o numero dos vertices - 1*/
C1: XA_B + XA_C + XA_D + XB_C + XB_F + XC_D + XC_E + XC_F + XD_E + XD_G + XD_H + XE_F + XE_G + XE_H + XF_K + XG_H + XG_I + XG_J + XH_J + XH_K + XH_L + XI_J + XJ_L + XK_L = 11;
/*Proibir ciclos de percusso*/
/*Proibir ciclos de tamanho 3*/
C2: XA_B + XB_C + XA_C <= 2;
C3: XA_C + XC_D + XA_D <= 2;
C4: XB_C + XC_F + XB_F <= 2;
C5: XC_D + XD_E + XC_E <= 2;
C6: XC_E + XE_F + XC_F <= 2;
C7: XD_E + XE_G + XD_G <= 2;
C8: XD_G + XG_I + XD_I <= 2;
C9: XE_G + XG_H + XE_H <= 2;
C10: XG_H + XH_J + XG_J <= 2;
C11: XG_I + XI_J + XG_J <= 2;
C12: XH_J + XJ_L + XH_L <= 2;
C13: XH_K + XK_L + XH_L <= 2;
/*Proibir ciclos de tamanho 4*/
C14: XA_B + XB_C + XC_D + XA_D <= 3;
C15: XB_C + XC_E + XE_F + XB_F <= 3;
C16: XC_D + XD_E + XE_F + XC_F <= 3;
C17: XD_E + XE_G + XG_I + XD_I <= 3;
/*Proibir ciclos de tamanho 5*/
C18: XB_C + XC_D + XD_E + XE_F + XB_F <= 4;
/*Proibir ciclos de tamanho 6*/
/*Proibir ciclos de tamanho 7*/
/*Proibir ciclos de tamanho 8*/
/*Proibir ciclos de tamanho 9*/
/*Proibir ciclos de tamanho 10*/
/*Proibir ciclos de tamanho 11*/
/*Xi_j se for 1, significa que passara pela aresta de i e j, ou seja, eles só podem ser 0 ou 1*/
bin XA_B;
bin XA_C;
bin XA_D;
bin XB_C;
bin XB_F;
bin XC_D;
bin XC_E;
bin XC_F;
bin XD_E;
bin XD_G;
bin XD_H;
bin XE_F;
bin XE_G;
bin XE_H;
bin XF_K;
bin XG_H;
bin XG_I;
bin XG_J;
bin XH_J;
bin XH_K;
bin XH_L;
bin XI_J;
bin XJ_L;
bin XK_L;
