def bank(x, y):
    for year in range(y):
        x *= 1.1
    return x
sum = int(input ("Введите сумму "))
years = int(input ("Введите количество лет "))

print(f"Через {years} лет на вашем счету будет {round(bank(sum, years), 2)} рублей")        