from calculator import Calculator
from tkinter import Tk


def main():
    root = Tk()
    root.geometry('800x300')
    Calculator(root)
    root.mainloop()


if __name__ == '__main__':
    main()
