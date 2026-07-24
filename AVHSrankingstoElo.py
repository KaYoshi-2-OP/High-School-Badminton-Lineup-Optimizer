import math
#defined formula calculate elo ratings
def calculate_elo_ratings(ranked_players):
    number_of_players = len(ranked_players)

    if number_of_players == 0:
        return []
    if number_of_players == 1:
        return [2200]
    elo_ratings = []
    for rank in range(1, number_of_players + 1):
        raw_elo = 1000 + 1200 * (
            (number_of_players - rank) / (number_of_players - 1)
        ) ** 1.8
        # This rounds to the nearest Elo
        elo = math.floor(raw_elo + 0.5)
        elo_ratings.append(elo)

    return elo_ratings


number_of_players = int(input("Number of ranked players: "))

players = []

for rank in range(1, number_of_players + 1):
    player_name = input(f"Rank {rank}: ")
    players.append(player_name)

ratings = calculate_elo_ratings(players)

print("\nElo ratings:")
print(ratings)
