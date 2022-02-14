import tkinter as tk
from visuo import visualisation
import figures


FIGURES = {
    'Square': figures.Square,
    'Rectangle': figures.Rectangle,
    'Circle': figures.Circle,
    'Triangle': figures.Triangle,
    'Trapezoid': figures.Trapezoid,
    'Rhombus': figures.Rhombus,
    'Sphere': figures.Sphere,
    'Cube': figures.Cube,
    'Parallelepiped': figures.Parallelepiped,
    'Pyramid': figures.Pyramid,
    'Cylinder': figures.Cylinder,
    'Cone': figures.Cone,
}


class Calculator(tk.Frame):
    """Основной класс приложения"""

    def __init__(self, master, *args, **kwargs):
        """Инициализатор, в котором создаётся базовая разметка фрейма"""
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.figure = figures.Sphere(42)
        self.params = []

        self.figure_name = tk.StringVar()
        self.figure_name.set(self.figure.name())
        self.dropdown = tk.OptionMenu(
            self.master, self.figure_name, *FIGURES.keys(), command=self.make_form)
        self.dropdown.config(width=16, height=1)
        self.dropdown.grid(column=0)

        self.calculate_button = tk.Button(
            self.master, text='Draw', width=16, command=self.make_graph_window).grid(column=0)

        self.form = []
        self.make_form(self.figure.name())

        self.results = []

    def destroy_widgets(self, widgets):
        """Функция, удаляющая виджеты из списка"""
        for widget in widgets:
            widget.destroy()

    def entry_update(self, param, i):
        """
        Callback-функция, которая вызывается на каждом обновлении поля ввода
        и обновляет список результатов
        """
        self.make_results()

    def make_figure(self, name, params):
        """Функция создаёт экземпляр фигуры по заданным параметрам"""
        updated_params = []

        for param in params:
            try:
                if param.startswith('-'):
                    raise ValueError
                updated_params.append(float(param))
            except ValueError as ve:
                updated_params.append(0.0)
        self.figure = FIGURES[name](*updated_params)

    def make_graph_window(self):
        """Функция создаёт окно графика для вырбанной фигуры"""
        visualisation(self.figure)

    def make_form(self, figure_name):
        """Метод создаёт список названий параметров и текстовые поля для их ввода"""
        self.figure_name = figure_name
        if len(self.form) != 0:
            self.destroy_widgets(self.form)
            self.params = []

        for i, param in enumerate(FIGURES[figure_name].parameters):

            # Создание списка параметров с функцией обратного вызова, срабатывающей в момент записи
            self.params.append(tk.StringVar())
            self.params[i].trace_add(
                'write', lambda name, index, mode, var=self.params[i], i=i: self.entry_update(var, i))
            # Разметка формы ввода
            lable = tk.Label(self.master, text=param,
                             width=20)
            lable.grid(column=1, row=i)
            entry = tk.Entry(self.master, width=30,
                             textvariable=self.params[i])
            entry.grid(column=2, row=i)
            self.form.append(lable)
            self.form.append(entry)

    def make_results(self):
        """Метод, генерирующий список результатов фигуры с заданными параметрами"""
        self.make_figure(str(self.figure_name), [
                         param.get() for param in self.params])

        if len(self.results) != 0:
            self.destroy_widgets(self.results)
            self.results = []

        for i, method in enumerate(self.figure.methods):
            # Разметка результатов
            method_name = tk.Label(
                self.master, text=method, width=10, anchor=tk.W)
            method_name.grid(column=3, row=i)
            result = tk.Label(
                self.master, text=str(self.figure.handle_method(method)))
            result.grid(column=4, row=i)
            self.results.append(method_name)
            self.results.append(result)