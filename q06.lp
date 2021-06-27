/*Função de custo com X sendo os binarios e seu valor é 1 quando o bairo possuir uma clinic*/
min: 235 X1_2 + 415 X1_3 + 301 X1_4 + 190 X1_5 + 300 X1_6 + 235 X2_1 + 350 X2_3 + 300 X2_4 + 301 X2_5 + 280 X2_6 + 415 X3_1 + 350 X3_2 + 290 X3_4 + 340 X3_5 + 420 X3_6 + 301 X4_1 + 300 X4_2 + 290 X4_3 + 180 X4_5 + 280 X4_6 + 190 X5_1 + 301 X5_2 + 340 X5_3 + 180 X5_4 + 400 X5_6 + 300 X6_1 + 280 X6_2 + 420 X6_3 + 280 X6_4 + 400 X6_5;
/*Ele vai sair de todas as cidades e a variavle Xij se for 1, significa que saiu de i e foi para j*/
/*Para a cidade 1*/
C1: X1_1 + X1_2 + X1_3 + X1_4 + X1_5 + X1_6 = 1;

/*Para a cidade 2*/
C2: X2_1 + X2_2 + X2_3 + X2_4 + X2_5 + X2_6 = 1;

/*Para a cidade 3*/
C3: X3_1 + X3_2 + X3_3 + X3_4 + X3_5 + X3_6 = 1;

/*Para a cidade 4*/
C4: X4_1 + X4_2 + X4_3 + X4_4 + X4_5 + X4_6 = 1;

/*Para a cidade 5*/
C5: X5_1 + X5_2 + X5_3 + X5_4 + X5_5 + X5_6 = 1;

/*Para a cidade 6*/
C6: X6_1 + X6_2 + X6_3 + X6_4 + X6_5 + X6_6 = 1;

/*Ele vai entrar em todas as cidades e a variavle Xij se for 1, significa que saiu de i e foi para j*/
/*Para a cidade 1*/
C7: X1_1 + X2_1 + X3_1 + X4_1 + X5_1 + X6_1 = 1;

/*Para a cidade 2*/
C8: X1_2 + X2_2 + X3_2 + X4_2 + X5_2 + X6_2 = 1;

/*Para a cidade 3*/
C9: X1_3 + X2_3 + X3_3 + X4_3 + X5_3 + X6_3 = 1;

/*Para a cidade 4*/
C10: X1_4 + X2_4 + X3_4 + X4_4 + X5_4 + X6_4 = 1;

/*Para a cidade 5*/
C11: X1_5 + X2_5 + X3_5 + X4_5 + X5_5 + X6_5 = 1;

/*Para a cidade 6*/
C12: X1_6 + X2_6 + X3_6 + X4_6 + X5_6 + X6_6 = 1;

/*Proibir ciclos de percusso*/
/*Proibir ciclos de tamanho 2*/
C13: X1_2 + X2_1 <= 1;
C14: X1_3 + X3_1 <= 1;
C15: X1_4 + X4_1 <= 1;
C16: X1_5 + X5_1 <= 1;
C17: X1_6 + X6_1 <= 1;
C18: X2_3 + X3_2 <= 1;
C19: X2_4 + X4_2 <= 1;
C20: X2_5 + X5_2 <= 1;
C21: X2_6 + X6_2 <= 1;
C22: X3_4 + X4_3 <= 1;
C23: X3_5 + X5_3 <= 1;
C24: X3_6 + X6_3 <= 1;
C25: X4_5 + X5_4 <= 1;
C26: X4_6 + X6_4 <= 1;
C27: X5_6 + X6_5 <= 1;
/*Proibir ciclos de tamanho 3*/
C28: X1_2 + X2_3 + X3_1 <= 2;
C29: X1_2 + X2_4 + X4_1 <= 2;
C30: X1_2 + X2_5 + X5_1 <= 2;
C31: X1_2 + X2_6 + X6_1 <= 2;
C32: X1_3 + X3_4 + X4_1 <= 2;
C33: X1_3 + X3_5 + X5_1 <= 2;
C34: X1_3 + X3_6 + X6_1 <= 2;
C35: X1_4 + X4_5 + X5_1 <= 2;
C36: X1_4 + X4_6 + X6_1 <= 2;
C37: X1_5 + X5_6 + X6_1 <= 2;
C38: X2_3 + X3_4 + X4_2 <= 2;
C39: X2_3 + X3_5 + X5_2 <= 2;
C40: X2_3 + X3_6 + X6_2 <= 2;
C41: X2_4 + X4_5 + X5_2 <= 2;
C42: X2_4 + X4_6 + X6_2 <= 2;
C43: X2_5 + X5_6 + X6_2 <= 2;
C44: X3_4 + X4_5 + X5_3 <= 2;
C45: X3_4 + X4_6 + X6_3 <= 2;
C46: X3_5 + X5_6 + X6_3 <= 2;
C47: X4_5 + X5_6 + X6_4 <= 2;
/*Proibir ciclos de tamanho 4*/
C48: X1_2 + X2_3 + X3_4 + X4_1 <= 3;
C49: X1_2 + X2_3 + X3_5 + X5_1 <= 3;
C50: X1_2 + X2_3 + X3_6 + X6_1 <= 3;
C51: X1_2 + X2_4 + X4_5 + X5_1 <= 3;
C52: X1_2 + X2_4 + X4_6 + X6_1 <= 3;
C53: X1_2 + X2_5 + X5_6 + X6_1 <= 3;
C54: X1_3 + X3_4 + X4_5 + X5_1 <= 3;
C55: X1_3 + X3_4 + X4_6 + X6_1 <= 3;
C56: X1_3 + X3_5 + X5_6 + X6_1 <= 3;
C57: X1_4 + X4_5 + X5_6 + X6_1 <= 3;
C58: X2_3 + X3_4 + X4_5 + X5_2 <= 3;
C59: X2_3 + X3_4 + X4_6 + X6_2 <= 3;
C60: X2_3 + X3_5 + X5_6 + X6_2 <= 3;
C61: X2_4 + X4_5 + X5_6 + X6_2 <= 3;
C62: X3_4 + X4_5 + X5_6 + X6_3 <= 3;
/*Proibir ciclos de tamanho 5*/
C63: X1_2 + X2_3 + X3_4 + X4_5 + X5_1 <= 4;
C64: X1_2 + X2_3 + X3_4 + X4_6 + X6_1 <= 4;
C65: X1_2 + X2_3 + X3_5 + X5_6 + X6_1 <= 4;
C66: X1_2 + X2_4 + X4_5 + X5_6 + X6_1 <= 4;
C67: X1_3 + X3_4 + X4_5 + X5_6 + X6_1 <= 4;
C68: X2_3 + X3_4 + X4_5 + X5_6 + X6_2 <= 4;
/*Xij se for 1, significa que saiu de i e foi para j, e todos Xii = 0*/
C69: X1_1 = 0;
C70: X2_2 = 0;
C71: X3_3 = 0;
C72: X4_4 = 0;
C73: X5_5 = 0;
C74: X6_6 = 0;
/*Xij se for 1, significa que saiu de i e foi para j, ou seja, eles só podem ser 0 ou 1*/
bin X1_1;
bin X1_2;
bin X1_3;
bin X1_4;
bin X1_5;
bin X1_6;
bin X2_1;
bin X2_2;
bin X2_3;
bin X2_4;
bin X2_5;
bin X2_6;
bin X3_1;
bin X3_2;
bin X3_3;
bin X3_4;
bin X3_5;
bin X3_6;
bin X4_1;
bin X4_2;
bin X4_3;
bin X4_4;
bin X4_5;
bin X4_6;
bin X5_1;
bin X5_2;
bin X5_3;
bin X5_4;
bin X5_5;
bin X5_6;
bin X6_1;
bin X6_2;
bin X6_3;
bin X6_4;
bin X6_5;
bin X6_6;
