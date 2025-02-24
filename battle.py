import requests


def get_pokemon_data(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()  # Convert response to JSON
    else:
        print("Pokémon not found!")
        return None


# Test fetching Pikachu
pikachu = get_pokemon_data("pikachu")
print(pikachu["name"], pikachu["types"][0]["type"]["name"])


def choose_pokemon():
    name = input("Choose your Pokémon: ").strip().lower()
    pokemon = get_pokemon_data(name)

    if pokemon:
        moves = [move["move"]["name"] for move in pokemon["moves"][:4]]  # Get first 4 moves
        abilities = [ability["ability"]["name"] for ability in pokemon["abilities"]]
        poke_type = pokemon["types"][0]["type"]["name"]

        return {
            "name": pokemon["name"],
            "moves": moves,
            "abilities": abilities,
            "type": poke_type,
            "hp": 100  # Set default HP
        }
    return None

import random

def get_random_pokemon():
    random_id = random.randint(1, 151)  # Get a random Pokémon from Gen 1
    data = get_pokemon_data(str(random_id))

    if data:
        moves = [move["move"]["name"] for move in data["moves"][:4]]
        abilities = [ability["ability"]["name"] for ability in data["abilities"]]
        poke_type = data["types"][0]["type"]["name"]

        return {
            "name": data["name"],
            "moves": moves,
            "abilities": abilities,
            "type": poke_type,
            "hp": 100  # Default HP
        }
    return None


def battle(player, opponent):
    print(f"\n🔥 {player['name'].capitalize()} vs {opponent['name'].capitalize()} 🔥")

    while player["hp"] > 0 and opponent["hp"] > 0:
        # Player's turn
        move = random.choice(player["moves"])
        damage = random.randint(10, 25)  # Random damage
        opponent["hp"] -= damage
        print(
            f"{player['name'].capitalize()} used {move}! It did {damage} damage. {opponent['name'].capitalize()} has {max(0, opponent['hp'])} HP left.")

        if opponent["hp"] <= 0:
            print(f"\n🎉 {player['name'].capitalize()} wins!")
            break

        # Opponent's turn
        move = random.choice(opponent["moves"])
        damage = random.randint(10, 25)
        player["hp"] -= damage
        print(
            f"{opponent['name'].capitalize()} used {move}! It did {damage} damage. {player['name'].capitalize()} has {max(0, player['hp'])} HP left.")

        if player["hp"] <= 0:
            print(f"\n💀 {opponent['name'].capitalize()} wins!")
            break


def main():
    print("🎮 Welcome to Pokémon Battle!")

    player_pokemon = choose_pokemon()
    if not player_pokemon:
        return

    opponent_pokemon = get_random_pokemon()
    if not opponent_pokemon:
        return

    print(f"\nYou chose {player_pokemon['name'].capitalize()} ({player_pokemon['type']})")
    print(f"Your opponent is {opponent_pokemon['name'].capitalize()} ({opponent_pokemon['type']})")

    battle(player_pokemon, opponent_pokemon)


if __name__ == "__main__":
    main()

