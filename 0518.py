# Original employee list with 10 names
employee_list = ["Anna", "Brian", "Celine", "David", "Ella", "Felix", "Grace", "Harry", "Isla", "James"]

# 1. Split the list into two sublists
sub_list1 = employee_list[:5]
sub_list2 = employee_list[5:]

# 2. Add a new employee to sub_list2
sub_list2.append("Kriti Brown")

# 3. Remove the second employee from sub_list1
del sub_list1[1]  # Removes "Brian"

# 4. Merge both sublists
merged_employees = sub_list1 + sub_list2

# 5. Initial salary list corresponding to each employee
salary_list = [45000, 52000, 48000, 50000, 53000, 47000, 49500, 51000, 46000, 55000]
salary_list.append(54000)  # Kriti Brown's assumed salary

# 6. Apply a 4% raise to each salary
updated_salaries = [round(salary * 1.04, 2) for salary in salary_list]

# 7. Sort the salaries and get the top 3
top_three = sorted(updated_salaries, reverse=True)[:3]

# Output results
print("Merged Employee List:", merged_employees)
print("Updated Salary List:", updated_salaries)
print("Top 3 Salaries:", top_three)