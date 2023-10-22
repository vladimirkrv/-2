money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

num_months = 0  # Количество месяцев, которое можно протянуть без долгов

while spend < money_capital + salary:
    num_months += 1
    money_capital += salary
    money_capital -= spend
    spend += spend * increase

print("Количество месяцев, которое можно протянуть без долгов:", num_months)
