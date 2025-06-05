import requests

base_url = "https://pokeapi.co/api/v2/"

def pokemon_info(name):
    url = f"{base_url}pokemon/{name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Name: {data['name'].capitalize()}")
        print(f"Height: {data['height']}")
        print(f"Weight: {data['weight']}")
        print("Types:", ", ".join([t['type']['name'] for t in data['types']]))
    else:
        print("Pokémon not found.")

pokemon_name = input("Enter a Pokémon name: ")
pokemon_info(pokemon_name)
