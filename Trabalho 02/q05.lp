/*Função de custo com X sendo os binarios, onde o seu valor é 1 quando o bairo possuir uma clinica*/
min: X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8 + X9 + X10 + X11 + X12;
/*Todas as cidades ou vão ter clinicas, ou vão estar a uma distancia menor que 5.3Km de distancia de uma*/
/*Para o bairro 1*/
C1: X1 + X2 + X9 + X12 >= 1;

/*Para o bairro 2*/
C2: X1 + X2 + X4 + X9 + X10 + X12 >= 1;

/*Para o bairro 3*/
C3: X3 + X4 + X5 + X10 + X11 >= 1;

/*Para o bairro 4*/
C4: X2 + X3 + X4 + X5 + X9 + X10 + X11 >= 1;

/*Para o bairro 5*/
C5: X3 + X4 + X5 + X10 + X11 + X12 >= 1;

/*Para o bairro 6*/
C6: X6 + X7 + X9 + X12 >= 1;

/*Para o bairro 7*/
C7: X6 + X7 + X8 + X9 + X11 + X12 >= 1;

/*Para o bairro 8*/
C8: X7 + X8 + X9 + X12 >= 1;

/*Para o bairro 9*/
C9: X1 + X2 + X4 + X6 + X7 + X8 + X9 + X10 + X12 >= 1;

/*Para o bairro 10*/
C10: X2 + X3 + X4 + X5 + X9 + X10 + X11 >= 1;

/*Para o bairro 11*/
C11: X3 + X4 + X5 + X7 + X10 + X11 + X12 >= 1;

/*Para o bairro 12*/
C12: X1 + X2 + X5 + X6 + X7 + X8 + X9 + X11 + X12 >= 1;

bin X1;
bin X2;
bin X3;
bin X4;
bin X5;
bin X6;
bin X7;
bin X8;
bin X9;
bin X10;
bin X11;
bin X12;
