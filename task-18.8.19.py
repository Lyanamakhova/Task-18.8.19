sum_tickets = 0
quantity_tickets = int(input("Введите количество билетов:"))
for age in range (quantity_tickets):
    age = int(input("Введите возраст посетителя:"))
    if age < 18 :
        sum_tickets += 0
    elif 18 <= age <= 25 :
        sum_tickets += 990
    elif age > 25 :
        sum_tickets += 1390
if quantity_tickets > 3 :
    sum_tickets -= sum_tickets / 100 * 10
    print(" Стоимость ваших билетов со скидкой составляет", sum_tickets)
else:
    print(" Стоимость ваших билетов ", sum_tickets)