"""
A program that calculates distance between two points
@dev erkut oğuz

"""

points = [(3, 5), (2, 0), (4, 7), (1, 1), (2, 3), (3, 0), (0, 4)]
distances = []


def calculate_eucledean_distance(point_a, point_b):
    delta_x = point_a[0] - point_b[0]
    delta_y = point_a[1] - point_b[1]
    return (delta_x**2 + delta_y**2) ** (1 / 2)


for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        distances.append(calculate_eucledean_distance(points[i], points[j]))


print(min(distances))
