import matplotlib.pyplot as plt
import numpy as np
import wavio
from scipy.io import wavfile


def my_stem(n, x):
	plt.stem(n, x)
	plt.title("Encoder")
	plt.ylabel("X")
	plt.xlabel("n")
	plt.show()


def my_plot(n, x):
	plt.plot(n, x)
	plt.title("Encoder")
	plt.ylabel("X")
	plt.xlabel("n")
	plt.show()


def write_wav_signal(y):
	length = len(y)
	wavio.write("ex.wav", y, length, sampwidth=1)


def read_wav_signal():
	rate, data = wavfile.read("ex.wav")
	y_data = []
	length = len(data)
	for i in range(0, length):
		y_data.append(0.019961328125 * data[i] - 2.090138671875)
	y_data = np.array(y_data, dtype=float)

	return y_data

# N = 400
# T = 0.04
# xf = np.linspace(0.0, 1000.0 / (2.0 * T), N // 2)
# plt.plot(xf, 2.0 / N * np.abs(y[0:N // 2]))
# plt.grid()
# plt.show()