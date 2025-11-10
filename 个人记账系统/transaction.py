"""
交易记录类
用于表示单笔收入或支出记录
"""

from datetime import datetime


class Transaction:
    """交易记录类"""
    
    def __init__(self, amount, category, description="", transaction_type="支出"):
        """
        初始化交易记录
        
        参数:
            amount: 金额（正数）
            category: 类别（如：餐饮、交通、工资等）
            description: 描述信息（可选）
            transaction_type: 类型，"收入" 或 "支出"
        """
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.transaction_type = transaction_type
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self):
        """将交易记录转换为字典格式（用于JSON存储）"""
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "transaction_type": self.transaction_type,
            "date": self.date
        }
    
    @classmethod
    def from_dict(cls, data):
        """从字典创建交易记录对象"""
        transaction = cls(
            amount=data["amount"],
            category=data["category"],
            description=data.get("description", ""),
            transaction_type=data["transaction_type"]
        )
        transaction.date = data["date"]  # 使用原始日期
        return transaction
    
    def __str__(self):
        """返回交易记录的字符串表示"""
        sign = "+" if self.transaction_type == "收入" else "-"
        return f"[{self.date}] {sign}¥{self.amount:.2f} - {self.category} - {self.description}"
    
    def __repr__(self):
        """返回交易记录的详细表示"""
        return f"Transaction({self.amount}, {self.category}, {self.transaction_type})"

