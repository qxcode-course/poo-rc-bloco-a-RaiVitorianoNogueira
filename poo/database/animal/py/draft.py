class Animal:
    def __init__(self, species: str, sound: str, age: int):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

    def life():






















def main():
    
    animal: Animal = Animal("", "")
    while True:

        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            species: str = args[1]
            sound: str = args[2]
            animal = Animal(species, sound)
        elif args[0] ==  "show":
            print(animal)
















main()