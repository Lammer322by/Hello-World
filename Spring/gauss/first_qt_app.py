from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QWidget, QLabel
import numpy as np
import sys
import gauss


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Eqations solver")
        layout = QVBoxLayout()
        
        if len(sys.argv)!=2:
            self.mxSize = 3
        else:
            self.mxSize = int(sys.argv[1])
        
        mxAGrid = QGridLayout()
        mxBGrid = QGridLayout()
        self.solve = QPushButton("Solve!")
        label1 = QLabel("Type coefficents:")
        label2 = QLabel("Type values:")
        label3 = QLabel("Your answer is:")
        self.answer = QLabel("")

        self.matrixA = np.zeros((self.mxSize, self.mxSize), dtype=float)
        self.matrixB = np.zeros(self.mxSize, dtype=float)
        self.inputList = np.empty((self.mxSize + 1, self.mxSize), dtype=QLineEdit)
        
        for i in range(self.mxSize):
            for j in range(self.mxSize):
                box = QLineEdit()
                box.setMaxLength(12)
                box.setPlaceholderText('0')
                box.textChanged.connect(self.numIn)
                box.textEdited.connect(self.numIn)
                self.inputList[i, j] = box
                mxAGrid.addWidget(box, i, j)

        for i in range(self.mxSize):
                box = QLineEdit()
                box.setMaxLength(6)
                box.setPlaceholderText('0')
                box.textChanged.connect(self.numIn)
                box.textEdited.connect(self.numIn)
                self.inputList[self.mxSize, i] = box
                mxBGrid.addWidget(box, 0, i)

        layout.addWidget(label1)
        layout.addLayout(mxAGrid)
        layout.addWidget(label2)
        layout.addLayout(mxBGrid)
        layout.addWidget(self.solve)
        layout.addWidget(label3)
        layout.addWidget(self.answer)

        mxAGrid.setContentsMargins(5, 5, 5, 20)
        mxBGrid.setContentsMargins(5, 5, 5, 20)
        self.solve.setCheckable(True)
        self.solve.clicked.connect(self.calculate)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def numIn(self, s):
        sender = self.sender()
        pos = np.where(self.inputList == sender)
        try:
            s = float(s)
        except ValueError:
            s = 0
        if pos[0] < self.mxSize:
            self.matrixA[pos] = s
        elif pos[0] == self.mxSize:
            self.matrixB[pos[1]] = s

    def calculate(self):
        self.solve.setCheckable(False)
        for box in self.inputList.flat:
            box.setReadOnly(True)
        res = gauss.gauss(self.matrixA, self.matrixB)
        self.solve.setCheckable(True)
        for box in self.inputList.flat:
            box.setReadOnly(False)
        out = ''
        for i in range(1, self.mxSize + 1):
            out += ('x' + str(i) + ' = ' + str(res[i-1]) + ';   ')
        self.answer.setText(out)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
