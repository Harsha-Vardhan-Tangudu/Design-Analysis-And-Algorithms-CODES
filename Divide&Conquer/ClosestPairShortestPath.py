import math
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair(points):
    if len(points) <= 1:
        return float('inf'), None, None

    # Base case: If there are only two points, calculate distance directly
    if len(sorted_points) == 2:
        return euclidean_distance(sorted_points[0], sorted_points[1]), sorted_points[0], sorted_points[1]
    
    # Sort points by x-coordinate
    sorted_points = sorted(points, key=lambda x: x[0])

    # Divide the points into two halves
    mid = len(sorted_points) // 2
    left_half = sorted_points[:mid]
    right_half = sorted_points[mid:]

    # Recursively find the closest pair in each half
    left_distance, left_point1, left_point2 = closest_pair(left_half)
    right_distance, right_point1, right_point2 = closest_pair(right_half)

    # Find the minimum distance among the two halves
    min_distance = min(left_distance, right_distance)

    # Merge the two halves and find the closest pair that spans both halves
    mid_strip_points = [point for point in sorted_points if abs(point[0] - sorted_points[mid][0]) < min_distance]
    mid_strip_points.sort(key=lambda x: x[1])  # Sort points by y-coordinate

    for i in range(len(mid_strip_points)):
        #i + 1: The loop starts from the index immediately following the current value of i. This ensures that we don't compare a point with itself.
        #It starts from the point at index i + 1 and goes up to either i + 8 or the end of the strip, whichever comes first
        for j in range(i + 1, min(i + 8, len(mid_strip_points))):
            distance = euclidean_distance(mid_strip_points[i], mid_strip_points[j])
            if distance < min_distance:
                min_distance = distance
                left_point1, left_point2 = mid_strip_points[i], mid_strip_points[j]

    return min_distance, left_point1, left_point2

# Example usage
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
distance, closest_point1, closest_point2 = closest_pair(points)

print(f"Closest Pair: {closest_point1} and {closest_point2}")
print(f"Distance: {distance}")