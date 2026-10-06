# # drivers = ["Hamilton", "Verstappen", "Piastri", "Norris", "Antonelli", "Russell"]

# # points = [200, 143, 234, 94, 67, 123]

# # for driver in drivers:
# #     print(drivers)
# # for p in points:
# #     print(points)

# # for drivers, points in zip(drivers, points):
# #     print(drivers,":", points)

# # drivers = [
# #     {"name": "Verstappen", "team": "Red Bull", "points": 575},
# #     {"name": "Hamilton", "team": "Mercedes", "points": 234},
# #     {"name": "Norris", "team": "McLaren", "points": 205},
# # ]

# # print(drivers[1]["name"])
# # for driver in drivers:
# #     if driver["points"]>220:
# #         print(driver["name"])

# # drivers.append({"name": "Antonelli", "team": "Mercedes", "points": 267})
# # for d in drivers:
# #     print(d)

# # def greet_driver(name):
# #     print("Hello, " + name)

# # greet_driver("Hamilton")
# # greet_driver("Norris")

# # def points_to_position(points):
# #     if points > 500:
# #         return "Championship contender"
# #     else:
# #         return "Midfield"

# # result = points_to_position(450)
# # print(result)   

# def has_high_points(driver):
#     return driver["points"] > 220

# drivers = [
#     {"name": "Verstappen", "team": "Red Bull", "points": 575},
#     {"name": "Hamilton", "team": "Mercedes", "points": 234},
#     {"name": "Norris", "team": "McLaren", "points": 205},
# ]

# def get_team(driver):
#     return driver["team"]
# for d in drivers:
#     print(get_team(d))


# def total_points(drivers_list):
#     total = 0
#     for d in drivers_list:
#         total = total + d["points"]
#     return total
# print(total_points(drivers))

# def avg_points(drivers_list):
#     return total_points(drivers_list)/(len(drivers_list))
# print(avg_points(drivers))

# def top_driver(drivers_list):
#     highest = drivers_list[0]
#     for d in drivers_list:
#         if d["points"] > highest["points"]:
#             highest == d
#     return highest["name"]
# print(top_driver(drivers))

# n=4
# for i in range(1, n + 1):
#     for j in range(i):
#         print ("*", end=" ")
#     print()

n = 5
for i in range (n):
    for j in range (n-i):
        print("*", end=" ")
    print()