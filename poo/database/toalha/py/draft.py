



#class Towel:
    def __init__(self, color: str , size: str):
        self.color: str = color #atributo
        self.size: str = size
        self.wetness: int = 0


    def dry(self, amount: int) -> None:
        self.wetness += amount

        if self.wetness >= self.isMaxWetness():
            self.wetness = self.isMaxWetness()
            print("Toalha molhada")
    def isMaxWetness(self) -> int:
        if self.size == "P": # early return
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0 # default return

    def __str__(self) -> str: # toString
        return f"Color:{self.color}, Size:{self.size}, Wet:{self.wetness}"




def main():    
    towel: Towel = Towel("", "")
    while True:
        line: str = input()
        args: list[str] = line.split(" ")
        
        if args[0] == "end":
            break
        elif args[0] == "new":
            color: str = args[1]
            size: str = args[2]
            towel = Towel(color,size)
        
        elif args[0] == "dry":
            

        else:
            print("fail: comando não encontrado")

main()


# referencias
#minha: Towel = Towel("blue", "P")
#minha.color = "blue"
#minha.size = "G"


#esposa = Towel("red", "G")
#esposa.color = "red"
#esposa.size = "G"

#gaiato = esposa



#print("Qual a cor da sua toalha")
#color = input()
#towel: Towel = Towel(color, "P")
#print(f"Sua toalha é {towel.color}")



