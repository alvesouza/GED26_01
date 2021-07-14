/*Função de custo com X sendo os unitarios e os y sendo os fixos*/
min: 0.81 XManacapuru_Porto_Velho + 0.95 XManacapuru_Goiania + 1.15 XManacapuru_Vitoria + 1.33 XManacapuru_Betim + 1.2 XManacapuru_Niteroi + 1.31 XManacapuru_Ponta_Grossa + 0.71 XPalmas_Porto_Velho + 0.95 XPalmas_Goiania + 1.1 XPalmas_Vitoria + 1.18 XPalmas_Betim + 1.2 XPalmas_Niteroi + 1.26 XPalmas_Ponta_Grossa + 1.34 XSalvador_Porto_Velho + 1.21 XSalvador_Goiania + 0.68 XSalvador_Vitoria + 0.79 XSalvador_Betim + 0.89 XSalvador_Niteroi + 1.0 XSalvador_Ponta_Grossa + 1.49 XGuarulhos_Porto_Velho + 1.23 XGuarulhos_Goiania + 0.95 XGuarulhos_Vitoria + 0.88 XGuarulhos_Betim + 0.71 XGuarulhos_Niteroi + 0.71 XGuarulhos_Ponta_Grossa + 1.6 XLondrina_Porto_Velho + 1.38 XLondrina_Goiania + 1.31 XLondrina_Vitoria + 1.1 XLondrina_Betim + 1.0 XLondrina_Niteroi + 0.44 XLondrina_Ponta_Grossa + 110000 YManacapuru + 121000 YPalmas + 133000 YSalvador + 144000 YGuarulhos + 135000 YLondrina;

/*Limite de oferta*/
C1: XManacapuru_Porto_Velho + XManacapuru_Goiania + XManacapuru_Vitoria + XManacapuru_Betim + XManacapuru_Niteroi + XManacapuru_Ponta_Grossa <= 380000 YManacapuru;

C2: XPalmas_Porto_Velho + XPalmas_Goiania + XPalmas_Vitoria + XPalmas_Betim + XPalmas_Niteroi + XPalmas_Ponta_Grossa <= 310000 YPalmas;

C3: XSalvador_Porto_Velho + XSalvador_Goiania + XSalvador_Vitoria + XSalvador_Betim + XSalvador_Niteroi + XSalvador_Ponta_Grossa <= 280000 YSalvador;

C4: XGuarulhos_Porto_Velho + XGuarulhos_Goiania + XGuarulhos_Vitoria + XGuarulhos_Betim + XGuarulhos_Niteroi + XGuarulhos_Ponta_Grossa <= 305000 YGuarulhos;

C5: XLondrina_Porto_Velho + XLondrina_Goiania + XLondrina_Vitoria + XLondrina_Betim + XLondrina_Niteroi + XLondrina_Ponta_Grossa <= 220000 YLondrina;

/*Satisfaz as demandas*/
C6: XManacapuru_Porto_Velho + XPalmas_Porto_Velho + XSalvador_Porto_Velho + XGuarulhos_Porto_Velho + XLondrina_Porto_Velho >= 120000;

C7: XManacapuru_Goiania + XPalmas_Goiania + XSalvador_Goiania + XGuarulhos_Goiania + XLondrina_Goiania >= 100000;

C8: XManacapuru_Vitoria + XPalmas_Vitoria + XSalvador_Vitoria + XGuarulhos_Vitoria + XLondrina_Vitoria >= 160000;

C9: XManacapuru_Betim + XPalmas_Betim + XSalvador_Betim + XGuarulhos_Betim + XLondrina_Betim >= 130000;

C10: XManacapuru_Niteroi + XPalmas_Niteroi + XSalvador_Niteroi + XGuarulhos_Niteroi + XLondrina_Niteroi >= 180000;

C11: XManacapuru_Ponta_Grossa + XPalmas_Ponta_Grossa + XSalvador_Ponta_Grossa + XGuarulhos_Ponta_Grossa + XLondrina_Ponta_Grossa >= 150000;

/*Todos os transportes são maior ou igual a zero*/
C12: XManacapuru_Porto_Velho >= 0;
C13: XManacapuru_Goiania >= 0;
C14: XManacapuru_Vitoria >= 0;
C15: XManacapuru_Betim >= 0;
C16: XManacapuru_Niteroi >= 0;
C17: XManacapuru_Ponta_Grossa >= 0;
C18: XPalmas_Porto_Velho >= 0;
C19: XPalmas_Goiania >= 0;
C20: XPalmas_Vitoria >= 0;
C21: XPalmas_Betim >= 0;
C22: XPalmas_Niteroi >= 0;
C23: XPalmas_Ponta_Grossa >= 0;
C24: XSalvador_Porto_Velho >= 0;
C25: XSalvador_Goiania >= 0;
C26: XSalvador_Vitoria >= 0;
C27: XSalvador_Betim >= 0;
C28: XSalvador_Niteroi >= 0;
C29: XSalvador_Ponta_Grossa >= 0;
C30: XGuarulhos_Porto_Velho >= 0;
C31: XGuarulhos_Goiania >= 0;
C32: XGuarulhos_Vitoria >= 0;
C33: XGuarulhos_Betim >= 0;
C34: XGuarulhos_Niteroi >= 0;
C35: XGuarulhos_Ponta_Grossa >= 0;
C36: XLondrina_Porto_Velho >= 0;
C37: XLondrina_Goiania >= 0;
C38: XLondrina_Vitoria >= 0;
C39: XLondrina_Betim >= 0;
C40: XLondrina_Niteroi >= 0;
C41: XLondrina_Ponta_Grossa >= 0;
bin YManacapuru;
bin YPalmas;
bin YSalvador;
bin YGuarulhos;
bin YLondrina;
