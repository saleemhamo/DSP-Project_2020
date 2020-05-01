from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from characters import *
from encoder import *
from signals_functions import *
from decoder import *

characters = read_chars()
list_chars = list(characters.values())
string = ''
encoded_signal = None
wav_signal = None
decoded_string = ""

file_name = None


class Ui_MainWindow(object):

	def decode_fft(self):
		global decoded_frequencies
		global decoded_string
		decoded_string, decoded_frequencies = decode_fft(wav_signal, list_chars, fs=10000)
		msg = QMessageBox()
		msg.setWindowTitle("Decoded String")
		msg.setText(decoded_string)
		x = msg.exec_()

	def decode_bpf(self):
		global decoded_frequencies
		global decoded_string
		decoded_string, decoded_frequencies = decode_fft(wav_signal, list_chars, fs=10000)
		msg = QMessageBox()
		msg.setWindowTitle("Decoded String")
		msg.setText(decoded_string)
		x = msg.exec_()

	def view_decoded_string(self):
		global decoded_string
		msg = QMessageBox()
		msg.setWindowTitle("Decoded String")
		msg.setText(decoded_string)
		x = msg.exec_()

	def more_info_decoder(self):
		global decoded_string
		msg = QMessageBox()
		msg.setWindowTitle("Information")
		msg.setText("The decoded String is : '{}'\n"
			     "The signal is consisted of {} samples"
			     "It was sampled at a sampling frequency = 10000Hz\n"
			     "It has {} charachters Each character is encoded to 40ms signal consinsts of 3 sinosoidal signals carrying the correspinding frequencies for that character\n"
			     "Number of samples/char = 400".format(decoded_string, len(wav_signal), len(decoded_string)))
		x = msg.exec_()

	def display_freq(self):
		global decoded_frequencies
		msg = QMessageBox()
		msg.setWindowTitle("Frequencies")
		msg.setText(decoded_frequencies)
		x = msg.exec_()

	def listen_decoder(self):
		global wav_signal
		write_wav_signal(wav_signal, "./wav_files/audio.wav")
		play_sound("./wav_files/audio.wav")

	def plot_decoder(self):
		global wav_signal
		global string
		x = np.arange(len(wav_signal))
		my_plot(x, wav_signal, "decoded")
		msg = QMessageBox()
		msg.setWindowTitle("Decoded Signal")
		msg.setIconPixmap(QPixmap("./images/plot-decoded.png"))
		x = msg.exec_()

	def reset_decoder(self):
		global wav_signal
		global decoded_string
		global file_name
		wav_signal = None
		decoded_string = ""
		file_name = None
		self.browse_btn.setEnabled(True)
		self.decode_ft_btn.setEnabled(False)
		self.decode_bpf_btn.setEnabled(False)
		self.more_info_btn_2.setEnabled(False)
		self.display_freq_btn.setEnabled(False)
		self.listen_btn_3.setEnabled(False)
		self.plot_btn_3.setEnabled(False)
		self.view_btn.setEnabled(False)

	def enable_btns_decoder(self):
		self.browse_btn.setEnabled(False)
		self.decode_ft_btn.setEnabled(True)
		self.decode_bpf_btn.setEnabled(True)
		self.more_info_btn_2.setEnabled(True)
		self.display_freq_btn.setEnabled(True)
		self.listen_btn_3.setEnabled(True)
		self.plot_btn_3.setEnabled(True)
		self.view_btn.setEnabled(True)

	def browse_file(self):
		global wav_signal
		global file_name
		file_name = QFileDialog.getOpenFileName()
		if file_name is not None:
			path = file_name[0]
			wav_signal = read_wav_signal(path)
		else:
			msg = QMessageBox()
			msg.setWindowTitle("Read ERROR")
			msg.setIcon(QMessageBox.Critical)
			msg.setText("Invalid File!")
			x = msg.exec_()

		self.enable_btns()

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
			encoded_signal, string = encode(string, characters)
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
		global string
		msg = QMessageBox()
		msg.setWindowTitle("Information")
		msg.setText("The String to encode is : '{}'\n"
			     "It was sampled at a sampling frequency = 10000Hz\n"
			     "Each character is encoded to 40ms signal consinsts of 3 sinosoidal signals carrying the correspinding frequencies for that character\n"
			     "".format(string))
		x = msg.exec_()

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
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1028, 840)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.tabs = QtWidgets.QTabWidget(self.centralwidget)
		self.tabs.setGeometry(QtCore.QRect(0, 0, 1051, 821))
		self.tabs.setStyleSheet("QTabBar::tab { height: 30px; width: 500px;}")
		self.tabs.setTabPosition(QtWidgets.QTabWidget.North)
		self.tabs.setTabShape(QtWidgets.QTabWidget.Triangular)
		self.tabs.setIconSize(QtCore.QSize(20, 20))
		self.tabs.setElideMode(QtCore.Qt.ElideMiddle)
		self.tabs.setDocumentMode(False)
		self.tabs.setTabsClosable(False)
		self.tabs.setMovable(True)
		self.tabs.setTabBarAutoHide(False)
		self.tabs.setObjectName("tabs")
		self.tab_1 = QtWidgets.QWidget()
		self.tab_1.setEnabled(True)
		self.tab_1.setAutoFillBackground(False)
		self.tab_1.setObjectName("tab_1")
		self.plot_btn = QtWidgets.QPushButton(self.tab_1)
		self.plot_btn.setGeometry(QtCore.QRect(190, 430, 271, 91))
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
		self.label_2 = QtWidgets.QLabel(self.tab_1)
		self.label_2.setGeometry(QtCore.QRect(310, 50, 481, 61))
		self.label_2.setStyleSheet("font: 75 20pt \"Orbitron\";\n"
					      "color: rgb(255, 255, 255)")
		self.label_2.setObjectName("label_2")
		self.label = QtWidgets.QLabel(self.tab_1)
		self.label.setGeometry(QtCore.QRect(-10, -10, 1071, 801))
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap("images/background.png"))
		self.label.setScaledContents(True)
		self.label.setObjectName("label")
		self.save_btn = QtWidgets.QPushButton(self.tab_1)
		self.save_btn.setGeometry(QtCore.QRect(190, 530, 271, 91))
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
		self.listen_btn = QtWidgets.QPushButton(self.tab_1)
		self.listen_btn.setGeometry(QtCore.QRect(530, 430, 271, 91))
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
		self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_1)
		self.plainTextEdit.setGeometry(QtCore.QRect(100, 140, 801, 91))
		self.plainTextEdit.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
						     "border: 5px solid rgb(172, 172, 172);")
		self.plainTextEdit.setObjectName("plainTextEdit")
		self.label_3 = QtWidgets.QLabel(self.tab_1)
		self.label_3.setGeometry(QtCore.QRect(20, 690, 141, 61))
		self.label_3.setStyleSheet("font: 75 8pt \"Orbitron\";\n"
					      "color: rgb(255, 255, 255)")
		self.label_3.setObjectName("label_3")
		self.generate_signal_btn = QtWidgets.QPushButton(self.tab_1)
		self.generate_signal_btn.setGeometry(QtCore.QRect(310, 300, 371, 91))
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
		self.reset_btn = QtWidgets.QPushButton(self.tab_1)
		self.reset_btn.setGeometry(QtCore.QRect(410, 650, 171, 71))
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
		self.more_info_btn = QtWidgets.QPushButton(self.tab_1)
		self.more_info_btn.setGeometry(QtCore.QRect(530, 530, 271, 91))
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
		self.label.raise_()
		self.plot_btn.raise_()
		self.label_2.raise_()
		self.save_btn.raise_()
		self.listen_btn.raise_()
		self.plainTextEdit.raise_()
		self.label_3.raise_()
		self.generate_signal_btn.raise_()
		self.reset_btn.raise_()
		self.more_info_btn.raise_()
		self.tabs.addTab(self.tab_1, "")
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.label_4 = QtWidgets.QLabel(self.tab_2)
		self.label_4.setGeometry(QtCore.QRect(-10, -10, 1071, 801))
		self.label_4.setText("")
		self.label_4.setPixmap(QtGui.QPixmap("images/background.png"))
		self.label_4.setScaledContents(True)
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(self.tab_2)
		self.label_5.setGeometry(QtCore.QRect(300, 50, 481, 61))
		self.label_5.setStyleSheet("font: 75 20pt \"Orbitron\";\n"
					      "color: rgb(255, 255, 255)")
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(self.tab_2)
		self.label_6.setGeometry(QtCore.QRect(10, 690, 141, 61))
		self.label_6.setStyleSheet("font: 75 8pt \"Orbitron\";\n"
					      "color: rgb(255, 255, 255)")
		self.label_6.setObjectName("label_6")
		self.browse_btn = QtWidgets.QPushButton(self.tab_2)
		self.browse_btn.setGeometry(QtCore.QRect(210, 170, 611, 71))
		self.browse_btn.setAutoFillBackground(False)
		self.browse_btn.setStyleSheet("    font: 75 10pt \"Orbitron\";\n"
						  "background-color: rgb(255, 97, 100) ; \n"
						  "    color: white; \n"
						  "    height: 20px;\n"
						  "    width: 60px;\n"
						  "    margin: 1px 0px 1px 0px;\n"
						  "    border: 1px transparent #2A2929;  \n"
						  "    border-radius: 20px\n"
						  "\n"
						  "")
		self.browse_btn.setObjectName("browse_btn")
		self.decode_ft_btn = QtWidgets.QPushButton(self.tab_2)
		self.decode_ft_btn.setGeometry(QtCore.QRect(150, 270, 331, 71))
		self.decode_ft_btn.setAutoFillBackground(False)
		self.decode_ft_btn.setStyleSheet("    font: 75 10pt \"Orbitron\";\n"
						     "background-color: rgb(255, 97, 100) ; \n"
						     "    color: white; \n"
						     "    height: 20px;\n"
						     "    width: 60px;\n"
						     "    margin: 1px 0px 1px 0px;\n"
						     "    border: 1px transparent #2A2929;  \n"
						     "    border-radius: 20px\n"
						     "\n"
						     "")
		self.decode_ft_btn.setObjectName("decode_ft_btn")
		self.decode_bpf_btn = QtWidgets.QPushButton(self.tab_2)
		self.decode_bpf_btn.setGeometry(QtCore.QRect(530, 270, 331, 71))
		self.decode_bpf_btn.setAutoFillBackground(False)
		self.decode_bpf_btn.setStyleSheet("    font: 75 10pt \"Orbitron\";\n"
						      "background-color: rgb(255, 97, 100) ; \n"
						      "    color: white; \n"
						      "    height: 20px;\n"
						      "    width: 60px;\n"
						      "    margin: 1px 0px 1px 0px;\n"
						      "    border: 1px transparent #2A2929;  \n"
						      "    border-radius: 20px\n"
						      "\n"
						      "")
		self.decode_bpf_btn.setObjectName("decode_bpf_btn")
		self.more_info_btn_2 = QtWidgets.QPushButton(self.tab_2)
		self.more_info_btn_2.setGeometry(QtCore.QRect(540, 570, 271, 91))
		self.more_info_btn_2.setAutoFillBackground(False)
		self.more_info_btn_2.setStyleSheet("\n"
							"\n"
							"    font: 75 8pt \"Orbitron\";\n"
							" background-color: rgb(172, 172, 172); \n"
							"    color: white; \n"
							"    height: 20px;\n"
							"    width: 60px;\n"
							"    margin: 1px 0px 1px 0px;\n"
							"    border: 1px transparent #2A2929;  \n"
							"    border-radius: 20px")
		self.more_info_btn_2.setObjectName("more_info_btn_2")
		self.display_freq_btn = QtWidgets.QPushButton(self.tab_2)
		self.display_freq_btn.setGeometry(QtCore.QRect(200, 570, 271, 91))
		self.display_freq_btn.setAutoFillBackground(False)
		self.display_freq_btn.setStyleSheet("\n"
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
		self.display_freq_btn.setObjectName("display_freq_btn")
		self.listen_btn_3 = QtWidgets.QPushButton(self.tab_2)
		self.listen_btn_3.setGeometry(QtCore.QRect(540, 460, 271, 91))
		self.listen_btn_3.setAutoFillBackground(False)
		self.listen_btn_3.setStyleSheet("\n"
						    "\n"
						    "    font: 75 8pt \"Orbitron\";\n"
						    " background-color: rgb(172, 172, 172); \n"
						    "    color: white; \n"
						    "    height: 20px;\n"
						    "    width: 60px;\n"
						    "    margin: 1px 0px 1px 0px;\n"
						    "    border: 1px transparent #2A2929;  \n"
						    "    border-radius: 20px")
		self.listen_btn_3.setObjectName("listen_btn_3")
		self.plot_btn_3 = QtWidgets.QPushButton(self.tab_2)
		self.plot_btn_3.setGeometry(QtCore.QRect(200, 460, 271, 91))
		self.plot_btn_3.setAutoFillBackground(False)
		self.plot_btn_3.setStyleSheet("\n"
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
		self.plot_btn_3.setObjectName("plot_btn_3")
		self.view_btn = QtWidgets.QPushButton(self.tab_2)
		self.view_btn.setGeometry(QtCore.QRect(280, 360, 471, 51))
		self.view_btn.setAutoFillBackground(False)
		self.view_btn.setStyleSheet("    font: 75 10pt \"Orbitron\";\n"
						"background-color: rgb(255, 97, 100) ; \n"
						"    color: white; \n"
						"    height: 20px;\n"
						"    width: 60px;\n"
						"    margin: 1px 0px 1px 0px;\n"
						"    border: 1px transparent #2A2929;  \n"
						"    border-radius: 20px\n"
						"\n"
						"")
		self.view_btn.setObjectName("view_btn")
		self.reset_btn_2 = QtWidgets.QPushButton(self.tab_2)
		self.reset_btn_2.setGeometry(QtCore.QRect(430, 670, 171, 71))
		self.reset_btn_2.setAutoFillBackground(False)
		self.reset_btn_2.setStyleSheet("    font: 75 10pt \"Orbitron\";\n"
						   "background-color: rgb(255, 97, 100) ; \n"
						   "    color: white; \n"
						   "    height: 20px;\n"
						   "    width: 60px;\n"
						   "    margin: 1px 0px 1px 0px;\n"
						   "    border: 1px transparent #2A2929;  \n"
						   "    border-radius: 20px\n"
						   "\n"
						   "")
		self.reset_btn_2.setObjectName("reset_btn_2")
		self.tabs.addTab(self.tab_2, "")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1028, 26))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		self.tabs.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		self.generate_signal_btn.clicked.connect(self.generate_signal)
		self.plot_btn.clicked.connect(self.plot_signal)
		self.save_btn.clicked.connect(self.save_signal)
		self.listen_btn.clicked.connect(self.listen_to_signal)
		self.more_info_btn.clicked.connect(self.more_info)
		self.reset_btn.clicked.connect(self.reset)

		self.decode_ft_btn.clicked.connect(self.decode_fft)
		self.decode_bpf_btn.clicked.connect(self.decode_bpf)
		self.more_info_btn_2.clicked.connect(self.more_info_decoder)
		self.display_freq_btn.clicked.connect(self.display_freq)
		self.listen_btn_3.clicked.connect(self.listen_decoder)
		self.plot_btn_3.clicked.connect(self.plot_decoder)
		self.reset_btn_2.clicked.connect(self.reset_decoder)
		self.browse_btn.clicked.connect(self.browse_file)
		self.view_btn.clicked.connect(self.view_decoded_string)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.plot_btn.setText(_translate("MainWindow", "Plot The Enecoded Signal"))
		self.label_2.setText(_translate("MainWindow", "String Encoder - Phase 1"))
		self.save_btn.setText(_translate("MainWindow", "Save The Enecoded Signal"))
		self.listen_btn.setText(_translate("MainWindow", "Listen To The Decoded Signal"))
		self.label_3.setText(_translate("MainWindow", "Done By:\n"
								    "Saleem Hamo\n"
								    "Mohammad Abbas\n"
								    "Ameer Paraskiva"))
		self.generate_signal_btn.setText(_translate("MainWindow", "Generate The Encoded Signal"))
		self.reset_btn.setText(_translate("MainWindow", "Reset"))
		self.more_info_btn.setText(_translate("MainWindow", "More Information"))
		self.tabs.setTabText(self.tabs.indexOf(self.tab_1), _translate("MainWindow", "Encoder"))
		self.label_5.setText(_translate("MainWindow", "String Decoder - Phase 2"))
		self.label_6.setText(_translate("MainWindow", "Done By:\n"
								    "Saleem Hamo\n"
								    "Mohammad Abbas\n"
								    "Ameer Paraskiva"))
		self.browse_btn.setText(_translate("MainWindow", "Browse WAV File"))
		self.decode_ft_btn.setText(_translate("MainWindow", "Decode Using FT"))
		self.decode_bpf_btn.setText(_translate("MainWindow", "Decode Using BPF"))
		self.more_info_btn_2.setText(_translate("MainWindow", "More Information"))
		self.display_freq_btn.setText(_translate("MainWindow", "Display All Carried Frequencies "))
		self.listen_btn_3.setText(_translate("MainWindow", "Listen To The Signal"))
		self.plot_btn_3.setText(_translate("MainWindow", "Plot The Signal"))
		self.view_btn.setText(_translate("MainWindow", "View The Decoded String"))
		self.reset_btn_2.setText(_translate("MainWindow", "Reset"))
		self.tabs.setTabText(self.tabs.indexOf(self.tab_2), _translate("MainWindow", "Decoder"))


if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
