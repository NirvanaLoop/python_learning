from flask import Flask, render_template, request, redirect, url_for, flash
from account import Account

app = Flask(__name__)
app.secret_key = "simple-secret-for-demo"

# 初始化账户（使用默认JSON存储）
account = Account()


@app.route("/", methods=["GET"])
def index():
    transactions = account.get_all_transactions()
    income_total = account.get_income_total()
    expense_total = account.get_expense_total()
    balance = account.get_balance()
    category_summary = account.get_category_summary()
    return render_template(
        "index.html",
        transactions=transactions,
        income_total=income_total,
        expense_total=expense_total,
        balance=balance,
        category_summary=category_summary,
    )


@app.route("/add", methods=["POST"])
def add():
    try:
        amount = float(request.form.get("amount", 0))
        category = (request.form.get("category") or "").strip()
        description = (request.form.get("description") or "").strip()
        transaction_type = request.form.get("transaction_type") or "支出"
        if amount <= 0:
            flash("金额必须大于0", "error")
            return redirect(url_for("index"))
        if not category:
            flash("类别不能为空", "error")
            return redirect(url_for("index"))
        account.add_transaction(amount, category, description, transaction_type)
        flash("记录已添加", "success")
    except ValueError:
        flash("金额格式错误", "error")
    except Exception as e:
        flash(f"出错了: {e}", "error")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
