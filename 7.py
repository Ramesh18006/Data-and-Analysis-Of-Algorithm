def distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return (dx * dx + dy * dy) ** 0.5 

def brute_force(points):
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
    return min_dist

def strip_closest(strip, d):
    min_dist = d
    strip.sort(key=lambda p: p[1])
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= min_dist:
                break
            d = distance(strip[i], strip[j])
            if d < min_dist:
                min_dist = d
    return min_dist

def closest_pair(points):
    def recursive(Px):
        if len(Px) <= 3:
            return brute_force(Px)
        mid = len(Px) // 2
        mid_x = Px[mid][0]
        left = Px[:mid]
        right = Px[mid:]
        d1 = recursive(left)
        d2 = recursive(right)
        d = min(d1, d2)
        strip = [p for p in Px if abs(p[0] - mid_x) < d]
        return min(d, strip_closest(strip, d))

    points.sort()
    return recursive(points)

# Example usage
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print("Closest distance:", closest_pair(points))
