from turtle import *
import os
speed(10)
color('cyan')
bgcolor('black')
b = 200
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1
os.system('pause')    