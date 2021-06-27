/*Função de minimo*/
min: 85.3 X1_1 + 88 X1_2 + 87.5 X1_3 + 82.4 X1_4 + 89.1 X1_5 + 86.7 X1_6 + 78.9 X2_1 + 77.4 X2_2 + 77.4 X2_3 + 76.5 X2_4 + 79.3 X2_5 + 78.3 X2_6 + 82 X3_1 + 81.3 X3_2 + 82.4 X3_3 + 80.6 X3_4 + 83.5 X3_5 + 81.7 X3_6 + 84.3 X4_1 + 84.6 X4_2 + 86.2 X4_3 + 83.3 X4_4 + 84.4 X4_5 + 85.5 X4_6;

/*Todo restaurante tem uma contrutora*/
C1: X1_1 + X1_2 + X1_3 + X1_4 + X1_5 + X1_6 = 1;

C2: X2_1 + X2_2 + X2_3 + X2_4 + X2_5 + X2_6 = 1;

C3: X3_1 + X3_2 + X3_3 + X3_4 + X3_5 + X3_6 = 1;

C4: X4_1 + X4_2 + X4_3 + X4_4 + X4_5 + X4_6 = 1;

/*toda construtora possui o limite de 1*/
C5: X1_1 + X2_1 + X3_1 + X4_1 <= 1;

C6: X1_2 + X2_2 + X3_2 + X4_2 <= 1;

C7: X1_3 + X2_3 + X3_3 + X4_3 <= 1;

C8: X1_4 + X2_4 + X3_4 + X4_4 <= 1;

C9: X1_5 + X2_5 + X3_5 + X4_5 <= 1;

C10: X1_6 + X2_6 + X3_6 + X4_6 <= 1;

/*Ou foi contruido ou não*/
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
