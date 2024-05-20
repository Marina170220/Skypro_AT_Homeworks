def is_year_leap(year: int):
    if year % 4 == 0:
        return True
    return False

year = int(input("Введите год "))
result = is_year_leap(year)
print(f"Год {year}: {result}")