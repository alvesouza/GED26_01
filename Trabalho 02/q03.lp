/*Função do pagamento*/
min: 5 Xseg + 5.5 Xter + 6.5 Xqua + 6.5 Xqui + 6.5 Xsex + 6.5 Xsab + 6 Xdom;

/*Numero de funcionarios trabalhando nos dias*/
/*seg*/
C1: Xqui + Xsex + Xsab + Xdom + Xseg >= 17;

/*ter*/
C2: Xsex + Xsab + Xdom + Xseg + Xter >= 13;

/*qua*/
C3: Xsab + Xdom + Xseg + Xter + Xqua >= 15;

/*qui*/
C4: Xdom + Xseg + Xter + Xqua + Xqui >= 24;

/*sex*/
C5: Xseg + Xter + Xqua + Xqui + Xsex >= 14;

/*sab*/
C6: Xter + Xqua + Xqui + Xsex + Xsab >= 16;

/*dom*/
C7: Xqua + Xqui + Xsex + Xsab + Xdom >= 11;

/*Todos os dias que os funcionarios começam precisam ter um numero de funcionarios maior ou igual que zero*/
C8: Xseg >= 0;
C9: Xter >= 0;
C10: Xqua >= 0;
C11: Xqui >= 0;
C12: Xsex >= 0;
C13: Xsab >= 0;
C14: Xdom >= 0;
/*O numero de funcionario eh inteiro*/
int Xseg;
int Xter;
int Xqua;
int Xqui;
int Xsex;
int Xsab;
int Xdom;
