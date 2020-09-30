# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:51:48 2019

@author: 220000177
"""

import nidaqmx
import time


class Configure_SW():
    def __init__(self, channel):
        self.SW = nidaqmx.Task()
        resource = 'cDAQ1Mod5/line' + str(channel) + ':' + str(channel)
        self.SW.di_channels.add_di_chan(resource)
    
    def Read_SW(self):
        value = self.SW.read()
        return value
    
    def Free(self):
        self.SW.close()

Start_SW = Configure_SW(0)
Stop_SW = Configure_SW(1)

Flash = nidaqmx.Task()
Flash.do_channels.add_do_chan('cDAQ1Mod7/line0:0')

#First let's store the morse code for the alphabet using a dictionary
Morse = {"A":".-","B":"-...","C":"-.-.", "D":"-..", "E":".", "F":"..-.",
         "G": "--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..",
         "M": "--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.",
         "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-",
         "Y":"-.--", "Z":"--.."}

ENCODE = 'MERRY CHRISTMAS'
MORSE_ENCODE = ''

for i in range(0, len(ENCODE)):
    char = ENCODE[i]
    if char == ' ':
        MORSE_ENCODE = MORSE_ENCODE + '^'
    else:
        MORSE_ENCODE = MORSE_ENCODE + Morse[char] + ' '
    
Start = False
while Start == False:
    Start = Start_SW.Read_SW()
Stop = False    
    
print(MORSE_ENCODE)
print(len(MORSE_ENCODE))
TL = .3         #Standard dot time length & inter-element gap
TL_3 = 3 * TL   #Standard dash time length & short gap (between letters)
TL_7 = 7 * TL   #Gap between words

while Stop == False:
    Stop = Stop_SW.Read_SW()
    for i in range(0, len(MORSE_ENCODE)):
        SL_T = TL
        if MORSE_ENCODE[i] == '.':
            on_time = TL
        elif MORSE_ENCODE[i] == '-':
            on_time = TL_3
        elif MORSE_ENCODE[i] == '^':
            on_time = 0
            SL_T = TL_7
        elif MORSE_ENCODE[i] == ' ':
            on_time = 0
            SL_T = TL_3
        else:
            on_time = 0
            SL_T = 0
        if on_time > 0:
            Flash.write(True)
        time.sleep(on_time)
        Flash.write(False)
        time.sleep(SL_T)
        i += 1
    time.sleep(5)
                      
Start_SW.Free()
Stop_SW.Free()
Flash.close()

