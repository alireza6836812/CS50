# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():
    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams_list = []
    # TODO: Read teams into memory from file
    name = sys.argv[1]
    with open(name) as file:
        reader = csv.DictReader(file)
        for i in reader:
            i["rating"] = int(i["rating"])
            teams_list.append(i)

    counts_dict = {}
    for i in range(0, N):
        winner = simulate_tournament(teams_list)
        if winner in counts_dict:
            counts_dict[winner] += 1
        else:
            counts_dict[winner] = 1

    for j in sorted(counts_dict, key=lambda j: counts_dict[j], reverse=True):
        print(f"{j}: {counts_dict[j] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    r1 = team1["rating"]
    r2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((r2 - r1) / 600))
    return random.random() < probability


def simulate_round(teams):
    winners_list = []

    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners_list.append(teams[i])
        else:
            winners_list.append(teams[i + 1])

    return winners_list


def simulate_tournament(teams):
    # TODO
    while len(teams)>1:
        teams = simulate_round(teams)
    return teams[0]["team"]


if __name__ == "__main__":
    main()
