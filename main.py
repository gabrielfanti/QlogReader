import re
import json

def parse_log_file(filename):
    # Expressão regular para extrair informações relevantes de cada linha do log
    pattern = r'(?P<minute>\d+):(?P<second>\d+) Kill: \d+ \d+ \d+: (?P<player1>\w+) killed (?P<player2>\w+) by (?P<cause>.*)'
    regex = re.compile(pattern)

    games = {}
    current_game = None

    with open(filename, 'r') as file:
        for line in file:
            match = regex.search(line)
            if match:
                minute = int(match.group('minute'))
                second = int(match.group('second'))
                player1 = match.group('player1')
                player2 = match.group('player2')
                cause = match.group('cause')

                if current_game is None:
                    current_game = "game_1"
                    games[current_game] = {
                        "total_kills": 0,
                        "players": [],
                        "kills": {}
                    }

                if current_game not in games:
                    games[current_game] = {
                        "total_kills": 0,
                        "players": [],
                        "kills": {}
                    }

                if player1 != "<world>":
                    games[current_game]["total_kills"] += 1
                    if player1 not in games[current_game]["players"]:
                        games[current_game]["players"].append(player1)
                        games[current_game]["kills"][player1] = 0
                    games[current_game]["kills"][player1] += 1

                if player2 != "<world>":
                    if player2 not in games[current_game]["players"]:
                        games[current_game]["players"].append(player2)
                        games[current_game]["kills"][player2] = 0

                if cause not in games[current_game]["kills"]:
                    games[current_game]["kills"][cause] = 0
                games[current_game]["kills"][cause] += 1

            elif "InitGame" in line:
                current_game = "game_" + str(len(games) + 1)

    return games

def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def print_report(games):
    for game, data in games.items():
        print("Game:", game)
        print("Total Kills:", data["total_kills"])
        print("Players:", data["players"])
        print("Kills:")
        for player, kills in data["kills"].items():
            print(player + ":", kills)
        print()

filename = "qgames.log"
games = parse_log_file(filename)
save_to_json(games, "games.json")
print_report(games)
