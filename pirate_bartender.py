import random 

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

adjectives = ["Salty", "Fizzy", "Bubbly", "Lemony", "Refreshing", "Intoxicating", "Light", "Sparkling", "Flaming", "Tangy"
]

nouns = ["Orange", "Volcano", "Zombie", "Sea-Dog", "Dung-bie", "Black Jack", "Scuttle"
]

# for key in questions:
#     print(questions[key])
#     print(key)

preferences = {} #create new dictionary
def drink_pref():
    """Asks customer for drink preference"""
    for key in questions:
        response = input(questions[key])
        if (response.lower() == "yes") or (response.lower() == "y"): #map new dictionary to a boolean value
            preferences[key] = True
        else:   
            preferences[key] = False
    return(preferences)
        
def create_drink(preferences):
    """Constructs a drink based on the preferences provided by the customer"""
    drink = [] #Create empty list
    for type in preferences:
        drink.append(random.choice(ingredients[type])) #append a corresponding ingredient from the "preference" dictionary; choose ingredient from one of the ingredient lists
    return(drink)

def name_cocktail():
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    return (adj + " " + noun)


if __name__ == '__main__':
        print("Ahoy matey! I'll make you a drink")
        while True:
            customer = input("Who be orderin?")
            preferences = drink_pref()
            drink = create_drink(preferences)
            cocktail = name_cocktail()
        
#   print_drink(drink)
            print("Got it! Coming right up {}.".format(customer))
            print("Orderup! This is a {}.".format(cocktail))
            print("It's made up of the following:")
            for items in drink:
                print(items)
    
            second_round = input("Care for another drink?")
            if (second_round.lower() == "yes") or (second_round.lower() == "y"):
                pass
            elif (second_round.lower() == "no") or (second_round.lower() == "n"):
                print("Ahoy, your drinks will cost you 3 pieces of gold!")
                break
        