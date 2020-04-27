from encoder import *
from decoder import *

from characters import *
from signals_functions import *

characters = read_chars()
list_chars = list(characters.values())

String = 'heey,yyy'
y = encode(String, characters)
write_wav_signal(y)

r = read_wav_signal()
print(decode_fft(r, list_chars))
