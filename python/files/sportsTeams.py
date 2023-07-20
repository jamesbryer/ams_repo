teams = ["Liverpool Football Club", "Mercedes-AMG Petronas Formula 1 Team",
         "Miami Heat", "Scuderia Ferarri", "Green Bay Packers"]

with open("python/files/teams.txt", "a") as file:
    for i in teams:
        file.write(i + "\n")

with open("python/files/teams.txt", "r") as file:
    file = file.readlines()
    counter = 1
    for line in file:
        if counter == 1 or counter == 4:
            print(line)
        counter += 1
