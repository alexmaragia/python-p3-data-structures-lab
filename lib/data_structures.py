# lib/data_structures.py

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
    # Returns a list of the names of each spicy food
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    # Returns a list of dictionaries where the heat level is greater than 5
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    # Outputs each spicy food in the specified format with the heat level represented by 🌶 emojis
    for food in spicy_foods:
        heat_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Returns a single dictionary for the spicy food whose cuisine matches the given cuisine
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # In case no match is found

def print_spiciest_foods(spicy_foods):
    # Outputs only the spicy foods with a heat level greater than 5
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    # Returns the average heat level of all spicy foods as an integer
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)  # Use // for integer division

def create_spicy_food(spicy_foods, spicy_food):
    # Adds a new spicy food to the list and returns the updated list
    spicy_foods.append(spicy_food)
    return spicy_foods
