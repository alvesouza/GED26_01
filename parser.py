
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
if __name__ == '__main__':
    Obras_Letras = ["A", "B", "C", "D", "E"]
    Obras_Listas = [
        Obra( "A", 1900, 24, 4, 390, 700),
        Obra( "B", 3100, 36, 22, 420, 530),
        Obra( "C", 2900, 24, 10, 510, 245),
        Obra( "D", 3700, 30, 24, 690, 810),
        Obra( "E", 2500, 28, 16, 550, 390),
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
            for centro_index in range(len( Centros_Distribuicao )):
                obra = Obras_Listas[obra_index]
                print("{0:.3f} X{1}{2}{3}".format(obra.custo[centro_index],
                                                Centros_Distribuicao[centro_index],
                                                mes,
                                                obra.nome,
                                                ), end="")

                if not (centro_index + 1 == len(Centros_Distribuicao) and mes == Mes_Final and obra_index + 1 == len(Obras_Listas)):
                    print(" +", end="")
    print(";\n")

    print("/*Estoque da Central de Compras não pode ficar menos que 0*/")

    #for mes_fim in range(1, Mes_Final + 1):
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
    print( " <= ", Estoque_Inicial_Central-0, end=";\n" )

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
