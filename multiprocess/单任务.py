import time

def sing():
    for i in range(3):
        print("singing...")
        time.sleep(0.5)

def dance():
    for i in range(3):
        print("dancing...")
        time.sleep(0.5)

if __name__ == "__main__":
    sing()
    dance()
