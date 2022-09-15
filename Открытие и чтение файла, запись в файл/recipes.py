def read_cook_book(file_name):
    with open(file_name, encoding="utf8") as file:
        cook_book = {}
        while True:
            food = file.readline().strip("\n")
            if not food:
                break
            ingr_count = int(file.readline().strip("\n"))
            ingr_info = []

            for _ in range(ingr_count):
                ingredient_name, quantity, measure = file.readline().strip("\n").split(" | ")
                ingr_info.append({"ingredient_name": ingredient_name, "quantity": int(quantity), "measure": measure})

            cook_book[food] = ingr_info
            file.readline()
        return cook_book

def mul_for_persons(cook_book, persons):
    ingredients = {}
    for dish in cook_book.values():
        for ingrs in dish:
            if ingredients.get(ingrs["ingredient_name"]):
                ingredients[ingrs["ingredient_name"]]["quantity"] += ingrs["quantity"]
            else:
                ingredients[ingrs["ingredient_name"]] = {'measure': ingrs["measure"], 'quantity': ingrs["quantity"]}
    return ingredients

cook_book = read_cook_book("recipes.txt")
mul_list = mul_for_persons(cook_book, 1)