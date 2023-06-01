spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    dish_name = [dish.get("name") for dish in spicy_foods]
    return dish_name

def get_spiciest_foods(spicy_foods):
    heat_over_five = [dish for dish in spicy_foods if dish["heat_level"] > 5]
    return heat_over_five

def print_spicy_foods(spicy_foods):
    dish_name = get_names(spicy_foods)
    cuisine_name = [dish.get("cuisine") for dish in spicy_foods]
    heat_amount = [dish.get("heat_level") for dish in spicy_foods]
    emoji_one = (heat_amount[0] * "🌶") 
    emoji_two = (heat_amount[1] * "🌶")
    emoji_three = (heat_amount[2] * "🌶")
    first = f"{dish_name[0]} ({cuisine_name[0]}) | Heat Level: {emoji_one}"
    second = f"{dish_name[1]} ({cuisine_name[1]}) | Heat Level: {emoji_two}"
    third = f"{dish_name[2]} ({cuisine_name[2]}) | Heat Level: {emoji_three}"
    print(first)
    print(second)
    print(third)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    dish_by_cuisine = [dish for dish in spicy_foods if dish["cuisine"] == cuisine]
    return dish_by_cuisine[0]

def print_spiciest_foods(spicy_foods):
    heat_over_five = [dish for dish in spicy_foods if dish["heat_level"] > 5]
    dish_name = get_names(heat_over_five)
    cuisine_name = [dish.get("cuisine") for dish in heat_over_five]
    heat_amount = [dish.get("heat_level") for dish in heat_over_five]
    emoji_one = (heat_amount[0] * "🌶") 
    emoji_two = (heat_amount[1] * "🌶")
    first = f"{dish_name[0]} ({cuisine_name[0]}) | Heat Level: {emoji_one}"
    second = f"{dish_name[1]} ({cuisine_name[1]}) | Heat Level: {emoji_two}"
    print(first)
    print(second)

def get_average_heat_level(spicy_foods):
    heat_amount = [dish.get("heat_level") for dish in spicy_foods]
    heats_average = (heat_amount[0] + heat_amount[1] + heat_amount[2])/3
    return heats_average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
