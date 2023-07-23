import json

with open("resources/end_points.json") as end_points_file:

    end_points = json.load(end_points_file)

print("End_points = ", end_points)
