import requests

def get_smarties_hero():
    response = requests.get("https://akabab.github.io/superhero-api/api/all.json")
    heroes = list(filter(lambda hero: hero.get("name") in ("Hulk", "Captain America", "Thanos"), response.json()))
    smarties_hero = max(heroes, key=lambda hero: hero.get("powerstats").get("intelligence"))
    return smarties_hero.get("name")

if __name__ == "__main__":
    print(get_smarties_hero())