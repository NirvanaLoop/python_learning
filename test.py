# 综合运用函数
# 输入两个数字，我要分别得到他的加减乘除的结果
# 获取用户输入的函数
def get_input():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    return a, b

# 计算和的函数
def add(a, b):
    return a + b

# 计算差的函数
def subtract(a, b):
    return a - b

# 计算积的函数
def multiply(a, b):
    return a * b

# 计算商的函数
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

# 主程序
def main():
    a, b = get_input()
    print(f"The sum of {a} and {b} is: {add(a, b)}")
    print(f"The difference between {a} and {b} is: {subtract(a, b)}")
    print(f"The product of {a} and {b} is: {multiply(a, b)}")
    print(f"The quotient of {a} and {b} is: {divide(a, b)}")

# 调用主程序
main()