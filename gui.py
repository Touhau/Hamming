import tkinter as tk

class gui(tk.Frame):
     def __init__(self, window):
        super().__init__(window)
        window.title('Алгоритм Хэмминга')
        window.geometry('440x220')
        # window.resizable(False, False)

        self.fieldText = tk.StringVar()
        self.entryField = tk.Entry(window, font = 'Arial 12', textvariable = self.fieldText)
        self.entryText = tk.Label(window, font = 'Arial 12', text = 'Введите двоичное число длиной до 8 символов')

        self.p1lbl = tk.Label(window, font = 'Arial 12', text = 'p1', width = 2, height = 1)
        self.p2lbl = tk.Label(window, font = 'Arial 12', text = 'p2', width = 2, height = 1)
        self.p3lbl = tk.Label(window, font = 'Arial 12', text = 'p3', width = 2, height = 1)
        self.p4lbl = tk.Label(window, font = 'Arial 12', text = 'p4', width = 2, height = 1)
        self.m1lbl = tk.Label(window, font = 'Arial 12', text = 'm1', width = 2, height = 1)
        self.m2lbl = tk.Label(window, font = 'Arial 12', text = 'm2', width = 2, height = 1)
        self.m3lbl = tk.Label(window, font = 'Arial 12', text = 'm3', width = 2, height = 1)
        self.m4lbl = tk.Label(window, font = 'Arial 12', text = 'm4', width = 2, height = 1)
        self.m5lbl = tk.Label(window, font = 'Arial 12', text = 'm5', width = 2, height = 1)
        self.m6lbl = tk.Label(window, font = 'Arial 12', text = 'm6', width = 2, height = 1)
        self.m7lbl = tk.Label(window, font = 'Arial 12', text = 'm7', width = 2, height = 1)
        self.m8lbl = tk.Label(window, font = 'Arial 12', text = 'm8', width = 2, height = 1)

        self.p1btn = tk.Button(window, font = 'Arial 12', text = '', width = 1, height = 1)
        self.p2btn = tk.Button(window, font = 'Arial 12', text = '', width = 1, height = 1)
        self.p3btn = tk.Button(window, font = 'Arial 12', text = '', width = 1, height = 1)
        self.p4btn = tk.Button(window, font = 'Arial 12', text = '', width = 1, height = 1)
        self.m1btn = tk.Button(window, font = 'Arial 12', text = '', width = 1, height = 1)
        self.m2btn = tk.Button(window, font = 'Arial 12', text = '', width = 1, height = 1)
        self.m3btn = tk.Button(window, font = 'Arial 12', text = '', width = 1, height = 1)
        self.m4btn = tk.Button(window, font = 'Arial 12', text = '', width = 1, height = 1)
        self.m5btn = tk.Button(window, font = 'Arial 12', text = '', width = 1, height = 1)
        self.m6btn = tk.Button(window, font = 'Arial 12', text = '', width = 1, height = 1)
        self.m7btn = tk.Button(window, font = 'Arial 12', text = '', width = 1, height = 1)
        self.m8btn = tk.Button(window, font = 'Arial 12', text = '', width = 1, height = 1)
        
        self.c1lbl = tk.Label(window, font = 'Arial 12', text = 'c1 =', width = 1, height = 1)
        self.c2lbl = tk.Label(window, font = 'Arial 12', text = 'c2 =', width = 1, height = 1)
        self.c3lbl = tk.Label(window, font = 'Arial 12', text = 'c3 =', width = 1, height = 1)
        self.c4lbl = tk.Label(window, font = 'Arial 12', text = 'c4 =', width = 1, height = 1)
        self.c1ent = tk.Entry(window, font = 'Arial 12', text = '', width = 1)
        self.c2ent = tk.Entry(window, font = 'Arial 12', text = '', width = 1)
        self.c3ent = tk.Entry(window, font = 'Arial 12', text = '', width = 1)
        self.c4ent = tk.Entry(window, font = 'Arial 12', text = '', width = 1)

        self.errorlbl = tk.Label(window, font = 'Arial 12', text = 'Бит')
        self.errorEnt = tk.Entry(window, font = 'Arial 12', width = 2)
        self.errorText = tk.Label(window, font = 'Arial 12', text = 'Допустите 1 ошибку')

        self.elementArrow = [self.p1lbl, self.p2lbl, self.p3lbl, self.p4lbl, self.m1lbl,\
                             self.m1lbl, self.m2lbl, self.m3lbl, self.m4lbl, self.m5lbl,\
                             self.m6lbl, self.m7lbl, self.m8lbl, self.p1btn, self.p2btn,\
                             self.p3btn, self.p4btn, self.m1btn, self.m2btn, self.m3btn,\
                             self.m4btn, self.m5btn, self.m6btn, self.m7btn, self.m8btn,\
                             self.c1lbl, self.c2lbl, self.c3lbl, self.c4lbl, self.c1ent,\
                            self.c2ent, self.c3ent, self.c4ent, self.errorlbl, self.errorEnt, self.errorText]

        self.entryText.grid(row = 0, column = 0, columnspan = 11)
        self.entryField.grid(row = 1, column = 0, columnspan = 11, sticky = 'nw', pady = 6, padx = 10)

        self.emptylbl = tk.Label(window, font = 'Arial 14')

        self.p1lbl.grid(row = 2, column = 0)
        self.p2lbl.grid(row = 2, column = 1)
        self.m1lbl.grid(row = 2, column = 2)
        self.p3lbl.grid(row = 2, column = 3)
        self.m2lbl.grid(row = 2, column = 4)
        self.m3lbl.grid(row = 2, column = 5)
        self.m4lbl.grid(row = 2, column = 6)
        self.p4lbl.grid(row = 2, column = 7)
        self.m5lbl.grid(row = 2, column = 8)
        self.m6lbl.grid(row = 2, column = 9)
        self.m7lbl.grid(row = 2, column = 10)
        self.m8lbl.grid(row = 2, column = 11)

        self.p1btn.grid(row = 3, column = 0, ipadx = 8)
        self.p2btn.grid(row = 3, column = 1, ipadx = 8)
        self.m1btn.grid(row = 3, column = 2, ipadx = 8)
        self.p3btn.grid(row = 3, column = 3, ipadx = 8)
        self.m2btn.grid(row = 3, column = 4, ipadx = 8)
        self.m3btn.grid(row = 3, column = 5, ipadx = 8)
        self.m4btn.grid(row = 3, column = 6, ipadx = 8)
        self.p4btn.grid(row = 3, column = 7, ipadx = 8)
        self.m5btn.grid(row = 3, column = 8, ipadx = 8)
        self.m6btn.grid(row = 3, column = 9, ipadx = 8)
        self.m7btn.grid(row = 3, column = 10, ipadx = 8)
        self.m8btn.grid(row = 3, column = 11, ipadx = 8)

        self.c1lbl.grid(row = 5, column = 0, ipadx = 6)
        self.c1ent.grid(row = 5, column = 1, ipadx = 6)
        self.c2lbl.grid(row = 5, column = 2, ipadx = 6)
        self.c2ent.grid(row = 5, column = 3, ipadx = 6)
        self.c3lbl.grid(row = 5, column = 4, ipadx = 6)
        self.c3ent.grid(row = 5, column = 5, ipadx = 6)
        self.c4lbl.grid(row = 5, column = 6, ipadx = 6)
        self.c4ent.grid(row = 5, column = 7, ipadx = 6)
        self.emptylbl.grid(row = 5, column = 8, columnspan = 4)

        self.errorlbl.grid(row = 5, column = 8)
        self.errorEnt.grid(row = 5, column = 9)
        self.errorText.grid(row = 4, column = 0, columnspan = 11, pady = 10)

        for i in self.elementArrow:
            i.grid_remove()






if __name__ == '__main__':
    root = tk.Tk()
    q = gui(root)
    q.mainloop()
