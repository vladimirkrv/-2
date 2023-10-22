salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

month_money_capital = 0  # Ежемесячные траты из подушки безопасности
money_capital = 0  # Подушка безопасности

for month in range(months):
    month_money_capital = spend - salary
    money_capital += month_money_capital
    spend += spend * increase

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
