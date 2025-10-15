class Rectangle:
    def __init__(self, length, width):
        self.width = width
        self.length =  length
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

def main():
    rect = Rectangle(5, 8)
    print("Area:", rect.area())
    print("Perimeter:", rect.perimeter())

if __name__ == "__main__":
    main()