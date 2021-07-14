/*Funcao para maximizar o fluxo para o 6*/
max: X1_6 + X5_6 + X7_6;
/*Equações dos fluxos para as respectivas cidades, onde os que estão apenas fazendo a transferencia, a varição deve ser zero*/
/*Cidade com o fluxo a se maximizar é 6 e saida é 9*/
/*Fluxo da cidade 1*/
C1: X8_1 - X1_2 - X1_4 - X1_5 - X1_6 - X1_7 = 0;

/*Fluxo da cidade 2*/
C2: X1_2 + X3_2 + X8_2 + X9_2 + X10_2 - X2_3 - X2_4 = 0;

/*Fluxo da cidade 3*/
C3: X2_3 + X10_3 - X3_2 - X3_4 = 0;

/*Fluxo da cidade 4*/
C4: X1_4 + X2_4 + X3_4 - X4_5 = 0;

/*Fluxo da cidade 5*/
C5: X1_5 + X4_5 - X5_6 = 0;

/*Fluxo da cidade 7*/
C6: X1_7 + X8_7 - X7_6 = 0;

/*Fluxo da cidade 8*/
C7: X9_8 - X8_1 - X8_2 - X8_7 = 0;

/*Fluxo da cidade 10*/
C8: X9_10 - X10_2 - X10_3 = 0;

/*nenhum fluxo vai passar do maximo*/
C9: X1_2 <= 10;
C10: X1_4 <= 20;
C11: X1_5 <= 20;
C12: X1_6 <= 5;
C13: X1_7 <= 15;
C14: X2_3 <= 5;
C15: X2_4 <= 10;
C16: X3_2 <= 15;
C17: X3_4 <= 5;
C18: X4_5 <= 10;
C19: X5_6 <= 5;
C20: X7_6 <= 10;
C21: X8_1 <= 5;
C22: X8_2 <= 20;
C23: X8_7 <= 5;
C24: X9_2 <= 15;
C25: X9_8 <= 20;
C26: X9_10 <= 10;
C27: X10_2 <= 5;
C28: X10_3 <= 15;
/*nenhum fluxo vai ser menor que zero*/
C29: X1_2 >= 0;
C30: X1_4 >= 0;
C31: X1_5 >= 0;
C32: X1_6 >= 0;
C33: X1_7 >= 0;
C34: X2_3 >= 0;
C35: X2_4 >= 0;
C36: X3_2 >= 0;
C37: X3_4 >= 0;
C38: X4_5 >= 0;
C39: X5_6 >= 0;
C40: X7_6 >= 0;
C41: X8_1 >= 0;
C42: X8_2 >= 0;
C43: X8_7 >= 0;
C44: X9_2 >= 0;
C45: X9_8 >= 0;
C46: X9_10 >= 0;
C47: X10_2 >= 0;
C48: X10_3 >= 0;
