import re
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
class Main(QDialog):
    global array7
    array7 = []

    def __init__(self):
        super(Main, self).__init__()
        loadUi('Form.ui', self)
        self.setWindowTitle('Работа с файлами в Python')
        self.pushButton_run.clicked.connect(self.run)
        self.pushButton_clean.clicked.connect(self.clean)
        self.pushButton_load.clicked.connect(self.load)
        self.pushButton_export.clicked.connect(self.export)


    def run(self):
        fm = self.find_max()
        self.textEdit_array.insertPlainText('Max = ' + str(fm[0]) + ' [' + str(fm[1]) + ',' + str(fm[2]) + ']\n' + '\n')
        sum = self.find_sum()
        l = len(str(sum))
        self.textEdit_array.insertPlainText('Sum = ' + str(sum) + '\n' + '\n')
        for i in array7:
            for j in i:
                if j == 0:
                    i[(i.index(j))] = sum
        for i in array7:
            for j in i:
                l2 = len(str(j))
                l1 = l - l2 + 1
                s = ""
                for i in range(l1):
                    s += " "
                self.textEdit_array.insertPlainText(str(j) + s)
            self.textEdit_array.insertPlainText('\n')
        return array7

    def find_sum(self):
        fm = self.find_max()
        sum = 0
        i = 0
        while i <= fm[1]:
            for j in range(5):
                if (i == fm[1]) and (j >= fm[2]):
                    break
                else:
                    sum += array7 [i][j]
            i += 1
        return sum

    def find_max(self):
        col = 0
        row = 0
        itr = 0
        max_num = 0
        for i in array7:
            for j in i:
                if j > max_num:
                    max_num = j
                    row = itr
                    col = i.index(j)
            itr += 1
        return [max_num, row, col]

    def clean(self):
        self.textEdit_array.setPlainText('')


    def export(self):
        ar = self.run()
        out_file = open(u'F:\PSU\Python\ZEA_Lab5\output.txt', 'w')  # открываем файл в режиме записи
        for row in array7:  # перебираем каждую строку массива
            for num in row:  # перебираем каждое значение строки
                out_file.write("%d " % num)  # записываем это значение
            out_file.write('\n')  # дописываем перевод на новую строку


    def load(self):
        global path_to_file
        path_to_file = QFileDialog.getOpenFileName(self, 'Открыть файл', '',
                                                   "Text Files (*.txt)")[0]

        if path_to_file:
            file = open(path_to_file, 'r')

            f = file.read()
            # выводим считанные данные на экран
            self.textEdit_array.insertPlainText("Полученные данные: \n" +
                                               f + "\n")

            array = []
            for num in re.findall(r'\b[0-9]+\b', f):
                array.append(num)
            sub = []
            for i in array:
                sub.append(int(i))
                if len(sub) > 4:
                    array7.append(sub)
                    sub = []
        print(array7)


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()