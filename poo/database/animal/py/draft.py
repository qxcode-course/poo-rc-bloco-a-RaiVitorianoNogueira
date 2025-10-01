class Animal:
    def __init__(self, species: str, sound: str, age: int = 0):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"
    
    def grow(self, i:int) -> None:
        if self.age >= 4:
            print(f"warning: {self.species} morreu ")
            return
        self.age  += i
        if self.age >= 4:
            self.age = 4
            print(f"warning: {self.species} morreu")
    def makeSound(self) -> str:
        if self.age == 0:
            return "---"
        if self.age >= 4:
            return "RIP"
        return self.sound
    
    





















def main():
    
    animal: Animal = Animal("", "",0)
    while True:

        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            species: str = args[1]
            sound: str = args[2]
            animal = Animal(species, sound,0)
        elif args[0] ==  "show":
            print(animal)
        elif args[0] == "grow":
            i: int = int(args[1])
            animal.grow(i)
        elif args[0] == "noise":
            print(animal.makeSound())

        else:
            print("fail: comando não encontrado")






main()