/*Função de minimo*/
min: 1 X11 + 2 X12 + 10000 X13 + 3 X14 + 1 X15 + 1 X21 + 3 X22 + 1 X23 + 10000 X24 + 2 X25 + 2 X31 + 1 X32 + 2 X33 + 2 X34 + 2 X35 + 1 X41 + 10000 X42 + 2 X43 + 2 X44 + 1 X45 + 3 X51 + 1 X52 + 1 X53 + 1 X54 + 1 X55 + 4 X61 + 1 X62 + 3 X63 + 3 X64 + 5 X65;

/*Limite de oferta*/
C1: X11 + X12 + X13 + X14 + X15 <= 2;

C2: X21 + X22 + X23 + X24 + X25 <= 4;

C3: X31 + X32 + X33 + X34 + X35 <= 3;

C4: X41 + X42 + X43 + X44 + X45 <= 4;

C5: X51 + X52 + X53 + X54 + X55 <= 5;

C6: X61 + X62 + X63 + X64 + X65 <= 2;

/*Limite de demanda*/
C7: X11 + X21 + X31 + X41 + X51 + X61 >= 6;

C8: X12 + X22 + X32 + X42 + X52 + X62 >= 4;

C9: X13 + X23 + X33 + X43 + X53 + X63 >= 2;

C10: X14 + X24 + X34 + X44 + X54 + X64 >= 3;

C11: X15 + X25 + X35 + X45 + X55 + X65 >= 2;

/*Nenhum transporte é menor que zero*/
C12: X11 >= 0;
C13: X12 >= 0;
C14: X13 >= 0;
C15: X14 >= 0;
C16: X15 >= 0;
C17: X21 >= 0;
C18: X22 >= 0;
C19: X23 >= 0;
C20: X24 >= 0;
C21: X25 >= 0;
C22: X31 >= 0;
C23: X32 >= 0;
C24: X33 >= 0;
C25: X34 >= 0;
C26: X35 >= 0;
C27: X41 >= 0;
C28: X42 >= 0;
C29: X43 >= 0;
C30: X44 >= 0;
C31: X45 >= 0;
C32: X51 >= 0;
C33: X52 >= 0;
C34: X53 >= 0;
C35: X54 >= 0;
C36: X55 >= 0;
C37: X61 >= 0;
C38: X62 >= 0;
C39: X63 >= 0;
C40: X64 >= 0;
C41: X65 >= 0;
/*Todos os transportes são inteiros*/
int X11;
int X12;
int X13;
int X14;
int X15;
int X21;
int X22;
int X23;
int X24;
int X25;
int X31;
int X32;
int X33;
int X34;
int X35;
int X41;
int X42;
int X43;
int X44;
int X45;
int X51;
int X52;
int X53;
int X54;
int X55;
int X61;
int X62;
int X63;
int X64;
int X65;
