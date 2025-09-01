import time

def display_hello_world():
    message = "Hello World"
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.2)  # 每个字符之间暂停0.2秒
    print()  # 打印换行

if __name__ == "__main__":
    display_hello_world() 