import pulp

# Оголошення проблеми
prob = pulp.LpProblem("Maximize Beverage Production", pulp.LpMaximize)

# Змінні рішень
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit Juice', lowBound=0, cat='Integer')

# Цільова функція
prob += lemonade + fruit_juice, "Total Beverages"

# Обмеження
prob += 2*lemonade + 1*fruit_juice <= 100, "Water"
prob += 1*lemonade <= 50, "Sugar"
prob += 1*lemonade <= 30, "Lemon Juice"
prob += 2*fruit_juice <= 40, "Fruit Puree"

# Розв'язок проблеми
prob.solve()

# Виведення результатів
print(f"Status: {pulp.LpStatus[prob.status]}")
print(f"Lemonade: {lemonade.varValue}")
print(f"Fruit Juice: {fruit_juice.varValue}")
print(f"Total Beverages: {lemonade.varValue + fruit_juice.varValue}")
