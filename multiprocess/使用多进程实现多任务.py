#1. 导入进程包
#2. 使用进程类创建进程对象
#3. 使用进程对象启动进程执行指定任务


import multiprocessing
import time

def sing():
    for i in range(3):
        print("singing...")
        time.sleep(1)

def dance():
    for i in range(3):
        print("dancing...")
        time.sleep(1)

if __name__ == "__main__":

    # 2.target 指定进程执行的函数名
    sing_process = multiprocessing.Process(target=sing)
    dance_process = multiprocessing.Process(target=dance)
    sing_process.start()
    dance_process.start()