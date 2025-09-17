



class Towel:
    def __init__(self, color: str, size: str):
        self.color: str = color #atributo
        self.size: str = size
        self.wetness: int = 0


# referencias
#minha: Towel = Towel("blue", "P")
#minha.color = "blue"
#minha.size = "G"


#esposa = Towel("red", "G")
#esposa.color = "red"
#esposa.size = "G"

#gaiato = esposa



print("Qual a cor da sua toalha")
color = input()
towel: Towel = Towel(color, "P")
print(f"Sua toalha é {towel.color}")



