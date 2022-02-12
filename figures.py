import math
from abc import ABC, abstractmethod


class Figure(ABC):
    methods = ['Area', 'Perimeter']

    @abstractmethod
    def handle_method(self, method):
       pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Figure3D(ABC):
    methods = ['Area', 'Volume']

    @abstractmethod
    def handle_method(self, method):
        pass

    @abstractmethod
    def get_volume(self):
        pass


class Square(Figure):
    name = 'Square'
    parameters = ['Side length']

    def __init__(self, side):
        self.side = side

    def get_area(self):
        try:
            result = self.side * self.side
            if result > 0 and type(self.get_perimeter()) != str:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def get_perimeter(self):
        try:
            result = self.side * 4
            if result > 0:
                return self.side * 4
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Perimeter':
            return self.get_perimeter()


class Rectangle(Square):
    name = 'Rectangle'
    parameters = ['Width', 'Length']

    def __init__(self, width, length):
        super().__init__(width)
        self.width = width
        self.length = length

    def get_area(self):
        try:
            result = self.width * self.length
            if result > 0:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def get_perimeter(self):
        try:
            result = 2 * (self.width + self.length)
            if result > 0 and type(self.get_area()) != str:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'


class Circle(Figure):
    name = 'Circle'
    parameters = ['Radius']

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        try:
            result = self.radius ** 2 * math.pi
            if result > 0:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def get_perimeter(self):
        try:
            result = 2 * self.radius * math.pi
            if result > 0 and type(self.get_area()) != str:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Perimeter':
            return self.get_perimeter()


class Triangle(Figure):
    name = 'Triangle'
    parameters = ['First side', 'Second side', 'Third side']

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        p = sum([self.side1, self.side2, self.side3]) / 2
        try:
            result = math.sqrt(p *
                               (p - self.side1) *
                               (p - self.side2) *
                               (p - self.side3))
            if result > 0:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def get_perimeter(self):
        try:
            result = sum([self.side1, self.side2, self.side3])
            if result > 0 and type(self.get_area()) != str:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Perimeter':
            return self.get_perimeter()


class Trapezoid(Figure):
    name = 'Trapezoid'
    parameters = ['Smaller base', 'Bigger base', 'First side', 'Second side']

    def __init__(self, base1, base2, side1, side2):
        self.base1 = base1
        self.base2 = base2
        self.side1 = side1
        self.side2 = side2

    def get_area(self):
        try:
            result = ((self.base1 + self.base2) / (4 * (self.base2 - self.base1))) * \
               math.sqrt((self.base1 - self.base2 + self.side1 + self.side2) *
                         (self.base1 - self.base2 + self.side1 - self.side2) *
                         (self.base1 - self.base2 - self.side1 + self.side2) *
                         (- self.base1 + self.base2 + self.side1 + self.side2))
            if result > 0:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def get_perimeter(self):
        try:
            result = sum([self.base1, self.base2, self.side1, self.side2])
            if result > 0 and type(self.get_area()) != str:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Perimeter':
            return self.get_perimeter()


class Rhombus(Figure):
    name = 'Rhombus'
    parameters = ['Side length', 'Angle\n(in radians)']

    def __init__(self, side, angle):
        self.side = side
        self.angle = angle

    def get_area(self):
        try:
            result = (self.side ** 2) * math.sin(self.angle)
            if result > 0:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def get_perimeter(self):
        try:
            result = self.side * 4
            if result > 0 and type(self.get_area()) != str:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Perimeter':
            return self.get_perimeter()


class Sphere(Figure3D):

    name = 'Sphere'
    parameters = ['Radius']

    def __init__(self, radius=0):
        self.radius = radius

    def get_area(self):
        try:
            result = 4 * math.pi * self.radius ** 2
            if result > 0 and type(self.get_volume()) != str:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def get_volume(self):
        try:
            result = (4 * math.pi * self.radius ** 3) / 3
            if result > 0:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Volume':
            return self.get_volume()


class Cube(Figure3D):
    name = 'Cube'
    parameters = ['Side length']

    def __init__(self, side=0):
        self.side = side

    def get_area(self):
        try:
            result = 6 * self.side ** 2
            if result > 0 and type(self.get_volume()) != str:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def get_volume(self):
        try:
            result = self.side ** 3
            if result > 0:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Volume':
            return self.get_volume()


class Parallelepiped(Figure3D):
    name = 'Parallelepiped'
    parameters = ['Base width', 'Base length', 'Height']

    def __init__(self, base_width, base_length, height):
        self.base_width = base_width
        self.base_length = base_length
        self.height = height

    def get_area(self):
        try:
            result = 2 * ((self.base_width * self.base_length) +
                          (self.height * self.base_length) +
                          (self.height * self.base_width))
            if result > 0 and type(self.get_volume()) != str:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def get_volume(self):
        try:
            result = self.base_width * self.base_length * self.height
            if result > 0:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Volume':
            return self.get_volume()


class Pyramid(Figure3D):
    name = 'Pyramid'
    parameters = ['Number of sides in base Polygon', 'Side', 'Height']

    def __init__(self, number, side,  height):
        self.number = number
        self.side = side
        self.height = height

    def get_area(self):
        try:
            r = self.side / (2*math.tan(math.pi/self.number))
            h = math.sqrt(self.height**2 + r ** 2)
            result = self.number * (self.side**2) / (4 * math.tan(math.pi/self.number)) + self.number * (0.5 * self.side * h)
            if result > 0 and type(self.get_volume()) != str:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def get_volume(self):
        try:
            result = (1/3) * self.height * self.number * (self.side**2) / (4 * math.tan(math.pi/self.number))
            if result > 0:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Volume':
            return self.get_volume()


class Cylinder(Figure3D):
    name = 'Cylinder'
    parameters = ['Radius', 'Height']

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_area(self):
        try:
            result = 2 * math.pi * ((self.radius**2) + self.radius * self.height)
            if result > 0 and type(self.get_volume()) != str:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def get_volume(self):
        try:
            result = math.pi * (self.radius**2) * self.height
            if result > 0:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Volume':
            return self.get_volume()


class Cone(Figure3D):
    name = 'Cone'
    parameters = ['Radius', 'Height']

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_area(self):
        try:
            l = math.sqrt(self.radius ** 2 + self.height ** 2)
            result = math.pi * self.radius * (l+self.radius)
            if result > 0 and type(self.get_volume()) != str:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def get_volume(self):
        try:
            result = (1/3) * math.pi * (self.radius**2) * self.height
            if result > 0:
                return result
            else:
                return 'incorrect input'
        except ValueError:
            return 'incorrect input'

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Volume':
            return self.get_volume()


if __name__ == '__main__':
    pass
