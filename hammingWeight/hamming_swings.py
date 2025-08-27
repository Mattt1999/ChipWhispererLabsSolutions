import numpy as np
import matplotlib.pylab as plt

aes_traces_100_tracedata = np.load(r"traces/lab3_1_traces.npy")
aes_traces_100_textindata = np.load(r"traces/lab3_1_textin.npy")

trace_array = aes_traces_100_tracedata
textin_array = aes_traces_100_textindata

one_list = []
zero_list = []

for i in range(len(trace_array)):
    if textin_array[i][0] == 0x00:
        zero_list.append(trace_array[i])
    else:
        one_list.append(trace_array[i])

trace_length = len(one_list[0])
print("Traces had original sample length of %d"%trace_length)


one_avg = np.mean(one_list, axis=0)
zero_avg = np.mean(zero_list, axis=0)

if len(one_avg) != trace_length:
    raise ValueError("Average length is only %d - check you did correct dimensions!"%one_avg)

plt.figure()
plt.plot(one_avg-zero_avg, 'r')
plt.show()
