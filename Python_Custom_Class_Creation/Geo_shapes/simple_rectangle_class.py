class Rectangle:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def get_area(self):
        return self.a * self.b

    def print_dimensions(self):
        return "Width =", str(self.a), "Height=", str(self.b)

R1 = Rectangle(5,4)
print(R1.print_dimensions())
