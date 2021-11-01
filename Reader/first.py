# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 设置“抓取设置”区域
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 431, 121))
        self.groupBox.setObjectName("groupBox")
        # 对“设置期数”控件进行设置
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        # 对“选择路径”标签进行设置
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        # 对“选择保存路径”文本框进行设置
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(160, 60, 201, 20))
        self.lineEdit.setObjectName("lineEdit")
        # 对“设置期数”控件进行设置
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 30, 100, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(265, 31, 150, 16))
        # self.label_3.setObjectName("label_3")
        # 对“确定”按钮进行设置
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(340, 90, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setStyleSheet("")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        # 对“选择”按钮进行设置
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 60, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        # 对“选项卡”进行设置
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 140, 431, 355))
        self.tabWidget.setObjectName("tabWidget")
        # 设置“选项卡”的第一个tab，加入QTabWidget表格
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        # 对QTabWidget表格进行设置
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(8, 5, 410, 295))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        # 设置第一列宽度
        self.tableWidget.setColumnWidth(0,130)
        # 设置自动填充容器
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # 设置垂直滚动条
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy()) # 版本api调整
        self.tabWidget.addTab(self.tab, "")
        # 设置“选项卡”的第二个tab，加入QTabWidget列表
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(8, 5, 410, 295))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        self.listWidget.setFont(font)
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode) # 版本api调整
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab_2, "")
        self.listWidget.setIconSize(QtCore.QSize(72,72)) # 图标大小
        self.listWidget.setMaximumHeight(800) # 最大宽度
        self.listWidget.setSpacing(12) # 间距大小
        # 显示垂直滚动条
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy()) # 版本api调整
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RCQ读者书库--阅读使人进步"))
        self.groupBox.setTitle(_translate("MainWindow", "抓取设置")) # 设置分组匡文本
        self.pushButton.setText(_translate("MainWindow", "确定"))  #设置按钮文本
        self.label.setText(_translate("MainWindow", "请选择抓取期数：")) # 设置标签文本
        # 设置默认路径为当前路径
        self.lineEdit.setText(_translate("MainWindow", os.getcwd()))
        # 获取当前年份和月份
        strDate = (str)(time.localtime().tm_year) + "-" + (str)(time.localtime().tm_mon)
        self.lineEdit_2.setText(_translate("MainWindow", strDate)) # 设置默认期数
        # 设置标签文本
        self.label_2.setText(_translate("MainWindow", "请选择保存路径："))
        # 设置标签文本
        self.label_3.setText(_translate("MainWindow", "(期数范围为0-24)"))
        # 设置按钮文本
        self.pushButton_2.setText(_translate("MainWindow", "选择"))
        item = self.tableWidget.horizontalHeaderItem(0)  # 获取表格第一列
        item.setText(_translate("MainWindow", "期数"))   # 设置表格第一列的标题
        item = self.tableWidget.horizontalHeaderItem(1)  # 获取表格的第二列
        item.setText(_translate("MainWindow", "名称"))   # 设置表格第二列的标题
        # 设置第一个选项卡的标题
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "按期数显示"))
        # 设置第二个选项卡的标题
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "按名称显示"))

# 主方法，程序从此处启动pyqt5的窗体
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # 创建窗体对象
    MainWindow = QtWidgets.QMainWindow()
    # 创建pyqt5的窗体对象
    ui = Ui_MainWindow()
    # 调用pyqt5窗体的方法对窗体对象进行初始化设置
    ui.setupUi(MainWindow)
    # 显示窗体
    MainWindow.show()
    # 程序关闭时退出进程
    sys.exit(app.exec_())
