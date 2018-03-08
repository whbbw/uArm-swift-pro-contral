#! /usr/bin/env python
#
# Support module generated by PAGE version 4.10
# In conjunction with Tcl version 8.6
#    Mar 06, 2018 03:53:43 PM


import sys, os

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


from time import sleep

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *
# import action_function



def set_Tk_var():
    global TCbox_shake_angle
    TCbox_shake_angle = "10"
    global TCbbox_push
    TCbbox_push = "350"
    global TCbox_pull
    TCbox_pull = "140"
    global TCbox_up
    TCbox_up = "170"
    global TCbox_down
    TCbox_down = "40"

def TB_down_key(self):
    print('uArmContralFrm_support.TB_down_key')
    down()

def TB_edit_key(self):
    print('uArmContralFrm_support.TB_edit_key')
    sys.stdout.flush()

def TB_f1_key(self):
    print('uArmContralFrm_support.TB_f1_key')
    sys.stdout.flush()

def TB_f2_key(self):
    print('uArmContralFrm_support.TB_f2_key')
    sys.stdout.flush()

def TB_f3_key(self):
    print('uArmContralFrm_support.TB_f3_key')
    sys.stdout.flush()

def TB_f4_key(self):
    print('uArmContralFrm_support.TB_f4_key')
    sys.stdout.flush()

def TB_f5_key(self):
    print('uArmContralFrm_support.TB_f5_key')
    sys.stdout.flush()

def TB_look_center(self):
    print('uArmContralFrm_support.TB_look_center')
    center_look()

def TB_look_left(self):
    print('uArmContralFrm_support.TB_look_left')
    left_look()

def TB_look_right(self):
    print('uArmContralFrm_support.TB_look_right')
    right_look()

def TB_pull_key(self):
    print('uArmContralFrm_support.TB_pull_key')
    pull()

def TB_push_key(self):
    print('uArmContralFrm_support.TB_push_key')
    push()

def TB_reset_key(self):
    print('uArmContralFrm_support.TB_reset_key')
    reset()

def TB_shake_left_key(self):
    print('uArmContralFrm_support.TB_shake_left_key')
    shake_left()

def TB_shake_right(self):
    print('uArmContralFrm_support.TB_shake_right')
    shake_right()

def TB_up_key(self):
    print('uArmContralFrm_support.TB_up_key')
    up()

def about_dialog(self):
    print('uArmContralFrm_support.about_dialog')
    sys.stdout.flush()

def setup_input_dialog(self):
    print('uArmContralFrm_support.setup_input_dialog')
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import uArmContralFrm
    uArmContralFrm.vp_start_gui()

