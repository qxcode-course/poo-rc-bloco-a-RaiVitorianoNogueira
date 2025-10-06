class Carro:
    def __init__(self, passMax: int = 2, gasMax: int = 100):
        self.passageiros: int = 0
        self.km: int = 0
        self.passMax:int = passMax
        self.gas:int = 0
        self.gasMax:int  = gasMax

    def __str__(self):
        return f"pass: {self.passageiros}, gas: {self.gas}, km: {self.km}"

    def entrar(self):
        if self.passageiros < self.passMax:
            self.passageiros += 1
        else:
            print("fail: limite de pessoas atingido")

    def sair(self):
        if self.passageiros > 0:
            self.passageiros -= 1
        else:
            print("fail: nao ha ninguem no carro")

    def abastecer(self, quantidade: int):
        if quantidade < 0:
            print("fail: valor invalido")
            return
        self.gas += quantidade
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def dirigir(self, distancia: int):
        if self.passageiros == 0:
            print("fail: nao ha ninguem no carro")
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return

        if self.gas < distancia:
            self.km += self.gas
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.gas = 0
        else:
            self.km += distancia
            self.gas -= distancia


def main():
    carro = Carro()

    while True:
        linha = input()
        print("$" + linha)
        partes = linha.split()

        comando = partes[0]

        if comando == "end":
            break
        elif comando == "show":
            print(carro)
        elif comando == "enter":
            carro.entrar()
        elif comando == "leave":
            carro.sair()
        elif comando == "fuel":
            qtd = int(partes[1])
            carro.abastecer(qtd)
        elif comando == "drive":
            dist = int(partes[1])
            carro.dirigir(dist)
        else:
            print("fail: comando nao encontrado")


main()
