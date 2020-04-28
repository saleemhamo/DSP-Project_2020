from scipy.io import wavfile
from scipy.signal import butter, lfilter
from scipy.signal import freqz
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft
from signals_functions import *


def butter_bandpass(lowcut, highcut, fs, order=5):
	nyq = 0.5 * fs
	low = lowcut / nyq
	high = highcut / nyq
	b, a = butter(order, [low, high], btype='band')
	return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
	b, a = butter_bandpass(lowcut, highcut, fs, order=order)
	y = lfilter(b, a, data)
	return y


def BPF(y_data, center, start, end):
	lowcut = center - 50
	highcut = center + 50
	fs = 10000.0
	for order in [3, 6, 9]:
		b, a = butter_bandpass(lowcut, highcut, fs, order=order)
	x = y_data[start:end]
	y = butter_bandpass_filter(x, lowcut, highcut, fs, order=6)
	return y


def check_freq(y_data, center, start, end):
	y = BPF(y_data, center, start, end)
	z = np.array(y)
	yf = fft(z)
	# my_plot_2(yf)

	for k in range(0, int(len(yf) / 2)):
		if int(abs(yf[k])) > 100:
			if k * 25 > center - 10 & k * 25 < center + 10:
				return True
	return False
