teams = ["Team A", "Team B", "Team C", "Team D"]

runs_scored = []
runs_conceded = []
wins = []
losses = []
draws = []
points = []

for i in range(4):
    print("\n-----", teams[i], "-----")

    total_scored = 0
    total_conceded = 0
    win = 0
    loss = 0
    draw = 0
    point = 0

    for j in range(3):
        print("\nMatch", j + 1)

        scored = int(input("Enter runs scored: "))
        conceded = int(input("Enter runs conceded: "))
        result = input("Enter result (win/loss/draw): ").lower()

        total_scored = total_scored + scored
        total_conceded = total_conceded + conceded

        if result == "win":
            win = win + 1
            point = point + 2

        elif result == "draw":
            draw = draw + 1
            point = point + 1

        elif result == "loss":
            loss = loss + 1

    runs_scored.append(total_scored)
    runs_conceded.append(total_conceded)
    wins.append(win)
    losses.append(loss)
    draws.append(draw)
    points.append(point)


highest_team = 0

for i in range(1, 4):
    if points[i] > points[highest_team]:
        highest_team = i

    elif points[i] == points[highest_team]:
        if runs_scored[i] > runs_scored[highest_team]:
            highest_team = i


print("\n========== TOURNAMENT TABLE ==========")

print("Team\t\tMatches\tWins\tLosses\tDraws\tPoints")

for i in range(4):
    print(
        teams[i],
        "\t\t",
        3,
        "\t",
        wins[i],
        "\t",
        losses[i],
        "\t",
        draws[i],
        "\t",
        points[i]
    )


print("\nHighest Ranked Team:", teams[highest_team])
print("Points:", points[highest_team])
print("Total Runs Scored:", runs_scored[highest_team])