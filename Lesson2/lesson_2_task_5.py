winter_months = [12, 1, 2]
spring_months = [3, 4, 5]
summer_months = [6, 7, 8]
fall_months = [9, 10, 11]


def month_to_season(month_number):
    if month_number in winter_months:
        print("Зима")
    elif month_number in spring_months:
        print("Весна")
    elif month_number in summer_months:
        print("Лето")
    elif month_number in fall_months:
        print("Осень")
    else:
        print("Такого месяца не существует")
    
    
number = int(input("Введите номер месяца "))
month_to_season(number)
