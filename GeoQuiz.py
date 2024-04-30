import random

countries_capitals = {
    "Poland": "Warsaw",
    "Germany": "Berlin",
    "France": "Paris",
    "Italy": "Rome",
    "Spain": "Madrid",
    "USA": "Washington",
    "Canada": "Ottawa",
    "Russia": "Moscow",
    "China": "Pekin",
    "Japan": "Tokyo",
    "Australia": "Canberra",
    "Brazil": "Brasilia",
    "Argentina": "Buenos Aires",
    "Egypt": "Cairo",
    "Nigeria": "Abuja",
    "Kenya": "Nairobi",
    "United Kingdom": "London",
    "South Korea": "Seoul",
    "Turkey": "Ankara",
    "Greece": "Athens",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Iran": "Tehran",
    "Iraq": "Baghdad",
    "Pakistan": "Islamabad",
    "Indonesia": "Jakarta",
    "Mexico": "Mexico",
    "Colombia": "Bogota",
    "Peru": "Lima",
    "Venezuela": "Caracas",
    "Cuba": "Havana",
}

def quiz():
    points = 0
    while True:
        country, capital = random.choice(list(countries_capitals.items()))

        player_guess = input(f"What is the capital of {country}? ")

        if player_guess.lower() == capital.lower():
            points += 1
            print(f"Good! points - {points}")
        else:
            points -= 1
            print(f"Wrong! points - {points}")

        country, capital = random.choice(list(countries_and_capitals.items()))

        player_guess = input(f"What is the country with the capital {capital}? ")

        if player_guess.lower() == country.lower():
            points += 1
            print(f"Good! points - {points}")
        else:
            points -= 1
            print(f"Wrong! points - {points}")

print("Welcome in geography quiz, made by Helion")
geography_quiz()
