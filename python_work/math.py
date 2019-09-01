z = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            print(f"{i} * {j} * {k} is {i * j * k} (iteration {z})")
            z = z + 1
