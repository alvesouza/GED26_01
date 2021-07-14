# Title     : TODO
# Objective : TODO
# Created by: pedro
# Created on: 13/07/2021

library(pracma)
C <- diag(1, 3); d <- rep(0, length(ativos) );#-c(0, 5, 0)
A_linha <- append( rep(1, length(ativos)), rep(0, length(ativos)*(length(ativos) - 1)), after = length(ativos) );
A <- matrix( A_linha, length(ativos), length(ativos), byrow=TRUE);
b <- append( 1, rep(0, length(ativos) - 1), after = 1 );#c(8, -2, 0)
step <- 0.0001;
ret <- 0.0005;
Aeq <- RetornoMed;
retornos <- c();
desvio_padroes <- c();
while ( ret < 0.0061 )
{
  beq <- ret;
  quad <- quadprog(2*covariancia, d, A, b, Aeq, beq, lb = 0);
  retornos <- append( retornos, ret, after = length(retornos));
  desvio_padroes <- append( desvio_padroes, quad$fval, after = length(desvio_padroes));
  ret <- ret + step;
}
quad
sum(quad$xmin)
t(quad$xmin)%*%RetornoMed