# Copyright 2018 <Quenos Blockchain R&D KFT>

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from PyQt5 import QtCore, QtGui, QtWidgets
from stylesheets.dark_theme import DarkTheme
from config.config import SystemConfiguration

class SettingsDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        sc = SystemConfiguration()
        self.macaroon_directory = ''
        self.tls_directory = ''
        self.lnd_address = ''
        self.lnd_port = ''
        self.setStyleSheet(DarkTheme.get_style_sheet())
        self.setObjectName("Settings")
        self.resize(730, 400)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(280, 310, 341, 50))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 50, 601, 231))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setIndent(-1)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setIndent(-1)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.admin_macaroon = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.admin_macaroon.setObjectName("admin_macaroon")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.admin_macaroon)
        self.tls_cert = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.tls_cert.setObjectName("tls_cert")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tls_cert)
        self.ip_lnd = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ip_lnd.setObjectName("ip_lnd")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ip_lnd)
        self.port_lnd = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.port_lnd.setObjectName("port_lnd")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.port_lnd)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setIndent(-1)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.macaroon_file_button = QtWidgets.QPushButton(self)
        self.macaroon_file_button.setGeometry(QtCore.QRect(650, 50, 44, 41))
        self.macaroon_file_button.setObjectName("macaroon_file_button")
        self.tls_file_button = QtWidgets.QPushButton(self)
        self.tls_file_button.setGeometry(QtCore.QRect(650, 110, 44, 41))
        self.tls_file_button.setObjectName("tls_file_button")

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.macaroon_file_button.clicked.connect(lambda: self.show_file_dialog('macaroon'))
        self.tls_file_button.clicked.connect(lambda: self.show_file_dialog('tls'))

        self.setWindowTitle("Dialog")
        self.label.setText("admin.macaroon:")
        self.label_2.setText("tls.cert:")
        self.label_3.setText("ip address LND:")
        self.admin_macaroon.setText(sc.admin_macaroon_directory)
        self.admin_macaroon.setToolTip("Directory of admin.macaroon")
        self.tls_cert.setText(sc.tls_cert_directory)
        self.tls_cert.setToolTip("Directory of the tls certificate")
        self.ip_lnd.setText(sc.lnd_rpc_address)
        self.ip_lnd.setToolTip("IP address where the node is hosted")
        self.port_lnd.setText(sc.lnd_rpc_port)
        self.port_lnd.setToolTip("Port at which LND node is listening for rpc commands")
        self.port_lnd.setText("10009")
        self.label_4.setText("port:")
        self.macaroon_file_button.setText("...")
        self.tls_file_button.setText("...")

    def accept(self):
        self.macaroon_directory = self.admin_macaroon.text()
        self.tls_directory = self.tls_cert.text()
        self.lnd_address = self.ip_lnd.text()
        self.lnd_port = self.port_lnd.text()

        self.hide()
        mb = QtWidgets.QMessageBox()
        mb.about(self, "Settings saved", "Changed settings will take effect after the next restart")

    def reject(self):
        self.hide()

    def show_file_dialog(self, who):
        directory_name = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        if who == "macaroon":
            self.admin_macaroon.setText(directory_name)
        elif who == "tls":
            self.tls_cert.setText(directory_name)
        else:
            raise ValueError
