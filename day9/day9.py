coordinates = []

with open('data.txt', 'r') as file:
    for line in file:
        numbers = line.strip().split(',')
        print(numbers)
        if len(numbers) >= 2:
            coord_tuple = (int(numbers[0]), int(numbers[1]))
            coordinates.append(coord_tuple)

print(coordinates)

distances = []

for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[j]
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        distances.append((coordinates[i], coordinates[j], distance))

distances.sort(key=lambda x: x[2], reverse=True)
print(distances)

if distances:
    point1, point2, _ = distances[0]
    horizontal_distance = abs(point2[0] - point1[0]) +1
    vertical_distance = abs(point2[1] - point1[1]) +1
    print(f"Horizontal distance: {horizontal_distance}")
    print(f"Vertical distance: {vertical_distance}")

    print('Results : ' + str(vertical_distance * horizontal_distance))