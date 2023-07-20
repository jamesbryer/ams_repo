newLine = "This is a new line\n"

with open("python/files/teams.txt", "r") as file:
    fileContents = file.read()

with open("python/files/teams.txt", "w") as file:
    file.write(newLine + fileContents)
