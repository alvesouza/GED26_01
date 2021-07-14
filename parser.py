
class Obra:
    def __init__(self, nome, ct, dp, ea, manaus, belem):
        self.nome = nome
        self.ct = ct
        self.ea = ea
        self.dp = dp
        self.custo = [ manaus*0.175, belem*0.175]

    def NC(self):
        CT = self.ct
        EA = self.ea
        DP = self.dp

        return -0.000209*CT*EA*EA + 0.00508*CT*EA - 0.015*DP*EA + 14.1*DP - 129.6

    def passa_mes(self):
        self.ea += 1

def trabalho01():
    Obras_Letras = ["A", "B", "C", "D", "E"]
    Obras_Listas = [
        Obra("A", 1900, 24, 4, 390, 700),
        Obra("B", 3100, 36, 22, 420, 530),
        Obra("C", 2900, 24, 10, 510, 245),
        Obra("D", 3700, 30, 24, 690, 810),
        Obra("E", 2500, 28, 16, 550, 390),
    ]
    Centros_Distribuicao = ["MANAUS", "BELEM"]
    Estoque_Inicial = [600, 800]
    Estoque_Max = [2000, 1500]

    Central = "Central"
    Estoque_Inicial_Central = 5500
    constraint = 1

    Mes_Final = 4

    print("min:", end=' ')
    for obra_index in range(len(Obras_Listas)):
        for mes in range(1, Mes_Final + 1):
            for centro_index in range(len(Centros_Distribuicao)):
                obra = Obras_Listas[obra_index]
                print("{0:.3f} X{1}{2}{3}".format(obra.custo[centro_index],
                                                  Centros_Distribuicao[centro_index],
                                                  mes,
                                                  obra.nome,
                                                  ), end="")

                if not (centro_index + 1 == len(Centros_Distribuicao) and mes == Mes_Final and obra_index + 1 == len(
                        Obras_Listas)):
                    print(" +", end="")
    print(";\n")

    print("/*Estoque da Central de Compras não pode ficar menos que 0*/")

    # for mes_fim in range(1, Mes_Final + 1):
    print("C{0}: ".format(constraint), end="")
    constraint += 1
    for mes in range(1, Mes_Final + 1):
        for centro_index in range(len(Centros_Distribuicao)):
            print(" X{0}{1}{2} ".format(
                Central,
                mes,
                Centros_Distribuicao[centro_index]
            ), end="")
            if not (centro_index + 1 == len(Centros_Distribuicao) and mes == Mes_Final):
                print("+", end="")
    print(" <= ", Estoque_Inicial_Central - 0, end=";\n")

    print("\n/*Estoques dos Centros de distribuição não podem ficar acima do limite*/")
    for centro_index in range(len(Centros_Distribuicao)):
        for mes_fim in range(1, Mes_Final + 1):
            print("C{0}: ".format(constraint), end="")
            constraint += 1
            for mes in range(1, mes_fim + 1):
                if not (mes == 1):
                    print("+", end="")
                print(" X{0}{1}{2} ".format(
                    Central,
                    mes,
                    Centros_Distribuicao[centro_index]
                ), end="")
                for obra_index in range(len(Obras_Listas)):
                    obra = Obras_Listas[obra_index]
                    print("- X{0}{1}{2} ".format(
                        Centros_Distribuicao[centro_index],
                        mes,
                        obra.nome,
                    ), end="")
            print(" <= ", Estoque_Max[centro_index] - Estoque_Inicial[centro_index], end=";\n")
        print("")

    print("\n/*Estoques dos Centros de distribuição não podem ficar abaixo do limite*/")
    for centro_index in range(len(Centros_Distribuicao)):
        for mes_fim in range(1, Mes_Final + 1):
            print("C{0}: ".format(constraint), end="")
            constraint += 1
            for mes in range(1, mes_fim + 1):
                if not (mes == 1):
                    print("+", end="")
                print(" X{0}{1}{2} ".format(
                    Central,
                    mes,
                    Centros_Distribuicao[centro_index]
                ), end="")
                for obra_index in range(len(Obras_Listas)):
                    obra = Obras_Listas[obra_index]
                    print("- X{0}{1}{2} ".format(
                        Centros_Distribuicao[centro_index],
                        mes,
                        obra.nome,
                    ), end="")
            print(" >= ", -Estoque_Inicial[centro_index] + 0, end=";\n")
        print("")

    print("/*Todos os meses as demandas de Cimento serão satisfeitas*/")
    for mes in range(1, Mes_Final + 1):
        for obra_index in range(len(Obras_Listas)):
            obra = Obras_Listas[obra_index]
            print("C{0}:".format(constraint), end="")
            constraint += 1
            for centro_index in range(len(Centros_Distribuicao)):
                print(" X{1}{2}{3} ".format(
                    constraint,
                    Centros_Distribuicao[centro_index],
                    mes,
                    obra.nome,
                ), end="")
                if centro_index + 1 < len(Centros_Distribuicao):
                    print("+", end="")
            print(">= {0:.5f};".format(obra.NC()))
            obra.passa_mes()
        print("")

    print("/*Toda distribuição é maior ou igual à zero*/")
    for mes in range(1, Mes_Final + 1):
        for centro_index in range(len(Centros_Distribuicao)):
            print("C{3}: X{0}{1}{2} >= 0".format(
                Central,
                mes,
                Centros_Distribuicao[centro_index],
                constraint
            ), end=";\n")
            constraint += 1
        for centro_index in range(len(Centros_Distribuicao)):
            for obra_index in range(len(Obras_Listas)):
                obra = Obras_Listas[obra_index]
                print("C{0}: X{1}{2}{3} >= 0".format(
                    constraint,
                    Centros_Distribuicao[centro_index],
                    mes,
                    obra.nome,
                ), end=";\n")
                constraint += 1

def trabalho02_01():
    x = 10000
    a = [2, 4, 3, 4, 5, 2]
    b = [6, 4, 2, 3, 2]
    C = [
        [1, 2, x, 3, 1],
        [1, 3, 1, x, 2],
        [2, 1, 2, 2, 2],
        [1, x, 2, 2, 1],
        [3, 1, 1, 1, 1],
        [4, 1, 3, 3, 5]
    ]

    print("/*Função de minimo*/")
    print("min:", end=' ')
    for i in range(1, len(a) + 1 ):
        for j in range(1, len(b) + 1):
            print("{0} X{1}_{2}".format( C[i-1][j-1], i, j), end="")
            if j != len(b) or i != len(a):
                print(" + ", end="")
    print(";", end="\n\n")

    constraint = 1
    print("/*Limite de oferta*/")
    for i in range(1, len(a) + 1):
        print("C{0}:".format(constraint), end=' ')
        constraint += 1
        for j in range(1, len(b) + 1):
            print("X{0}_{1}".format(i, j), end="")
            if j != len(b):
                print(" + ", end="")
            else:
                print(" <= {0};".format(a[i-1]), end="")
        print("", end="\n\n")

    print("/*Limite de demanda*/")
    for j in range(1, len(b) + 1):
        print("C{0}:".format(constraint), end=' ')
        constraint += 1
        for i in range(1, len(a) + 1):
            print("X{0}_{1}".format(i, j), end="")
            if i != len(a):
                print(" + ", end="")
            else:
                print(" >= {0};".format(b[j - 1]), end="")
        print("", end="\n\n")

    print("/*Nenhum transporte é menor que zero*/")
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            print("C{0}: X{1}_{2} >= 0;".format( constraint, i, j))
            constraint += 1

    print("/*Todos os transportes são inteiros*/")
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            print("int X{1}_{2};".format(constraint, i, j))
            constraint += 1

def trabalho02_02():
    x = 10000
    a = [1, 1, 1, 1]
    b = [1, 1, 1, 1, 1, 1]
    C = [
        [85.3, 88, 87.5, 82.4, 89.1, 86.7],
        [78.9, 77.4, 77.4, 76.5, 79.3, 78.3],
        [82, 81.3, 82.4, 80.6, 83.5, 81.7],
        [84.3, 84.6, 86.2, 83.3, 84.4, 85.5]
    ]

    print("/*Função de minimo*/")
    print("min:", end=' ')
    for i in range(1, len(a) + 1 ):
        for j in range(1, len(b) + 1):
            print("{0} X{1}_{2}".format( C[i-1][j-1], i, j), end="")
            if j != len(b) or i != len(a):
                print(" + ", end="")
    print(";", end="\n\n")

    constraint = 1
    print("/*Todo restaurante tem uma contrutora*/")
    for i in range(1, len(a) + 1):
        print("C{0}:".format(constraint), end=' ')
        constraint += 1
        for j in range(1, len(b) + 1):
            print("X{0}_{1}".format(i, j), end="")
            if j != len(b):
                print(" + ", end="")
            else:
                print(" = {0};".format(a[i-1]), end="")
        print("", end="\n\n")

    print("/*toda construtora possui o limite de 1*/")
    for j in range(1, len(b) + 1):
        print("C{0}:".format(constraint), end=' ')
        constraint += 1
        for i in range(1, len(a) + 1):
            print("X{0}_{1}".format(i, j), end="")
            if i != len(a):
                print(" + ", end="")
            else:
                print(" <= {0};".format(b[j - 1]), end="")
        print("", end="\n\n")

    print("/*Ou foi contruido ou não*/")
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            print("bin X{1}_{2};".format(constraint, i, j))
            constraint += 1

def trabalho02_03():

    demanda_func = [ 17, 13, 15, 24, 14, 16, 11]
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
    pagamento = [1, 1, 1, 1, 1, 1.5, 2]

    print("/*Função do pagamento*/")
    print("min:", end=' ')
    for i in range(7):
        custo = 0
        j = 0
        while j < 5:
            custo += pagamento[(i + j)%7]
            j += 1

        print("{0} X{1}".format(custo, dias[i]), end="")
        if i != 6:
            print(" + ", end="")
    print(";", end="\n\n")

    constraint = 1
    print("/*Numero de funcionarios trabalhando nos dias*/")
    for i in range(7):
        print("/*{0}*/".format(dias[i]))
        custo = 0
        dias_trabalhador = i - 4
        if dias_trabalhador < 0:
            dias_trabalhador += 7
        j = 0
        print("C{0}:".format(constraint), end=' ')
        constraint += 1
        while j < 5:
            print("X{0}".format(dias[(dias_trabalhador + j)%7]), end="")
            j += 1
            if j != 5:
                print(" + ", end="")
        print(" >= {0};".format(demanda_func[i]), end="\n\n")

    print("/*Todos os dias que os funcionarios começam precisam ter um numero de funcionarios maior ou igual que zero*/")
    for i in range(7):
        print("C{0}: X{1} >= 0;".format( constraint, dias[i]))
        constraint += 1

    print("/*O numero de funcionario eh inteiro*/")
    for i in range(7):
        print("int X{0};".format(dias[i]))
        constraint += 1

def trabalho02_04():
    cidades_recebem = ["Porto_Velho", "Goiania", "Vitoria", "Betim", "Niteroi", "Ponta_Grossa"]
    demandas = [120000, 100000, 160000, 130000, 180000, 150000]

    cidades_depositos = ["Manacapuru", "Palmas", "Salvador", "Guarulhos", "Londrina"]
    custo_fixo = [ 110000, 121000, 133000, 144000, 135000]
    capacidade = [ 380000, 310000, 280000, 305000, 220000]
    custo_unit = [
        [0.81, 0.95, 1.15, 1.33, 1.2, 1.31],
        [0.71, 0.95, 1.10, 1.18, 1.20, 1.26],
        [1.34, 1.21, 0.68, 0.79, 0.89, 1.00],
        [1.49, 1.23, 0.95, 0.88, 0.71, 0.71],
        [1.60, 1.38, 1.31, 1.10, 1.00, 0.44]
    ]

    print("/*Função de custo com X sendo os unitarios e os y sendo os fixos*/")
    print("min:", end=' ')
    for i in range(len(cidades_depositos)):
        for j in range(len(cidades_recebem)):
            print("{0} X{1}_{2}".format(custo_unit[i][j], cidades_depositos[i], cidades_recebem[j] ), end="")
            print(" + ", end="")

    for i in range(len(cidades_depositos)):
        print("{0} Y{1}".format(custo_fixo[i], cidades_depositos[i]), end="")
        if i + 1 != len(cidades_depositos):
            print(" + ", end="")
    print(";", end="\n\n")

    constraint = 1
    print("/*Limite de oferta*/")
    for i in range(len(cidades_depositos)):
        print("C{0}:".format(constraint), end=' ')
        constraint += 1
        for j in range(len(cidades_recebem)):
            print("X{0}_{1}".format(cidades_depositos[i], cidades_recebem[j]), end="")
            if j + 1 != len(cidades_recebem):
                print(" + ", end="")
            else:
                print(" <= {0} Y{1};".format(capacidade[i], cidades_depositos[i]), end="")
        print("", end="\n\n")

    print("/*Satisfaz as demandas*/")
    for j in range(len(cidades_recebem)):
        print("C{0}:".format(constraint), end=' ')
        constraint += 1
        for i in range(len(cidades_depositos)):
            print("X{0}_{1}".format(cidades_depositos[i], cidades_recebem[j]), end="")
            if i + 1 != len(cidades_depositos):
                print(" + ", end="")
            else:
                print(" >= {0};".format(demandas[j]), end="")
        print("", end="\n\n")

    print("/*Todos os transportes são maior ou igual a zero*/")
    for i in range(len(cidades_depositos)):
        for j in range(len(cidades_recebem)):
            print("C{0}: X{1}_{2} >= 0;".format(constraint, cidades_depositos[i], cidades_recebem[j]))
            constraint += 1

    for i in range(len(cidades_depositos)):
        print("bin Y{1};".format(custo_fixo[i], cidades_depositos[i]))

def trabalho02_05():
    populacao = [20000, 15000, 18000, 35000, 18000, 23000, 31000, 8000, 13000, 21000, 17500, 26000]
    max_distancia = 5.3
    D = [
        [0, 3, 9.3, 7.7, 10.2, 7.3, 7, 6.6, 2.6, 6.6, 8.3, 5.1],
        [3, 0, 6.3, 4.7, 7.5, 6.5, 6.2, 5.8, 1.8, 3.6, 7.5, 4.3],
        [9.3, 6.3, 0, 1.6, 4.4, 9.8, 9.7, 10.8, 6.8, 2.7, 4.6, 7.8],
        [7.7, 4.7, 1.6, 0, 2.8, 8.2, 8.1, 9.2, 5.2, 1.1, 3, 6.2],
        [10.2, 7.5, 4.4, 2.8, 0, 5.4, 7.0, 8.9, 7.6, 3.9, 1.9, 5.1],
        [7.3, 6.5, 9.8, 8.2, 5.4, 0, 4.1, 6, 4.7, 8.8, 5.4, 2.2],
        [7, 6.2, 9.7, 8.1, 7, 4.1, 0, 5.3, 4.4, 8.5, 5.1, 1.9],
        [6.6, 5.8, 10.8, 9.2, 8.9, 6, 5.3, 0, 4, 8.1, 7, 3.8],
        [2.6, 1.8, 6.8, 5.2, 7.6, 4.7, 4.4, 4, 0, 4.1, 5.7, 2.5],
        [6.6, 3.6, 2.7, 1.1, 3.9, 8.8, 8.5, 8.1, 4.1, 0, 4, 6.6],
        [8.3, 7.5, 4.6, 3, 1.9, 5.4, 5.1, 7, 5.7, 4, 0, 3.2],
        [5.1, 4.3, 7.8, 6.2, 5.1, 2.2, 1.9, 3.8, 2.5, 6.6, 3.2, 0]
    ]

    D_allow = []
    for i in range(len(D)):
        d_new = []
        for j in range(len(D[i])):
            if D[i][j] <= max_distancia:
                d_new.append(j)

        D_allow.append(d_new)
    #print(D_allow)

    print("/*Função de custo com X sendo os binarios, onde o seu valor é 1 quando o bairo possuir uma clinica*/")
    print("min:", end=' ')
    for i in range(len(D_allow)):
        print("X{0}".format( i + 1 ), end="")
        if i + 1 != len(D_allow):
            print(" + ", end="")
    print(";")

    constraint = 1
    print("/*Todas as cidades ou vão ter clinicas, ou vão estar a uma distancia menor que {0}Km de distancia de uma*/".format(max_distancia))
    for i in range(len(D_allow)):
        print("/*Para o bairro {0}*/".format(i + 1))
        print("C{0}:".format(constraint), end=' ')
        constraint += 1
        for j in range(len(D_allow[i])):
            print("X{0}".format(D_allow[i][j] + 1), end="")
            if j + 1 != len(D_allow[i]):
                print(" + ", end="")
            else:
                print(" >= 1;", end="")
        print("", end="\n\n")

    for i in range(len(D_allow)):
        print("bin X{0};".format(i+1))

def find_cicles(route_now = [0], size_cicle = 2, num_cities = 12):
    routes = []
    if len(route_now) == size_cicle:
        #for i in range(num_cities):
        #    if i in route_now:
        #        continue
        new_route = route_now.copy()
        new_route.append(route_now[0])
        routes.append(new_route)
    else:
        for i in range(num_cities):
            if i in route_now or (len(route_now) > 1 and i < route_now[len(route_now) - 1]) or i < route_now[len(route_now) - 1]:
                continue
            new_route = route_now.copy()
            new_route.append(i)
            aux_routes = find_cicles(new_route, size_cicle, num_cities)
            for j in range(len(aux_routes)):
                routes.append(aux_routes[j])
    return routes


def trabalho02_06():
    D = [
        [0, 235, 415, 301, 190, 300],#1
        [235, 0, 350, 300, 301, 280],#2
        [415, 350, 0, 290, 340, 420],#3
        [301, 300, 290, 0, 180, 280],#4
        [190, 301, 340, 180, 0, 400],#5
        [300, 280, 420, 280, 400, 0],#6
    ]

    print("/*Função de custo com X sendo os binarios e seu valor é 1 quando o bairo possuir uma clinic*/")
    print("min:", end=' ')
    for i in range(len(D)):
        for j in range(len(D)):
            if i == j:
                continue
            print("{0} X{1}_{2}".format(D[i][j], i + 1, j + 1), end="")
            if i + 1 != len(D) or j + 2 != len(D):
                print(" + ", end="")
    print(";")

    constraint = 1
    print("/*Ele vai sair de todas as cidades e a variavle Xij se for 1, significa que saiu de i e foi para j*/")
    for i in range(len(D)):
        print("/*Para a cidade {0}*/".format(i + 1))
        print("C{0}:".format(constraint), end=' ')
        constraint += 1
        for j in range(len(D[i])):
            print("X{0}_{1}".format(i + 1, j + 1), end="")
            if j + 1 != len(D[i]):
                print(" + ", end="")
            else:
                print(" = 1;", end="")
        print("", end="\n\n")

    print("/*Ele vai entrar em todas as cidades e a variavle Xij se for 1, significa que saiu de i e foi para j*/")
    for i in range(len(D)):
        print("/*Para a cidade {0}*/".format(i + 1))
        print("C{0}:".format(constraint), end=' ')
        constraint += 1
        for j in range(len(D[i])):
            print("X{0}_{1}".format(j + 1, i + 1), end="")
            if j + 1 != len(D[i]):
                print(" + ", end="")
            else:
                print(" = 1;", end="")
        print("", end="\n\n")

    print("/*Proibir ciclos de percusso*/")
    num_ciclos = 2
    size_max = len(D)
    while num_ciclos < size_max:
        print("/*Proibir ciclos de tamanho {0}*/".format(num_ciclos))
        for i in range(len(D)):
            list_cicles = find_cicles([i], num_ciclos, len(D))
            for j in range(len(list_cicles)):
                cicle = list_cicles[j]
                print("C{0}: ".format(constraint), end="")
                constraint += 1
                size_cicle = len(cicle) - 1
                for index in range(size_cicle):
                    print("X{0}_{1}".format(cicle[index] + 1, cicle[index + 1] + 1), end="")
                    if index + 1 != size_cicle:
                        print(" + ", end="")
                    else:
                        print(" <= {0};".format(num_ciclos - 1))
        num_ciclos += 1

    print("/*Xij se for 1, significa que saiu de i e foi para j, e todos Xii = 0*/")
    for i in range(len(D)):
        print("C{0}: X{1}_{1} = 0;".format(constraint, i + 1))
        constraint += 1

    print("/*Xij se for 1, significa que saiu de i e foi para j, ou seja, eles só podem ser 0 ou 1*/")
    for i in range(len(D)):
        for j in range(len(D)):
            print("bin X{0}_{1};".format(i + 1, j + 1))

def trabalho02_07():
    fluxo_to_max = 6
    fluxo_from = [9]
    Manda_IDs = [
        [2, 4, 5, 6, 7],#1
        [3, 4],#2
        [2, 4],#3
        [5],#4
        [6],#5
        [],#6
        [6],#7
        [1, 2, 7],#8
        [2, 8, 10],#9
        [2, 3],#10
    ]
    Recebe_IDs = []
    for i in range(len(Manda_IDs)):
        Recebe_IDs.append([])

    for i in range(len(Manda_IDs)):
        for id in Manda_IDs[i]:
            Recebe_IDs[id-1].append(i+1)

    #print(Recebe_IDs)
    Max = [
        [10, 20, 20, 5, 15],#1
        [5, 10],#2
        [15, 5],#3
        [10],#4
        [5],#5
        [],#6
        [10],#7
        [5, 20, 5],#8
        [15, 20, 10],#9
        [5, 15],#10
    ]

    print("/*Funcao para maximizar o fluxo para o {0}*/".format(fluxo_to_max))
    print("max:", end=' ')
    recebe_list = Recebe_IDs[fluxo_to_max-1]
    for i in range(len(recebe_list)):
        print("X{0}_{1}".format( recebe_list[i], fluxo_to_max), end="")
        if i + 1 != len(recebe_list):
            print(" + ", end="")
    print(";")

    constraint = 1
    print("/*Equações dos fluxos para as respectivas cidades, onde os que estão apenas fazendo a transferencia, a varição deve ser zero*/")
    print("/*Cidade com o fluxo a se maximizar é {0} e saida é {1}*/".format(fluxo_to_max, fluxo_from[0]))
    for i in range(len(Max)):
        if i + 1 == fluxo_to_max or (i+1) in fluxo_from:
            continue
        print("/*Fluxo da cidade {0}*/".format(i + 1))
        print("C{0}:".format(constraint), end=' ')
        constraint += 1
        recebe_list = Recebe_IDs[i]
        for j in range(len(recebe_list)):
            print("X{0}_{1}".format(recebe_list[j], i + 1), end="")
            if j + 1 != len(recebe_list):
                print(" + ", end="")
            #else:
            #    print(" = 1;", end="")
        manda_list = Manda_IDs[i]
        for j in range(len(manda_list)):
            print(" - X{0}_{1}".format(i + 1, manda_list[j]), end="")
        print(" = 0;", end="\n\n")

    print("/*nenhum fluxo vai passar do maximo*/")
    for i in range(len(Max)):
        max_list = Max[i]
        manda_list = Manda_IDs[i]
        for j in range(len(max_list)):
            print("C{0}: X{1}_{2} <= {3};".format(
                constraint,
                i + 1,
                manda_list[j],
                max_list[j]
            ))
            constraint += 1

    print("/*nenhum fluxo vai ser menor que zero*/")
    for i in range(len(Max)):
        max_list = Max[i]
        manda_list = Manda_IDs[i]
        for j in range(len(max_list)):
            print("C{0}: X{1}_{2} >= 0;".format(
                constraint,
                i + 1,
                manda_list[j],
            ))
            constraint += 1
import collections
def already_equivalent( All_Collections, new_collection):
    for collection in All_Collections:
        if collection == new_collection:
            return True
    return False

def find_cicles_2(route_now = [0], size_cicle = 2, Manda_IDs = []):
    num_cidades = len(Manda_IDs)
    All_Collections = []
    routes = []
    list_cities = Manda_IDs[route_now[len(route_now)-1]]
    if len(route_now) == size_cicle:
        #for i in range(num_cities):
        #    if i in route_now:
        #        continue
        if route_now[0] in list_cities:
            new_route = route_now.copy()
            new_route.append(route_now[0])
            routes.append(new_route)
    else:
        for i in list_cities:
            if i in route_now:
                continue
            new_route = route_now.copy()
            new_route.append(i)
            aux_routes = find_cicles_2(new_route, size_cicle, Manda_IDs)
            for j in range(len(aux_routes)):
                if aux_routes[j][0] == aux_routes[j][size_cicle]:
                    new_collection = collections.Counter(aux_routes[j][:-1])
                    if not already_equivalent(All_Collections, new_collection):
                        routes.append(aux_routes[j])
                        All_Collections.append(new_collection)
    return routes


def trabalho02_08():
    fluxo_to_max = 6
    fluxo_from = [9]
    cities = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 'L']
    Manda_IDs = [
        [1, 2, 3],#A0
        [0, 2, 5],#B1
        [0, 1, 3, 4, 5],#C2
        [0, 2, 4, 6, 7],#D3
        [2, 3, 5, 6, 7],#E4
        [1, 2, 4, 10],#F5
        [3, 4, 7, 8, 9],#G6
        [4, 6, 9, 10, 11],#H7
        [3, 6, 9],#I8
        [6, 7, 8, 11],#J9
        [5, 7, 11],#K10
        [7, 9, 10],#L11
    ]
    Recebe_IDs = []
    for i in range(len(Manda_IDs)):
        Recebe_IDs.append([])

    for i in range(len(Manda_IDs)):
        for id in Manda_IDs[i]:
            Recebe_IDs[id-1].append(i+1)

    #print(Recebe_IDs)
    Max = [
        [1, 4, 8],#A0
        [1, 3, 3],#B1
        [4, 3, 7, 7, 6],#C2
        [8, 7, 4, 5, 2],#D3
        [7, 4, 8, 3, 2],#E4
        [3, 6, 8, 4],#F5
        [5, 3, 6, 3, 4],#G6
        [2, 6, 2, 4, 7],#H7
        [2, 3, 5],#I8
        [4, 2, 5, 6],#J9
        [4, 4, 2],#K10
        [7, 6, 2],#L11
    ]

    print("/*Funcao para minimizar o tamanho das arestas*/".format(fluxo_to_max))
    print("min:", end=' ')
    for i in range(len(Max)):
        list_max = Max[i]
        list_Ids = Manda_IDs[i]
        for j in range(len(list_max)):
            if list_Ids[j] > i:
                if i > 0 or j > 0:
                    print(" + ", end="")
                print("{0} X{1}_{2}".format( list_max[j], cities[i], cities[list_Ids[j]]), end="")

    print(";")

    constraint = 1
    print("/*O numero de arestas de um arvore minima é o numero dos vertices - 1*/".format(fluxo_to_max))
    print("C{0}:".format(constraint), end=' ')
    constraint += 1
    for i in range(len(Max)):
        list_max = Max[i]
        list_Ids = Manda_IDs[i]
        for j in range(len(list_max)):
            if list_Ids[j] > i:
                if i > 0 or j > 0:
                    print(" + ", end="")
                print("X{1}_{2}".format(list_max[j], cities[i], cities[list_Ids[j]]), end="")

    print(" = {0};".format(len(Max)-1))
    print("/*Proibir ciclos de percusso*/")
    num_ciclos = 3
    size_max = len(Max)
    while num_ciclos < size_max:
        print("/*Proibir ciclos de tamanho {0}*/".format(num_ciclos))
        All_Collections = []
        for i in range(size_max):
            list_cicles = find_cicles_2([i], num_ciclos, Manda_IDs)

            for j in range(len(list_cicles)):
                cicle = list_cicles[j]
                new_collection = collections.Counter(cicle[:-1])
                if not already_equivalent(All_Collections, new_collection):
                    All_Collections.append(new_collection)
                else:
                    continue
                print("C{0}: ".format(constraint), end="")
                constraint += 1
                size_cicle = len(cicle) - 1
                for index in range(size_cicle):
                    if cicle[index] > cicle[index + 1]:
                        print("X{0}_{1}".format(cities[cicle[index+1]], cities[cicle[index]]), end="")
                    else:
                        print("X{0}_{1}".format(cities[cicle[index]], cities[cicle[index+1]]), end="")
                    if index + 1 != size_cicle:
                        print(" + ", end="")
                    else:
                        print(" <= {0};".format(num_ciclos - 1))
        num_ciclos += 1

    #print("/*Xij se for 1, significa que saiu de i e foi para j, e todos Xii = 0*/")
    #for i in range(len(D)):
    #    print("C{0}: X{1}{1} = 0;".format(constraint, i + 1))
    #    constraint += 1

    print("/*Xi_j se for 1, significa que passara pela aresta de i e j, ou seja, eles só podem ser 0 ou 1*/")
    for i in range(len(Max)):
        list_max = Max[i]
        list_Ids = Manda_IDs[i]
        for j in range(len(list_max)):
            if list_Ids[j] > i:
                print("bin X{0}_{1};".format( cities[i], cities[list_Ids[j]]))


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []
        self.path = [[]]*vertices
        self.dist = []

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm. The function
    # also detects negative weight cycle
    def BellmanFord(self, src):

        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        self.dist = [float("Inf")] * self.V
        self.dist[src] = 0
        self.path = [[]]*self.V
        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                if self.dist[u] != float("Inf") and self.dist[u] + w < self.dist[v]:
                    self.dist[v] = self.dist[u] + w
                    self.path[v] = self.path[u].copy()
                    self.path[v].append(v)

        # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle.

        for u, v, w in self.graph:
            if self.dist[u] != float("Inf") and self.dist[u] + w < self.dist[v]:
                print("Graph contains negative weight cycle")
                return

def trabalho03_01_01():
    cidades = {'SFS': 0, 'POP': 1, 'JAL':2, 'FER': 3, 'AND': 4, 'ART': 5, 'PPD': 6, 'ASS':7, 
        'BTT': 8, 'MAR': 9, 'BAU': 10, 'SJP': 11, 'OLP': 12, 'BAR': 13, 'RBP': 14, 'CAT': 15,
        'ARQ': 16,'SCL': 17, 'PCD': 18, 'CJD': 19, 'CAP': 20, 'SPO': 21, 'JUN': 22, 'SOR': 23,
        'TQB': 24,'API': 25, 'JUQ': 26, 'SBC': 27, 'SAN': 28, 'CGT': 29, 'SJC': 30
    }
    cidades_populacao = {
        'SFS': 32563, 'POP': 4152, 'JAL':49201, 'FER': 69402, 'AND': 57202, 'ART': 198129, 
        'PPD': 230371, 'ASS':105087,'BTT': 148130, 'MAR': 240590, 'BAU': 379297, 'SJP': 464983,
        'OLP': 55130, 'BAR': 122833, 'RBP': 711825, 'CAT': 122497, 'ARQ': 238339,'SCL': 254484,
        'PCD': 168641, 'CJD': 52405, 'CAP': 1213792, 'SPO': 12330000, 'JUN': 423006, 'SOR': 687357,
        'TQB': 23256,'API': 24226, 'JUQ': 31646, 'SBC': 844483, 'SAN': 433656, 'CGT': 123389, 'SJC': 729737
    }

    cidades_lista = [""]*len(cidades)
    lista_keys = list( cidades.items() )
    for a in lista_keys:
        cidades_lista[a[1]] = a[0]

    Manda_IDs = [
        [2, 1, 4],  # SFS0
        [3, 12, 13],  # POP1
        [3, 4, 5],  # JAL2
        [11],  # FER3
        [5, 6],  # AND4
        [6, 9, 11],  # ART5
        [9, 7],  # PPD6
        [24, 8],  # ASS7
        [20, 23, 24, 25],  # BTT8
        [7, 10],  # MAR9
        [16, 8],  # BAU10
        [12, 15],  # SJP11
        [13, 14, 15], # OLP12
        [14, 18], # BAR13
        [16, 17, 18], # RBP14
        [9, 10, 16, 14], # CAT15
        [17], # ARQ16
        [18, 20, 8], # SCL17
        [19, 20], # PCD18
        [29, 30], # CJD19
        [19, 30, 22, 23], # CAP20
        [27], # SPO21
        [21], # JUN22
        [26, 21, 27], # SOR23
        [25], # TQB24
        [23, 26], # API25
        [27, 28], # JUQ26
        [30, 28, 29], # SBC27
        [29], # SAN28
        [], # CGT29
        [29], # SJC30
    ]
    Custo_Passagens = [
        [32, 44, 56],  # SFS0
        [40, 124, 160],  # POP1
        [40, 88, 96],  # JAL2
        [116],  # FER3
        [92, 136],  # AND4
        [96, 144, 84],  # ART5
        [36, 36],  # PPD6
        [52, 96],  # ASS7
        [100, 56, 28, 44],  # BTT8
        [16, 96],  # MAR9
        [56, 44],  # BAU10
        [76, 92, 180],  # SJP11
        [136, 128, 52], # OLP12
        [36, 88], # BAR13
        [56, 84, 100], # RBP14
        [92, 148, 120, 116], # CAT15
        [24], # ARQ16
        [72, 172, 76],  # SCL17
        [180, 152], # PCD18
        [100, 60], # CJD19
        [100, 92, 8, 60], # CAP20
        [8, 16], # SPO21
        [44], # JUN22
        [40, 36, 52], # SOR23
        [16], # TQB24
        [28, 32], # API25
        [60, 80], # JUQ26
        [80, 48, 96], # SBC27
        [44], # SAN28
        [], # CGT29
        [36], # SJC30
    ]
    Recebe_IDs = []
    for i in range(len(Manda_IDs)):
        Recebe_IDs.append([])

    for i in range(len(Manda_IDs)):
        for id in Manda_IDs[i]:
            Recebe_IDs[id - 1].append(i + 1)

    #fix custo
    for i in range(0, len(cidades_lista)):
        city_name_from = cidades_lista[i]
        ids_go = Manda_IDs[i]
        for j in range(0, len(ids_go)):
            city_name_to = cidades_lista[ids_go[j]]
            if cidades_populacao[city_name_from] > 70000 or cidades_populacao[city_name_to] > 70000:
                Custo_Passagens[i][j] = Custo_Passagens[i][j]/2
            else:
                Custo_Passagens[i][j] = Custo_Passagens[i][j] * 3 / 4

    #adciona grafo

    g = Graph(len(cidades))

    for i in range(0, len(Manda_IDs)):
        ids_go = Manda_IDs[i]
        for j in range(0, len(ids_go) ):
            g.addEdge(i, ids_go[j], Custo_Passagens[i][j] )

    #determina o caminho com menor custo
    # menor custo de SFS para SPO

    g.BellmanFord(cidades["SFS"])
    lista_cidades_IDS = g.path[cidades["SPO"]]
    custo = g.dist[cidades["SPO"]]
    #escreve as siglas das cidades
    caminho = ["SFS"]
    for cidade_id in lista_cidades_IDS:
        caminho.append(cidades_lista[cidade_id])

    # menor custo de são paulo o para CGT de SPO
    g.BellmanFord(cidades["SPO"])
    custo += g.dist[cidades["CGT"]]# custo para CGT
    lista_cidades_IDS = g.path[cidades["CGT"]]# cminho para CGT
    for cidade_id in lista_cidades_IDS:
        caminho.append(cidades_lista[cidade_id])
    print("custo = ", custo)
    print("caminho => ", caminho)
    print("valor da passagem é ", custo/( 1 - 0.4 ))

def trabalho03_01_02():
    cidades = {'SFS': 0, 'POP': 1, 'JAL': 2, 'FER': 3, 'AND': 4, 'ART': 5, 'PPD': 6, 'ASS': 7,
               'BTT': 8, 'MAR': 9, 'BAU': 10, 'SJP': 11, 'OLP': 12, 'BAR': 13, 'RBP': 14, 'CAT': 15,
               'ARQ': 16, 'SCL': 17, 'PCD': 18, 'CJD': 19, 'CAP': 20, 'SPO': 21, 'JUN': 22, 'SOR': 23,
               'TQB': 24, 'API': 25, 'JUQ': 26, 'SBC': 27, 'SAN': 28, 'CGT': 29, 'SJC': 30
               }
    cidades_populacao = {
        'SFS': 32563, 'POP': 4152, 'JAL': 49201, 'FER': 69402, 'AND': 57202, 'ART': 198129,
        'PPD': 230371, 'ASS': 105087, 'BTT': 148130, 'MAR': 240590, 'BAU': 379297, 'SJP': 464983,
        'OLP': 55130, 'BAR': 122833, 'RBP': 711825, 'CAT': 122497, 'ARQ': 238339, 'SCL': 254484,
        'PCD': 168641, 'CJD': 52405, 'CAP': 1213792, 'SPO': 12330000, 'JUN': 423006, 'SOR': 687357,
        'TQB': 23256, 'API': 24226, 'JUQ': 31646, 'SBC': 844483, 'SAN': 433656, 'CGT': 123389, 'SJC': 729737
    }

    cidades_lista = [""] * len(cidades)
    lista_keys = list(cidades.items())
    for a in lista_keys:
        cidades_lista[a[1]] = a[0]

    Manda_IDs = [
        [2, 1, 4],  # SFS0
        [3, 12, 13],  # POP1
        [3, 4, 5],  # JAL2
        [11],  # FER3
        [5, 6],  # AND4
        [6, 9, 11],  # ART5
        [9, 7],  # PPD6
        [24, 8],  # ASS7
        [20, 23, 24, 25],  # BTT8
        [7, 10],  # MAR9
        [16, 8],  # BAU10
        [12, 15],  # SJP11
        [13, 14, 15],  # OLP12
        [14, 18],  # BAR13
        [16, 17, 18],  # RBP14
        [9, 10, 16, 14],  # CAT15
        [17],  # ARQ16
        [18, 20, 8],  # SCL17
        [19, 20],  # PCD18
        [29, 30],  # CJD19
        [19, 30, 22, 23],  # CAP20
        [27],  # SPO21
        [21],  # JUN22
        [26, 21, 27],  # SOR23
        [25],  # TQB24
        [23, 26],  # API25
        [27, 28],  # JUQ26
        [30, 28, 29],  # SBC27
        [29],  # SAN28
        [],  # CGT29
        [29],  # SJC30
    ]
    Custo_Passagens = [
        [32, 44, 56],  # SFS0
        [40, 124, 160],  # POP1
        [40, 88, 96],  # JAL2
        [116],  # FER3
        [92, 136],  # AND4
        [96, 144, 84],  # ART5
        [36, 36],  # PPD6
        [52, 96],  # ASS7
        [100, 56, 28, 44],  # BTT8
        [16, 96],  # MAR9
        [56, 44],  # BAU10
        [76, 92, 180],  # SJP11
        [136, 128, 52],  # OLP12
        [36, 88],  # BAR13
        [56, 84, 100],  # RBP14
        [92, 148, 120, 116],  # CAT15
        [24],  # ARQ16
        [72, 172, 76],  # SCL17
        [180, 152],  # PCD18
        [100, 60],  # CJD19
        [100, 92, 8, 60],  # CAP20
        [8, 16],  # SPO21
        [44],  # JUN22
        [40, 36, 52],  # SOR23
        [16],  # TQB24
        [28, 32],  # API25
        [60, 80],  # JUQ26
        [80, 48, 96],  # SBC27
        [44],  # SAN28
        [],  # CGT29
        [36],  # SJC30
    ]
    Recebe_IDs = []
    for i in range(len(Manda_IDs)):
        Recebe_IDs.append([])

    for i in range(len(Manda_IDs)):
        for id in Manda_IDs[i]:
            Recebe_IDs[id].append(i)

    # fix custo
    for i in range(0, len(cidades_lista)):
        city_name_from = cidades_lista[i]
        ids_go = Manda_IDs[i]
        for j in range(0, len(ids_go)):
            city_name_to = cidades_lista[ids_go[j]]
            if cidades_populacao[city_name_from] > 70000 or cidades_populacao[city_name_to] > 70000:
                Custo_Passagens[i][j] = Custo_Passagens[i][j] / 2
            else:
                Custo_Passagens[i][j] = Custo_Passagens[i][j] * 3 / 4

    print("/*Funcao para minimizar o custo da passagem*/")
    print("min:", end=' ')
    for i in range(len( Custo_Passagens )):
        list_custo = Custo_Passagens[i]
        list_Ids = Manda_IDs[i]
        for j in range(len(list_Ids)):
            if i > 0 or j > 0:
                print(" + ", end="")
            print("{0} X{1}_{2}".format(list_custo[j], cidades_lista[i], cidades_lista[list_Ids[j]]), end="")

    print(";\n")

    constraint = 1
    print("/*O numero de saidas da cidade {0} eh 1*/".format("SFS"))
    print("C{0}:".format(constraint), end=' ')
    constraint += 1
    id = cidades["SFS"]
    list_Ids = Manda_IDs[id]
    for j in range(len(list_Ids)):
        if j > 0:
            print(" + ", end="")
        print("X{0}_{1}".format(cidades_lista[id], cidades_lista[list_Ids[j]]), end="")
    print(" = 1\n")

    print("/*O numero de saidas da cidade {0} eh 1, assim garantindo que passa por SPO*/".format("SPO"))
    print("C{0}:".format(constraint), end=' ')
    constraint += 1
    id = cidades["SPO"]
    list_Ids = Manda_IDs[id]
    for j in range(len(list_Ids)):
        if j > 0:
            print(" + ", end="")
        print("X{0}_{1}".format(cidades_lista[id], cidades_lista[list_Ids[j]]), end="")
    print(" = 1\n")

    print("/*O numero de entrada pela cidade {0} eh 1, assim garantindo que passa por SPO*/".format("CGT"))
    print("C{0}:".format(constraint), end=' ')
    constraint += 1
    id = cidades["CGT"]
    recebe_Id = Recebe_IDs[id]
    for j in range(len(recebe_Id)):
        if j > 0:
            print(" + ", end="")
        print("X{0}_{1}".format( cidades_lista[recebe_Id[j]], cidades_lista[id] ), end="")
    print(" = 1\n")

    print("/*O numero de entradas deve ser o mesmo que o de saida*/")
    for i in range(len(cidades)):
        if cidades_lista[i] == "SFS" or cidades_lista[i] == "CGT":
            continue
        print("/*Para a cidade {0}*/".format(cidades_lista[i]))
        print("C{0}:".format(constraint), end=' ')
        constraint += 1
        list_Ids = Manda_IDs[i]
        recebe_Id = Recebe_IDs[i]
        for j in range(len(list_Ids)):
            if j > 0:
                print(" + ", end="")
            print("X{0}_{1}".format(cidades_lista[i], cidades_lista[list_Ids[j]]), end="")
        for j in range(len(recebe_Id)):
            print(" - ", end="")
            print("X{0}_{1}".format( cidades_lista[recebe_Id[j]], cidades_lista[i]), end="")

        print(" = 0;")


    print("/*Xi_j se for 1, significa que passara pela aresta de i e j, ou seja, eles só podem ser 0 ou 1*/")
    for i in range(len(cidades)):
        list_Ids = Manda_IDs[i]
        for j in range(len(list_Ids)):
            if list_Ids[j] > i:
                print("bin X{0}_{1};".format(cidades_lista[i], cidades_lista[list_Ids[j]]))


def trabalho03_03():
    fluxo_to_max = 6
    fluxo_from = [9]
    Manda_IDs = [
        [2, 4, 5, 6, 7],#1
        [3, 4],#2
        [2, 4],#3
        [5],#4
        [6],#5
        [],#6
        [6],#7
        [1, 2, 7],#8
        [2, 8, 10],#9
        [2, 3],#10
    ]
    Recebe_IDs = []
    for i in range(len(Manda_IDs)):
        Recebe_IDs.append([])

    for i in range(len(Manda_IDs)):
        for id in Manda_IDs[i]:
            Recebe_IDs[id-1].append(i+1)

    #print(Recebe_IDs)
    Max = [
        [10, 20, 20, 5, 15],#1
        [5, 10],#2
        [15, 5],#3
        [10],#4
        [5],#5
        [],#6
        [10],#7
        [5, 20, 5],#8
        [15, 20, 10],#9
        [5, 15],#10
    ]

    print("/*Funcao para maximizar o fluxo para o {0}*/".format(fluxo_to_max))
    print("max:", end=' ')
    recebe_list = Recebe_IDs[fluxo_to_max-1]
    for i in range(len(recebe_list)):
        print("X{0}_{1}".format( recebe_list[i], fluxo_to_max), end="")
        if i + 1 != len(recebe_list):
            print(" + ", end="")
    print(";")

    constraint = 1
    print("/*Equações dos fluxos para as respectivas cidades, onde os que estão apenas fazendo a transferencia, a varição deve ser zero*/")
    print("/*Cidade com o fluxo a se maximizar é {0} e saida é {1}*/".format(fluxo_to_max, fluxo_from[0]))
    for i in range(len(Max)):
        if i + 1 == fluxo_to_max or (i+1) in fluxo_from:
            continue
        print("/*Fluxo da cidade {0}*/".format(i + 1))
        print("C{0}:".format(constraint), end=' ')
        constraint += 1
        recebe_list = Recebe_IDs[i]
        for j in range(len(recebe_list)):
            print("X{0}_{1}".format(recebe_list[j], i + 1), end="")
            if j + 1 != len(recebe_list):
                print(" + ", end="")
            #else:
            #    print(" = 1;", end="")
        manda_list = Manda_IDs[i]
        for j in range(len(manda_list)):
            print(" - X{0}_{1}".format(i + 1, manda_list[j]), end="")
        print(" = 0;", end="\n\n")

    print("/*nenhum fluxo vai passar do maximo*/")
    for i in range(len(Max)):
        max_list = Max[i]
        manda_list = Manda_IDs[i]
        for j in range(len(max_list)):
            print("C{0}: X{1}_{2} <= {3};".format(
                constraint,
                i + 1,
                manda_list[j],
                max_list[j]
            ))
            constraint += 1

    print("/*nenhum fluxo vai ser menor que zero*/")
    for i in range(len(Max)):
        max_list = Max[i]
        manda_list = Manda_IDs[i]
        for j in range(len(max_list)):
            print("C{0}: X{1}_{2} >= 0;".format(
                constraint,
                i + 1,
                manda_list[j],
            ))
            constraint += 1

if __name__ == '__main__':
    trabalho03_01_02()
    #print(find_cicles([3], 2, 5))
