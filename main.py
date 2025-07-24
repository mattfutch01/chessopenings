from games import get_game_data
import json
import pandas as pd
from collections import Counter

USERNAME = "USERNAME"

BADRESULT = ["lose", "checkmated", "timeout"]

get_game_data()

with open("USERNAME_games.json") as f:
    data = json.load(f)
    
games = data.get('games', [])
df = pd.json_normalize(games)

won_white_games = []
won_black_games = []
lost_white_games = []
lost_black_games = []

for _, row in df.iterrows():
    if row.get('white.username') == USERNAME and row.get('white.result') == "win":
        full_name = row['eco'].removeprefix("https://www.chess.com/openings/")
        if full_name == "Undefined":
            continue
        correct = full_name.split("-")[0:2]
        won_white_games.append(correct)

    elif row.get('black.username') == USERNAME and row.get('black.result') == "win":
        full_name = row['eco'].removeprefix("https://www.chess.com/openings/")
        if full_name == "Undefined":
            continue
        correct = full_name.split("-")[0:2]
        won_black_games.append(correct)

    elif row.get('white.username') == USERNAME and row.get('white.result') in BADRESULT:
        full_name = row['eco'].removeprefix("https://www.chess.com/openings/")
        if full_name == "Undefined":
            continue
        correct = full_name.split("-")[0:2]
        lost_white_games.append(correct)

    elif row.get('black.username') == USERNAME and row.get('black.result') in BADRESULT:
        full_name = row['eco'].removeprefix("https://www.chess.com/openings/")
        if full_name == "Undefined":
            continue
        correct = full_name.split("-")[0:2]
        lost_black_games.append(correct)

print("Worst White Openings")
C = Counter(tuple(o) for o in lost_white_games).most_common(5)
for opening, number in C:
    print(opening, number, "losses")

print("Worst Black Openings")
P = Counter(tuple(o) for o in lost_black_games).most_common(5)
for opening, number in P:
    print(opening, number, "losses")