rent = int(input("Enter amount of rent : "))
food = int(input("enter the amount money which spent on food : "))
electricity_spend = int(input("Enter number of units : "))
charge_per_unit = int(input("enter the charge per unit : "))
persons = int(input("enter number of person : "))

total_electricity = electricity_spend * charge_per_unit
total_expense = rent + food + total_electricity

print("Total expense is : ", total_expense/persons)