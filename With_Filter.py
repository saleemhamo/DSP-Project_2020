from typing import Dict, List, Any, Union

import matplotlib.pyplot as plt
import numpy as np
import wavio
from numpy.fft import fft


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


def read_chars():
	chars = {}
	chars_file = open('chars.txt', "r+")
	for i in range(0, 27):
		line = chars_file.readline()
		char = line.split(' ')
		chars[char[0]] = {'char': char[0], 'low': int(char[1]), 'middle': int(char[2]), 'high': int(char[3])}

	chars[' '] = chars.pop('space')
	return chars


def encode(string, chars):
	fs = 10000  # samples per second
	T = 0.04  # sample duration (seconds)
	n = np.arange(0, fs * T, 1)
	string = string.lower()
	y = []
	for i in range(0, len(string)):
		x = np.cos(2 * np.pi * chars[string[i]]['low'] * n / fs) + np.cos(
			2 * np.pi * chars[string[i]]['middle'] * n / fs) + np.cos(
			2 * np.pi * chars[string[i]]['high'] * n / fs)
		y = np.concatenate([y, x])
	return y


def band_pass_filter(x, center_frequency, bandwidth):
	start = int(center_frequency - bandwidth / 2)
	end = int(center_frequency + bandwidth / 2)
	h = np.concatenate(
		[np.zeros(start, dtype=int), np.ones(end - start, dtype=int), np.zeros(len(x) - end, dtype=int)])
	print(h)
	y = np.multiply(h, x)

	print(y)


# a = np.arange(20)
# print(a)
# band_pass_filter(a, 10, 8)

characters = read_chars()
# print(characters)
String = 'HELLOOOOOOO'
y = encode(String, characters)
m = np.arange(0, len(y), 1)
# my_plot(m, y)

wavio.write("ex.wav", y, 10000, sampwidth=1)
wav = wavio.read("ex.wav")
#
#

list_chars = list(characters.values())

sample_length = len(wav.data)

step = 400
N = 400
T = 0.04
start = 0
end = N

decoded_sting = ''

for c in range(0, int(sample_length / 400)):
	z = y[start:end]
	yf = fft(z)

	start += step
	end += step

	signal = np.arange(0)

	for j in range(0, len(yf)):
		signal = np.concatenate([signal, [abs(yf[j])]])

	band_pass_filter(signal, 100, 20)

# # xf = np.linspace(0.0, 1000.0 / (2.0 * T), N // 2)
# # plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))
# # plt.grid()
# # plt.show()
#
# # freq = []
# # for i in range(0, int(len(yf) / 2)):
# # 	if int(abs(yf[i])) > 10:
# # 		freq.append(i * 25)
# #
# # low = freq[0]
# # middle = freq[1]
# # high = freq[2]
# #
# # for i in range(0, len(characters)):
# # 	if (list_chars[i]['low'] == low) & (list_chars[i]['middle'] == middle) & (list_chars[i]['high'] == high):
# # 		# print(list_chars[i]['char'])
# # 		decoded_sting += list_chars[i]['char']
#
#
# print(decoded_sting)
