
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
            print("{0} X{1}{2}".format( C[i-1][j-1], i, j), end="")
            if j != len(b) or i != len(a):
                print(" + ", end="")
    print(";", end="\n\n")

    constraint = 1
    print("/*Limite de oferta*/")
    for i in range(1, len(a) + 1):
        print("C{0}:".format(constraint), end=' ')
        constraint += 1
        for j in range(1, len(b) + 1):
            print("X{0}{1}".format(i, j), end="")
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
            print("X{0}{1}".format(i, j), end="")
            if i != len(a):
                print(" + ", end="")
            else:
                print(" >= {0};".format(b[j - 1]), end="")
        print("", end="\n\n")

    print("/*Nenhum transporte é menor que zero*/")
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            print("C{0}: X{1}{2} >= 0;".format( constraint, i, j))
            constraint += 1

    print("/*Todos os transportes são inteiros*/")
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            print("int X{1}{2};".format(constraint, i, j))
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
            print("{0} X{1}{2}".format( C[i-1][j-1], i, j), end="")
            if j != len(b) or i != len(a):
                print(" + ", end="")
    print(";", end="\n\n")

    constraint = 1
    print("/*Todo restaurante tem uma contrutora*/")
    for i in range(1, len(a) + 1):
        print("C{0}:".format(constraint), end=' ')
        constraint += 1
        for j in range(1, len(b) + 1):
            print("X{0}{1}".format(i, j), end="")
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
            print("X{0}{1}".format(i, j), end="")
            if i != len(a):
                print(" + ", end="")
            else:
                print(" <= {0};".format(b[j - 1]), end="")
        print("", end="\n\n")

    print("/*Ou foi contruido ou não*/")
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            print("bin X{1}{2};".format(constraint, i, j))
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
    print("/*toda construtora possui o limite de 1*/")
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

    print("/*Todos os dias o numero de funcionarios tem que ser maior que zero*/")
    for i in range(7):
        print("C{0}: X{1} >= 0;".format( constraint, dias[i]))
        constraint += 1

    print("/*Ou foi contruido ou não*/")
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

    print("/*Função de custo com X sendo os unitarios e os y sendo os fixos*/")
    print("min:", end=' ')
    for i in range(len(cidades_depositos)):
        for j in range(len(cidades_recebem)):
            print("{0} X{1}{2}".format(custo_unit[i][j], cidades_depositos[i], cidades_recebem[j] ), end="")
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
            print("X{0}{1}".format(cidades_depositos[i], cidades_recebem[j]), end="")
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
            print("X{0}{1}".format(cidades_depositos[i], cidades_recebem[j]), end="")
            if i + 1 != len(cidades_depositos):
                print(" + ", end="")
            else:
                print(" >= {0};".format(demandas[j]), end="")
        print("", end="\n\n")

    print("/*Todos os transportes são maior ou igual a zero*/")
    for i in range(len(cidades_depositos)):
        for j in range(len(cidades_recebem)):
            print("C{0}: X{1}{2} >= 0;".format(constraint, cidades_depositos[i], cidades_recebem[j]))
            constraint += 1

    for i in range(len(cidades_depositos)):
        print("bin Y{1};".format(custo_fixo[i], cidades_depositos[i]))


if __name__ == '__main__':
    trabalho02_04()
