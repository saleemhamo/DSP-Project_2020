def read_chars():
	chars = {}
	chars_file = open('chars.txt', "r+")
	for i in range(0, 27):
		line = chars_file.readline()
		char = line.split(' ')
		# print(int(char[1]) + int(char[1])+int(char[3]))
		chars[char[0]] = {'char': char[0], 'low': int(char[1]), 'middle': int(char[2]), 'high': int(char[3])}

	chars[' '] = chars.pop('space')
	chars[' ']['char'] = ' '
	return chars
