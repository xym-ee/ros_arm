# coding=UTF-8

'''
串口舵机协议的封装，提供上层使用接口
'''
import time
from servo_set import servo_set4



servo_set4(2048, 2048, 2048 , 2048 , 1000)

time.sleep(2)

servo_set4(2048, 1500, 1500, 1500, 1000)

time.sleep(2)

servo_set4(1000, 1500, 1500, 1500, 1000)

time.sleep(1)

servo_set4(3000, 1500, 1500, 1500, 2500)

time.sleep(3)

servo_set4(3000, 1500, 1500, 2500, 1500)

time.sleep(3)


servo_set4(3000, 1500, 1500, 1500, 1000)

time.sleep(1)


servo_set4(3000, 1500, 1500, 2500, 1000)

time.sleep(1)

servo_set4(3000, 1500, 1500, 1500, 1000)

time.sleep(1)

servo_set4(3000, 1500, 1500, 2500, 1000)

time.sleep(1)
