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

    @abstractmethod
    def handle_param(self, param):
        pass


class Figure3D(ABC):
    methods = ['Area', 'Volume']

    @abstractmethod
    def handle_method(self, method):
        pass

    @abstractmethod
    def get_volume(self):
        pass

    @abstractmethod
    def handle_param(self, param):
        pass


class Square(Figure):

    name = 'Square'
    parameters = ['Side length']

    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return self.side * 4

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Perimeter':
            return self.get_perimeter()

    def handle_param(self, param):
        if param == 'Side length':
            return self.side


class Rectangle(Square):
    name = 'Rectangle'
    parameters = ['Width', 'Height']

    def __init__(self, width=0, height=0):
        super().__init__(width)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def handle_param(self, param):
        if param == 'Width':
            return self.width
        elif param == 'Height':
            return self.height


class Circle(Figure):
    name = 'Circle'
    parameters = ['Radius']

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * math.pi

    def get_perimeter(self):
        return 2 * self.radius * math.pi

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Perimeter':
            return self.get_perimeter()

    def handle_param(self, param):
        if param == 'Radius':
            return self.radius


class Triangle(Figure):
    name = 'Triangle'
    parameters = ['First side', 'Second side', 'Third side']

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        return math.sqrt(self.get_perimeter()/2 *
                         (self.get_perimeter()/2 - self.side1) *
                         (self.get_perimeter()/2 - self.side2) *
                         (self.get_perimeter()/2 - self.side3))

    def get_perimeter(self):
        return sum([self.side1, self.side2, self.side3])

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Perimeter':
            return self.get_perimeter()

    def handle_param(self, param):
        if param == 'First side':
            return self.side1
        elif param == 'Second side':
            return self.side2
        elif param == 'Third side':
            return self.side3


class Trapezoid(Figure):
    name = 'Trapezoid'
    parameters = ['Smaller base', 'Bigger base', 'First side', 'Second side']

    def __init__(self, base1, base2, side1, side2):
        self.base1 = base1
        self.base2 = base2
        self.side1 = side1
        self.side2 = side2

    def get_area(self):
        return ((self.base1 + self.base2) / (4 * (self.base2 - self.base1))) * \
               math.sqrt((self.base1 - self.base2 + self.side1 + self.side2) *
                         (self.base1 - self.base2 + self.side1 - self.side2) *
                         (self.base1 - self.base2 - self.side1 + self.side2) *
                         (- self.base1 + self.base2 + self.side1 + self.side2))

    def get_perimeter(self):
        return sum([self.base1, self.base2, self.side1, self.side2])

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Perimeter':
            return self.get_perimeter()

    def handle_param(self, param):
        if param == 'Smaller base':
            return self.base1
        elif param == 'Bigger base':
            return self.base2
        elif param == 'First Side':
            return self.side1
        elif param == 'Second side':
            return self.side2


class Rhombus(Figure):
    name = 'Rhombus'
    parameters = ['Side length', 'Angle between']

    def __init__(self, side, angle):
        self.side = side
        self.angle = angle

    def get_area(self):
        return (self.side ** 2) * math.sin(self.angle)

    def get_perimeter(self):
        return self.side * 4

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Perimeter':
            return self.get_perimeter()

    def handle_param(self, param):
        if param == 'Side length':
            return self.side
        elif param == 'Angle between':
            return self.angle


class Sphere(Figure3D):

    name = 'Sphere'
    parameters = ['Radius']

    def __init__(self, radius=0):
        self.radius = radius

    def get_area(self):
        return 4 * math.pi * self.radius ** 2

    def get_volume(self):
        return (4 * math.pi * self.radius ** 3) / 3

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Volume':
            return self.get_volume()

    def handle_param(self, param):
        if param == 'Radius':
            return self.radius


class Cube(Figure3D):
    name = 'Cube'
    parameters = ['Side length']

    def __init__(self, side=0):
        self.side = side

    def get_area(self):
        return 6 * self.side ** 2

    def get_volume(self):
        return self.side ** 3

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Volume':
            return self.get_volume()

    def handle_param(self, param):
        if param == 'Side length':
            return self.side


class Parallelepiped(Figure3D):
    name = 'Parallelepiped'
    parameters = ['Base side1', 'Base side2', 'Base angle between', 'Height']

    def __init__(self, base_side1, base_side2, angle, height):
        self.base_side1 = base_side1
        self.base_side2 = base_side2
        self.angle = angle
        self.height = height

    def get_area(self):
        return 2 * (self.base_side1 * self.base_side2 * math.sin(self.angle)) + \
               2 * (self.base_side1 * self.height) + \
               2 * (self.base_side2 * self.height)

    def get_volume(self):
        return self.height * (self.base_side1 * self.base_side2 * math.sin(self.angle))

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Volume':
            return self.get_volume()

    def handle_param(self, param):
        if param == 'Base side1':
            return self.base_side1
        elif param == 'Base side2':
            return self.base_side2
        elif param == 'Base angle between':
            return self.angle
        elif param == 'Height':
            return self.height


class Pyramid(Figure3D):
    name = 'Pyramid'
    parameters = ['Number of sides in base Polygon', 'Side', 'Height']

    def __init__(self, number, side,  height):
        self.number = number
        self.side = side
        self.height = height

    def get_area(self):
        return

    def get_volume(self):
        return self.height * (self.base_side1 * self.base_side2 * math.sin(self.angle))

    def handle_method(self, method):
        if method == 'Area':
            return self.get_area()
        elif method == 'Volume':
            return self.get_volume()

    def handle_param(self, param):
        if param == 'Base side1':
            return self.base_side1
        elif param == 'Base side2':
            return self.base_side2
        elif param == 'Base angle between':
            return self.angle
        elif param == 'Height':
            return self.height


if __name__ == '__main__':
    pass
