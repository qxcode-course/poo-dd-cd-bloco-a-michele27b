
class Towel:
    def __init__(self, color: str, size: str):
        self.color = color
        self.size = size
        self.wetness: int = 0

    def __str__(self):
        return f"color:"    

towel = Towel("green", "G")
toalha = Towel("red", "P")
print(towel.color)
towel.color = "write"
print(towel.color)
print(towel.size)    
print(towel.wetness)


    