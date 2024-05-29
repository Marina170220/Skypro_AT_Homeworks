from smartphone import Smartphone

catalog = []
brands = ["Samsung", "Xiaomi", "Apple", "Honor", "Vivo"]
models = ["A5", "S500", "A-254v", "8965", "un-87"]
numbers = ["+79102568421", "+79001002222", "+79012544545", "+79999001100", "+79201234567"]


for i in range(len(brands)):
    catalog.append(Smartphone(brands[i], models[i], numbers[i]))
    print(catalog[i].brand, "-", catalog[i].model,".", catalog[i].number)
