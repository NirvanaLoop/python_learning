"""
账户管理类
负责管理所有交易记录，提供记账、查询、统计等功能
"""

import json
import os
from transaction import Transaction


class Account:
    """账户管理类"""
    
    def __init__(self, data_file="data/transactions.json"):
        """
        初始化账户
        
        参数:
            data_file: 数据文件路径
        """
        self.data_file = data_file
        self.transactions = []
        self._load_data()
    
    def _load_data(self):
        """从文件加载交易记录"""
        # 确保数据目录存在
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        
        # 如果文件存在，读取数据
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.transactions = [Transaction.from_dict(item) for item in data]
            except (json.JSONDecodeError, FileNotFoundError):
                self.transactions = []
        else:
            self.transactions = []
    
    def _save_data(self):
        """保存交易记录到文件"""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        data = [t.to_dict() for t in self.transactions]
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def add_transaction(self, amount, category, description="", transaction_type="支出"):
        """
        添加交易记录
        
        参数:
            amount: 金额
            category: 类别
            description: 描述
            transaction_type: 类型（"收入" 或 "支出"）
        """
        transaction = Transaction(amount, category, description, transaction_type)
        self.transactions.append(transaction)
        self._save_data()
        return transaction
    
    def get_balance(self):
        """计算账户余额"""
        balance = 0
        for t in self.transactions:
            if t.transaction_type == "收入":
                balance += t.amount
            else:
                balance -= t.amount
        return balance
    
    def get_income_total(self):
        """计算总收入"""
        return sum(t.amount for t in self.transactions if t.transaction_type == "收入")
    
    def get_expense_total(self):
        """计算总支出"""
        return sum(t.amount for t in self.transactions if t.transaction_type == "支出")
    
    def get_transactions_by_category(self, category):
        """按类别查询交易记录"""
        return [t for t in self.transactions if t.category == category]
    
    def get_transactions_by_type(self, transaction_type):
        """按类型查询交易记录（收入/支出）"""
        return [t for t in self.transactions if t.transaction_type == transaction_type]
    
    def get_category_summary(self):
        """按类别统计支出"""
        category_dict = {}
        for t in self.transactions:
            if t.transaction_type == "支出":
                if t.category not in category_dict:
                    category_dict[t.category] = 0
                category_dict[t.category] += t.amount
        return category_dict
    
    def get_all_transactions(self):
        """获取所有交易记录"""
        return self.transactions
    
    def show_summary(self):
        """显示账户摘要"""
        income = self.get_income_total()
        expense = self.get_expense_total()
        balance = self.get_balance()
        
        print("\n" + "="*50)
        print("账户摘要")
        print("="*50)
        print(f"总收入:     ¥{income:.2f}")
        print(f"总支出:     ¥{expense:.2f}")
        print(f"账户余额:   ¥{balance:.2f}")
        print("="*50)
        
        # 显示支出分类统计
        category_summary = self.get_category_summary()
        if category_summary:
            print("\n支出分类统计:")
            for category, amount in sorted(category_summary.items(), key=lambda x: x[1], reverse=True):
                print(f"  {category}: ¥{amount:.2f}")

