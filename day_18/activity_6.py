pythagorean_triplets = [(x,y,z) for x in range(1,31) for y in range(1,31) for z in range(1,31) if x**2+y**2==z**2]

print(pythagorean_triplets)