import numpy as np
import re

def encode(string, chars):
	fs = 10000  # samples per second
	T = 0.04  # sample duration (seconds)
	n = np.arange(0, fs * T, 1)
	string = string.lower()
	string = re.sub(r'\W', " ", string)

	y = []
	for i in range(0, len(string)):
		x = np.cos(2 * np.pi * chars[string[i]]['low'] * n / fs) + np.cos(
			2 * np.pi * chars[string[i]]['middle'] * n / fs) + np.cos(
			2 * np.pi * chars[string[i]]['high'] * n / fs)
		y = np.concatenate([y, x])
	# print(len(y))

	return y, string
