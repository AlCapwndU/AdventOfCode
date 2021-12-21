from collections import defaultdict
import math
import matplotlib.pyplot as plt






def run(data):
    path = []
    min_risk = 99999999999999999999999999999999999999999999
    visited = defaultdict(bool, {(0, 0): True})
    all_paths = []
    risk = -1*data[(0,0)]
    risk_path=[]
    path = []

    def getPaths(cave_system, u, dest, visited, risk):
        visited[u] = True
        risk += cave_system[u]
        nonlocal min_risk
        if risk > min_risk:
            visited[u] = False
            return

        if u == dest:
            if risk < min_risk:
                min_risk = risk
                # for point in [c for c in visited if visited[c]]:
                #     plt.scatter(point[0], point[1])
                #
                # # plt.axis("equal")
                # plt.gca().invert_yaxis()
                # plt.show()
                # plt.clf()

        else:
            for x, y in [(u[0] + i, u[1] + j) for i in (0, 1) for j in (0, 1) if
                         (i != 0 or j != 0) and abs(i) != abs(j)]:
                if (x, y) in cave_system and not visited[(x, y)]:
                    getPaths(cave_system, (x, y), dest, visited, risk)

        visited[u] = False
        return

    getPaths(dict(data), (0, 0), (int(math.sqrt(len(data)))-1, int(math.sqrt(len(data)))-1), visited, risk)

    return min_risk
