class FinanceTracker:
    def __init__(self):
        self.daily_income = 0
        self.expenses = {'食費': 0, '交通費': 0, '家賃': 0, '遊び': 0}  # それぞれの分野の支出
        self.balance = 0
食費, 交通費, 家賃, 遊び, デート, 光熱費, メイク, 服
    def record_income(self, amount):
        self.daily_income += amount
        self.balance += amount

    def record_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
            self.balance -= amount

    def show_balance(self):
        print(f"残高: {self.balance}")

    def show_expense_summary(self):
        print("分野別支出:")
        for category, amount in self.expenses.items():
            print(f"{category}: {amount}")

    def show_history(self):
        print(f"日々の収入: {self.daily_income}")
        self.show_expense_summary()
        self.show_balance()

def main():
    tracker = FinanceTracker()

    while True:
        print("\n1. 収入を記録する")
        print("2. 支出を記録する")
        print("3. 残高を表示する")
        print("4. 分野別支出を表示する")
        print("5. 履歴を表示する")
        print("6. 終了")

        choice = input("選択してください: ")

        if choice == '1':
            income = float(input("収入を入力してください: "))
            tracker.record_income(income)
        elif choice == '2':
            category = input("支出の分野を選んでください(食費, 交通費, 家賃, 遊び, デート, 光熱費, メイク, 服): ")
            expense = float(input("支出金額を入力してください: "))
            tracker.record_expense(category, expense)
        elif choice == '3':
            tracker.show_balance()
        elif choice == '4':
            tracker.show_expense_summary()
        elif choice == '5':
            tracker.show_history()
        elif choice == '6':
            print("終了します。")
            break
        else:
            print("無効な選択です。もう一度選んでください。")

if __name__ == "__main__":
    main()
