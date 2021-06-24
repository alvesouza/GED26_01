/*Função de minimo*/
min: 85.3 X11 + 88 X12 + 87.5 X13 + 82.4 X14 + 89.1 X15 + 86.7 X16 + 78.9 X21 + 77.4 X22 + 77.4 X23 + 76.5 X24 + 79.3 X25 + 78.3 X26 + 82 X31 + 81.3 X32 + 82.4 X33 + 80.6 X34 + 83.5 X35 + 81.7 X36 + 84.3 X41 + 84.6 X42 + 86.2 X43 + 83.3 X44 + 84.4 X45 + 85.5 X46;

/*Todo restaurante tem uma contrutora*/
C1: X11 + X12 + X13 + X14 + X15 + X16 = 1;

C2: X21 + X22 + X23 + X24 + X25 + X26 = 1;

C3: X31 + X32 + X33 + X34 + X35 + X36 = 1;

C4: X41 + X42 + X43 + X44 + X45 + X46 = 1;

/*toda construtora possui o limite de 1*/
C5: X11 + X21 + X31 + X41 <= 1;

C6: X12 + X22 + X32 + X42 <= 1;

C7: X13 + X23 + X33 + X43 <= 1;

C8: X14 + X24 + X34 + X44 <= 1;

C9: X15 + X25 + X35 + X45 <= 1;

C10: X16 + X26 + X36 + X46 <= 1;

/*Ou foi contruido ou não*/
bin X11;
bin X12;
bin X13;
bin X14;
bin X15;
bin X16;
bin X21;
bin X22;
bin X23;
bin X24;
bin X25;
bin X26;
bin X31;
bin X32;
bin X33;
bin X34;
bin X35;
bin X36;
bin X41;
bin X42;
bin X43;
bin X44;
bin X45;
bin X46;
