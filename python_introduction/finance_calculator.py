#Personal Finance Calculator

monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

saving_monthly = monthly_income - total_monthly_expenses

projected_savingn = saving_monthly * 12 + (saving_monthly * 12 * 0.05)

print(f"Projected savings after one year, with interest, is: {projected_savingn}$")

