import json
import requests

def get_game_data(username: str = "USERNAME", year: str = "2025", month: str = "01"):
    url = f"https://api.chess.com/pub/player/{username}/games/{year}/{month}"

    try:
        headers = {
            'User-Agent': 'My User Agent 1.0'       
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        with open(f"{username}_games.json", 'w') as file:
            json.dumps(data, file)
        return data

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None