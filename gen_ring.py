
def gen_ring(point, distance):
    ring = []
    for x in range(point[0] - distance, point[0] + distance + 1):
        ring.append((x, point[1] - distance))
        ring.append((x, point[1] + distance))
    for y in range(point[1] - distance, point[1] + distance + 1):
        ring.append((point[0] - distance, y))
        ring.append((point[0] + distance, y))

    return ring


point = (10, 10)
distance = 5
ring = gen_ring(point, distance)
print(ring)
print(set(ring))

print((5, 5) in set(ring))
print((25, 25) in set(ring))
