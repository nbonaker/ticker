import sys
from PyQt4 import QtGui

class myQLabel(QtGui.QLabel):
    def __init__(self, *args, **kargs):
        super(myQLabel, self).__init__(*args, **kargs)

        self.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored,
                                             QtGui.QSizePolicy.Ignored))


        self.setMinSize(14)
        # self.setMaximumHeight(40)

    def setMinSize(self, minfs):

        f = self.font()
        f.setPixelSize(minfs)
        br = QtGui.QFontMetrics(f).boundingRect(self.text())

        self.setMinimumSize(br.width(), br.height())

    def resizeEvent(self, event):
        super(myQLabel, self).resizeEvent(event)

        if not self.text():
            return

        # --- fetch current parameters ----

        f = self.font()
        cr = self.contentsRect()

        # --- iterate to find the font size that fits the contentsRect ---

        dw = event.size().width() - event.oldSize().width()  # width change
        dh = event.size().height() - event.oldSize().height()  # height change

        fs = max(f.pixelSize(), 1)
        while True:

            f.setPixelSize(fs)
            br = QtGui.QFontMetrics(f).boundingRect(self.text())

            if dw >= 0 and dh >= 0:  # label is expanding

                if br.height() <= cr.height()*0.8 and br.width() <= cr.width()*0.8:
                    fs += 1
                else:
                    f.setPixelSize(max(fs - 1, 1))  # backtrack
                    break

            else:  # label is shrinking

                if br.height() > cr.height()*0.8 or br.width() > cr.width()*0.8:
                    fs -= 1
                else:
                    break

            if fs < 1: break

        # --- update font size ---

        self.setFont(f)

    def update_font(self, sign):
        self.setMinSize(14)
        f = self.font()
        cr = self.contentsRect()

        # --- iterate to find the font size that fits the contentsRect ---

        dw = sign
        dh = sign

        fs = max(f.pixelSize(), 1)
        while True:

            f.setPixelSize(fs)
            br = QtGui.QFontMetrics(f).boundingRect(self.text())

            if dw >= 0 and dh >= 0:  # label is expanding

                if br.height() <= cr.height()*0.8 and br.width() <= cr.width()*0.8:
                    fs += 1
                else:
                    f.setPixelSize(max(fs - 1, 1))  # backtrack
                    break

            else:  # label is shrinking

                if br.height() > cr.height()*0.8 or br.width() > cr.width()*0.8:
                    fs -= 1
                else:
                    break

            if fs < 1: break

        # --- update font size ---

        self.setFont(f)


class letterGrid(QtGui.QWidget):
    def __init__(self, parent):
        super(letterGrid, self).__init__()

        #---- Prepare a Layout ----

        grid = QtGui.QGridLayout()
        self.parent = parent
        if self.parent is not None:
            self.alphabet = self.parent.key_grid.T.tolist()
        else:
            self.alphabet = [['a', 'g', 'm', 's', 'y', '$'], ['b', 'h', 'n', 't', 'z', '#'], ['c', 'i', 'o', 'u', '.', '0'], ['d', 'j', 'p', 'v', ',', '1'], ['e', 'k', 'q', 'w', '?', '2'], ['f', 'l', 'r', 'x', '_', '3']]

        self.letter_boxes = []
        for col in range(len(self.alphabet)):
            boxes = []
            for key in range(len(self.alphabet[col])):
                text = self.alphabet[col][key]
                if text == '$':
                    text = 'Delete'
                if text == '#':
                    text = 'Undo'
                widget = myQLabel(text)
                grid.addWidget(widget, col, key)
                grid.setRowStretch(key, 1)
                grid.setRowMinimumHeight(key, 25)

                widget.setStyleSheet("border: 1px outset black; background-color:")
                widget.update_font(-1)
                widget.update()
                boxes += [widget]
            self.letter_boxes += [boxes]

        self.setLayout(grid)
        self.resize(500, 300)
        # self.update_alpha()

    def update_alpha(self):
        self.alphabet = self.parent.key_grid.T.tolist()
        for col in range(len(self.alphabet)):
            for key in range(len(self.alphabet[col])):
                widget = self.letter_boxes[col][key]
                text = self.alphabet[col][key]
                if text == '$':
                    text = 'Delete'
                if text == '#':
                    text = 'Undo'
                widget.setText(text)
                font = widget.font()
                font.setPixelSize(70)
                widget.setFont(font)
                widget.update_font(-1)
                widget.update()





    def highlight(self, letter):
        letter_col, letter_row = self.index_letter(letter)
        if letter_col is not None:
            for col in range(len(self.alphabet)):
                for box in self.letter_boxes[col]:
                    if col == letter_col:
                        box.setStyleSheet("border: 1px outset black; background-color:#aaaaff")
                    else:
                        box.setStyleSheet("border: 1px outset black; background-color:")

            self.letter_boxes[letter_col][letter_row].setStyleSheet("border: 1px outset black; background-color:#7777ff")


    def index_letter(self, letter):
        col = 0
        for column in self.alphabet:
            if letter in column:
                return (col, column.index(letter))
            col += 1
        return None, None



if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)

    instance = letterGrid(None)
    instance.show()

    sys.exit(app.exec_())