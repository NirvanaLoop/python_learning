"""
个人记账系统 - 主程序
提供命令行交互界面
"""

from account import Account


def print_menu():
    """打印主菜单"""
    print("\n" + "="*50)
    print("个人记账系统")
    print("="*50)
    print("1. 添加收入")
    print("2. 添加支出")
    print("3. 查看所有记录")
    print("4. 查看收入记录")
    print("5. 查看支出记录")
    print("6. 按类别查询")
    print("7. 查看账户摘要")
    print("0. 退出")
    print("="*50)


def add_income(account):
    """添加收入记录"""
    print("\n--- 添加收入 ---")
    try:
        amount = float(input("请输入金额: "))
        category = input("请输入类别（如：工资、奖金等）: ").strip()
        description = input("请输入描述（可选，直接回车跳过）: ").strip()
        
        if amount <= 0:
            print("❌ 金额必须大于0！")
            return
        
        transaction = account.add_transaction(amount, category, description, "收入")
        print(f"✅ 收入记录已添加: {transaction}")
    except ValueError:
        print("❌ 输入格式错误，请输入数字！")
    except Exception as e:
        print(f"❌ 发生错误: {e}")


def add_expense(account):
    """添加支出记录"""
    print("\n--- 添加支出 ---")
    try:
        amount = float(input("请输入金额: "))
        category = input("请输入类别（如：餐饮、交通、购物等）: ").strip()
        description = input("请输入描述（可选，直接回车跳过）: ").strip()
        
        if amount <= 0:
            print("❌ 金额必须大于0！")
            return
        
        if not category:
            print("❌ 类别不能为空！")
            return
        
        transaction = account.add_transaction(amount, category, description, "支出")
        print(f"✅ 支出记录已添加: {transaction}")
    except ValueError:
        print("❌ 输入格式错误，请输入数字！")
    except Exception as e:
        print(f"❌ 发生错误: {e}")


def show_all_transactions(account):
    """显示所有交易记录"""
    transactions = account.get_all_transactions()
    if not transactions:
        print("\n暂无交易记录")
        return
    
    print("\n--- 所有交易记录 ---")
    for i, t in enumerate(transactions, 1):
        print(f"{i}. {t}")


def show_income_transactions(account):
    """显示收入记录"""
    transactions = account.get_transactions_by_type("收入")
    if not transactions:
        print("\n暂无收入记录")
        return
    
    print("\n--- 收入记录 ---")
    total = 0
    for i, t in enumerate(transactions, 1):
        print(f"{i}. {t}")
        total += t.amount
    print(f"\n总收入: ¥{total:.2f}")


def show_expense_transactions(account):
    """显示支出记录"""
    transactions = account.get_transactions_by_type("支出")
    if not transactions:
        print("\n暂无支出记录")
        return
    
    print("\n--- 支出记录 ---")
    total = 0
    for i, t in enumerate(transactions, 1):
        print(f"{i}. {t}")
        total += t.amount
    print(f"\n总支出: ¥{total:.2f}")


def query_by_category(account):
    """按类别查询"""
    category = input("\n请输入要查询的类别: ").strip()
    if not category:
        print("❌ 类别不能为空！")
        return
    
    transactions = account.get_transactions_by_category(category)
    if not transactions:
        print(f"\n暂无类别为 '{category}' 的记录")
        return
    
    print(f"\n--- 类别 '{category}' 的记录 ---")
    total = 0
    for i, t in enumerate(transactions, 1):
        print(f"{i}. {t}")
        if t.transaction_type == "收入":
            total += t.amount
        else:
            total -= t.amount
    print(f"\n该类别总计: ¥{total:.2f}")


def main():
    """主函数"""
    print("欢迎使用个人记账系统！")
    
    # 创建账户对象
    account = Account()
    
    # 主循环
    while True:
        print_menu()
        choice = input("请选择操作 (0-7): ").strip()
        
        if choice == "0":
            print("\n感谢使用，再见！")
            break
        elif choice == "1":
            add_income(account)
        elif choice == "2":
            add_expense(account)
        elif choice == "3":
            show_all_transactions(account)
        elif choice == "4":
            show_income_transactions(account)
        elif choice == "5":
            show_expense_transactions(account)
        elif choice == "6":
            query_by_category(account)
        elif choice == "7":
            account.show_summary()
        else:
            print("❌ 无效的选择，请重新输入！")
        
        # 等待用户按键继续
        if choice != "0":
            input("\n按回车键继续...")


if __name__ == "__main__":
    main()

