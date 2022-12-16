from collections import defaultdict


def run(data):
    caves = defaultdict(lambda x: ".")

    for structure in data:
        points = []
        for point in structure.split(" -> "):
            points.append(tuple([int(value) for value in point.split(",")]))
        for i in range(1, len(points)):
            caves[points[i]] = "#"
            caves[points[i-1]] = "#"
            if points[i - 1][0] == points[i][0]:
                for n in range(points[i - 1][1], points[i][1],
                               int(((points[i][1] - points[i - 1][1]) / abs(points[i][1] - points[i - 1][1])))):
                    caves[(points[i][0], n)] = "#"
            elif points[i - 1][1] == points[i][1]:
                for n in range(points[i - 1][0], points[i][0],
                               int(((points[i][0] - points[i - 1][0]) / abs(points[i][0] - points[i - 1][0])))):
                    caves[(n, points[i][1])] = "#"
        print(points)

    return
