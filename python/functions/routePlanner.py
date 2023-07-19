""" You will be given a list of integers, they will be the height of a peak from ground level (1 = 100m). The peaks will appear in a single line as you travel from point A to B.
Rules:
You don’t have to climb every peak. But you want to climb as many peaks as possible
You only want to increase your altitude as going up and down would be too exhaustive.
There is no going backwards.
There can be more than one possible output. """


def routePlanner(list):
    lastPeak = 0
    route = []
    for peak in list:
        if peak > lastPeak:
            route.append(peak)
            lastPeak = peak
    return route


testRoute = [3, 6, 23, 12, 8, 4, 2, 7, 8, 45,]
print("The best route is:", routePlanner(testRoute))
