income = float(input("Enter your monthly income: "))
fixed_expenses = float(input("Enter your total fixed expenses: "))
num_var_expenses = int(input("How many variable expenses do you have? "))
total_variable_expenses = 0

for i in range(num_var_expenses):
    expense = input("Enter expense name: ")
    amount = float(input("Enter amount for " + expense + ": "))
    total_variable_expenses += amount

total_expenses = fixed_expenses + total_variable_expenses

if total_expenses > income:
    print("Warning: Your expenses exceed your income.")
remaining_budget = income - total_expenses
print("Remaining budget: ", remaining_budget)
