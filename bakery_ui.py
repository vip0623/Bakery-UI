import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')
        label1 = Label(window, text="샌드위치 (5000원)")
        entry1 = Entry(window)
        label2 = Label(window, text="케이크 (20000원)")
        entry2 = Entry(window)
        button = Button(window, text="주문하기", command=lambda:self.send_order(entry1.get(),entry2.get()))
        label1.grid(row=0, column=0)
        entry1.grid(row=0, column=1)
        label2.grid(row=1, column=0)
        entry2.grid(row=1, column=1)
        button.grid(row=2, column=0)


    def send_order(self,num1,num2):
        order_text = self.name
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            if num1>0 and num2>0:
                order_text += ": 샌드위치 (5000원) " + str(num1) + "개, 케이크 (20000원) " + str(num2) + "개"
            elif num1>0 and num2<=0:
                order_text += ": 샌드위치 (5000원) " + str(num1) + "개"
            elif num1<=0 and num2>0:
                order_text += ": 케이크 (20000원) " + str(num2) + "개"
        elif num1.isdigit() == False and num2.isdigit() == True:
            num2 = int(num2)
            if num2>0:
                order_text += ": 케이크 (20000원) " + str(num2) + "개"
            else:
                order_text = ""
        elif num1.isdigit() == True and num2.isdigit() == False:
            num1 = int(num1)
            if num1>0:
                order_text += ": 샌드위치 (5000원) " + str(num1) + "개"
            else:
                order_text = ""
        else:
            order_text = ""
        self.bakeryView.add_order(order_text)


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
