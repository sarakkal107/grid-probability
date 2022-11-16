import random
import string

row = 100
col = 50

# Generate files
for x in range(10):

    grid = [[""]*col for i in range(row)]
    actions = ["" for i in range(row)]
    path = [[""]*2 for i in range(row)]
    sensor = ["" for i in range(row)]

    # Generate Maps
    for i in range(row):
        for j in range(col):
            rand = random.random()
            if rand <= 0.5 and rand > 0:
                grid[i][j] = "N"
            elif rand > 0.5 and rand > 0.7:
                grid[i][j] = "H"
            elif rand > 0.7 and rand > 0.9:
                grid[i][j] = "T"
            else:
                grid[i][j] = "B"

    # Create and write to map
    with open('maps/map{}'.format(x+1), 'w') as f:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                f.write(grid[i][j] + " ")
            f.write("\n")
        f.close()

    # Generate Paths
    for y in range(10):
        startX = random.randint(0, row-1)
        startY = random.randint(0, col-1)

        while grid[startX][startY] == "B":
            startX = random.randint(0, row-1)
            startY = random.randint(0, col-1)

        player = [startX, startY]

        # Generating Actions
        for i in range(row):
            rand = random.random()
            if rand > 0 and rand <= 0.25:
                actions[i] = "U"
            elif rand > 0.25 and rand <= 0.50:
                actions[i] = "L"
            elif rand > 0.50 and rand <= 0.75:
                actions[i] = "D"
            else:
                actions[i] = "R"

        # Generate the Ground Truths
        for i in range(len(actions)):
            rand = random.random()
            if rand > 0 and rand <= 0.9:
                if actions[i] == "U" and (player[1]+1 < col) and (grid[player[0]][player[1]+1] != "B"):
                    player[1] += 1
                if actions[i] == "L" and (player[0]+1 < row) and (grid[player[0]+1][player[1]] != "B"):
                    player[0] += 1
                if actions[i] == "D" and (player[1]-1 > 0) and (grid[player[0]][player[1]-1] != "B"):
                    player[1] -= 1
                if actions[i] == "R" and (player[0]-1 > 0) and (grid[player[0]-1][player[1]] != "B"):
                    player[0] -= 1
            path[i] = [player[0], player[1]]

        # Generate the Sensor Readings
        for i in range(len(path)):
            rand = random.random()
            if rand > 0 and rand <= 0.9:
                sensor[i] = grid[path[i][0]][path[i][1]]
            elif rand > 0.9 and rand <= 0.95:
                if grid[path[i][0]][path[i][1]] == "N":
                    sensor[i] = "H"
                if grid[path[i][0]][path[i][1]] == "H":
                    sensor[i] = "T"
                if grid[path[i][0]][path[i][1]] == "T":
                    sensor[i] = "N"
            elif rand > 0.95 and rand <= 1:
                if grid[path[i][0]][path[i][1]] == "N":
                    sensor[i] = "T"
                if grid[path[i][0]][path[i][1]] == "H":
                    sensor[i] = "N"
                if grid[path[i][0]][path[i][1]] == "T":
                    sensor[i] = "H"

        # Create and write to data
        with open('maps/map{}_data{}.txt'.format(x+1, y+1), 'w') as f:
            f.write("Start: \n" + str(startX) + " " + str(startY))
            f.write("\n")

            f.write("Path: \n")
            for i in range(len(path)):
                f.write(str(path[i][0]) + " " + str(path[i][1]))
                f.write("\n")

            f.write("Actions: \n")
            for i in range(len(actions)):
                f.write(actions[i])
            f.write("\n")

            f.write("Sensor Readings: \n")
            for i in range(len(sensor)):
                f.write(str(sensor[i]))

            f.close()
