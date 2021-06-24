/*Função de custo com X sendo os unitarios e os y sendo os fixos*/
min: 0.81 XManacapuruPorto_Velho + 0.95 XManacapuruGoiania + 1.15 XManacapuruVitoria + 1.33 XManacapuruBetim + 1.2 XManacapuruNiteroi + 1.31 XManacapuruPonta_Grossa + 0.71 XPalmasPorto_Velho + 0.95 XPalmasGoiania + 1.1 XPalmasVitoria + 1.18 XPalmasBetim + 1.2 XPalmasNiteroi + 1.26 XPalmasPonta_Grossa + 1.34 XSalvadorPorto_Velho + 1.21 XSalvadorGoiania + 0.68 XSalvadorVitoria + 0.79 XSalvadorBetim + 0.89 XSalvadorNiteroi + 1.0 XSalvadorPonta_Grossa + 1.49 XGuarulhosPorto_Velho + 1.23 XGuarulhosGoiania + 0.95 XGuarulhosVitoria + 0.88 XGuarulhosBetim + 0.71 XGuarulhosNiteroi + 0.71 XGuarulhosPonta_Grossa + 1.6 XLondrinaPorto_Velho + 1.38 XLondrinaGoiania + 1.31 XLondrinaVitoria + 1.1 XLondrinaBetim + 1.0 XLondrinaNiteroi + 0.44 XLondrinaPonta_Grossa + 110000 YManacapuru + 121000 YPalmas + 133000 YSalvador + 144000 YGuarulhos + 135000 YLondrina;

/*Limite de oferta*/
C1: XManacapuruPorto_Velho + XManacapuruGoiania + XManacapuruVitoria + XManacapuruBetim + XManacapuruNiteroi + XManacapuruPonta_Grossa <= 380000 YManacapuru;

C2: XPalmasPorto_Velho + XPalmasGoiania + XPalmasVitoria + XPalmasBetim + XPalmasNiteroi + XPalmasPonta_Grossa <= 310000 YPalmas;

C3: XSalvadorPorto_Velho + XSalvadorGoiania + XSalvadorVitoria + XSalvadorBetim + XSalvadorNiteroi + XSalvadorPonta_Grossa <= 280000 YSalvador;

C4: XGuarulhosPorto_Velho + XGuarulhosGoiania + XGuarulhosVitoria + XGuarulhosBetim + XGuarulhosNiteroi + XGuarulhosPonta_Grossa <= 305000 YGuarulhos;

C5: XLondrinaPorto_Velho + XLondrinaGoiania + XLondrinaVitoria + XLondrinaBetim + XLondrinaNiteroi + XLondrinaPonta_Grossa <= 220000 YLondrina;

/*Satisfaz as demandas*/
C6: XManacapuruPorto_Velho + XPalmasPorto_Velho + XSalvadorPorto_Velho + XGuarulhosPorto_Velho + XLondrinaPorto_Velho >= 120000;

C7: XManacapuruGoiania + XPalmasGoiania + XSalvadorGoiania + XGuarulhosGoiania + XLondrinaGoiania >= 100000;

C8: XManacapuruVitoria + XPalmasVitoria + XSalvadorVitoria + XGuarulhosVitoria + XLondrinaVitoria >= 160000;

C9: XManacapuruBetim + XPalmasBetim + XSalvadorBetim + XGuarulhosBetim + XLondrinaBetim >= 130000;

C10: XManacapuruNiteroi + XPalmasNiteroi + XSalvadorNiteroi + XGuarulhosNiteroi + XLondrinaNiteroi >= 180000;

C11: XManacapuruPonta_Grossa + XPalmasPonta_Grossa + XSalvadorPonta_Grossa + XGuarulhosPonta_Grossa + XLondrinaPonta_Grossa >= 150000;

/*Todos os transportes são maior ou igual a zero*/
C12: XManacapuruPorto_Velho >= 0;
C13: XManacapuruGoiania >= 0;
C14: XManacapuruVitoria >= 0;
C15: XManacapuruBetim >= 0;
C16: XManacapuruNiteroi >= 0;
C17: XManacapuruPonta_Grossa >= 0;
C18: XPalmasPorto_Velho >= 0;
C19: XPalmasGoiania >= 0;
C20: XPalmasVitoria >= 0;
C21: XPalmasBetim >= 0;
C22: XPalmasNiteroi >= 0;
C23: XPalmasPonta_Grossa >= 0;
C24: XSalvadorPorto_Velho >= 0;
C25: XSalvadorGoiania >= 0;
C26: XSalvadorVitoria >= 0;
C27: XSalvadorBetim >= 0;
C28: XSalvadorNiteroi >= 0;
C29: XSalvadorPonta_Grossa >= 0;
C30: XGuarulhosPorto_Velho >= 0;
C31: XGuarulhosGoiania >= 0;
C32: XGuarulhosVitoria >= 0;
C33: XGuarulhosBetim >= 0;
C34: XGuarulhosNiteroi >= 0;
C35: XGuarulhosPonta_Grossa >= 0;
C36: XLondrinaPorto_Velho >= 0;
C37: XLondrinaGoiania >= 0;
C38: XLondrinaVitoria >= 0;
C39: XLondrinaBetim >= 0;
C40: XLondrinaNiteroi >= 0;
C41: XLondrinaPonta_Grossa >= 0;
bin YManacapuru;
bin YPalmas;
bin YSalvador;
bin YGuarulhos;
bin YLondrina;
