def normalize_gender(gender):
    """
    Convert common gender inputs into 'Boys' or 'Girls'.
    """
    gender = gender.strip().lower()

    if gender in ["boy", "boys", "male", "m", "b"]:
        return "Boys"

    if gender in ["girl", "girls", "female", "f", "g"]:
        return "Girls"

    raise ValueError(
        f"Invalid gender '{gender}'. Enter Boys or Girls."
    )


def classify_by_gender(players):
    """
    Separate players into boys' and girls' ladders,
    then sort each ladder by rank.
    """
    classified_players = {
        "Boys": [],
        "Girls": []
    }

    for player in players:
        gender = normalize_gender(player["gender"])

        classified_players[gender].append({
            "name": player["name"],
            "rank": player["rank"]
        })

    for gender in classified_players:
        classified_players[gender].sort(
            key=lambda player: player["rank"]
        )

        # Make sure ranks contain 1, 2, 3, ..., N
        actual_ranks = [
            player["rank"]
            for player in classified_players[gender]
        ]

        expected_ranks = list(
            range(1, len(classified_players[gender]) + 1)
        )

        if actual_ranks != expected_ranks:
            raise ValueError(
                f"{gender} ranks must contain every rank "
                f"from 1 through {len(expected_ranks)}."
            )

    return classified_players
