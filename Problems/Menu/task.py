pizza = "Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy"
salad = "Caesar salad, Green salad, Tuna salad, Fruit salad"
soup = "Chicken soup, Ramen, Tomato soup, Mushroom cream soup"
str_in = input()
if str_in == "pizza":
    print(pizza)
elif str_in == "salad":
    print(salad)
elif str_in == "soup":
    print(soup)
else:
    print("Sorry, we don't have it in the menu")