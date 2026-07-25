import csv

from gender_classifier import classify_by_gender
from AVHSrankingstoElo import calculate_elo_ratings


def load_roster(filename):
    """
    Read player names, genders, and ranks from a CSV file.
    """
    players = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            players.append({
                "name": row["name"].strip(),
                "gender": row["gender"].strip(),
                "rank": int(row["rank"])
            })

    return players


def assign_initial_ratings(players):
    """
    Classify players by gender and calculate Elo ratings
    independently for each gender ladder.
    """
    classified_players = classify_by_gender(players)
    rated_players = []

    for gender in ["Boys", "Girls"]:
        gender_players = classified_players[gender]
        elo_ratings = calculate_elo_ratings(gender_players)

        for player, elo in zip(gender_players, elo_ratings):
            rated_players.append({
                "name": player["name"],
                "gender": gender,
                "rank": player["rank"],
                "preseason_elo": elo,
                "current_elo": elo
            })

    return rated_players


def save_ratings(filename, rated_players):
    """
    Save the initialized player ratings to another CSV file.
    """
    column_names = [
        "name",
        "gender",
        "rank",
        "preseason_elo",
        "current_elo"
    ]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=column_names
        )

        writer.writeheader()
        writer.writerows(rated_players)


def main():
    players = load_roster("roster.csv")
    rated_players = assign_initial_ratings(players)

    save_ratings(
        "initial_player_ratings.csv",
        rated_players
    )

    print(
        f"Successfully initialized "
        f"{len(rated_players)} players."
    )

    print("Ratings saved to initial_player_ratings.csv")


if __name__ == "__main__":
    main()
