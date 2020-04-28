from encoder import *
from decoder import *
from characters import *
from signals_functions import *

characters = read_chars()
list_chars = list(characters.values())

String = 'a a'
y = encode(String, characters)
write_wav_signal(y, "ex.wav")

r = read_wav_signal("ex.wav")


# print(decode_fft(r, list_chars))

# print(decode_BPF(r, list_chars))
