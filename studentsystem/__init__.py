import difflib
import os
import re
import textwrap
import string
import datetime

from PyQt5 import QtWidgets, QtGui
import sys

class edc():
    def fil(self, n):
        print(pow(n,3))

class QAZ():
    def fil(self, n):
        print(pow(n,-3))

class WSX(edc,QAZ):
    def fil(self, n):
        super().fil(n)
    def __bool__(self):
        return True

def displaymatch(match: re.Match):
    if match is None:
        return None
    return '<match: %r, group=%r>' % (match.group(), match.groups())

if __name__ == '__main__':
    # va = re.compile("^[a]")
    # textwrap.wrap()
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget();
    window.show()
    sys.exit(app.exec_())
