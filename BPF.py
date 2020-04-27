from scipy.io import wavfile
from scipy.signal import butter, lfilter
from scipy.signal import freqz
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft


# N = 400
# T = 0.04
# z = wav.data[0:400]
# yf = fft(z)
# xf = np.linspace(0.0, 1000.0 / (2.0 * T), N // 2)
# plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))
# plt.grid()
# # plt.show()

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


def run():
    rate, data = wavfile.read("ex.wav")
    y_data = []

    for i in range(0, len(data)):
        y_data.append(0.019961328125 * data[i] - 2.090138671875)

    y_data = np.array(y_data, dtype=float)

    # Sample rate and desired cutoff frequencies (in Hz).
    fs = 10000.0
    lowcut = 100.0
    highcut = 200.0

    # Plot the frequency response for a few different orders.
    plt.figure(1)
    plt.clf()
    for order in [3, 6, 9]:
        b, a = butter_bandpass(lowcut, highcut, fs, order=order)
        w, h = freqz(b, a, worN=2000)
    #     plt.plot((fs * 0.5 / np.pi) * w, abs(h), label="order = %d" % order)
    #
    # plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)],
    #          '--', label='sqrt(0.5)')
    # plt.xlabel('Frequency (Hz)')
    # plt.ylabel('Gain')
    # plt.grid(True)
    # plt.legend(loc='best')

    # Filter a noisy signal.
    T = 0.04
    nsamples = T * fs

    t = np.linspace(0, T, int(nsamples), endpoint=False)
    a = 0.02
    f0 = 600.0
    x = y_data[0:400]
    # x = 0.1 * np.sin(2 * np.pi * 1.2 * np.sqrt(t))
    # x += 0.01 * np.cos(2 * np.pi * 312 * t + 0.1)
    # x += a * np.cos(2 * np.pi * f0 * t + .11)
    # x += 0.03 * np.cos(2 * np.pi * 2000 * t)
    # plt.figure(2)
    # plt.clf()
    # plt.plot(t, x, label='Noisy signal')

    y = butter_bandpass_filter(x, lowcut, highcut, fs, order=6)
    # plt.plot(t, y, label='Filtered signal (%g Hz)' % f0)
    # plt.xlabel('time (seconds)')
    # plt.hlines([-a, a], 0, T, linestyles='--')
    # plt.grid(True)
    # plt.axis('tight')
    # plt.legend(loc='upper left')
    # plt.show()


    N = 400
    z = np.array(y)
    yf = fft(z)
    xf = np.linspace(0.0, 1000.0 / (2.0 * T), N // 2)
    plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))
    plt.grid()
    plt.show()


    for k in range(0, int(len(yf)/2)):
        if abs(yf[k]) > 100:
            print("Found freq")
            print(int(abs(yf[k])))
            print(k)
            # print("Found freq")
