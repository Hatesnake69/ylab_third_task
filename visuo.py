from figures import *
import matplotlib.pyplot as plt
from numpy import linspace, pi, sin, cos, sqrt
import numpy as np
from itertools import product, combinations


def visualisation(figure):
    if figure.name() == "Square":
        x_list = [0, figure.side, figure.side, 0, 0]
        y_list = [0, 0, figure.side, figure.side, 0]
        plt.plot(x_list, y_list)
        plt.axis('equal')
        plt.show()

    elif figure.name() == 'Circle':
        t = linspace(0, 2 * pi, 100)
        plt.plot(figure.radius * cos(t) + figure.radius, figure.radius * sin(t) + figure.radius)
        plt.axis('equal')
        plt.show()

    elif figure.name() == 'Rectangle':
        x_list = [0, figure.width, figure.width, 0, 0]
        y_list = [0, 0, figure.length, figure.length, 0]
        plt.plot(x_list, y_list)
        plt.axis('equal')
        plt.show()

    elif figure.name() == 'Triangle':
        y3 = sqrt(1 / (4 * (figure.side1 ** 2))*(figure.get_perimeter()*(figure.get_perimeter()-2*figure.side2)*(figure.get_perimeter()-2*figure.side3)*(figure.get_perimeter()-2*figure.side1)))
        x3 = sqrt((figure.side3 ** 2) - (y3 ** 2))
        x_list = [0, figure.side1, x3, 0]
        y_list = [0, 0, y3, 0]
        plt.plot(x_list, y_list)
        plt.axis('equal')
        plt.show()

    elif figure.name() == 'Trapezoid':
        try:
            for i in [figure.base1, figure.base2, figure.side1, figure.side2]:
                a = 1/i
        except:
            return
        y3 = sqrt(figure.side2**2 - (((figure.base2-figure.base1)**2+figure.side1**2-figure.side2**2)/(2*(figure.base2-figure.base1)))**2)
        x3 = figure.base2 - sqrt(figure.side2**2 - y3 ** 2)
        x4 = sqrt(figure.side2**2 - y3 ** 2)
        x_list = [0, figure.base2, x3, x4, 0]
        y_list = [0, 0, y3, y3, 0]
        plt.plot(x_list, y_list)
        plt.axis('equal')
        plt.show()

    elif figure.name() == 'Rhombus':
        y3 = figure.side * sin(figure.angle)
        x3 = sqrt(figure.side**2 - y3**2) + figure.side
        x4 = sqrt(figure.side**2 - y3**2)
        x_list = [0, figure.side, x3, x4, 0]
        y_list = [0, 0, y3, y3, 0]
        plt.plot(x_list, y_list)
        plt.axis('equal')
        plt.show()

    elif figure.name() == 'Sphere':
        u, v = np.mgrid[0:2 * pi:20j, 0:pi:20j]
        x = np.cos(u) * np.sin(v) * figure.radius
        y = np.sin(u) * np.sin(v) * figure.radius
        z = np.cos(v) * figure.radius
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z)
        plt.axis('auto')
        plt.show()

    elif figure.name() == 'Cube':
        r = [0, figure.side]
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for s, e in combinations(np.array(list(product(r, r, r))), 2):
            if np.sum(np.abs(s - e)) == r[1] - r[0]:
                ax.plot3D(*zip(s, e), color="b")
        plt.show()

    elif figure.name() == 'Parallelepiped':
        fig = plt.figure()
        a = figure.base_width
        b = figure.base_length
        h = figure.height
        ax = fig.add_subplot(projection='3d')
        x1 = [0, a, a, 0, 0, 0, 0, a, a, 0]
        y1 = [0, 0, b, b, 0, 0, b, b, 0, 0]
        z1 = [0, 0, 0, 0, 0, h, h, h, h, h]
        x2 = [a, a]
        y2 = [0, 0]
        z2 = [h, 0]
        x3 = [a, a]
        y3 = [b, b]
        z3 = [h, 0]
        x4 = [0, 0]
        y4 = [b, b]
        z4 = [h, 0]
        ax.plot(x1, y1, z1, color='b')
        ax.plot(x2, y2, z2, color='b')
        ax.plot(x3, y3, z3, color='b')
        ax.plot(x4, y4, z4, color='b')
        ax.set_xlim3d(0, max([a, b, h]))
        ax.set_ylim3d(0, max([a, b, h]))
        ax.set_zlim3d(0, max([a, b, h]))
        plt.show()

    elif figure.name() == 'Pyramid':
        if math.modf(figure.number)[0] > 0.0001 or figure.number < 3:
            raise ValueError
        fig = plt.figure()
        n = figure.number
        a = figure.side
        h = figure.height
        r = a / (2*sin(pi/n))
        tet = 2*pi / n
        ax = fig.add_subplot(projection='3d')
        x1 = r
        y1 = 0
        for i in range(int(n)):
            x2 = x1*cos(tet) - y1*sin(tet)
            y2 = x1*sin(tet) + y1*cos(tet)
            x = [x1, x2]
            y = [y1, y2]
            z = [0, 0]
            xx = [x1, 0]
            yy = [y1, 0]
            zz = [0, h]
            ax.plot(x, y, z, color='b')
            ax.plot(xx, yy, zz, color='b')
            x1 = x2
            y1 = y2
        ax.set_xlim3d(-max([a, r, h]), max([a, r, h]))
        ax.set_ylim3d(-max([a, r, h]), max([a, r, h]))
        ax.set_zlim3d(0, max([a, r, h]))
        plt.show()

    elif figure.name() == 'Cylinder':
        fig = plt.figure()
        n = 300
        h = figure.height
        r = figure.radius
        a = 2 * r * sin(pi / n)
        tet = 2*pi / n
        ax = fig.add_subplot(projection='3d')

        x1 = r
        y1 = 0
        for i in range(int(n)):
            x2 = x1*cos(tet) - y1*sin(tet)
            y2 = x1*sin(tet) + y1*cos(tet)
            x = [x1, x2]
            y = [y1, y2]
            z = [0, 0]
            xx = [x1, 0]
            yy = [y1, 0]
            zz = [0, h]
            ax.plot(x, y, z, color='b')
            ax.plot(xx, yy, zz, color='b')
            x1 = x2
            y1 = y2
        ax.set_xlim3d(-max([a, r, h]), max([a, r, h]))
        ax.set_ylim3d(-max([a, r, h]), max([a, r, h]))
        ax.set_zlim3d(0, max([a, r, h]))
        plt.show()

    elif figure.name() == 'Cone':
        fig = plt.figure()
        n = 400
        h = figure.height
        r = figure.radius
        a = 2 * r * sin(pi / n)
        tet = 2*pi / n
        ax = fig.add_subplot(projection='3d')
        x1 = r
        y1 = 0
        for i in range(int(n)):
            x2 = x1*cos(tet) - y1*sin(tet)
            y2 = x1*sin(tet) + y1*cos(tet)
            x = [x1, x2]
            y = [y1, y2]
            z = [0, 0]
            xx = [x1, x1]
            yy = [y1, y1]
            zz = [0, h]
            ax.plot(x, y, z, color='b')
            ax.plot(xx, yy, zz, color='b')
            x1 = x2
            y1 = y2
        ax.set_xlim3d(-max([a, r, h]), max([a, r, h]))
        ax.set_ylim3d(-max([a, r, h]), max([a, r, h]))
        ax.set_zlim3d(0, max([a, r, h]))
        plt.show()


if __name__ == '__main__':
    pass
    # fig = Square(3)
    # visualisation(fig)
    # fig = Circle(2)
    # visualisation(fig)
    # fig2 = Rectangle(2, 7)
    # visualisation(fig2)
    # fig3 = Triangle(3, 5, 4)
    # visualisation(fig3)
    # fig4 = Trapezoid(3, 5, 2, 2)
    # visualisation(fig4)
    # fig = Sphere(3)
    # visualisation(fig)
    # fig = Cube(2)
    # visualisation(fig)
    # fig = Parallelepiped(1,2,3)
    # visualisation(fig)
    # fig = Pyramid(34,1,23)
    # # visualisation(fig)
    # # fig = Cylinder(1, 1)
    # # visualisation(fig)
    # fig = Cone(3, 10)
    # visualisation(fig)
