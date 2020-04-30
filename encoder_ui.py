from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

from characters import *
from encoder import *
from signals_functions import *

characters = read_chars()
list_chars = list(characters.values())
string = ''

encoded_signal = None


class Ui_MainWindow(object):

	def enable_btns(self):
		self.generate_signal_btn.setEnabled(False)
		self.plot_btn.setEnabled(True)
		self.listen_btn.setEnabled(True)
		self.more_info_btn.setEnabled(True)
		self.save_btn.setEnabled(True)

	def generate_signal(self):
		global string
		global encoded_signal

		string = str(self.plainTextEdit.toPlainText())
		if len(string) == 0:
			msg = QMessageBox()
			msg.setWindowTitle("Read ERROR")
			msg.setIcon(QMessageBox.Critical)

			msg.setText("Enter a string to Encode")
			x = msg.exec_()
		else:
			encoded_signal = encode(string, characters)
			print("{} is encoded".format(string))
			self.enable_btns()

	def plot_signal(self):
		global encoded_signal
		global string
		x = np.arange(len(encoded_signal))
		my_plot(x, encoded_signal, string)
		msg = QMessageBox()
		msg.setWindowTitle("Encoded Signal of '{}'".format(string))
		msg.setIconPixmap(QPixmap("./images/plot-{}.png".format(string)))
		x = msg.exec_()


	def listen_to_signal(self):
		global encoded_signal
		write_wav_signal(encoded_signal, "./wav_files/audio.wav")
		play_sound("./wav_files/audio.wav")

	def save_signal(self):
		global string
		global encoded_signal
		write_wav_signal(encoded_signal, "./wav_files/audio-saved-{}.wav".format(string))

	def more_info(self):
		pass

	def reset(self):
		global string
		global encoded_signal
		encoded_signal = None
		string = ''
		self.generate_signal_btn.setEnabled(True)
		self.plot_btn.setEnabled(False)
		self.listen_btn.setEnabled(False)
		self.more_info_btn.setEnabled(False)
		self.save_btn.setEnabled(False)
		self.plainTextEdit.clear()


	def setupUi(self, MainWindow):
		MainWindow.setObjectName("DSP - Course Project")
		MainWindow.resize(1055, 830)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(0, -10, 1061, 811))
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap("./images/background.png"))
		self.label.setScaledContents(True)
		self.label.setObjectName("label")
		self.go_to_decoder_btn = QtWidgets.QPushButton(self.centralwidget)
		self.go_to_decoder_btn.setGeometry(QtCore.QRect(840, 20, 201, 51))
		self.go_to_decoder_btn.setAutoFillBackground(False)
		self.go_to_decoder_btn.setStyleSheet("\n"
							  "\n"
							  "    font: 75 8pt \"Orbitron\";\n"
							  " background-color: rgb(172, 172, 172); \n"
							  "    color: white; \n"
							  "    height: 20px;\n"
							  "    width: 60px;\n"
							  "    margin: 1px 0px 1px 0px;\n"
							  "    border: 1px transparent #2A2929;  \n"
							  "    border-radius: 20px")
		self.go_to_decoder_btn.setObjectName("go_to_decoder_btn")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(310, 40, 481, 61))
		self.label_2.setStyleSheet("font: 75 20pt \"Orbitron\";\n"
					      "color: rgb(255, 255, 255)")
		self.label_2.setObjectName("label_2")
		self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
		self.plainTextEdit.setGeometry(QtCore.QRect(130, 160, 801, 91))
		self.plainTextEdit.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
						     "border: 5px solid rgb(172, 172, 172);")
		self.plainTextEdit.setObjectName("plainTextEdit")
		self.plot_btn = QtWidgets.QPushButton(self.centralwidget)
		self.plot_btn.setGeometry(QtCore.QRect(220, 420, 271, 91))
		self.plot_btn.setAutoFillBackground(False)
		self.plot_btn.setStyleSheet("\n"
						"\n"
						"    font: 75 8pt \"Orbitron\";\n"
						" background-color: rgb(172, 172, 172); \n"
						"    color: white; \n"
						"    height: 20px;\n"
						"    width: 60px;\n"
						"    margin: 1px 0px 1px 0px;\n"
						"    border: 1px transparent #2A2929;  \n"
						"    border-radius: 20px\n"
						"\n"
						"\n"
						"")
		self.plot_btn.setObjectName("plot_btn")
		self.more_info_btn = QtWidgets.QPushButton(self.centralwidget)
		self.more_info_btn.setGeometry(QtCore.QRect(580, 550, 271, 91))
		self.more_info_btn.setAutoFillBackground(False)
		self.more_info_btn.setStyleSheet("\n"
						     "\n"
						     "    font: 75 8pt \"Orbitron\";\n"
						     " background-color: rgb(172, 172, 172); \n"
						     "    color: white; \n"
						     "    height: 20px;\n"
						     "    width: 60px;\n"
						     "    margin: 1px 0px 1px 0px;\n"
						     "    border: 1px transparent #2A2929;  \n"
						     "    border-radius: 20px")
		self.more_info_btn.setObjectName("more_info_btn")
		self.save_btn = QtWidgets.QPushButton(self.centralwidget)
		self.save_btn.setGeometry(QtCore.QRect(220, 550, 271, 91))
		self.save_btn.setAutoFillBackground(False)
		self.save_btn.setStyleSheet("\n"
						"\n"
						"    font: 75 8pt \"Orbitron\";\n"
						" background-color: rgb(172, 172, 172); \n"
						"    color: white; \n"
						"    height: 20px;\n"
						"    width: 60px;\n"
						"    margin: 1px 0px 1px 0px;\n"
						"    border: 1px transparent #2A2929;  \n"
						"    border-radius: 20px")
		self.save_btn.setObjectName("save_btn")
		self.listen_btn = QtWidgets.QPushButton(self.centralwidget)
		self.listen_btn.setGeometry(QtCore.QRect(580, 420, 271, 91))
		self.listen_btn.setAutoFillBackground(False)
		self.listen_btn.setStyleSheet("\n"
						  "\n"
						  "    font: 75 8pt \"Orbitron\";\n"
						  " background-color: rgb(172, 172, 172); \n"
						  "    color: white; \n"
						  "    height: 20px;\n"
						  "    width: 60px;\n"
						  "    margin: 1px 0px 1px 0px;\n"
						  "    border: 1px transparent #2A2929;  \n"
						  "    border-radius: 20px")
		self.listen_btn.setObjectName("listen_btn")
		self.generate_signal_btn = QtWidgets.QPushButton(self.centralwidget)
		self.generate_signal_btn.setGeometry(QtCore.QRect(360, 280, 371, 91))
		self.generate_signal_btn.setAutoFillBackground(False)
		self.generate_signal_btn.setStyleSheet("    font: 75 10pt \"Orbitron\";\n"
							    "background-color: rgb(255, 97, 100) ; \n"
							    "    color: white; \n"
							    "    height: 20px;\n"
							    "    width: 60px;\n"
							    "    margin: 1px 0px 1px 0px;\n"
							    "    border: 1px transparent #2A2929;  \n"
							    "    border-radius: 20px\n"
							    "\n"
							    "")
		self.generate_signal_btn.setObjectName("generate_signal_btn")
		self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
		self.reset_btn.setGeometry(QtCore.QRect(460, 660, 171, 71))
		self.reset_btn.setAutoFillBackground(False)
		self.reset_btn.setStyleSheet("    font: 75 10pt \"Orbitron\";\n"
						 "background-color: rgb(255, 97, 100) ; \n"
						 "    color: white; \n"
						 "    height: 20px;\n"
						 "    width: 60px;\n"
						 "    margin: 1px 0px 1px 0px;\n"
						 "    border: 1px transparent #2A2929;  \n"
						 "    border-radius: 20px\n"
						 "\n"
						 "")
		self.reset_btn.setObjectName("reset_btn")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(20, 680, 141, 61))
		self.label_3.setStyleSheet("font: 75 8pt \"Orbitron\";\n"
					      "color: rgb(255, 255, 255)")
		self.label_3.setObjectName("label_3")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1055, 26))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		self.generate_signal_btn.clicked.connect(self.generate_signal)
		self.plot_btn.clicked.connect(self.plot_signal)
		self.save_btn.clicked.connect(self.save_signal)
		self.listen_btn.clicked.connect(self.listen_to_signal)
		# self.more_info_btn.clicked.connect(self.more_info)
		# # self.go_to_decoder_btn.clicked.connect(self.)
		self.reset_btn.clicked.connect(self.reset)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "DSP Course Project"))
		self.go_to_decoder_btn.setText(_translate("MainWindow", "Go To Decoder"))
		self.label_2.setText(_translate("MainWindow", "String Encoder - Phase 1"))
		self.plot_btn.setText(_translate("MainWindow", "Plot The Enecoded Signal"))
		self.more_info_btn.setText(_translate("MainWindow", "More Information"))
		self.save_btn.setText(_translate("MainWindow", "Save The Enecoded Signal"))
		self.listen_btn.setText(_translate("MainWindow", "Listen To The Decoded Signal"))
		self.generate_signal_btn.setText(_translate("MainWindow", "Generate The Encoded Signal"))
		self.reset_btn.setText(_translate("MainWindow", "Reset"))
		self.label_3.setText(_translate("MainWindow", "Done By:\n"
								    "Saleem Hamo\n"
								    "Mohammad Abbas\n"
								    "Ameer Paraskiva"))


if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	ui.reset()
	sys.exit(app.exec_())
