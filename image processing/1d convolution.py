import numpy as np
import matplotlib.pyplot as plt
import sys
import getopt as go


def convolution_1d(signal, kernel):
    """
    Performs 1D convolution between a signal and a kernel.

    signalgs:
    - signal (list or numpy signalray): The input signal.
    - kernel (list or numpy signalray): The convolution kernel.

    Returns:
    - conv_result (list): The result of the convolution operation.
    """
    signal_length = len(signal)
    kernel_size = len(kernel)
    conv_result_length = signal_length - kernel_size + 1
    conv_result = [0] * conv_result_length

    # Perform the convolution
    for i in range(conv_result_length):
        for j in range(kernel_size):
            conv_result[i] += signal[i + j] * kernel[j]

    return conv_result


if __name__ == "__main__":
    datasize = 20
    vval = 0.3333
    np.random.seed(0)

    kernel = [vval, vval, vval]
    signal = [np.random.randint(10) for i in range(datasize)]
    padded_signal = np.pad(signal, pad_width=2, mode='constant', constant_values=0)

    # Pad the signal to handle edge cases

    result = convolution_1d(padded_signal, kernel)
    # numpy convolve automatically pads the signal
    result_of_numpy = np.convolve(signal, kernel)
    plt.plot(padded_signal)
    plt.plot(result_of_numpy)
    plt.plot(result)

    plt.show()
