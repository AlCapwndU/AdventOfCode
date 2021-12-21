# from collections import defaultdict
# import sys
# sys.setrecursionlimit(1000)
#
#
# def getPaths(cave_system, u, visited, path, all_paths, double_cave, recursion_map):
#     if (u, tuple(sorted(visited.items())), double_cave) in recursion_map:
#         if path:
#             path.pop()
#             visited[u] = False
#     else:
#         recursion_map[(u, tuple(sorted(visited.items())), double_cave)] = True
#     visited[u] = True
#     path.append(u)
#
#     if u == "end":
#         all_paths.append(path.copy())
#     else:
#         for i in cave_system[u]:
#             if i.isupper():
#                 getPaths(cave_system, i, visited, path, all_paths, double_cave,recursion_map)
#             else:
#                 l_case=[n for n in path if n.islower()]
#                 twice = any([True for i in l_case if l_case.count(i) > 1])
#                 if twice and not visited[i]:
#                     getPaths(cave_system, i, visited, path, all_paths, double_cave,recursion_map)
#                 else:
#                     getPaths(cave_system, i, visited, path, all_paths, double_cave, recursion_map)
#
#
#
#     path.pop()
#     visited[u] = False
#
#
#
#
# def run(data):
#
#     cave_system = defaultdict(list)
#     v = 0
#     visited = defaultdict(bool)
#     for path in data:
#         caves = path.split("-")
#         visited[caves[1]] = False
#         visited[caves[0]] = False
#         if caves[1] != "start" and caves[0] != "end":
#             cave_system[caves[0]].append(caves[1])
#             v+=1
#
#         if caves[0] != "start" and caves[1] != "end":
#             cave_system[caves[1]].append(caves[0])
#             v+=1
#
#
#     recursion_map=defaultdict(bool)
#     path = []
#     all_paths = []
#     double_cave = ""
#     getPaths(cave_system,"start",visited, path, all_paths, double_cave,recursion_map)
#
#
#
#     return len(all_paths)






