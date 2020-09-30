# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:08:55 2019

@author: 220000177
"""

import nidaqmx
import matplotlib.pyplot as plt
import time

#plt.ion()  Interactive plot on
i = 0
start_chan = '0'
end_chan = '1'

device = 'cDAQ1Mod1/ai' + start_chan + ':' + end_chan
with nidaqmx.Task() as task:
    #task.ai_channels.add_ai_thrmcpl("cDAQ1Mod1/ai0:0")
    task.ai_channels.add_ai_thrmcpl_chan("cDaq1Mod1/ai0:1", min_val=0.0,
                                     max_val=100.0, units=nidaqmx.constants.TemperatureUnits.DEG_F,
                                     thermocouple_type=nidaqmx.constants.ThermocoupleType.J)
#                                     cjc_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE, cjc_val=2.0,
#                                     cjc_channel="")
    
    
    
    
    
#    task.ai_channels.add_ai_thrmcpl_chan(device, units = nidaqmx.constants.TemperatureUnits.DEG_F)
#    nidaqmx.constants.ThermocoupleType.J
#    nidaqmx.constants.TemperatureUnits.DEG_F
#    nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE()
    while i<25:

        data = task.read(number_of_samples_per_channel = 1)
        plt.scatter(i,data[0], c='r')
        plt.scatter(i, data[1],c='b')
        plt.pause(0.1)
        i = i  + 1
        plt.ylim(0, 100)
        print(data)
plt.show()

#
#task.ai_channels.add_ai_thrmcpl_chan("cDaq1Mod1/ai0:2",name_to_assign_to_channel="", min_val=0.0,
#                                     max_val=100.0, units=nidaqmx.constants.TemperatureUnits.DEG_C,
#                                     thermocouple_type=nidaqmx.constants.ThermocoupleType.K,
#                                     cjc_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE, cjc_val=20.0,
#                                     cjc_channel="")