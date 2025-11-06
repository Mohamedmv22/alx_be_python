#principal رئس المال , rate معدل الفائدة السنوي, time الوقت

principal = 1000
rate = 0.05 #5%
time = 3

interest = principal * rate * time
total_amount = principal + interest

print("Interest: ", interest)
print("Total amount after 3 years: ", total_amount)

