class Rectangle:
    def __init__(self, length, width):
        self.width = width
        self.length =  length
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height        
    


def main():
    rect = Rectangle(5, 8)
    tri = Triangle(5, 8)
    print("Area:", rect.area())
    print("Perimeter:", rect.perimeter())
    print("Area:", tri.area())

if __name__ == "__main__":
    main()