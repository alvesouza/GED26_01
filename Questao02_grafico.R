# Title     : TODO
# Objective : TODO
# Created by: pedro
# Created on: 13/07/2021

library(ggplot2)
library(hrbrthemes)

data_frame<- data.frame(
  retorno = retornos,
  desvio_padrao = desvio_padroes
)

# Basic scatter plot.
p1 <- ggplot(data_frame, aes(x=retorno, y=desvio_padrao)) +
  geom_point( color="#69b3a2")

p1

# with linear trend
p2 <- ggplot(data_frame, aes(x=retorno, y=desvio_padrao)) +
  geom_point() +
  geom_smooth(method=lm , color="red", se=FALSE)

p2

# linear trend + confidence interval
p3 <- ggplot(data_frame, aes(x=retorno, y=desvio_padrao)) +
  geom_point() +
  geom_smooth(method=lm , color="red", fill="#69b3a2", se=TRUE)

p3