from PyQt5 import QtWidgets
from gui import Ui_MainWindow
import sys

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.bitArray = [self.ui.p1lbl, self.ui.p2lbl, self.ui.p3lbl, self.ui.p4lbl,self.ui.c1lbl,\
                        self.ui.c2lbl, self.ui.c3lbl, self.ui.c4lbl, self.ui.errorlbl, self.ui.m1lbl,\
                        self.ui.m2lbl, self.ui.m3lbl, self.ui.m4lbl, self.ui.m5lbl, self.ui.m6lbl,\
                        self.ui.m7lbl, self.ui.m8lbl, self.ui.p1btn, self.ui.p2btn, self.ui.p3btn,\
                        self.ui.p4btn, self.ui.m1btn, self.ui.m2btn, self.ui.m3btn, self.ui.m4btn,\
                        self.ui.m5btn, self.ui.m6btn, self.ui.m7btn, self.ui.m8btn, self.ui.c1ent,\
                        self.ui.c2ent, self.ui.c3ent, self.ui.c4ent, self.ui.errortxt, self.ui.errorent]
        for i in self.bitArray:
            i.setVisible(False)
        
        
        



if __name__ == "__main__":    
    app = QtWidgets.QApplication([])
    applc = window()
    applc.show()
    sys.exit(app.exec())
            