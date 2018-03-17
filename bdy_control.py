import win32gui
import win32con
import win32api

from pymouse import PyMouse

import time

# 百度网盘离线下载按钮的坐标
download_button_x = 520
download_button_y = 110

# 新建离线下载任务页面开始下载按钮坐标
start_download_button_x = 480
start_download_button_y = 255

# 离线任务列表后台运行按钮
back_run_button_x = 485
back_run_button_y = 360

def click_window_button(name, x, y):
    '''
    模拟鼠标点击一个窗口的某一位置，通常是按钮的位置
    '''

    window_handle = win32gui.FindWindow(None, name)

    time_out = 30
    while window_handle == 0x00:
        time.sleep(1)
        window_handle = win32gui.FindWindow(None, name)
        time_out = time_out - 1
        if(0x00 == time_out):
            return 0x01

    left, top, right, bottom = win32gui.GetWindowRect(window_handle)

    x += left
    y += top

    mouse = PyMouse()

    mouse.click(x, y)

    return 0x00

def download_link(link):
    '''
    使用百度网盘离线下载功能下载 link 的内容
    '''

    # 打开离线下载页面，通过模拟鼠标点击离线下载按钮实现
    click_window_button('欢迎使用百度网盘', download_button_x, download_button_y)

    time.sleep(1)

    time_out = 30

    # 得到离线下载页面编辑框的句柄并填充下载地址
    download_window_handle = win32gui.FindWindow(None, '新建离线下载任务窗口')
    
    while download_window_handle == 0x00:
        time.sleep(1)
        download_window_handle = win32gui.FindWindow(None, '新建离线下载任务窗口')
        time_out = time_out - 1
        if(time_out == 0x00):
            print('等待 新建离线下载任务窗口 超时！！！')
            return 0x01

    edit_handle = win32gui.FindWindowEx(download_window_handle, 0, None, None)
    win32api.SendMessage(edit_handle, win32con.WM_SETTEXT, 0, link)

    # 点击开始下载按钮
    click_window_button('新建离线下载任务窗口', start_download_button_x, start_download_button_y)

    time.sleep(2)

    # 点击后台运行按钮，结束本次下载任务
    if(0x01 == click_window_button('离线下载任务列表', back_run_button_x, back_run_button_y)):
        print('等待 离线下载任务列表 超时！！！')

    time.sleep(2)
    