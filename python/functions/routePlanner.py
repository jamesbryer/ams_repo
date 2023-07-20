""" You will be given a list of integers, they will be the height of a peak from ground level (1 = 100m). The peaks will appear in a single line as you travel from point A to B.
Rules:
You don’t have to climb every peak. But you want to climb as many peaks as possible
You only want to increase your altitude as going up and down would be too exhaustive.
There is no going backwards.
There can be more than one possible output. """

# as per the example, we are assuming the 1st item in the list is the start and the last item in the list is the end we cannot move left, only right.


def routePlanner(peaksList):
    route = [peaksList[0]]  # Initialize the route with the first peak
    while len(peaksList) > 1:
        # Find the next lowest peak (excluding the first one)
        nextLowest = min(peaksList[1:])
        # Find the index of the next lowest peak
        index = peaksList.index(nextLowest)
        route.append(nextLowest)  # Add the next lowest peak to the route
        # Update the peaksList to start from the next lowest peak
        peaksList = peaksList[index:]
    return route


testRoute = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print("The best route is:", routePlanner(testRoute))


def betterRoutePlanner(peaksList):
    routes = []
    for startPoint in peaksList[1:]:
        route = [startPoint]
        for peak in peaksList[peaksList.index(startPoint):]:
            if peak > route[-1]:
                route.append(peak)
        routes.append(route)
    for i in routes:
        print(i)
    # longestRoute = max(routes, key=len)
    # return longestRoute


longestRoute = betterRoutePlanner(testRoute)
print("The best route is:", longestRoute)
