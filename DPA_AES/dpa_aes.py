#capture the traces - this is a simulated lab, so we will use previously captured traces. 
import numpy as np

aes_traces_2500_tracedata = np.load(r"traces/lab3_3_traces.npy")
aes_traces_2500_textindata = np.load(r"traces/lab3_3_textin.npy")

trace_array = aes_traces_2500_tracedata
textin_array = aes_traces_2500_textindata

#the complete attack - assuming the leakage bit is bit 0
from tqdm import tnrange
import numpy as np

#Store your key_guess here, compare to known_key
key_guess = [0] * 16 
known_key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
bit = 0

for subkey in tnrange(0, 16, desc="Attacking Subkey"):    
    
        mean_diffs = [0] * 256

        for byte_guess in range(0, 256):
                one_list=[]
                zero_list=[]

                for trace in range(0, numtraces):
                    input_byte = textin_array[trace][subkey]            
 
                    #this code assumes that the leakage bit is bit 0!

                    hypothetical_leakage = aes_internal(input_byte, byte_guess) 

                    if (hypothetical_leakage & (1 << bit)) == 1:
                        one_list.append(trace_array[trace])
                    else:
                        zero_list.append(trace_array[trace])

                one_avg = np.asarray(one_list).mean(axis=0)
                zero_avg = np.asarray(zero_list).mean(axis=0)

                max_diff_value = np.max(np.abs((one_avg - zero_avg)))
                mean_diffs[byte_guess] = max_diff_value

        ranked_guesses = np.argsort(mean_diffs)[::-1]

        key_guess[subkey] = ranked_guesses[0]
        
for i in range(0, 16):
    print("The key is {:02X}".format(key_guess[i]))
