import tkinter as tk
from tkinter import messagebox as mb
from gui import gui 
import re

class engine(gui):
    def __init__(self, window):
        super().__init__(window)
        self.fieldText.trace('w', lambda *args: self.fieldTextfunc())
        self.m_btn_array = [self.m1btn, self.m2btn, self.m3btn, self.m4btn,\
                            self.m5btn, self.m6btn, self.m7btn, self.m8btn]
        self.m_lbl_array = [self.m1lbl, self.m2lbl, self.m3lbl, self.m4lbl,\
                            self.m5lbl, self.m6lbl, self.m7lbl, self.m8lbl]
        self.p_lbl_array = [self.p1lbl, self.p2lbl, self.p3lbl, self.p4lbl]
        self.p_btn_array = [self.p1btn, self.p2btn, self.p3btn, self.p4btn]
        self.c_lbl_array = [self.c1lbl, self.c2lbl, self.c3lbl, self.c4lbl]
        self.c_ent_array = [self.c1ent, self.c2ent, self.c3ent, self.c4ent]


    def fieldTextfunc(self):
        if 0 < len(self.entryField.get()) <= 8:
            a = re.findall('[^01]', self.entryField.get())
            if len(a) == 0:
                self.p_number = self.pFind(self.entryField.get())
                for i in range(len(self.entryField.get())):
                    self.m_btn_array[i].grid()
                    self.m_lbl_array[i].grid()
                    self.m_btn_array[i].config(text = self.entryField.get()[i])
                
                self.errorText.grid()
                
                for i in range(len(self.p_number)):
                    self.p_lbl_array[i].grid()
                    self.p_btn_array[i].grid()
                    self.p_btn_array[i].config(text = self.p_number[i])
                    self.c_lbl_array[i].grid()
                    self.c_ent_array[i].grid()
                for i in range(len(self.p_number)):
                    self.c_ent_array[i].delete(0, tk.END)
                    self.c_ent_array[i].insert(0, '0')
                
                for i in range(len(self.p_number), 4):
                    self.p_btn_array[i].grid_remove()
                    self.p_lbl_array[i].grid_remove()
                    self.c_lbl_array[i].grid_remove()
                    self.c_ent_array[i].grid_remove()
                for i in range(len(self.entryField.get()), 8):
                    self.m_lbl_array[i].grid_remove()
                    self.m_btn_array[i].grid_remove()
                    
            else:
                mb.showwarning(title = 'Ошибка', message = 'Введите двоиичное число')
                self.entryField.delete(0, tk.END)
                for i in self.elementArrow:
                    i.grid_remove()

        elif len(self.entryField.get()) == 0:
            for i in self.elementArrow:
                i.grid_remove()
        else:
            mb.showwarning(title = 'Ошибка', message = 'Превышена длина строки')
            self.entryField.delete(8, tk.END)
    
    def pFind(self, text):
        p = []
        if len(text) == 1:
            p.append(text)
            p.append(text)
            return p
        elif 1 < len(text) <= 4:
            text = text.ljust(4, '0')
            p1 = str((int(text[0])+int(text[1])+int(text[3]))%2)
            p2 = str((int(text[0])+int(text[2])+int(text[3]))%2)
            p3 = str((int(text[1])+int(text[2])+int(text[3]))%2)
            p.append(p1)
            p.append(p2)
            p.append(p3)
            return p
        else:
            text = text.ljust(8, '0')
            p1 = str((int(text[0])+int(text[1])+int(text[3])+int(text[4])+int(text[6]))%2)
            p2 = str((int(text[0])+int(text[2])+int(text[3])+int(text[5])+int(text[6]))%2)
            p3 = str((int(text[1])+int(text[2])+int(text[3])+int(text[7]))%2)
            p4 = str((int(text[4])+int(text[5])+int(text[6])+int(text[7]))%2)
            p.append(p1)
            p.append(p2)
            p.append(p3)
            p.append(p4)
            return p





if __name__ == '__main__':
    root = tk.Tk()
    q = engine(root)
    q.mainloop()



