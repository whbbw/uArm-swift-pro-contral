# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 09:37:22 2018

@author: whbbw
"""

import sys, os
from time import sleep

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *




def loger():
    #logger_init(logging.VERBOSE)
    #logger_init(logging.DEBUG)
    logger_init(logging.INFO)

def creat_swift():
    print('setup swift ...')
    global swift
    #swift = SwiftAPI(dev_port = '/dev/ttyACM0')
    #swift = SwiftAPI(filters = {'hwid': 'USB VID:PID=2341:0042'})
    swift = SwiftAPI() # default by filters: {'hwid': 'USB VID:PID=2341:0042'}
    print('sleep 2 sec ...')
    sleep(2)
    return swift

def show_dev_info():
    
    dev_info = swift.get_device_info()
    print('device info: ')
    print(dev_info)
    return str(dev_info)


def reset():
    '''
    初始位置
    '''
    swift.set_polar(s = 105, r = 90, h = 40, 
                       speed = 4000, wait = True, timeout = 20)
    
def push(s = 350):
    '''
    镜头前推
    '''
    t_s = s
    swift.set_polar(s = t_s, h = 50,
                       speed = 4000, wait = True, timeout = 20)

def pull(s = 150):
    '''
    镜头后拉
    '''
    t_s = s
    swift.set_polar(s = t_s, h = 50,
                       speed = 4000, wait = True, timeout = 20)

def shake_left( n = 1):
    '''
    镜头左摇
    '''
    for i in range(n):
        print("运行第" + str(i) + "次，每次增加角度10度。")
        swift.set_polar( r= 10, speed = 4000, relative = 1,
                                    wait = True, timeout = 20)
    
    
def shake_right(n = 1):
    '''
    镜头右摇
    '''
    for i in range(n):
        print("运行第" + str(i) + "次，每次增加角度10度。")
        swift.set_polar( r= -10, speed = 4000, relative = 1,
                                    wait = True, timeout = 20)


def up( h = 170):
    '''
    镜头抬高
    '''
    t_h = h
    swift.set_polar(s= 250, h = t_h, wait = True, timeout = 20)

    
    
def down( h = 40):
    '''
    镜头降低
    '''
    t_h = h
    swift.set_polar(s = 250, h = t_h, wait = True, timeout = 20)

def left_look():
    '''
    左看
    '''
    d = swift.get_servo_angle(3)
    print(d)
    if d > 360 or d < 30:
        d = 0
    elif d < 360 and d >= 150:
        d = 180
    elif d <= 150 and d >= 30:
        d = 90
    print(d)

    if d == 90:
        for i in range(int(d), -10, -10):
            print("转动到" + str(i) + "度。")
            swift.set_wrist(i, True, 10)
            sleep(0.05)
    else:
        print("不能到达！")

def center_look():
    '''
    前看
    '''
    d = swift.get_servo_angle(3)
    print(d)
    if d > 360 or d < 30:
        d = 0
    elif d < 360 and d >= 150:
        d = 180
    elif d <= 150 and d >= 30:
        d = 90
    print(d)

    if d == 0:
        for i in range(int(d), 100, 10):
            print("转动到" + str(i) + "度。")
            swift.set_wrist(i)
            sleep(0.05)
    elif d == 180:
        for i in range(int(d), 80, -10):
            print("转动到" + str(i) + "度。")
            swift.set_wrist(i, True, 10)
            sleep(0.05)
    else:
        print("不能到达！")

def right_look():
    '''
    右看
    '''
    d = swift.get_servo_angle(3)
    print(d)
    if d > 360 or d < 30:
        d = 0
    elif d < 360 and d >= 150:
        d = 180
    elif d <= 150 and d >= 30:
        d = 90
    print(d)

    if d == 90:
        for i in range(int(d), 190, 10):
            print("转动到" + str(i) + "度。")
            swift.set_wrist(i, True, 10)
            sleep(0.05)
    else:
        print("不能到达！")

def f1_key():
    print("初始化位置")
    
    reset()
    
    msg = swift.get_position()
    print(msg)
    
    sleep(1)
    
    print("向左摇40度")
    
    shake_left(4)
    
    msg = swift.get_position()
    print(msg)
    
    sleep(1)
    
    print("前推")
    
    push()
    
    msg = swift.get_position()
    print(msg)
    
    sleep(1)
    
    print("抬升")
    
    up()
    
    msg = swift.get_position()
    print(msg)
    
    sleep(1)
    
    print("下降")
    
    down()
    
    msg = swift.get_position()
    print(msg)
    
    
    sleep(1)
    
    print("后拉")
    
    
    pull()
    
    msg = swift.get_position()
    print(msg)
    
    sleep(1)
    
    print("返回初始化位置")
    
    reset()
    
    msg = swift.get_position()
    print(msg)
    
    sleep(1)

def f2_key():
    
    left_look()
    sleep(10)
    center_look()
    sleep(10)
    right_look()

def f3_key():
    for i in range(5):
        left_look()
        center_look()
        right_look()
        center_look()
        down()
        up()
    
def f4_key():
    
    print("抬升")
    up()
    
    msg = swift.get_position()
    print(msg)
    sleep(1)
    
    print("下降")
    down()
    
    msg = swift.get_position()
    print(msg)
    sleep(1)
    
    print("初始化位置")
    reset()
    
    msg = swift.get_position()
    print(msg)
    sleep(1)
    
    print("向左摇20度")
    shake_left(2)
    
    msg = swift.get_position()
    print(msg)
    sleep(2)
    
    print("前推")
    push()
    
    msg = swift.get_position()
    print(msg)
    sleep(1)
    
    print("后拉")
    pull()
    
    msg = swift.get_position()
    print(msg)
    sleep(1)
    
    print("向左摇20度")
    shake_left(2)
    
    msg = swift.get_position()
    print(msg)
    sleep(2)
    
    print("前推")
    push()
    
    msg = swift.get_position()
    print(msg)
    sleep(1)
    
    print("后拉")
    pull()
    
    msg = swift.get_position()
    print(msg)
    sleep(1)
    
    print("向右摇60度")
    shake_right(6)
    
    msg = swift.get_position()
    print(msg)
    sleep(2)
    
    print("前推")
    push()
    
    msg = swift.get_position()
    print(msg)
    sleep(1)
    
    print("后拉")
    pull()
    
    msg = swift.get_position()
    print(msg)
    sleep(1)
    
    print("向右摇20度")
    shake_right(2)
    
    msg = swift.get_position()
    print(msg)
    sleep(2)
    
    print("前推")
    push()
    
    msg = swift.get_position()
    print(msg)
    sleep(1)
    
    print("后拉")
    pull()
    
    msg = swift.get_position()
    print(msg)
    sleep(1)
    
    print("向左摇80度")
    shake_left(8)
    
    msg = swift.get_position()
    print(msg)
    sleep(0.1)
    
    
    print("返回初始化位置")
    reset()
    
    msg = swift.get_position()
    print(msg)
    sleep(10)