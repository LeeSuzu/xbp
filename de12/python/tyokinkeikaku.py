def savings_plan():
    monthly_income = float(input("毎月の収入を入力してください: "))
    monthly_expenses = float(input("毎月の支出を入力してください: "))
    saving_goal = float(input("貯金目標額を入力してください: "))
    savings = 0
    months = 0

    while savings < saving_goal:
        savings += (monthly_income - monthly_expenses)
        months += 1
        print(f"{months} ヶ月目の貯金額: {savings:.2f} 円")

    print(f"貯金目標額 {saving_goal:.2f} 円 を達成するには、{months} ヶ月かかります。")

savings_plan()
