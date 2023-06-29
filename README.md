# Quake 3 Log Reader

This project consists of a Python script that analyzes the log file of the Quake 3 game and extracts relevant information for each match. It groups game data and collects player kill information, saving the results to a JSON file.

## Features

- Reads the `qgames.log` file present in the same folder as the script.
- Groups game data for each match.
- Collects kill data, including the total number of kills per player and per cause of death.
- Generates a printed report for each match, displaying player statistics and kills by type.
- Saves the data to a JSON file named `games.json`.

## Supported Log Format

The script expects the `qgames.log` file to be in the following format:

<minute>:<second> Kill: <number> <number> <number>: <player1> killed <player2> by <cause>

For example:

20:32 Kill: 1 2 7: Player1 killed Player2 by MOD_SHOTGUN
20:35 Kill: 3 1 5: Player3 killed Player1 by MOD_MACHINEGUN

## Running the Script

Make sure you have Python installed on your system. Then, follow these steps:

1. Clone this repository or download the files.
2. Place the `qgames.log` file in the same folder as the `main.py` script.
3. Open the terminal or command prompt and navigate to the project folder.
4. Run the command `python main.py`.
5. The script will process the log file, generate the report in the console, and save the data to `games.json`.

## Example Report

Here's an example of the report that will be displayed in the console:

Game: game_1
Total Kills: 14
Players: ['Player1', 'Player2', 'Player3']
Kills:
Player1: 6
Player2: 4
Player3: 4

Game: game_2
Total Kills: 10
Players: ['Player1', 'Player2', 'Player3']
Kills:
Player1: 3
Player2: 2
Player3: 5

## Saved Data in JSON

The data will be saved in a JSON file named `games.json` with the following format:

```json
{
    "game_1": {
        "total_kills": 14,
        "players": [
            "Player1",
            "Player2",
            "Player3"
        ],
        "kills": {
            "Player1": 6,
            "Player2": 4,
            "Player3": 4,
            "MOD_SHOTGUN": 7,
            "MOD_RAILGUN": 3,
            "MOD_MACHINEGUN": 4
        }
    },
    "game_2": {
        "total_kills": 10,
        "players": [
            "Player1",
            "Player2",
            "Player3"
        ],
        "kills": {
            "Player1": 3,
            "Player2": 2,
            "Player3": 5,
            "MOD_SHOTGUN": 4,
            "MOD_RAILGUN": 2,
            "MOD_MACHINEGUN": 4
        }
    }
}
