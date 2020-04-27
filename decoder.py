from numpy.fft import fft


def decode_fft(y_data, list_chars):
	sample_length = len(y_data)
	step = 400
	N = 400
	T = 0.04
	start = 0
	end = N
	decoded_sting = ''
	for c in range(0, int(sample_length / 400)):

		z = y_data[start:end]

		yf = fft(z)
		start += step
		end += step

		freq = []
		for i in range(5, int(len(yf) / 2)):
			if int(abs(yf[i])) > 10:
				freq.append(i * 25)

		low = freq[0]
		middle = freq[1]
		high = freq[2]

		for i in range(0, len(list_chars)):
			if (list_chars[i]['low'] == low) & (list_chars[i]['middle'] == middle) & (
				 list_chars[i]['high'] == high):
				# print(list_chars[i]['char'])
				decoded_sting += list_chars[i]['char']

	return decoded_sting


