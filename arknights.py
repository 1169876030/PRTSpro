import os
import sys
import time
import pyautogui as auto
from PIL import Image
import subprocess

#初始化变量
pausetime = 0
ip = '127.0.0.1:7555'
c = 0.8
sc = True
mc = False
filename = 'screenshot.png'
num = 0
i = 0
def screen():
    screenExecute = subprocess.Popen("adb shell screencap -p /sdcard/screenshot.png", stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    stdout, stderr = screenExecute.communicate()
    stdout = stdout.decode("utf-8")
    stderr = stderr.decode("utf-8")


def saveComputer():
    screenExecute = subprocess.Popen("adb pull /sdcard/screenshot.png", stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    stdout, stderr = screenExecute.communicate()
    stdout = stdout.decode("utf-8")


def screenshot():
    screen()
    saveComputer()
#def screenshot():
#    os.system(f"adb shell screencap -p /sdcard/{filename}")
#    os.system(f"adb pull /sdcard/{filename}")

#初始化连接adb
def init():
    print("PRTS代理作战pro")
    print("初始化中。。。。。。")
    os.system(f'adb connect {ip}')
    screenshot()
    try:
        global SR 
        img = Image.open(filename)
        SR = f'{img.size[0]}x{img.size[1]}'
        print(f'分辨率：{SR}')
        print(f'点击间隔：{pausetime}')
        print(f'图片识别率：{c}')
        print(f'碎石模式：{sc}')
        print(f'嗑药模式：{mc}')
        print('初始化完成')
    except:
        print('adb连接失败，请打开模拟器后重试')
        sys.exit(0)

#点击
def tap(x:int or tuple, y=None):
    if y is None:
        x, y = x
    os.system(f'adb shell input tap {x} {y}')

#找图
def find(pic:str, msg=None, click=True):
    p = auto.locate(f'./picture/{pic}', filename, confidence=c)
    if p:
        if msg:
            print(msg)
        if click:
            tap(auto.center(p))
            time.sleep(pausetime)
    return p

def play(num:int):
    i = 0
    while i < num or num == 0:
        screenshot()
        if find('1.png', click=False):
            if find('6.png', '开启代理指挥'):
                pass
            find('1.png', '准备行动')
            time.sleep(2)
        elif find('7.png', click=False):
            if mc and not sc:
                if not find('8.png', '理智不足，准备嗑药', click=False):
                    find('7.png', '成功嗑药')
                    time.sleep(1)
                else :
                    print('理智不足，停止刷图')
                    break
            elif sc:
                find('7.png', '成功碎石')
                time.sleep(1)
            else :
                print('理智不足，停止刷图')
                break
        elif find('2.png', '进入地图'):
            print(f'第{i+1}次刷图开始')
            time.sleep(5)
        elif find('3.png', click=False):
            print(f'第{i+1}次刷图中')
            while find('3.png', click=False):
                screenshot()
                #print('脚本正常运行')
                time.sleep(5)
            print('战斗结束')
        elif find('9.png', '升级，理智恢复，继续刷图'):
            pass
        elif find('5.png', click=False):
            tap(100, 100)
            time.sleep(0.5)
        elif find('4.png', f'第{i+1}次战斗胜利', click=False):
            tap(100, 100)
            i += 1

if __name__ == '__main__':
    init()
    while True:
        try:
            num = input("请输入次数,0为无限(或exit退出)：")
            if num == 'exit':
                #os.system(f'adb disconnect {ip}')
                os.system('taskkill /f /im adb.exe /t')
                break
            else:
                play(int(num))
        except ValueError as e:
            print('非法输入')
        except Exception as e:
            print(e)