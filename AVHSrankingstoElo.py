import math
from gender_classifier import classify_by_gender
def calculate_elo_ratings(ranked_players):
    """
    Calculate Elo ratings for one gender ladder.
    
    ranked_players must already be sorted from Rank 1
    through the last rank.
    """
    number_of_players = len(ranked_players)

    if number_of_players == 0:
        return []

    if number_of_players == 1:
        return [2200]

    elo_ratings = []

    for rank in range(1, number_of_players + 1):
        raw_elo = 1000 + 1200 * (
            (number_of_players - rank)
            / (number_of_players - 1)
        ) ** 1.8

        rounded_elo = math.floor(raw_elo + 0.5)
        elo_ratings.append(rounded_elo)

    return elo_ratings


def main():
    number_of_players = int(
        input("Total number of players: ")
    )

    players = []

    for player_number in range(1, number_of_players + 1):
        print(f"\nPlayer {player_number}")

        name = input("Name: ")
        gender = input("Gender (Boys/Girls): ")
        rank = int(input("Rank within gender: "))

        players.append({
            "name": name,
            "gender": gender,
            "rank": rank
        })

    try:
        classified_players = classify_by_gender(players)
    except ValueError as error:
        print(f"\nError: {error}")
        return

    for gender in ["Boys", "Girls"]:
        gender_players = classified_players[gender]

        if not gender_players:
            continue

        elo_ratings = calculate_elo_ratings(gender_players)

        print(f"\n{gender} Elo Ratings:")

        for player, elo in zip(gender_players, elo_ratings):
            print(
                f'Rank {player["rank"]}: '
                f'{player["name"]} — {elo}'
            )

        print(f"\n{gender} Elo list:")
        print(elo_ratings)


if __name__ == "__main__":
    main()
