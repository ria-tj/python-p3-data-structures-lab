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

    return [food['name'] for food in spicy_foods]
    
def get_spiciest_foods(spicy_foods):
    
    return [food for food in spicy_foods if food ['heat_level']>5]

def print_spicy_foods(spicy_foods):
   
   for food in spicy_foods:
        heat = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    
    for food in spicy_foods:
        if food['cuisine'].lower() == cuisine.lower():
            return food
    return None


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            heat = "🌶" * food['heat_level']
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")
     
     

def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    count = len(spicy_foods)
    return round(total_heat / count) if count > 0 else 0

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods