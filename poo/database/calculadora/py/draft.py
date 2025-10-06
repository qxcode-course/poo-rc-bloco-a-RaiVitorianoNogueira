class Calculadora:
    def __init__(self, batteryMax: int):
        self.display: float = 0.0
        self.battery: int = 0
        self.batteryMax: int = batteryMax

    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"

    def gastarBateria(self) -> bool:
        if self.battery <= 0:
            print("fail: bateria insuficiente")
            return False
        self.battery -= 1
        return True

    def charge(self, valor: int) -> None:
        self.battery += valor
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def somar(self, a: float, b: float) -> None:
        if not self.gastarBateria():
            return
        self.display = a + b

    def dividir(self, a: float, b: float) -> None:
        if not self.gastarBateria():
            return
        if b == 0:
            print("fail: divisao por zero")
            return
        self.display = a / b


def main():
    calc: Calculadora | None = None

    while True:
        comando = input()
        print(f"${comando}")
        partes = comando.split()

        if partes[0] == "end":
            break
        elif partes[0] == "init":
            maximo = int(partes[1])
            calc = Calculadora(maximo)
        elif partes[0] == "show":
            if calc is not None:
                print(calc)
            else:
                print("fail: calc nao inicializada")
        elif partes[0] == "charge":
            if calc is not None:
                valor = int(partes[1])
                calc.charge(valor)
            else:
                print("fail: calc nao inicializada")
        elif partes[0] == "sum":
            if calc is not None:
                a = float(partes[1])
                b = float(partes[2])
                calc.somar(a, b)
            else:
                print("fail: calc nao inicializada")
        elif partes[0] == "div":
            if calc is not None:
                a = float(partes[1])
                b = float(partes[2])
                calc.dividir(a, b)
            else:
                print("fail: calc nao inicializada")
        else:
            print("fail: comando invalido")


main()
