def euclidean_algorithm(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
