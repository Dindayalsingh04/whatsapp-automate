from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.name_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_line_edit.setObjectName("name_line_edit")
        self.gridLayout.addWidget(self.name_line_edit, 0, 1, 1, 1)
        self.phone_number_label = QtWidgets.QLabel(self.centralwidget)
        self.phone_number_label.setObjectName("phone_number_label")
        self.gridLayout.addWidget(self.phone_number_label, 1, 0, 1, 1)
        self.phone_number_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_number_line_edit.setObjectName("phone_number_line_edit")
        self.gridLayout.addWidget(self.phone_number_line_edit, 1, 1, 1, 1)
        self.message_label = QtWidgets.QLabel(self.centralwidget)
        self.message_label.setObjectName("message_label")
        self.gridLayout.addWidget(self.message_label, 2, 0, 1, 1)
        self.message_text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.message_text_edit.setObjectName("message_text_edit")
        self.gridLayout.addWidget(self.message_text_edit, 2, 1, 1, 1)
        self.schedule_datetime_label = QtWidgets.QLabel(self.centralwidget)
        self.schedule_datetime_label.setObjectName("schedule_datetime_label")
        self.gridLayout.addWidget(self.schedule_datetime_label, 3, 0, 1, 1)
        self.schedule_datetime_edit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.schedule_datetime_edit.setObjectName("schedule_datetime_edit")
        self.gridLayout.addWidget(self.schedule_datetime_edit, 3, 1, 1, 1)
        self.schedule_datetime_edit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.schedule_datetime_edit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setObjectName("send_button")
        self.gridLayout.addWidget(self.send_button, 4, 0, 1, 2)
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setObjectName("status_label")
        self.gridLayout.addWidget(self.status_label, 5, 0, 1, 2)

        self.centralwidget.setLayout(self.gridLayout) # Setting layout on central widget FIRST
        MainWindow.setCentralWidget(self.centralwidget) # Setting central widget

        self.menubar = QtWidgets.QMenuBar(MainWindow) # THEN creating and setting menubar
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHistory = QtWidgets.QMenu(self.menubar)
        self.menuHistory.setObjectName("menuHistory")
        MainWindow.setMenuBar(self.menubar)
        self.actionTwilio_Settings = QtGui.QAction(MainWindow)
        self.actionTwilio_Settings.setObjectName("actionTwilio_Settings")
        self.actionView_History = QtGui.QAction(MainWindow)
        self.actionView_History.setObjectName("actionView_History")
        self.menuSettings.addAction(self.actionTwilio_Settings)
        self.menuHistory.addAction(self.actionView_History)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHistory.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WhatsApp Scheduler"))
        self.name_label.setText(_translate("MainWindow", "Name:"))
        self.phone_number_label.setText(_translate("MainWindow", "Phone Number:"))
        self.message_label.setText(_translate("MainWindow", "Message:"))
        self.schedule_datetime_label.setText(_translate("MainWindow", "Schedule Time:"))
        self.send_button.setText(_translate("MainWindow", "Schedule Message"))
        self.status_label.setText(_translate("MainWindow", "Ready"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHistory.setTitle(_translate("MainWindow", "History"))
        self.actionTwilio_Settings.setText(_translate("MainWindow", "Twilio Settings"))
        self.actionView_History.setText(_translate("MainWindow", "View History"))