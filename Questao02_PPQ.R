# Title     : TODO
# Objective : TODO
# Created by: pedro
# Created on: 11/07/2021
# Assume we want to minimize: 1/2 x^T x - (0 5 0) %*% x
# under the constraints:      A x <= b
# with b = (8,-2, 0)
# and      ( 4  3  0)
#      A = (-2 -1  0)
#          ( 0  2,-1)
# and possibly equality constraint  3x1 + 2x2 + x3 = 1
# or upper bound c(1.5, 1.5, 1.5).
library(pracma)
C <- diag(1, 3); d <- rep(0, length(ativos) );#-c(0, 5, 0)
#A_linha <- append( -RetornoMed, rep(0, length(ativos)*(length(ativos) - 1)), after = length(RetornoMed) );
A_linha <- append( rep(1, length(ativos)), rep(0, length(ativos)*(length(ativos) - 1)), after = length(ativos) );
A <- matrix( A_linha, length(ativos), length(ativos), byrow=TRUE);
ret <- 0.005;
b <- append( 1, rep(0, length(ativos) - 1), after = 1 );#c(8, -2, 0)

#Aeq <- rep(1, length(ativos) );  beq <- 1;
Aeq <- RetornoMed;  beq <- ret;
quad <- quadprog(2*covariancia, d, A, b, Aeq, beq, lb = 0)
#covariancia[,10]
quad
sum(quad$xmin)
t(quad$xmin)%*%RetornoMed