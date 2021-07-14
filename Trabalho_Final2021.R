
#install.packages("BatchGetSymbols")
#install.packages("tidyverse")
#install.packages("ggplot2")
#install.packages("Amelia")
#install.packages("reshape2")
#install.packages("ggthemes")
#install.packages("plyr")
#install.packages("quadprog")

require(BatchGetSymbols)
require(tidyverse)
require(ggplot2)
require(Amelia)
require(reshape2)
require(ggthemes) 
require(plyr)

library(quadprog)

############# Baixando todos os dados do IBOV - Todas as a??es ###############

papeis = GetIbovStocks()$tickers # no caso do Bovespa

papeis

papeis = paste0(papeis,'.SA')


############ Baixando os dados de mais de 1 ativo   ############################

bg = '2021-03-11' #o per?odo inicial, geralmente ap?s os anos 2000
lst = Sys.Date()  #aqui coloquei a data de hoje, mas poderia ser qualquer outra
lst = '2021-06-11'
bench = '^BVSP' 
data = BatchGetSymbols(tickers = papeis,bench.ticker = bench,
       first.date = bg,last.date = lst) #comando que ir? baixar os 

tickers = papeis

data1=data$df.tickers
Dados=data1[complete.cases(data1),] # tirando os NA's


colnames(Dados)[1] = "Abertura"
colnames(Dados)[2] = "Maximo"
colnames(Dados)[3] = "Minimo"
colnames(Dados)[4] = "Fechamento"
colnames(Dados)[5] = "Volume"
colnames(Dados)[6] = "Fechamento_Ajustado"
colnames(Dados)[7] = "Data"
colnames(Dados)[8] = "Codigo"
colnames(Dados)[9] = "Retorno_Ajust"
colnames(Dados)[10] = "Retorno_Fecham"


######### Criando a matriz dos Fechamentos Diarios dos Ativos  ###########

vetaux=rep(NA,length(papeis)) ## Relacionado com os Codigos que de fato foram
## extraidos pela fun??o BatchGetSymbols

indaux=rep(NA,length(papeis)) ## Relacionado com os indices no vetor Dados em
## que as informacoes sobre um ativo terminam e comecam as informacoes de
## outro ativo

indaux[1]=1
vetaux[1]=Dados[1,8]
k=1
v=length(Dados[,8])
t=1

for (i in 1:(v-1)){
  
  if(Dados[(i+1),8]!=Dados[i,8]){
    k=k+1
    indaux[k]=i+1
    vetaux[k]=Dados[i+1,8] 
  }
  t=t+1
}
indaux=indaux[complete.cases(indaux)]

vetaux=vetaux[complete.cases(vetaux)]

## Gerando o vetor ndados, que cont?m as quantidades de dados v?lidos de
## cada ativo 

ndados=rep(NA,length(indaux))

for (i in 1:(length(indaux)-1)){
  ndados[i]=indaux[i+1]-indaux[i]
}

ndados[length(ndados)]=length(Dados[,8])-indaux[length(indaux)]+1



###############################################################################

## Gerando a Matriz MDadosFech, que contem todos os fechamentos di?rios, por 
## todo o per?odo considerado, sendo cada ativo em uma coluna da matriz.

papeis=vetaux

n=length(papeis)

Fech = Dados[,6] # Essa matriz contem todos os fechamentos de todos os ativos,
# empilhados, come?ando pela ABEV3.SA e terminando com YDUQ3.SA #

MDadosFech = matrix(NA,nrow = max(ndados), ncol = n) # Criando uma matriz vazia

for (i in 1:(n)){
  
  linf = indaux[i]
  
  for (j in 1:ndados[i]){
    
    MDadosFech[j,i]=Fech[linf+j-1]
   
  }
}

tail(MDadosFech)
colnames(MDadosFech)= papeis # Nomeando as colunas da Matriz MDadosFech

###############################################################################

## Gerando a Matriz MDadosRet, que contem todos os retornos di?rios, por todo o
## per?odo considerado, sendo cada ativo em uma coluna da matriz.

Ret = Dados[,10] # Essa matriz contem todos os retornos di?rios de todos os
# ativos, empilhados, come?ando pelo ABEV3.SA e terminando com YDUQ3.SA #

MDadosRet = matrix(0,nrow = max(ndados), ncol = n)  ## Criando uma matriz vazia

for (i in 1:(n)){
  
  linf = indaux[i]
  
  for (j in 1:ndados[i]){
    
    MDadosRet[j,i]=Ret[linf+j-1]
    
  }
}
MDadosRet
tail(MDadosRet)
colnames(MDadosRet)= papeis # Nomeando as colunas da Matriz MDadosFech

###############################################################################
# Escolha dos ativos que vao compor a carteira. Nesse codigo abaixo serio es- #
# colhidas as acoes que tiveram ao maior retorno m?dio no per?odo considerado #
###############################################################################

# OBS: voce esta livre para usar outro codigo que escolhe as acoes usando outro
# crit?rio que desejar. At? recomendo que voc? use seu pr?prio critario.

#### Calculando as medias de todos os retornos diarios para todos os ativos
RetornoMedTotal = colMeans(MDadosRet, na.rm=T) ## Desprezando os dados NA
RetornoMedTotal

RetornoMedTotalDecreas=sort(RetornoMedTotal, decreasing=TRUE) ## Coloca o vetor
## de retornos m?dios em ordem decrescente

ativos=names(RetornoMedTotalDecreas) ## Pega os nomes dos ativos em ordem
## decrescentes de retornos m?dios

nativos = 10  ## Estabelece o n?mero de ativos que v?o compor a carteira

ativos = ativos[1:nativos]  ## Escolhe somente os ativos com maiores retornos
## m?dios no per?odo considerado

Retornos = MDadosRet[,ativos]  ### Retornos apenas dos ativos de interesse


# Calculando as variancias e os desvios-padroes de dos retornos diarios para #
# todos os ativos

VarRet = rep(NA,nativos)

for (j in 1:nativos){
  
  VarRet[j]=var(Retornos[,j], na.rm=T)
  
}

DPRet = sqrt(VarRet)  ## Calcula o desvio padrao dos retornos relativos a cada
## um dos ativos considerados na composiçao da carteira


##############################################################################

covariancia

covariancia = cov(Retornos)

RetornoMed = colMeans(Retornos) ## Calcula os valores esperados dos retornos 
## relativos a cada um dos ativos considerados na composi??o da carteira

n = nativos

###### A partir desse ponto voc? pode fazer o seu codigo para fazer a aloca??o
###### de capital na sua carteira eficiente.
  



