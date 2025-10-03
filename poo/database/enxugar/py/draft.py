class Towel:
    def __init__(self, color: str, size: str):
        self.color = color
        self.size = size
        self.wetness = 0 

    def __str__(self) -> str:
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"

    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        elif self.size == "M":
            return 20
        elif self.size == "G":
            return 30
        return 0

    def isDry(self) -> str:
        return "sim" if self.wetness == 0 else "nao"

    def dry(self, amount: int) -> None:
        max_wetness = self.getMaxWetness()
        new_wetness = self.wetness + amount

        if new_wetness >= max_wetness:
            if self.wetness < max_wetness or amount > 0:
                 print("toalha encharcada")
            
            self.wetness = max_wetness
            
        else:
            self.wetness = new_wetness
    
    def wringOut(self) -> None:
        self.wetness = 0



def main():
    towel = None
    
    try:
        while True:
            line = input()
            line = line.strip()
            
            if not line:
                continue

            print(f"${line}")

            parts = line.split()
            if not parts:
                continue
                
            cmd = parts[0]
            
            if cmd == "criar":
                if len(parts) >= 3:
                    color = parts[1]
                    size = parts[2]
                    towel = Towel(color, size)
            
            elif cmd == "mostrar":
                if towel:
                    print(towel)

            elif cmd == "seca":
                if towel:
                    print(towel.isDry())

            elif cmd == "enxugar":
                if towel and len(parts) > 1:
                    try:
                        amount = int(parts[1])
                        towel.dry(amount)
                    except ValueError:
                        pass
            
            elif cmd == "torcer":
                if towel:
                    towel.wringOut()
            
            elif cmd == "end":
                break
    except EOFError:
        pass
    except:
        pass

if __name__ == "__main__":
    main()